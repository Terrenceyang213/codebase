# 控制台常用指令

## 数据库
    一个mongodb中可以建立多个数据库。

    MongoDB的默认数据库为"db"，该数据库存储在data目录中。

    MongoDB的单个实例可以容纳多个独立的数据库，每一个都有自己的集合和权限，不同的数据库也放置在不同的文件中。

### 启动控制台
> mongo


### 现实已有数据库
> show dbs
admin       0.000GB
local       0.000GB
quantaxis  30.986GB
runoob      0.000GB

### 显示当前数据库对象或集合。
> db
test

### 连接到指定数据库/创建数据库
1. link
> use local
switched to db local

2. create db
> use learnmg
switched to db learnmg
> show dbs
admin       0.000GB
local       0.000GB
quantaxis  30.986GB
runoob      0.000GB

可以看到，我们刚创建的数据库 runoob 并不在数据库的列表中， 要显示它，我们需要向 runoob 数据库插入一些数据。

> db.learnmg.insert({"name":"yh"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin       0.000GB
learnmg     0.000GB
local       0.000GB
quantaxis  30.986GB
runoob      0.000GB

### 删除数据库
> db
learnmg
> db.dropDatabase()
{ "dropped" : "learnmg", "ok" : 1 }
> show dbs
admin       0.000GB
local       0.000GB
quantaxis  30.986GB
runoob      0.000GB



### 特殊数据库
- admin： 从权限的角度来看，这是"root"数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。
- local: 这个数据永远不会被复制，可以用来存储限于本地单台服务器的任意集合
- config: 当Mongo用于分片设置时，config数据库在内部使用，用于保存分片的相关信息。


## 集合

    集合就是 MongoDB 文档组，类似于 RDBMS （关系数据库管理系统：Relational Database Management System)中的表格。

    集合存在于数据库中，集合没有固定的结构，这意味着你在对集合可以插入不同格式和类型的数据，但通常情况下我们插入集合的数据都会有一定的关联性。

    比如，我们可以将以下不同数据结构的文档插入到集合中：

    {"site":"www.baidu.com"}
    {"site":"www.google.com","name":"Google"}
    {"site":"www.runoob.com","name":"菜鸟教程","num":5}

### 创建集合
- db.createCollection(name, options)
    1. name: 要创建的集合名称
    2. options: 可选参数, 指定有关内存大小及索引的选项
        1. capped:  布尔 	（可选）如果为 true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。当该值为 true 时，必须指定 size 参数。
        2. size 	数值 	（可选）为固定集合指定一个最大值，即字节数。如果 capped 为 true，也需要指定该字段。
        3. max 	    数值 	（可选）指定固定集合中包含文档的最大数量。
1. 
> use learnmg
switched to db learnmg
> db
learnmg
> db.createCollection("yh")
{ "ok" : 1 }
> show collections
yh

2. 
创建固定集合 mycol，整个集合空间大小 6142800 B, 文档最大个数为 10000 个。
> db.createCollection("mycol", { capped : true, autoIndexId : true, size : 
   6142800, max : 10000 } )
{ "ok" : 1 }


3. 
在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。
> db.mycol2.insert({"name" : "菜鸟教程"})
> show collections
mycol2
...

### 删除集合

- db.collection.drop()

1. 
> show collections
col2
yh
> db.col2.drop()
true
> show collections
yh

## 文档(Document)

    文档是一组键值(key-value)对(即 BSON)。MongoDB 的文档不需要设置相同的字段，并且相同的字段不需要相同的数据类型，这与关系型数据库有很大的区别，也是 MongoDB 非常突出的特点。

    一个简单的文档例子如下：
    `{"site":"www.runoob.com", "name":"菜鸟教程"}`


    1. 文档中的键/值对是有序的。
    2. 文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
    3. MongoDB区分类型和大小写。
    4. MongoDB的文档不能有重复的键。
    5. 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。

### 插入文档

MongoDB 使用 insert() 或 save() 方法向集合中插入文档，语法如下：

1. db.COLLECTION_NAME.insert(document)
2. db.COLLECTION_NAME.save(document)
   1. save()：如果 _id 主键存在则更新数据，如果不存在就插入数据。该方法新版本中已废弃，可以使用 db.collection.insertOne() 或 db.collection.replaceOne() 来代替。
   2. insert(): 若插入的数据主键已经存在，则会抛 org.springframework.dao.DuplicateKeyException 异常，提示主键重复，不保存当前数据。
3. db.collection.insertOne() 用于向集合插入一个新文档
    1. 语法 
        > db.collection.insertOne(
         < document >,
            {
                writeConcern: <document>
            }
        )
4. db.collection.insertMany() 用于向集合插入一个多个文档
    1. 语法
        > db.collection.insertMany(
        [ <document 1> , <document 2>, ... ],
            {
                writeConcern: <document>,
                ordered: <boolean>
            }
        )
    2. document：要写入的文档。
    3. writeConcern：写入策略，默认为 1，即要求确认写操作，0 是不要求。
    4. ordered：指定是否按顺序写入，默认 true，按顺序写入。


5. 例子：
    >db.col.insert({title: 'MongoDB 教程', 
        description: 'MongoDB 是一个 Nosql 数据库',
        by: '菜鸟教程',
        url: 'http://www.runoob.com',
        tags: ['mongodb', 'database', 'NoSQL'],
        likes: 100
    })
    > db.col.find()
    { "_id" : ObjectId("61bc7e59c98c9e9ecaf6eb99"), "title" : "MongoDB 教程", "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }

6. 变量插入
    > document=({title: 'MongoDB 教程',
    ...     description: 'MongoDB 是一个 Nosql 数据库',
    ...     by: '菜鸟教程',
    ...     url: 'http://www.runoob.com',
    ...     tags: ['mongodb', 'database', 'NoSQL'],
    ...     likes: 100
    ... });
    {
            "title" : "MongoDB 教程",
            "description" : "MongoDB 是一个 Nosql 数据库",
            "by" : "菜鸟教程",
            "url" : "http://www.runoob.com",
            "tags" : [
                    "mongodb",
                    "database",
                    "NoSQL"
            ],
            "likes" : 100
    }
    > db.col.insert(document)
    WriteResult({ "nInserted" : 1 })
7. 插入单条数据
    > var document = db.collection.insertOne({"a": 3})
    > document
    {
            "acknowledged" : true,
            "insertedId" : ObjectId("571a218011a82a1d94c02333")
    }

8. 插入多条数据
    > var res = db.collection.insertMany([{"b": 3}, {'c': 4}])
    > res
    {
            "acknowledged" : true,
            "insertedIds" : [
                    ObjectId("571a22a911a82a1d94c02337"),
                    ObjectId("571a22a911a82a1d94c02338")
            ]
    }

### 更新文档

1. update() 方法用于更新已存在的文档。语法格式如下：
    1. 语法
        > db.collection.update(
        <query>,
        <update>,
            {
                upsert: <boolean>,
                multi: <boolean>,
                writeConcern: <document>
            }
        )
    2. query : update的查询条件，类似sql update查询内where后面的。
    3. update : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
    4. upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
    5. multi : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
    6. writeConcern :可选，抛出异常的级别。
2. 更新实例
   1. 插入一条doc
        > db.col.insert({
            title: 'MongoDB 教程', 
            description: 'MongoDB 是一个 Nosql 数据库',
            by: '菜鸟教程',
            url: 'http://www.runoob.com',
            tags: ['mongodb', 'database', 'NoSQL'],
            likes: 100
        })
   2. 更新
        > db.col.update({'title':'MongoDB 教程'},{$set:{'title':'MongoDB'}})
        WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })   # 输出信息
        > db.col.find().pretty()
        {
            "_id" : ObjectId("56064f89ade2f21f36b03136"),
            "title" : "MongoDB",
            "description" : "MongoDB 是一个 Nosql 数据库",
            "by" : "菜鸟教程",
            "url" : "http://www.runoob.com",
            "tags" : [
                    "mongodb",
                    "database",
                    "NoSQL"
            ],
            "likes" : 100
        }


