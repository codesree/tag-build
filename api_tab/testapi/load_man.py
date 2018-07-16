from pymongo import MongoClient
import datetime


def loader():
    time_stamp = datetime.datetime.now().isoformat()
    userid = 'c2408856'
    policy_number = 'SHL000001258'
    status = 'active'
    col.insert(
                   {
                    "policy_number": policy_number,
                    "created_by": userid,
                    "created_on": time_stamp,
                    "status": status
                  }
    )




def updater():
    time_stamp = datetime.datetime.now().isoformat()
    userid = 'c2408873'
    policy_number = 'SHL000001234'
    status = 'active'
    col.update(
        {
            "policy_number": "SHL000001234",
        },
        {
            "$set":
                {
                        "created_quote" : "QUOTE data"
                }
         })


def perform():
    podata = col.find()
    lister = []
    for doc in podata:
        print(type(doc))
        print(doc)
        del doc['created_quote']
        del doc['_id']
        lister.append(doc)

    print(type(podata))
    print(podata)
    print(lister)


if __name__ == '__main__':
    db = MongoClient()
    con = db['testman']

    col = con['policy_hub']

    my_op = "perform"

    if my_op == "update":
        updater()
    elif my_op == "insert":
        print('am doing an insertion')
        loader()
    elif my_op == "perform":
        print("processing....")
        perform()







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



