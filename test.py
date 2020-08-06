import pymongo
import pprint
from bson.json_util import dumps

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
coll = db['events']

f = open('output.json', 'w')

for x in coll.find():
    f.write(dumps(x))
    f.write(', ')
