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
            col = con['policy_base']
            print('connected to Policy_tag now........')

    def policy_base(self):
        self.policyent = col.find_one({"tname":"policy_hub"})
        del self.policyent['_id']
        #self.policyent = json.dumps(self.policyent,indent= 5)
        self.policy_list = self.policyent["data"]
        return self.policy_list


    def policy_log(self,userid,policy_number):
        time_stamp = datetime.datetime.now().isoformat()
        self.puser = userid
        self.policy_number = policy_number
        status = 'active'
        col.update(
            {
                "tname": "policy_hub",
            },
            {
                "$addToSet":
                    {
                        "data":
                            {
                                "policy_number": self.policy_number,
                                "created_by": self.puser,
                                "created_on": time_stamp,
                                "status": status,
                            }
                    }
            })
        print("Log operation completed.....")