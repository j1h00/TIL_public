# mongoDB 03 : Modeling

## Intro 

RDBMS 의 Data Modeling 은 경험이 몇 번 있고, 정규화 개념을 나름대로 잘 파악하고 있어 ERD 를 그리는 데 큰 문제가 없었지만, MongoDB 와 같은 NoSQL 은 사용 경험이 없고, 컬렉션의 구성이나 도큐멘트의 형식이 너무 자유로워 어떻게 모델링을 해야 할 지 고민이 많았다. 

프로젝트 팀원분이 올려주신 블로그 글을 읽었는데, 도움이 많이 되었다. 

>[MongoDB 이해하기](https://kciter.so/posts/about-mongodb)

특히 MongoDB 패턴 예제를 통해 흔히 사용되는 패턴에 대해 알 수 있었고, 프로젝트에 적용해보면 좋겠다고 생각했다.  

## Model Tree Structure 

###### Parent References

```json
[
  { _id: "MongoDB", parent: "Databases" },
  { _id: "dbm", parent: "Databases" },
  { _id: "Databases", parent: "Programming" },
  { _id: "Languages", parent: "Programming" },
  { _id: "Programming", parent: "Books" },
  { _id: "Books", parent: null }
]
```

- 하위 트리를 모두 찾아야 하는 경우 적합하지 않다. 

###### Child References

```json
[
  { _id: "MongoDB", children: [] },
  { _id: "dbm", children: [] },
  { _id: "Databases", children: [ "MongoDB", "dbm" ] },
  { _id: "Languages", children: [] },
  { _id: "Programming", children: [ "Databases", "Languages" ] },
  { _id: "Books", children: [ "Programming" ] }
]
```

- Parent Document 도 찾을 순 있지만, Parent references 보다는 탐색 성능이 느리다. 

###### Array of Ancestors

```json
[
  { _id: "MongoDB", ancestors: [ "Books", "Programming", "Databases" ], parent: "Databases" },
  { _id: "dbm", ancestors: [ "Books", "Programming", "Databases" ], parent: "Databases" },
  { _id: "Databases", ancestors: [ "Books", "Programming" ], parent: "Programming" },
  { _id: "Languages", ancestors: [ "Books", "Programming" ], parent: "Programming" },
  { _id: "Programming", ancestors: [ "Books" ], parent: "Books" },
  { _id: "Books", ancestors: [ ], parent: null }
]
```

- 여러 부모 Document 를 가진 경우엔 적합하지 않다. 
- BreadCrumb 등에 쓸 수 있다. 

###### Materialized Paths

```json
[
  { _id: "Books", path: null },
  { _id: "Programming", path: ",Books," },
  { _id: "Databases", path: ",Books,Programming," },
  { _id: "Languages", path: ",Books,Programming," },
  { _id: "MongoDB", path: ",Books,Programming,Databases," },
  { _id: "dbm", path: ",Books,Programming,Databases," }
]
```

- Array of Ancestors 와 비슷하지만, array 가 아닌 string 타입을 이용한다. => 정규식 사용 가능

#### Nested Sets

```json
[
  { _id: "Books", parent: 0, left: 1, right: 12 },
  { _id: "Programming", parent: "Books", left: 2, right: 11 },
  { _id: "Languages", parent: "Programming", left: 3, right: 4 },
  { _id: "Databases", parent: "Programming", left: 5, right: 10 },
  { _id: "MongoDB", parent: "Databases", left: 6, right: 7 },
  { _id: "dbm", parent: "Databases", left: 8, right: 9 }
]
```

- 하위 트리를 찾는 데 효율적이지만, 구조가 변경되는 경우.. 다시 번호 매기는데 비용이 크다. 

## Model Relationships

RDBMS 와 마찬가지로, `1:1` , `1:N` , `N:M` 구조로 구성하는 것이 가능하다. 

1. `1:1` 구성은 가급적이면 Sub Document 로 Embed 하는 방식이 좋다. (Document 크기가 너무 큰 경우만 분리)

2. `1:N` 1이 N 을 참조하는 방식

   ```json
   // 1이 N을 참조하는 방식
   // Movie Collection
   {
     title: 'Star Wars',
     reviews: [1, 2, 3]
   }
   
   // Review Collection
   [
     {
       _id: 1,
       comment: 'Good'
     },
     {
       _id: 2,
       comment: 'Good'
     },
     {
       _id: 3,
       comment: 'Good'
     }
   ]
   ```

   ```json
   // N이 1을 참조하는 방식
   // Movie Collection
   {
     title: 'Star Wars',
   }
   
   // Review Collection
   [
     {
       _id: 1,
       title: 'Star wars',
       comment: 'Good'
     },
     {
       _id: 2,
       title: 'Star wars',
       comment: 'Good'
     },
     {
       _id: 3,
       title: 'Star wars',
       comment: 'Good'
     }
   ]
   ```

## Modeling Pattern 

>MongoDB는 Subquery나 Join과 같은 기능을 제공해주지 않는다. `Aggregation`을 이용하면 엇비슷하게 사용할 수 있지만 여러 Collection을 참조하게 되면 성능이 크게 느려지기에 권장하지 않는다.
>
>이 때 최대한 여러 Collection을 참조하는 것을 방지하고 데이터를 단순화하기 위해 **모델링 패턴**을 이용할 수 있다

###### Attribute 

동일한 필드를 묶어서 인덱싱 수를 줄이는 방법 

```json
{
  title: "Star Wars",
  director: "George Lucas",
  ...
  release_US: ISODate("1977-05-20T01:00:00+01:00"),
  release_France: ISODate("1977-10-19T01:00:00+01:00"),
  release_Italy: ISODate("1977-10-20T01:00:00+01:00"),
  release_UK: ISODate("1977-12-27T01:00:00+01:00"),
  ...
}
```

위와 같은 경우 각 국의 개봉 날짜로 검색하는 경우 각각의 키에 인덱스를 걸어줘야 한다. 

```json
{release_US: 1}
{release_France: 1}
{release_Italy: 1}
...
```

하지만 인덱스가 너무 많아져 관리가 복잡하고 용량이 증가한다. 이 때 아래와 같이 사용하면 인덱스를 두개 로 줄일 수 있다. 

```json
{
  title: "Star Wars",
  director: "George Lucas",
  ...
  releases: [
    {
      location: "USA",
      date: ISODate("1977-05-20T01:00:00+01:00")
    },
    {
      location: "France",
      date: ISODate("1977-10-19T01:00:00+01:00")
    },
    {
      location: "Italy",
      date: ISODate("1977-10-20T01:00:00+01:00")
    },
    {
      location: "UK",
      date: ISODate("1977-12-27T01:00:00+01:00")
    },
    ...
  ],
  ...
}
```

```json
{ "releases.location": 1, "releases.date": 1}
```

###### Extended Reference 

>Extended Reference 패턴은 서로 관계가 있는 Document에서 자주 사용되는 데이터를 저장해두는 패턴이다. MongoDB에선 성능을 위해 Join대신 쿼리를 두 번 날려 연관 데이터를 불러오는 방식을 많이 사용하는데 데이터가 많아질수록 불리하기 때문에 데이터가 많아지고 참조 자주 필요할 수록 Extended Reference 패턴을 사용해야한다.

Join 이 필요한 경우, 필요한 데이터를 연관된 Collection 에서 일부의 Document 에만 저장하는 것을 의미한다. 

###### Subset 

관계가 있는 Document 사이에 자주 사용되는 데이터를 부분적으로 Embed 하는 패턴 (Extended Reference 와 조금 차이가 있다.)

연관된 두 개의 Collection 에서 데이터를 가져오기 위해, 두 번 쿼리를 날려야하는 상황이 있다면..?

빠르게 몇 개의 데이터만 Embed 하여 저장해두면, 빠르게 사용자에게 데이터를 전달할 수 있다. 

하지만 데이터 수정이 발생한다면 양쪽을 모두 수정해야 한다. 

###### Computed

미리 통계 수치를 계산하여 데이터 삽입 시 추가한다. 

###### Bucket

하나의 필드를 기준으로 Document 들을 묶는다. (실시간으로 데이터가 들어오는 시계열 데이터에 적합)

예를 들어, 아래와 같은 로그 데이터 수집 시 

```json
{
  sensor_id: 12345,
  timestamp: ISODate("2019-01-31T10:00:00.000Z"),
  temperature: 40
}

{
  sensor_id: 12345,
  timestamp: ISODate("2019-01-31T10:01:00.000Z"),
  temperature: 40
}

{
  sensor_id: 12345,
  timestamp: ISODate("2019-01-31T10:02:00.000Z"),
  temperature: 41
}
```

위와 같은 document 들을 아래처럼 묶는다. 

```json
{
    sensor_id: 12345,
    start_date: ISODate("2019-01-31T10:00:00.000Z"),
    end_date: ISODate("2019-01-31T10:59:59.000Z"),
    measurements: [
      {
      timestamp: ISODate("2019-01-31T10:00:00.000Z"),
      temperature: 40
      },
      {
      timestamp: ISODate("2019-01-31T10:01:00.000Z"),
      temperature: 40
      },
      ...
      {
      timestamp: ISODate("2019-01-31T10:42:00.000Z"),
      temperature: 42
      }
    ],
   transaction_count: 42,
   sum_temperature: 2413
} 
```

- 이 경우 필드 추가 삭제가 용이하고, 인덱스 크기 절약도 가능하다. 
- 다만 크기 제한을 벗어나지 않도록, 기준점을 가지고 묶는 것이 좋다. 

###### Schema versioning

서비스를 운영하다 보면, Schema 를 변경해야 할 가능성이 높은데, Schema versioning 을 통해 기존 데이터를 급하게 마이그레이션 하지 않아도 된다. 

```json
{
  "_id": "<ObjectId>",
  "schema_version": "2",
  "name": "Anakin Skywalker (Retired)",
  "contact_method": [
    { "work": "503-555-0210" },
    { "mobile": "503-555-0220" },
    { "twitter": "@anakinskywalker" },
    { "skype": "AlwaysWithYou" }
  ]
}
```

- 이처럼 `schema_version` 필드를 추가하면, 원하는 데이터 조회 시 특정 버전의 데이터만 가져올 수 있으므로 충돌 없이 작업이 가능하다. 
- 물론 추후에 천천히 마이그레이션 작업을 해야 한다. 





















