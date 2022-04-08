# 概念对比
|SQL Terms/Concepts |MongoDB Terms/Concepts|
| --------  | :-----  |
|database   |  database|
|table      |   collection|
|row        |document or BSON document|
|column     |field|
|index      |index|
|table joins|$lookup, embedded documents|
|primary key :Specify any unique column or column combination as primary key.|primary key:In MongoDB, the primary key is automatically set to the _id field.|
|aggregation (e.g. group by)| aggregation pipeline:See the SQL to Aggregation Mapping Chart.|
|SELECT INTO NEW_TABLE|$out:See the SQL to Aggregation Mapping Chart.|
|MERGE INTO TABLE|$merge (Available starting in MongoDB 4.2):See the SQL to Aggregation Mapping Chart.|
|UNION ALL|$unionWith (Available starting in MongoDB 4.4)|
|transactions|transactions|

# create/alter语法对比
1. 创建
   1. > CREATE TABLE people (
    id MEDIUMINT NOT NULL
        AUTO_INCREMENT,
    user_id Varchar(30),
    age Number,
    status char(1),
    PRIMARY KEY (id)
    )
    2. 隐式创建
        > db.people.insertOne( {
        user_id: "abc123",
        age: 55,
        status: "A"
        } )
    3. 显示创建
        > db.createCollection("people")
2. 修改表结构
   1. SQL
        > ALTER TABLE people
        ADD join_date DATETIME
   2.  mongo不强制要求表的字段结构，但是可通过统一update来增加字段
        > db.people.updateMany(
            { },
            { $set: { join_date: new Date() } }
        )
3. 创建index
   1. SQL
        > CREATE INDEX idx_user_id_asc
            ON people(user_id)
   2. Mongo
        > db.people.createIndex( { user_id: 1 } )
   3. SQL
        > CREATE INDEX
        idx_user_id_asc_age_desc
        ON people(user_id, age DESC)
   4. Mongo 
        > db.people.createIndex( { user_id: 1, age: -1 } )
4. 删除drop
   1. SQL
        > DROP TABLE people
   2. Mongo
        > db.people.drop()

# insert/insertOne/insertMany
1. SQL
    > INSERT INTO people(user_id, age, status)
        VALUES ("bcd001", 45, "A")
2. Mongo
    > db.people.insertOne(
    { user_id: "bcd001", age: 45, status: "A" }
    )


# select/find
1. 
    1. > SELECT * FROM people
    2. > db.people.find()
2. 字段选择，注意：mongo默认查询_id
    1. > SELECT id, user_id, status FROM people
    2. > db.people.find(
        { },
        { user_id: 1, status: 1 }
        )
    3. > SELECT user_id, status FROM people
    4. > db.people.find(
        { },
        { user_id: 1, status: 1, _id: 0 }
        )
3. where
   1. > SELECT * FROM people
        WHERE status = "A"
   2. > db.people.find( { status: "A" }  )


4. 指定字段和条件
   1. > SELECT user_id, status FROM people
        WHERE status = "A"
   2. > db.people.find(
        { status: "A" },
        { user_id: 1, status: 1, _id: 0 }
        )
5. !=/$ne
   1. > SELECT * FROM people WHERE status != "A"
   2. > db.people.find(
       { status: { $ne: "A" } }
        )
6. AND/,
   1. > SELECT * FROM people
        WHERE status = "A" AND age = 50
   2. > db.people.find(
        { status: "A", age: 50 }
        )
7. OR/$or
   1. > SELECT * FROM people
        WHERE status = "A" OR age = 50
   2. > db.people.find(
        { $or: [ { status: "A" } , { age: 50 } ] }
        )
8. >/$gt
   1. > SELECT * FROM people
        WHERE age > 25
   2. > db.people.find(
            { age: { $gt: 25 } }
        )
9. </$lt
   1.  > SELECT * FROM people
         WHERE age < 25
   2.  > db.people.find(
        { age: { $lt: 25 } }
        )
10. d
    1. > SELECT * FROM people
            WHERE age > 25 AND   age <= 50
    2. > db.people.find(
        { age: { $gt: 25, $lte: 50 } }
        )
11. like
    1. > SELECT * FROM people
        WHERE user_id like "%bc%"
       1. > db.people.find( { user_id: /bc/ } )
       2. > db.people.find( { user_id: { $regex: /bc/ } } )
    2. > SELECT * FROM people
        WHERE user_id like "bc%"
       1. > db.people.find( { user_id: /^bc/ } )
       2. > db.people.find( { user_id: { $regex: /^bc/ } } )
12. order by
    1. > SELECT * FROM people
            WHERE status = "A"
            ORDER BY user_id ASC
       1. > db.people.find( { status: "A" } ).sort( { user_id: 1 } )
    2. > SELECT * FROM people WHERE status = "A"
            ORDER BY user_id DESC
       1. > db.people.find( { status: "A" } ).sort( { user_id: -1 } )
13. count()
    1. > SELECT COUNT(*) FROM people
       1. > db.people.count()
        db.people.find().count()
    
    2. > SELECT COUNT(user_id) FROM people
       1. > db.people.count( { user_id: { $exists: true } } )
       2. > db.people.find( { user_id: { $exists: true } } ).count()

    3. > SELECT COUNT(*) FROM people
        WHERE age > 30
       1. > db.people.count( { age: { $gt: 30 } } )
       2. > db.people.find( { age: { $gt: 30 } } ).count()
14. distinct
    1.  > SELECT DISTINCT(status) FROM people
        1.  > db.people.aggregate( [ { $group : { _id : "$status" } } ] )
        2.  > db.people.distinct( "status" )
15. limit/skip
    1.  > SELECT * FROM people LIMIT 1
        1. > db.people.findOne()
        2. > db.people.find().limit(1)
    2. > SELECT * FROM people LIMIT 5 SKIP 10 
       1. > db.people.find().limit(5).skip(10)
16. explain
    1.  > EXPLAIN SELECT * FROM people WHERE status = "A"
        1. > db.people.find( { status: "A" } ).explain()

# Update Records
1. > UPDATE people SET status = "C"
    WHERE age > 25
    1. > db.people.updateMany(
        { age: { $gt: 25 } } , 
{ $set: { status: "C" } }
    )
2. > UPDATE people SET age = age + 3
    WHERE status = "A"
    1. > db.people.updateMany(
        { status: "A" } ,
        { $inc: { age: 3 } }
        )

# delete
1. > DELETE FROM people WHERE status = "D"
    1. > db.people.deleteMany( { status: "D" } )
2. > DELETE FROM people
   1. > db.people.deleteMany({})
