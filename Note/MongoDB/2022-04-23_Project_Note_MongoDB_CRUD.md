# mongoDB 02 : CRUD

>[NoSQL DB (몽고DB/mongodb) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/nosql-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AA%BD%EA%B3%A0db-%EC%9E%94%EC%9E%AC%EB%AF%B8%EC%BD%94%EB%94%A9/dashboard)

위 강의를 듣고 정리한 내용입니다. 

## Document CRUD 

### insert 

**insertOne**

```bash
db.users.insertOne({
	name: "sue", 
	age: 26,
	status: "pending",
})
```

same as 

```sql
INSERT INTO people (user_id, age, statue) 
VALUES ("bcd001", 45, "A")
```

**insertMany**

```bash
db.articles.insertMany(
   [
     { subject: "coffee", author: "xyz", views: 50 },
     { subject: "Coffee Shopping", author: "efg", views: 5 },
     { subject: "Baking a cake", author: "abc", views: 90  },
     { subject: "baking", author: "xyz", views: 100 },
     { subject: "Café Con Leche", author: "abc", views: 200 },
     { subject: "Сырники", author: "jkl", views: 80 },
     { subject: "coffee and cream", author: "efg", views: 10 },
     { subject: "Cafe con Leche", author: "xyz", views: 10 },
     { subject: "coffees", author: "xyz", views: 10 },
     { subject: "coffee1", author: "xyz", views: 10 }
   ]
)
```

### Read 

**findOne, find**

```bash
db.users.find(
	{ age: { $gt: 18 } },
	{ name: 1, adress: 1 }
).limit(5)

# SELECT * FROM people
db.people.find() 

# SELECT * FROM people
db.people.find()

# SELECT _id, user_id, status FROM people
db.people.find({ }, { user_id: 1, status: 1 })

# SELECT user_id, status FROM people
db.people.find({ },{ _id: 0, user_id: 1, status: 1, }) 

# SELECT * FROM people WHERE status = "A"
db.people.find({ status: "A" })

# SELECT * FROM people WHERE status = "A" AND age = 50
db.people.find({ status: "A", age: 50 })

# SELECT * FROM people WHERE status = "A" OR age = 50
db.people.find({ $or: [ { status: "A" } , { age: 50 } ] })
```

#### 비교 문법

`$eq`     =    Matches values that are equal to a specified value.
`$gt`    >    Matches values that are greater than a specified value.
`$gte`    >=   Matches values that are greater than or equal to a specified value.

`$lt`     <    Matches values that are less than a specified value.
`$lte`    <=   Matches values that are less than or equal to a specified value.
`$ne`     !=   Matches all values that are not equal to a specified value.
`$in`          Matches any of the values specified in an array.
`$nin`         Matches none of the values specified in an array.

ex)

```bash
# - SELECT * FROM people WHERE age > 25
db.people.find({ age: { $gt: 25 } })

#  - SELECT * FROM people WHERE age < 25
db.people.find({ age: { $lt: 25 } })

# - SELECT * FROM people WHERE age > 25 AND age <= 50
db.people.find({ age: { $gt: 25, $lte: 50 } })

# - SELECT * FROM people WHERE age = 5 or age = 15
db.people.find( { age: { $nin: [ 5, 15 ] } } ))

# - SELECT * FROM people WHERE user_id like "%bc%"
db.people.find( { user_id: /bc/ } )
db.people.find( { user_id: { $regex: /bc/ } } )
                                               
# - SELECT * FROM people WHERE user_id like "bc%"
db.people.find( { user_id: /^bc/ } )
db.people.find( { user_id: { $regex: /^bc/ } } )

# - SELECT * FROM people WHERE status = "A" ORDER BY user_id ASC                                                   
db.people.find( { status: "A" } ).sort( { user_id: 1 } ) 

# - SELECT * FROM people WHERE status = "A" ORDER BY user_id DESC
db.people.find( { status: "A" } ).sort( { user_id: -1 } ) 

# SELECT COUNT(*) FROM people
db.people.count()
db.people.find().count()
                                      
# - SELECT COUNT(user_id) FROM people                                      
db.people.count( { user_id: { $exists: true } } )
db.people.find( { user_id: { $exists: true } } ).count()

# - SELECT COUNT(*) FROM people WHERE age > 30
db.people.count( { age: { $gt: 30 } } )
db.people.find( { age: { $gt: 30 } } ).count()
                              
# - SELECT DISTINCT(status) FROM people
db.people.distinct( "status" )

# - SELECT * FROM people LIMIT 1 
db.people.findOne()
db.people.find().limit(1)
```

### Update

**updateOne, updateMany**

- `$set` : field 값 설정 
- `$inc` : field 값 증가 감소

```bash
# - UPDATE people SET status = "C" WHERE age > 25
db.people.updateMany( 
	{ age: { $gt: 25 } }, 
	{ $set: { status: "C" } } 
)
# document 하나만 수정하려면 updata One

# - UPDATE people SET age = age + 3 WHERE status = "A"
db.people.updateMany( 
	{ status: "A" }, 
	{ $inc: { age: 3 } } 
)
```

### Delete 

**removeOne, removeMany**

```bash
# DELETE FROm people WHERE status = "D"
db.people.deleteMany({	status: "D" })

# DELETE FROM people
db.people.deleteMany({})
```

