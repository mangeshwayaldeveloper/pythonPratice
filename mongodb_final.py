import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['db007']
collection=db['ass']
dict={'name':"ashish zattu","rate":23}
collection.insert_one(dict)
