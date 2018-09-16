import uuid
from pymongo import MongoClient
import json
import pprint


class Monprocess():
    def __init__(self,spinner):
        global col
        if spinner == 'crq':
            db = MongoClient()
            con = db['testman']
            col = con['create_quote']
            print('connected to create_quote now........')
            self.initer_guid()
            self.geiter_guid()
            self.updpro_guid()
        elif spinner == 'acq':
            db = MongoClient()
            con = db['testman']
            col = con['accept_quote']
            print('connected to accept_quote now........')
        elif spinner == 'ctp':
            db = MongoClient()
            con = db['testman']
            col = con['conv_to_policy']
            print('connected to conv_to_policy now.......')
        else:
            pass


    def initer_guid(self):
        # ________________________________initialize GUIDs_____________________________________
        global guid_dict
        guid_dict = {'personid': 0,
                     'addressid': 0,
                     'contactid': 0,
                     'bankid': 0,
                     'vehicleid': 0,
                     'digitalinid': 0,
                     'damageitemid': 0,
                     'accessoryid': 0,
                     'drivertstid': 0,
                     'prorataid':0
                     }

    def geiter_guid(self):
        count_gdk = guid_dict.keys()
        gdk_val = len(count_gdk)

        print(gdk_val)

        for key in guid_dict.keys():
            gval = uuid.uuid4()
            gval = str(gval)
            guid_dict[key] = gval
            print(guid_dict[key])

    def updpro_guid(self):
        # _____________________________Update GUIDs_____________________________________________
        col.update(
            {
                'RequestType': 'C'
            },
            {
                "$set": {
                    "Persons.0.PersonID": "" + guid_dict['personid'] + "",
                    "QuoteDetails.Vehicle.0.Drivers.0.PersonID": "" + guid_dict['personid'] + "",
                    "Persons.0.BankingIDS": "" + guid_dict['bankid'] + "",
                    "BankingDetails.0.BankingID": "" + guid_dict['bankid'] + "",
                    "Persons.0.ContactIDS": "" + guid_dict['contactid'] + "",
                    "Contacts.0.ContactID": "" + guid_dict['contactid'] + "",
                    "Persons.0.AddressIDS": "" + guid_dict['addressid'] + "",
                    "Addressses.0.AddressID": "" + guid_dict['addressid'] + "",
                    "QuoteDetails.Vehicle.0.Parking.DayParkingAddressID": "" + guid_dict['addressid'] + "",
                    "QuoteDetails.Vehicle.0.Parking.NightParkingAddressID": "" + guid_dict['addressid'] + "",
                    "Persons.0.DriverTests.0.DriverTestID": "" + guid_dict['drivertstid'] + "",
                    "QuoteDetails.Vehicle.0.VehicleID": "" + guid_dict['vehicleid'] + "",
                    "QuoteDetails.Vehicle.0.MotorAccessories.0.AccessoryID": "" + guid_dict['accessoryid'] + "",
                    "QuoteDetails.Vehicle.0.DigitalInspections.0.DigitalInspectionID": "" + guid_dict['digitalinid'] + "",
                    "QuoteDetails.Vehicle.0.DigitalInspections.0.DamagedItems.0.DamagedItemID": "" + guid_dict['damageitemid'] + "",
                         }
            }
        )


    def procdata(self):
        self.crq_data = col.find_one({"RequestType": "C"})
        del self.crq_data['_id']
        # print(crq_data)
        self.crq_data = json.dumps(self.crq_data, indent=5)
        return self.crq_data

    def guid_checker(self):
        gdata = guid_dict
        print(gdata)

    def acq_bankupd(self,usr_crq):
        bank_dict = {
            'bankid':0,
            'accnum':0,
            'accnum':0,
            'accnam':0,
            'accsur':0,
            'accini':0,
            'accidn':0,
            'accibt':0,
            'acctyp':0,
            'accavs':0,
            'accrsp':0,
        }
        ddata = {}
        ddata = usr_crq
        print(ddata)
        print(type(ddata))
        bank_dict['bankid'] = ddata["BankingDetails"][0]["BankingID"]
        bank_dict['accnum'] = ddata["BankingDetails"][0]["AccountNumber"]
        bank_dict['accnam'] = ddata["BankingDetails"][0]["AccountHolderName"]
        bank_dict['accsur'] = ddata["BankingDetails"][0]["AccountHolderSurname"]
        bank_dict['accini'] = ddata["BankingDetails"][0]["AccountHolderInitials"]
        bank_dict['accidn'] = ddata["BankingDetails"][0]["AccountHolderIDNumber"]
        bank_dict['accibt'] = ddata["BankingDetails"][0]["AccountHolderBranchCode"]
        bank_dict['acctyp'] = ddata["BankingDetails"][0]["AccountType"]
        bank_dict['accavs'] = ddata["BankingDetails"][0]["AVSDone"]
        bank_dict['accrsp'] = ddata["BankingDetails"][0]["AVSResponse"]

        # Bool to str for updating Mongo collection

        accavs = bank_dict['accavs']
        accavs = str(accavs)
        bank_dict['accavs'] = accavs


        return bank_dict

    def ctp_procdata(self,get_policy):
        policy_no = get_policy
        col.update(
            {
                "SystemID": "200"
            },
            {
                "$set": {
                    "QuoteNumber": "" + policy_no + "",
                  }
            }
        )
        self.ctp_data = col.find_one({"SystemID": "200"})
        del self.ctp_data['_id']
        print(self.ctp_data)
        self.ctp_data = json.dumps(self.ctp_data, indent=5)
        return self.ctp_data


    def acq_procdata(self,get_bankd,quote_n):
        upd_bankd = {}
        upd_bankd = get_bankd
        upd_quote = quote_n
        col.update(
            {
                "SystemID": "200"
            },
            {
                "$set": {
                    "CalculateProRataID":""+guid_dict['prorataid']+"",
                    "QuoteNumber":""+upd_quote+"",
                    "BankingDetails.BankingID": "" + upd_bankd['bankid'] + "",
                    "BankingDetails.AccountNumber": "" + upd_bankd['accnum'] + "",
                    "BankingDetails.AccountHolderName": "" + upd_bankd['accnam'] + "",
                    "BankingDetails.AccountHolderSurname": "" + upd_bankd['accsur'] + "",
                    "BankingDetails.AccountHolderInitials": "" + upd_bankd['accini'] + "",
                    "BankingDetails.AccountHolderIDNumber": "" + upd_bankd['accidn'] + "",
                    "BankingDetails.AccountHolderBranchCode": "" + upd_bankd['accibt'] + "",
                    "BankingDetails.AccountType": "" + upd_bankd['acctyp'] + "",
                    "BankingDetails.AVSDone": "" + upd_bankd['accavs'] + "",
                    "BankingDetails.AVSResponse": "" + upd_bankd['accrsp'] + "",
                }
            }
        )

        self.acq_data = col.find_one({"SystemID": "200"})
        del self.acq_data['_id']
        print(self.acq_data)
        self.acq_data = json.dumps(self.acq_data, indent=5)
        return self.acq_data