### 删除文档

1. db.collection.remove
   1. 语法
        > db.collection.remove(
        <query>,
            {
                justOne: <boolean>,
                writeConcern: <document>
            }
        )
   2. query :（可选）删除的文档的条件。
   3. justOne : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。
   4. writeConcern :（可选）抛出异常的级别。
2. db.collection.deleteMany({})
   1. 语法
3. db.collection.deleteOne({})
   1. 语法
4. db.collection.remove实例
   1. 插入两条同样的数据
        > db.col.insert({title: 'MongoDB 教程', 
            description: 'MongoDB 是一个 Nosql 数据库',
            by: '菜鸟教程',
            url: 'http://www.runoob.com',
            tags: ['mongodb', 'database', 'NoSQL'],
            likes: 100
        })
        > db.col.find().pretty()
        {
                "_id" : ObjectId("61bc7e59c98c9e9ecaf6eb99"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }
        {
                "_id" : ObjectId("61bc7eeac98c9e9ecaf6eb9a"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }
        {
                "_id" : ObjectId("61bc8608c98c9e9ecaf6eb9b"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }
   2. 删除一条数据
        > db.col.remove({'title':'MongoDB 教程'},justOne=true)
        WriteResult({ "nRemoved" : 1 })
        > db.col.find().pretty()
        {
                "_id" : ObjectId("61bc7eeac98c9e9ecaf6eb9a"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }
        {
                "_id" : ObjectId("61bc8608c98c9e9ecaf6eb9b"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }
5. db.collection.deleteOne({})实例
   1. 删除
        > db.col.deleteOne( {'title':'MongoDB 教程' )
        { "acknowledged" : true, "deletedCount" : 1 }
        > db.col.find().pretty()
        {
                "_id" : ObjectId("61bc8608c98c9e9ecaf6eb9b"),
                "title" : "MongoDB 教程",
                "description" : "MongoDB 是一个 Nosql 数据库",
                "by" : "菜鸟教程",
                "url" : "http://www.runoob.com",
                "tags" : [
                        "mongodb",
                        "database",
                        "NoSQL"
                ],
                "likes" : 100
        }



### 查询文档

1. 查询格式
   1. 语法
        > db.collection.find(query, projection)
   2. query ：可选，使用查询操作符指定查询条件
   3. projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。
   4. 如果你需要以易读的方式来读取数据，可以使用 pretty() 方法，语法格式如下：
        > db.collection.find().pretty()

#### 比较条件

1. 比较条件格式
   1. 等于 -        {<key>:<value>}        - db.col.find({"by":"菜鸟教程"}).pretty()      - where by = '菜鸟教程'
   2. 小于 -        {<key>:{$lt:<value>}}  - db.col.find({"likes":{$lt:50}}).pretty()    - where likes < 50
   3. 小于或等于 -  {<key>:{$lte:<value>}}  - db.col.find({"likes":{$lte:50}}).pretty()   - where likes <= 50
   4. 大于 -        {<key>:{$gt:<value>}}  - db.col.find({"likes":{$gt:50}}).pretty()    - where likes > 50
   5. 大于或等于 -  {<key>:{$gte:<value>}} - db.col.find({"likes":{$gte:50}}).pretty()    - where likes >= 50
   6. 不等于    -	{<key>:{$ne:<value>}}  - db.col.find({"likes":{$ne:50}}).pretty() 	- where likes != 50

#### 逻辑操作符
1. 逻辑AND：MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，即常规 SQL 的 AND 条件。
   1. db.col.find({key1:value1, key2:value2}).pretty()
   2. 等价于WHERE key1=value1 AND key2=value2
2. 逻辑OR
   1. > db.col.find({$or: [{key1: value1}, {key2:value2}]}
3. AND 与 OR连用
   1. > db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
   2. 等价于where likes>50 AND (by = '菜鸟教程' OR title = 'MongoDB 教程')
   
#### 案例应用
4. 实例
   1. 样例数据
        > db.col.insert({
        ...     title: 'PHP 教程',
        ...     description: 'PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。',
        ...     by: '菜鸟教程',
        ...     url: 'http://www.runoob.com',
        ...     tags: ['php'],
        ...     likes: 200
        ... })
        > db.col.insert({title: 'Java 教程',
        ...     description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
        ...     by: '菜鸟教程',
        ...     url: 'http://www.runoob.com',
        ...     tags: ['java'],
        ...     likes: 150
        ... })
        > db.col.insert({title: 'MongoDB 教程',
        ...     description: 'MongoDB 是一个 Nosql 数据库',
        ...     by: '菜鸟教程',
        ...     url: 'http://www.runoob.com',
        ...     tags: ['mongodb'],
        ...     likes: 100
        ... })
   2. 全部获取
      1. > db.col.find()
      2. select * from col;
      3. > db.col.find({},{"title":1})
      4. select title from col; 会带有_id字段
      5. > db.col.find({},{"title":1,_id:0})
      6. select title from col; 不带有_id字段
   3. 大于条件
      1. > db.col.find({likes : {$gt : 100}})
      2. Select * from col where likes > 100;
      3. > db.col.find({likes : {$gte : 100}})
      4. Select * from col where likes >=100;
   4. 小于条件
      1. > db.col.find({likes : {$lt : 150}})
      2. Select * from col where likes < 150;
      3. > db.col.find({likes : {$lte : 150}})
      4. Select * from col where likes <= 150;
   5. 联合逻辑条件
      1. > db.col.find({likes : {$lt :200, $gt : 100}})
      2. Select * from col where likes>100 AND  likes<200;
      3. > db.col.find({"by":"菜鸟教程", "title":"MongoDB 教程"}).pretty()
      4. select * from col where by = "菜鸟教程" and title = "MongoDB 教程"
      5. > db.col.find({$or:[{"by":"菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
      6. select * from col where by = "菜鸟教程" or title = "MongoDB 教程"
      7. > db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
      8. select * from col where likes > 50 and (by = "菜鸟教程" or title = "MongoDB 教程");

#### $type 操作符
类型 	数字 	备注
Double 	1 	 
String 	2 	 
Object 	3 	 
Array 	4 	 
Binary data 	5 	 
Undefined 	6 	已废弃。
Object id 	7 	 
Boolean 	8 	 
Date 	9 	 
Null 	10 	 
Regular Expression 	11 	 
JavaScript 	13 	 
Symbol 	14 	 
JavaScript (with scope) 	15 	 
32-bit integer 	16 	 
Timestamp 	17 	 
64-bit integer 	18 	 
Min key 	255 	Query with -1.
Max key 	127 	 

> db.col.find({"title" : {$type : 2}})
{ "_id" : ObjectId("61bc8db6c98c9e9ecaf6eb9c"), "title" : "PHP 教程", "description" : "PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "php" ], "likes" : 200 }
{ "_id" : ObjectId("61bc8dbcc98c9e9ecaf6eb9d"), "title" : "Java 教程", "description" : "Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "java" ], "likes" : 150 }
{ "_id" : ObjectId("61bc8dc7c98c9e9ecaf6eb9e"), "title" : "MongoDB 教程", "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb" ], "likes" : 100 }
> db.col.find({"title" : {$type : 'string'}})

#### limit/skip
1. limit : 如果你需要在MongoDB中读取指定数量的数据记录，可以使用MongoDB的Limit方法，limit()方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。
   1. > db.col.find({},{"title":1,_id:0})
   2. select title from col;
       { "title" : "PHP 教程" }
       { "title" : "Java 教程" }
       { "title" : "MongoDB 教程" }
   3. > db.col.find({},{"title":1,_id:0}).limit(2)
   4. select limit 2 title from col
       { "title" : "PHP 教程" }
       { "title" : "Java 教程" }
2. skip: 我们除了可以使用limit()方法来读取指定数量的数据外，还可以使用skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。
   1. > db.col.find({},{"title":1,_id:0}).limit(1).skip(1)
        > db.col.find({},{"title":1,_id:0}).limit(1)
        { "title" : "PHP 教程" }
        > db.col.find({},{"title":1,_id:0}).limit(1).skip(1)
        { "title" : "Java 教程" }

#### 排序
1. > db.col.find({},{"title":1,_id:0}).sort({"likes":-1})
   1. select title from col order by likes desc;
    { "title" : "PHP 教程", "likes" : 200 }
    { "title" : "Java 教程", "likes" : 150 }
    { "title" : "MongoDB 教程", "likes" : 100 }


### 聚合aggregate

> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])
> select by_user, count(*) as num_tutorial  from mycol group by by_user

1. $sum	计算总和。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
   2. select by_user, sum(likes) as num_tutorial from mycol group by by_user;
2. $avg	计算平均值	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])
   2. select by_user, avg(likes) as num_tutorial from mycol group by by_user;
3. $min	获取集合中所有文档对应值得最小值。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])
   2. select by_user, min(likes) as num_tutorial from mycol group by by_user;
4. $max	获取集合中所有文档对应值得最大值。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])
   2. select by_user, max(likes) as num_tutorial from mycol group by by_user;
5. $push	将值加入一个数组中，不会判断是否有重复的值。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])
   2. 
6. $addToSet	将值加入一个数组中，会判断是否有重复的值，若相同的值在数组中已经存在了，则不加入。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])
   2. 
