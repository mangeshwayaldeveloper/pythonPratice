import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['mangesh2']
collection=db['table']
insert=[
 {'name':'mangesh','age':23},
 {'name':'pavan','age':25},
 {'name':'rushi','age':19}
]
collection.insert_many(insert)
one=collection.find_one({'name':'pavan'})
print(one)