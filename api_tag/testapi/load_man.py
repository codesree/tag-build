from pymongo import MongoClient
import datetime
import json


class mongodbman():

    def __init__(self):
        global col
        db = MongoClient()
        con = db['testman']
        col = con['policy_hub']

    def loader(self):
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

    def updater(self):
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
                        "created_quote": "QUOTE data"
                    }
            })

    def perform(self):
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

    def amendpro(self,selp):
        self.policy = selp
        qcur = col.find_one({"policy_number": self.policy})

        self.qdata = qcur['created_quote']
        #print('quote :', self.qdata)
        self.qdata = json.loads(self.qdata)


        col.update(
            {
                "policy_number":self.policy},
                   {"$set":
                         {
                             "amend_quote":self.qdata
                         }
                   })
        self.perform_tokens()
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



    def asset_manager(self,motor,building,home,stacker):
        global con
        db = MongoClient()
        con = db['mongo_builder']

        self.motor = motor
        self.building = building
        self.home = home
        self.stacker = stacker

        if self.motor != 'ok':
            col = con['vehicle_item']
            motor_item = col.find_one({'name': 'Vehicle'})
            print(type(motor_item))
            del motor_item['_id']

            col = con['vehicle_asset']

            col.update({'name': 'Vehicles'},
                       {'$set': {
                           'items.0': motor_item
                       }
                       }
                       )
        elif self.building != 'ok':
            col = con['building_item']
            build_item = col.find_one({'name': 'Buildings'})

            del build_item['_id']

            col = con['building_asset']
            col.update({'name': 'Buildings'},
                       {'$set': {
                           'items.0': build_item
                       }
                       }
                       )


        elif self.home != 'ok':
            col = con['homecontent_items']
            build_item = col.find_one({'name': 'HomeContent'})
            del build_item['_id']

            col = con['homecontent_asset']
            col.update({'name': 'HomeContents'},
                       {'$set': {
                           'items.0': build_item
                       }
                       }
                       )


        elif self.stacker == 'do':
            asset_stack = self.get_asset_stack()
            col = con['asset_api']
            print(motor_as)
            col.update({'quoteHeader.srsId': 'SRS_ID'},
                       {'$set': {
                           'sections': asset_stack

                       }
                       }
                       )


    def get_asset_stack(self):
        db = MongoClient()
        con = db['mongo_builder']


        col = con['vehicle_asset']

        asset_stack = []

        global motor_as

        motor_as = col.find_one({'name': 'Vehicles'})
        del motor_as['_id']
        asset_stack.append(motor_as)

        global build_as
        col = con['building_asset']
        build_as = col.find_one({'name': 'Buildings'})
        del build_as['_id']
        asset_stack.append(build_as)

        global home_as
        col = con['homecontent_asset']
        home_as = col.find_one({'name': 'HomeContents'})
        del home_as['_id']
        asset_stack.append(home_as)

        return asset_stack

    def test_home_contents(self):
        db = MongoClient()
        con = db['mongo_builder']

        col = con['homecontent_items']
        col.update({'name': 'HomeContents'},
                   {'$set': {
                       'itemProperties.4.value': 16
                   }
                   }
                   )
        build_item = col.find_one({'name': 'HomeContents'})
        del build_item['_id']

        col = con['homecontent_asset']
        col.update({'name': 'HomeContents'},
                   {'$set': {
                       'items.0': build_item
                   }
                   }
                   )


if __name__ == '__main__':

    dbops = mongodbman()

    my_op = "home_asset_test"

    if my_op == "update":
        dbops.updater()
    elif my_op == "insert":
        print('am doing an insertion')
        dbops.loader()
    elif my_op == "perform":
        print("processing....")
        dbops.perform()
    elif my_op == "amend":
        policyn = "SHL000003115"
        dbops.amendpro(policyn)
    elif my_op =='asset':
        motor = 'ok'
        building = 'ok'
        home = 'ok'
        stacker = 'do'
        dbops.asset_manager(motor,building,home,stacker)
    elif my_op == 'home_asset_test':
        dbops.test_home_contents()








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



