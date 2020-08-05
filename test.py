import pymongo
import json
import pprint
import os

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
coll = db['events']

db.coll.delete_many({'id': '1'})

for x in coll.find():
    pprint.pprint(x)