7. $first	根据资源文档的排序获取第一个文档数据。	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])
8. $last	根据资源文档的排序获取最后一个文档数据	
   1. db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])

## 索引Index

索引通常能够极大的提高查询的效率，如果没有索引，MongoDB在读取数据时必须扫描集合中的每个文件并选取那些符合查询条件的记录。
这种扫描全集合的查询效率是非常低的，特别在处理大量的数据时，查询可以要花费几十秒甚至几分钟，这对网站的性能是非常致命的。
索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，**索引是对数据库表中一列或多列的值进行排序的一种结构**。

### 创建索引
> db.collection.createIndex(keys, options)
语法中 Key 值为你要创建的索引字段，1 为指定按升序创建索引，如果你想按降序来创建索引指定为 -1 即可。
> db.col.createIndex({"title":1})
> db.col.createIndex({"title":1,"description":-1})
> db.values.createIndex({open: 1, close: 1}, {background: true})

1. background	Boolean	
   1. 建索引过程会阻塞其它数据库操作，background可指定以后台方式创建索引，即增加 "background" 可选参数。 "background" 默认值为false。
2. unique	Boolean	
   1. 建立的索引是否唯一。指定为true创建唯一索引。默认值为false.
3. name	string	
   1. 索引的名称。如果未指定，MongoDB的通过连接索引的字段名和排序顺序生成一个索引名称。
4. dropDups	Boolean	
   1. 3.0+版本已废弃。在建立唯一索引时是否删除重复记录,指定 true 创建唯一索引。默认值为 false.
5. sparse	Boolean	
   1. 对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档.。默认值为 false.
6. expireAfterSeconds	integer	
   1. 指定一个以秒为单位的数值，完成 TTL设定，设定集合的生存时间。
7. v	index version	
   1. 索引的版本号。默认的索引版本取决于mongod创建索引时运行的版本。
8. weights	document	
   1. 索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重。
9. default_language	string	
   1.  对于文本索引，该参数决定了停用词及词干和词器的规则的列表。 默认为英语
10. language_override	string	
    1.  对于文本索引，该参数指定了包含在文档中的字段名，语言覆盖默认的language，默认值为 language.

### 索引其他操作
1、查看集合索引

db.col.getIndexes()

2、查看集合索引大小

db.col.totalIndexSize()

3、删除集合所有索引

db.col.dropIndexes()

4、删除集合指定索引

db.col.dropIndex("索引名称")