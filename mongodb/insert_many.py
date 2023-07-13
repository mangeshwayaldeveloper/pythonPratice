import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['database007']
col=db['col007']
record=[
 {'name':'mangesh','age':23,'city':'pune'},
 {'name':'sumit','age':24,'city':'pune'},
 {'name':'ashish','age':25,'city':'pune'},
 {'name':'shubham','age':26,'city':'pune'},
]
# col.insert_many(record)
# x=col.find({},{'name'})
# for data in x:
#  print(data)
#
# prev={'age':23}
# nex={'$set':{'name':'sonu'}}
# col.update_one(prev,nex)
#
# d=col.find_one({'age':23})
# print(d)
#
# # delete
dels={'name':'dalla'}
col.delete_many(dels)
#
# f=col.find()
# for df in f:
#  print(df)
#
# prev={'name':'ashish'}
# net={'$set':{'name':'dalla'}}
# col.update_one(prev,net)