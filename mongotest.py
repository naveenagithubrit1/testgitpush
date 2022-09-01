import pymongo

client = pymongo.MongoClient("mongodb+srv://NaveenaK:Keerthi123@cluster0.vtb1yah.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Keerthi",
    "email":"abcdnaveena@gmail.com",
    "surname":"Kutcherlapati"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)