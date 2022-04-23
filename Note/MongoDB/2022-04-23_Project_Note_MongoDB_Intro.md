# mongoDB 01 : Intro 

>[NoSQL DB (몽고DB/mongodb) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/nosql-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AA%BD%EA%B3%A0db-%EC%9E%94%EC%9E%AC%EB%AF%B8%EC%BD%94%EB%94%A9/dashboard)

위 강의를 듣고 정리한 내용입니다. 

## 1. Intro 

- Not only SQL
- RDBMS의 한계를 극복하기 위해 만들어진 새로운 형태의 데이터저장소
- RDBMS처럼 고정된 스키마 및 JOIN 이 존재하지 않음
  - Schema, Table, Column 과 같이 정해진 규격이 없고, Join 이 불가능하며, 트랜잭션을 사용하지 않는다. 
  - 분산처리가 쉽다. 
- 스키마 변경? ALERT 등 필요 없음

**1.1. Why NoSQL?**

- RDBMS를 기본으로 사용하지만,
- 초당 데이터가 수십만개씩 쌓이는 서비스가 많아지면서(쇼셜, 온라인 서비스등), NoSQL을 사용하는 경우가 많아지고 있음
- 경험적 수치
  - 95% read, 5% write 경우는 RDBMS 가 성능이 나쁘지 않음
  - 50% write > 인 경우 RDBMS는 성능 저하 또는 불안정
  - NoSQL + Redis (In memory cache) 등을 고려하게 됨

* 관계형 데이터베이스 종류
  - MySQL, Oracle, PostgreSQL, SQLlite

* NoSQL 데이터베이스는 각 데이터베이스마다 기반으로 하는 데이터 모델이 다르므로, 데이터 모델별로 대표적인 데이터베이스를 알아둘 필요가 있음
  - 각기 데이터베이스 다루는 인터페이스가 다름
    - Key/Value Store : redis, riak
    - Wide Column Store : HBASE, cassandra
    - Document Store : mongoDB, CouchDB
    - Graph Store : Neo4j, intifiniteGraph 

    

**1.2 mongoDB ? **

* mongoDB는 document db
  - JSON 기반의 Document 기반 데이터 관리
  
  - ex)
  
    ```json
    {
        "_id": ObjectId("5099803df3f42312312391"),
        "username": "davelee",
        "name": { first: "Dave", last: "Lee" }
    }
    ```

**1.3 MongoDB 데이터 구조**

- RDMBS
  - Database - Table - data

MongoDB 

- Database
  - Collection (table 대신)
    - Document (low 대신, column 개념은 없다.)

Collection 에 JSON 형태의 Document (하나의 record) 를 넣는다. 



## 2. Install 

**2.1 mac => Homebrew**

`brew intsall mongodb`

`mongod` or `brew services start mongodb`

**2.2 windows**

​		https://www.mongodb.com/download-center/community

**2.3 AWS EC2 (ubuntu)** 

설치

* Import the public key(GPG key) used by the package management system.
  - sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
* Create a list file for MongoDB.
  - echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
* Reload local package database.
  - sudo apt-get update
* Install the MongoDB packages.
  - sudo apt-get install -y mongodb-org
  - mpngodb-org 패키지: A metapackage that will automatically install the four component packages, mongodb-org-server, mongodb-org-mongos, mongodb-org-shell, and mongodb-org-tools
  - The MongoDB instance stores its data files in /var/lib/mongodb and its log files in /var/log/mongodb by default, and runs using the mongodb user account. You can specify alternate log and data file directories in /etc/mongod.conf.
* Start MongoDB
  - sudo service mongod start
* Verify that MongoDB has started successfully
  - Verify that the mongod process has started successfully by checking the contents of the log file at /var/log/mongodb/mongod.log for a line reading
  - [initandlisten] waiting for connections on port <port>
  - where <port> is the port configured in /etc/mongod.conf, 27017 by default.
* Stop MongoDB
  - sudo service mongod stop

------

설정 

* AWS Management Console -> EC2 -> Security Groups -> EC2's Security Group -> Add Custom TCP Rule, 27017, AnyWhere

