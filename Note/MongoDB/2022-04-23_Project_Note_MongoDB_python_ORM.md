# mongoDB 03 : python ORM 

>[NoSQL DB (몽고DB/mongodb) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/nosql-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AA%BD%EA%B3%A0db-%EC%9E%94%EC%9E%AC%EB%AF%B8%EC%BD%94%EB%94%A9/dashboard)

위 강의를 듣고 정리한 내용입니다. 

## find 

#### sort 

- same sa `ORDER BY`
- find 로 조회 시, 정렬 조건 명시

```python
result = actor_collection.find().sort('actor_name')

# ASCENDING & DESCENDING
result = actor_collection.find().sort('actor_name', pymongo.ASCENDING)


# multiple field 
# sort by multiple fields
result = actor_collection.find().sort(
  [
    ('actor_name', pymongo.ASCENDING),
    ('actor_rate', pymongo.DESCENDING)
  ]
)
```

#### exists

- embedded document 에서 필드값 존재 여부에 따라 검색

```python
# result 에는 documents (records) 존재
result = actor_collection.find(
  {'actor_info.특기' : {'$exists' : False}}
)

result = actor_collection.find(
  {'actor_info.홈페이지' : {'$exists' : True}}
)
```

#### or

```python
# name이 aaron이고, age가 20이거나 30인 doc
docs = test_insert_collection.find(
  { 
    'name' : 'aaron', 
   	'$or' : [ 
      { 'age' : {'$lte' : 20 } }, 
      { 'age' : 30 } 
    ] 
  }
):

# name 이 fox 이거나 나이가 27세 이상인 doc (name, age 만)
docs = test_insert_collection.find(
  {
    '$or' : [ 
      {'age' : {'$gte' : 27}}, 
      {'name' : 'fox'}
    ]
  }, 
  {'name':1, 'age':1, '_id':0}
)
```

#### nor

- or 와 사용법이 동일

#### in / nin 

```python 
# age 가 해당 리스트 안에 존재하는 원소와 일치하는 doc
docs = test_insert_collection.find(
  {'age' : {'$in' : [20, 21, 25, 27]}}
)
```

#### skip 

```python
# 검색 결과 앞에 n개 만큼 건너뜀
docs = test_insert_collection.find(
  {'age' : {'$nin' : [20, 21, 25, 27]}}
).skip(3)
```

#### limit 

```python 
# 검색결과 개수 제한 (n개만 출력)
docs = test_insert_collection.find(
  {'age' : {'$nin' : [20, 21, 25, 27]}}
).limit(3)
```



## python list search 

검색 결과에서 특성 컬럼의 값만을 얻고 싶은 경우, 단순히 python 리스트를 for 문으로 iterate 하면서 값을 얻어내면 된다. 

```python
# 배우들 중, 범죄도시에 출연한 배우들의 이름만 출력
for doc in actor_collection.find({'movie_list' : '범죄도시'}):
    print(doc['actor_name'])
```

리스트로 비교하기 위해선, 값 뿐만 아니라 순서까지 정확히 일치해야 한다. 

```python
# 결과 없음
for doc in actor_collection.find({'movie_list' : ['부라더', '범죄도시']}):
    print(doc['actor_name'])
```

- python list 비교 시 순서까지 같아야 한다

만약 순서에 관계 없이 찾고자 하는 경우 `$all`

```python
for doc in actor_collection.find({'movie_list' : {'$all' :  ['부라더', '범죄도시'] }} ):
    print(doc['actor_name'])
```

### etc

`$elemMatch` : 적어도 한 개의 원소가 모든 조건을 만족하는 경우 

```python
score.find({'results' :  {'$elemMatch' : { '$gte': 80, '$lt': 85 }}})
```

인덱스 특정하여 검색하기 

```python
# movie_list 의 0번째 원소가 범죄도시인 경우에만
actor_collection.find({'movie_list.0' : '범죄도시'} )
```

`$size`: 리스트 개수로 검색

```python
actor_collection.find({'movie_list' : {'$size' : 3}} )
```



## Update

`upsert=True`

- update 시 option 
- 찾지 못한 경우, insert

```python 
result = actor_collection.update_one({'actor_name' : '류승룡'}, 
                           {'$set' : {'actor_name' : '류승룡', 'actor_rate' : 42230}}, 
                           upsert=True)
```

`upserted_id` 

```python
result.upserted_id
```

