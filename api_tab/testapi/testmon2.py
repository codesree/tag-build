from pymongo import MongoClient
import datetime


db = MongoClient()
con = db['learn-mongo']

col = con['policy_tag']

time_stamp = datetime.datetime.now().isoformat()
userid = 'c2408873'
policy_number = 'SHL000009053'
status = 'active'

col.insert({
            "policy_number":policy_number,
            "created_by":userid,
            "created_on":time_stamp,
            "status":status
        })



