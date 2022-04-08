import pymongo as pymg

#%% 连接与断开
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.learnmg # test是数据库
client.close()

# with client:
#    pass

#%% 系统相关指令
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.learnmg
    print(f'集合list:{db.list_collection_names()}')
# 集合list:['yh', 'col', 'cars']

#%% 运行命令
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.learnmg
    status = db.command("serverStatus")
    pprint(status)

# {'asserts': {'msg': 0, 'regular': 0, 'rollovers': 0, 'user': 0, 'warning': 0},
#  'connections': {'available': 999996, 'current': 4, 'totalCreated': 29},
#  'extra_info': {'availPageFileMB': 11041,
#                 'note': 'fields vary by platform',
#                 'page_faults': 188074,
#                 'ramMB': 24413,
#                 'totalPageFileMB': 27101,
#                 'usagePageFileMB': 280},
#  'globalLock': {'activeClients': {'readers': 0, 'total': 12, 'writers': 0},
#                 'currentQueue': {'readers': 0, 'total': 0, 'writers': 0},
#                 'totalTime': 200487180000},
#  'host': 'DESKTOP-A2RKUD5',
#  'localTime': datetime.datetime(2021, 12, 18, 15, 8, 23, 333000),
#  'locks': {'Collection': {'acquireCount': {'r': 983040, 'w': 22}},
#            'Database': {'acquireCount': {'R': 21,
#                                          'W': 45,
#                                          'r': 983078,
#                                          'w': 22}},
#            'Global': {'acquireCount': {'W': 4, 'r': 2113926, 'w': 67}},
#            'Metadata': {'acquireCount': {'w': 1}}},
#  'mem': {'bits': 64,
#          'mapped': 0,
#          'mappedWithJournal': 0,
#          'resident': 23,
#          'supported': True,
#                                 'transaction range of IDs currently pinned by named snapshots': 0,
#                                 'transaction sync calls': 0,
#                                 'transactions committed': 48,
#                                 'transactions rolled back': 6208},
#                 'uri': 'statistics:'}}

#%% 单个数据库使用状态的统计信息

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.testdb
    print(db.collection_names())

    status = db.command("dbstats")
    pprint(status)

# []
# {'avgObjSize': 0,
#  'collections': 0,
#  'dataSize': 0,
#  'db': 'testdb',
#  'fileSize': 0,
#  'indexSize': 0,
#  'indexes': 0,
#  'numExtents': 0,
#  'objects': 0,
#  'ok': 1.0,
#  'storageSize': 0,
#  'views': 0}
# c:\base\codebase\python\pymongo\pymg_basic_usage.py:9: DeprecationWarning: collection_names is deprecated. Use list_collection_names instead.
#   {'name': 'Skoda', 'price': 9000},

#%% 插入数据
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

cars = [    {'name': 'Audi', 'price': 52642},
            {'name': 'Mercedes', 'price': 57127},
            {'name': 'Skoda', 'price': 9000},
            {'name': 'Volvo', 'price': 29000},
            {'name': 'Bentley', 'price': 350000},
            {'name': 'Citroen', 'price': 21000},
            {'name': 'Hummer', 'price': 41400},
            {'name': 'Volkswagen', 'price': 21600} ]
with client:
    db = client.learnmg # test是数据库
    db.cars.insert_many(cars)

#%% 删除集合
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
with client:
    db = client.learnmg
    print(f'集合list:{db.list_collection_names()}')
    db.cars.drop()
    print(f'集合list:{db.list_collection_names()}')
# 集合list:['yh', 'col', 'cars']
# 集合list:['yh', 'col']