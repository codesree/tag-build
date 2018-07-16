import uuid
from pymongo import MongoClient
import json
import pprint
import datetime


class Policy_starter():
    def __init__(self,spinner):
        global col
        if spinner == 'get_policy' or spinner == 'log_policy':
            db = MongoClient()
            con = db['testman']
            col = con['policy_hub']
            print('connected to Policy_tag now........')

    def policy_base(self):
        self.pldata = col.find()
        self.policy_list = []
        for doc in self.pldata:
            del doc['created_quote']
            del doc['_id']
            self.policy_list.append(doc)
        return self.policy_list


    def policy_log(self,userid,policy_number):
        time_stamp = datetime.datetime.now().isoformat()
        self.puser = userid
        self.policy_number = policy_number
        status = 'active'
        col.insert(
            {
                "policy_number": self.policy_number,
                "created_by": self.puser,
                "created_on": time_stamp,
                "status": status
            })
        print("Log operation completed.....")

    def get_quote(self,policy_no):
        self.policy = policy_no
        qcur = col.find_one({"policy_number":self.policy})

        self.qdata = qcur['created_quote']
        print('quote :',self.qdata)
        self.qdata = json.loads(self.qdata)
        self.prepare_amend(self.qdata,self.policy)



    def prepare_amend(self,qdata,policy):
        self.qdata = qdata
        self.policy = policy
        col.update(
            {
                "policy_number":self.policy
            },
            {
                "$set":{
                    "amend_quote":self.qdata
                }
            }
        )




