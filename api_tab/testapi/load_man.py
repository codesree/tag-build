from pymongo import MongoClient
import datetime



def loader():
    time_stamp = datetime.datetime.now().isoformat()
    userid = 'c2408873'
    policy_number = 'SHL000009234'
    status = 'active'
    col.insert({
        "tname": "policy_hub",
            "data": [
                {
                    "policy_number": policy_number,
                    "created_by": userid,
                    "created_on": time_stamp,
                    "status": status
                  },
                 ]}
    )

def updater():
    time_stamp = datetime.datetime.now().isoformat()
    userid = 'c2408873'
    policy_number = 'SHL000003435'
    status = 'active'
    col.update(
        {
            "tname": "policy_hub",
        },
        {
            "$addToSet":
                {"data":
                    {
                    "policy_number": policy_number,
                    "created_by": userid,
                    "created_on": time_stamp,
                    "status": status
                    }
                }
         })


if __name__ == '__main__':
    db = MongoClient()
    con = db['testman']

    col = con['policy_base']

    my_op = "update"

    if my_op == "update":
        updater()
    elif my_op == "insert":
        loader()

"""
R E F E R E N C E S -----------------------------------------

print(con.collection_names())

checkif = "accept_quote" in con.collection_names()

if checkif is True:
    col = con['accept_quote']
    acdata = col.find_one({"SystemID": "200"})

con.create_collection('load_test')
col = con['load_test']
col.insert(acdata)

time_stamp = datetime.datetime.now().isoformat()
userid = 'c2408873'
policy_number = 'SHL000009053'
status = 'active'

col.insert({
            "policy_number":policy_number,
            "created_by":userid,
            "created_on":time_stamp,
            "status":status
        })"""



