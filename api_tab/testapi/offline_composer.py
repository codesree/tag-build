from pymongo import MongoClient
import json
import datetime


class Composer():
    def __init__(self,tcon):
        global col
        db = MongoClient()
        con = db['testman']
        col = con[tcon]

    def load_man(self,quoted):
        time_stamp = datetime.datetime.now().isoformat()
        userid = 'c2408873'
        policy_number = 'SHL000003116'
        status = 'active'
        col.insert(
            {
                            "policy_number": policy_number,
                            "created_by": userid,
                            "created_on": time_stamp,
                            "status": status,
                            "created_quote": quoted
            })

    def amendpro(self,selp):
        self.policy = selp
        qcur = col.find_one({"policy_number": self.policy})

        self.qdata = qcur['created_quote']
        print('quote :', self.qdata)
        self.qdata = json.loads(self.qdata)


        col.update({"policy_number":self.policy},
                   {"$set":
                         {
                             "amend_quote":self.qdata
                         }
                   })
        print("type of upd token",type(upd_token))
        print("Update token",upd_token)
        col.update({
            "policy_number":self.policy
        },
            {
                "$set":upd_token
            }
        )
        acur = col.find_one({"policy_number": self.policy})

        self.amdata = acur['amend_quote']
        self.amdata = json.dumps(self.amdata, indent=5)

        return self.amdata

    def perform_tokens(self):
        global upd_token
        upd_token = {}
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
        upd_token.update(toPersons,toVehicle,toITCDetails,toMotorAccessories,toDrivers,toAddressses,
                         toBankingDetails,toContacts)
