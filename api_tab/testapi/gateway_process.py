import requests
import json
from pymongo import MongoClient
import datetime

head = {'Content-Type': 'application/json','Accept': 'application/json'}

db = MongoClient()
con = db['testman']
col = con['policy_tag']

#do_req = api_req
#data = json.dumps(do_req)
#print(type(data))

crq_data = col.find()
checker = {}
for doc in crq_data:
    print(doc)
    checker = doc

print(checker)
"""
for ilist in data:
    ok_d = {"Policy":data}

#actual_data = json.dumps(crq_data)

print(" Now the document is....")
print(ok_d)
print(type(ok_d))

global i_id
i_id = 0

for id_key in ok_d:
    del ok_d["Policies"][i_id]["_id"]
    i_id = i_id + 1
    print("existing..")

print(ok_d)


"""


"""
response = requests.get("http://19289iisjnb001v/Policies/policies/SHL000009053/200/100/1",
                         headers=head)
do_resp = response.json()

print("Response from API Gateway",response.status_code)
print(do_resp)

print(type(do_resp))

do_resp = json.dumps(do_resp,indent=5)
print(do_resp)
"""