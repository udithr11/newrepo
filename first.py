import pymongo
client = pymongo.MongoClient("mongodb+srv://udithr:Ammazz123@cluster0.vqc1j4v.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":"udith",
   "email":"udithr11@gmail.com",
   "surname":"r"}

db1=client['first']
coll=db1['test']
coll.insert_one(d)