* 외부 접속 허용
  - sudo vi /etc/mongod.conf
    - bindIp: 0.0.0.0   으로 변경
  - sudo service mongod restart

* 계정을 만들어야 함 (그렇지 않으면 외부에서 해당 포트/주소로 아무나 접속이 가능하기 때문)
  - EC2 에서 다음 명령 실행

    ```bash
    mongo
    use admin
    db.createUser( 
        {   user: "davelee",
            pwd: "korea123",
            roles: [ "userAdminAnyDatabase",
            "dbAdminAnyDatabase",
            "readWriteAnyDatabase"] 
        } 
    )
    
    security:
      authorization: enabled
      
      - sudo service mongod restart
    ```

### Basic use 

#### Robomongo

- mongoDB 관리 GUI tool 
- https://robomongo.org/download

아래 document 를 insert 

```json
{
    "name"  : "Dave Lee",
    "age"   : 22,
    "major" : "CS"
}
{
    "name"  : "David Oh",
    "age"   : 24,
    "major" : "Japanense"
}
```

- GUI 에서 _id, name, age, major 4개의 컬럼이 생성된 것을 확인 
- 실제로 mongoDB 에 컬럼의 개념은 없다. 

아래 document 를 추가 

```json
{
    "name"     : "이종수",
    "age"      : 54,
    "minor"    : "CS",
    "nickname" : "wink"
}
```

- minor, nickname 이 추가로 생성된 것을 확인 가능하다. 

#### Shell Commands

```bash
# mongo shell 시작 
$ mongo # local 
$ mongo -- host 'host_address' --port 'port' # remote

# 전체 DB 열람
show dbs 

# DB 선택 (없을 시 생성)
use [DB name]

# 선택한 DB 의 컬렉션 열람
show collections 

# DB 현황 확인
db 
db.stats()

# collection 생성 및 삭제 
# capped : 제한된 크기로 컬렉션 생성, 저장 공간이 차면 기존 공간을 재사용하므로, 일정 시간 동안만 저장하는 로그에 적합
db.createCollection("employees", {capped:true, size:10000})
db.employees.isCapped()
db.employees.drop()

# 아래 방법으로 해당 컬렉션의 데이터 열람 및 조작 
db.[Collection name].함수() 
db.employees.state()
db.employees.renameCollection("emp")
db.emp.drop()
```

-----

1. SQL 과 비교하여, mongoDB collection 의 생성/변경은 

- PRIMARY KEY 를 위한 별도의 컬럼을 만들 필요가 없다. 
  - collection 에서 `_id` 가 document 마다 자동으로 생성되어 pk 역할을 한다. 
- 컬럼마다 데이터 타입을 정할 필요가 없다. 

따라서, SQL 에서 최초에 `CREATE TALBE` 로 테이블을 생성하며 타입과 PK 를 설정해주어야 하는 것에 반해, mongoDB 에선 바로 아래와 같이 컬렉션 생성이 가능하다. 

```sql
CREATE TABLE people (
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
  user_id Varchar(30),
  age Number, 
  status char(1),
  PRIMARY KEY (id)
)
```

```bash
# insertOne or insertMany
db.people.insertOne({
	user_id: "abc123",
  age: 55,
  status: "A"
})

# createCollection 
db.createCollection("people")
```

2. collection 구조 변경 

기존 Document 의 컬럼을 변경하는 것이 아니라, 새로운 Document 에 필요한 새로운 컬럼을 자유롭게 추가 / 삭제하여 넣으면 된다. (ALTER TABLE 이 필요 없다.) 

만약 기존 Document 에 컬럼을 변경해야 할 경우 

- SQL 

```sql
ALTER TABLE people 
ADD COLUMN join_data DATETIME 
```

- mongodb

```bash
db.people.updataMany({}, {
	$unset: {
		"join_date": ""
	}
})
```



#### pymongo library 

with python 

```bash 
$ pip install pymongo
```

connect

```python
import pymongo

# conn = pymongo.MongoClient()
conn = pymongo.MongoClient('mongodb://13.209.140.30')
```

- 이후 명령어는 생략.. (python 으로 사용할 일이 아직까지 없다.)
