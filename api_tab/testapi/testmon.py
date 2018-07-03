from pymongo import MongoClient
import requests
import json
import pprint

db = MongoClient()
con = db['testman']

print(con.collection_names())
"""
checkif = "accept_quote" in con.collection_names()

if checkif is True:
    col = con['accept_quote']
    acdata = col.find_one({"SystemID": "200"})

con.create_collection('load_test')
col = con['load_test']
col.insert(acdata)
"""


checkif = "test_collect" in con.collection_names()
print(checkif)

if checkif is True:
    col = con['test_collect']
    fdata = col.find({"Job":"Business Analyst"})
    print(fdata)
    """data1 = {"name": "Paul",
         "Job": "Business Analyst"
        }
data2 = {"name": "Isco",
         "Job": "Developer"
         }
col.insert([data1,
            data2])"""  # Array Insertion ..............
elif checkif is False:
    pass
    """con.create_collection('test_collect')
    col = con['test_collect']
    data = {"name": "Jeevitha",
            "Job": "Business Analyst"
            }
    col.insert(data)"""
else:
    pass

col = con['test_collect']
print(col.count() == 0)


#check = con.create_collection('test_collection')
#print("exception data....",check)

"""col = con['test_collect']
data = {"name": "Srekanth",
        "Job":"SDET"
        }
col.insert_many(data)"""
