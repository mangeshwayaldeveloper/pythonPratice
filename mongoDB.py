import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
print("welcome to pymongo")
print(client)
db = client['mangesh']
collection = db['mycollec']
dict = {'name': 'mangesh', 'marks': 100}
collection.insert_one(dict)

# use insert many
inserts = [
 {'_id': 1, 'name': 'mangesh', 'rollno': 432, 'age': 22},
 {'_id': 2, 'name': 'Shubham', 'rollno': 365, 'age': 23},
 {'_id': 3, 'name': 'Ashish Dalle', 'rollno': 369, 'age': 21},
 {'_id': 4, 'name': 'Sumit ', 'rollno': 345, 'age': 21},
 {'_id': 5, 'name': 'vinay', 'rollno': 418, 'age': 22}
]

# collection.insert_many(inserts)

# update
# prev = {'name': "Sumit"}
# nexts = {"$set": {'name': 'sumit'}}
# upt = collection.update_many(prev, nexts)
# print(upt)

# delete
# delete_one
# pre={'name':'sumit'}
# one=collection.delete_one(pre)
# print(one)

# delete_many
pre={'name':'mangesh'}
one=collection.delete_many(pre)
print(one)
print(one.deleted_count)
