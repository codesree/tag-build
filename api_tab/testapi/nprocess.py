import uuid
from pymongo import MongoClient
import json
import pprint
import datetime


class Policy_starter():
    def __init__(self,spinner):
        global col
        if spinner == 'get_policy' or spinner == 'log_policy'\
                or spinner == 'amend_policy':
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
        self.process_amendment(self.qdata,self.policy)

        acur = col.find_one({"policy_number":self.policy})

        self.amdata = acur['amend_quote']

        return self.amdata

    def process_amendment(self,qdata,policy):
        self.qdata = qdata
        self.policy = policy
        col.find_one({"policy_number"})
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

        self.perform_tokens()

        col.update({
            "policy_number": self.policy
        },
            {"$set": [
                toPersons,
                toVehicle,
                toMotorAccessories,
                toDrivers,
                toBankingDetails,
                toITCDetails,
                toContacts,
                toAddressses

            ]
            }
        )

    def perform_tokens(self):
        global toPersons
        global toAddressses
        global toBankingDetails, toContacts, toITCDetails, toMotorAccessories, toVehicle, toDrivers
        toPersons = {
            "amend_quote.Persons.0.State": "POLICY",
            "amend_quote.Persons.0.Status": "ACTIVE",
            "amend_quote.Persons.0.ActionType": "U"
        }
        toVehicle = {
            "amend_quote.QuoteDetails.Vehicle.0": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0": "U"
        }
        toMotorAccessories = {
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0": "U"
        }
        toDrivers = {
            "amend_quote.Persons.0.DriverTests.0": "POLICY",
            "amend_quote.Persons.0.DriverTests.0": "ACTIVE",
            "amend_quote.Persons.0.DriverTests.0": "U"
        }
        toITCDetails = {
            "amend_quote.ITCDetails": "POLICY",
            "amend_quote.ITCDetails": "ACTIVE",
            "amend_quote.ITCDetails": "U"
        }
        toContacts = {
            "amend_quote.Contacts": "POLICY",
            "amend_quote.Contacts": "ACTIVE",
            "amend_quote.Contacts": "U"
        }
        toBankingDetails = {
            "amend_quote.BankingDetails": "POLICY",
            "amend_quote.BankingDetails": "ACTIVE",
            "amend_quote.BankingDetails": "U"
        }
        toAddressses = {
            "amend_quote.Addressses": "POLICY",
            "amend_quote.Addressses": "ACTIVE",
            "amend_quote.Addressses": "U"
        }




