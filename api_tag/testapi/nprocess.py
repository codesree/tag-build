import uuid
from pymongo import MongoClient
import json
import pprint
import datetime


class Policy_starter():
    def __init__(self,spinner):
        global col
        if spinner == 'get_policy' or spinner == 'log_policy' or spinner == 'amend_policy':
            db = MongoClient()
            con = db['testman']
            col = con['policy_hub']
            print('connected to Policy_hub now........')
        elif spinner == "acdec_amend":
            db = MongoClient()
            con = db['testman']
            col = con['accept_policy_amendment']
            print('connected to accept_policy_amendment now........')


    def policy_base(self):
        self.pldata = col.find({})
        self.policy_list = []
        for doc in self.pldata:
            del doc['created_quote']
            del doc['_id']
            self.policy_list.append(doc)
        return self.policy_list

    def accept_amendment(self,policy_n,decision):
        self.policy_n = policy_n
        self.decision = decision

        col.update({
            'SystemID':200
        },
            {
                '$set':{
                    "PolicyNumber":self.policy_n,
                    "Decision":self.decision
                }
            })

        self.ac_amd = col.find_one({"PolicyNumber":self.policy_n})
        self.ac_amd = json.dumps(self.ac_amd,indent= 4)

        return self.ac_amd






    def policy_log(self,userid,policy_number,quotes):
        time_stamp = datetime.datetime.now().isoformat()
        self.puser = userid
        self.policy_number = policy_number
        self.quotes = quotes
        status = 'active'
        col.insert(
            {
                "policy_number": self.policy_number,
                "created_by": self.puser,
                "created_on": time_stamp,
                "status": status,
                "created_quote":self.quotes

            })
        print("Log operation completed.....")

    def get_quote(self,policy_no):
        self.policy = policy_no
        qcur = col.find_one({"policy_number":self.policy})

        self.qdata = qcur['created_quote']
        print('quote :',self.qdata)
        self.qdata = json.loads(self.qdata)
        self.process_amendment(self.qdata,self.policy)

        acur = col.find_one({"policy_number":self.policy})

        self.amdata = acur['amend_quote']
        del self.amdata['RequestType']
        del self.amdata['QuoteNumber']


        self.amdata = json.dumps(self.amdata, indent=5)

        return self.amdata

    def process_amendment(self,qdata,policy):
        self.qdata = qdata
        self.policy = policy
        #col.find_one({"policy_number"})
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

        self.perform_tokens(self.policy)

        col.update({
            "policy_number": self.policy
        },
            {
                "$set":upd_token
            }

        )

    def perform_tokens(self,poltoken):
        self.poltoken = poltoken
        global upd_token
        upd_token = {}

        toPolicy  = {"amend_quote.PolicyNumber":self.poltoken}
        upd_token.update(toPolicy)

        toPersons = {
            "amend_quote.Persons.0.State": "POLICY",
            "amend_quote.Persons.0.Status": "ACTIVE",
            "amend_quote.Persons.0.ActionType": "U"
        }
        upd_token.update(toPersons)
        toVehicle = {
            "amend_quote.QuoteDetails.Vehicle.0.State": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0.Status": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0.ActionType": "U"
        }
        upd_token.update(toVehicle)

        toMotorAccessories = {
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.State": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.Status": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.ActionType": "U"
        }
        upd_token.update(toMotorAccessories)

        toDrivers = {
            "amend_quote.Persons.0.DriverTests.0.State": "POLICY",
            "amend_quote.Persons.0.DriverTests.0.Status": "ACTIVE",
            "amend_quote.Persons.0.DriverTests.0.ActionType": "U"
        }
        upd_token.update(toDrivers)

        toITCDetails = {
            "amend_quote.ITCDetails.State": "POLICY",
            "amend_quote.ITCDetails.Status": "ACTIVE",
            "amend_quote.ITCDetails.ActionType": "U"
        }
        upd_token.update(toITCDetails)

        toContacts = {
            "amend_quote.Contacts.0.State": "POLICY",
            "amend_quote.Contacts.0.Status": "ACTIVE",
            "amend_quote.Contacts.0.ActionType": "U"
        }
        upd_token.update(toContacts)

        toBankingDetails = {
            "amend_quote.BankingDetails.0.State": "POLICY",
            "amend_quote.BankingDetails.0.Status": "ACTIVE",
            "amend_quote.BankingDetails.0.ActionType": "U"
        }
        upd_token.update(toBankingDetails)

        toAddressses = {
            "amend_quote.Addressses.0.State": "POLICY",
            "amend_quote.Addressses.0.Status": "ACTIVE",
            "amend_quote.Addressses.0.ActionType": "U"
        }
        upd_token.update(toAddressses)




