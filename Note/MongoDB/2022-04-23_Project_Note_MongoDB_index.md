# mongoDB 04 : INDEX

>[NoSQL DB (몽고DB/mongodb) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/nosql-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AA%BD%EA%B3%A0db-%EC%9E%94%EC%9E%AC%EB%AF%B8%EC%BD%94%EB%94%A9/dashboard)

위 강의를 듣고 정리한 내용입니다. 

## INDEX

>https://docs.mongodb.com/manual/indexes/

- SQL index 와 동일한 개념으로, 검색을 더 빠르게 수행하고자 만드는 추가적인 data structure!
- index 가 없는 경우, collection scan 으로 document 를 하나하나 조회하는 방식으로 검색한다. 
- index 를 등록할 시, document 를 가리키는 포인터 값으로 이루어진 B-Tree 데이터 구조를 생성한다. 
  - B-Tree : Balanced Binary Search Tree, Binary Search 로 조회 속도가 빠르다.

- MongoDB 의 모든 컬렉션은 기본적으로 `_id` 필드에 인덱스가 존재한다. (`_id` 를 기반으로 기본 인덱스를 생성)

**Single field index**

`_id` 외에도, 사용자가 지정할 수 있는 단일 필드 인덱스 

```bash
db.COLLECTION.createIndex(
	{ 'field': 1 }
)

# or 

db.COLLECTION.createIndex(
	{ 'field': -1 }
)
```

- key 의 value 에는 1, -1 둘 중 하나를 부여 
- ASCENDING, DESCENDING 

**Compound field index**

2개 이상의 필드를 사용하는 인덱스 

```bash 
db.COLLECTION.createIndex(
	{ 'field1': 1 },
	{ 'field2': -1 }
)
```

- 위 경우처럼 방향을 서로 반대로 한 경우, `db.x.find({a:1,b:1})`, `db.x.find({a:-1,b:-1})` 쿼리에는 효과가 없다. 

**text index**

```bash
db.COLLECTION.createIndex(
	{ 'field': 'text' },
)
```

- 텍스트 관련 데이터의 효율적인 쿼리가 가능 

python 에서 다음과 같이 사용

```python 
db.articles.create_index([('name', pymongo.TEXT)])


# coffee 포함
result = db.articles.find({'$text' : {'$search' : 'coffee'}})

# java || coffee || shop 포함 
result = db.articles.find({'$text' : {'$search' : 'java coffee shop'}})


# coffee shop 으로 정확한 검색
result = db.articles.find({'$text': {'$search':"\"coffee shop\"" } } )

# 대소문자 구별 
result = db.articles.find({'$text' : {'$search' : 'coffee', '$caseSensitive' : True}})

# 정규표현식 
result = db.articles.find({'name' : {'$regex' : 'Cof.+'}})
```





