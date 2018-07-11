from pymongo import MongoClient
import requests
import json
import pprint

db = MongoClient()
con = db['testman']

col = con['policy_base']

data = col.find_one({"tname": "policy_hub"})

del data['_id']

data = json.dumps(data,indent=5)

print(data)
























