from pymongo import MongoClient
import datetime
import json
import requests
import logging
import uuid,os



class Asset_stack():
    def __init__(self):
        global con
        db = MongoClient()
        con = db['mongo_builder']

    def update_homecontent_item(self,rkey,rfact,rcount,tinfo):

        col = con['homecontent_items']
        ucount = 0
        print("Update started for home_content testcase.....")
        while ucount < rcount:
            if tinfo == "rate_enums":
                print('ucount:',ucount)
                for factnum in rfact.values():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': factnum
                               }
                               }
                               )
                    self.process_homecontent_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': "" + factnum + ""
                               }
                               }
                               )
                    self.process_homecontent_item(ucount)
            ucount = ucount + 1

    def update_allrisks_item(self, rkey, rfact, rcount, tinfo):

        col = con['allrisks_item']
        ucount = 0
        print("Update started for AllRisks testcase.....")
        while ucount < rcount:
            if tinfo == "rate_enums":
                print('ucount:', ucount)
                for factnum in rfact.values():
                    if rkey == "discountType":
                        col.update({"itemType" : "AllRisk"},
                                   {'$set': {
                                       'discountDetails.discountType' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    if rkey == "discountType":
                        col.update({"itemType": "AllRisk"},
                                   {'$set': {
                                       'discountDetails.discountType': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
            ucount = ucount + 1

    def update_vehicle_item(self,rkey,rfact,rcount,tinfo):

        col = con['vehicle_item']
        print("rcount is..",rcount)
        ucount = 0
        while ucount < rcount:
            if tinfo == "rate_enums":
                for factnum in rfact.values():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': factnum
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': ""+factnum+""
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "cars":
                    card = rfact[ucount]
                    print("Build for",card['make'],"--",card['model'])
                    maked = card['make']
                    modeld = card['model']
                    yeard = card['year']
                    col.update({'itemProperties.name': "Make"},
                               {'$set': {
                                   'itemProperties.$.value': "" + maked + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Model"},
                               {'$set': {
                                   'itemProperties.$.value': "" + modeld + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Year"},
                               {'$set': {
                                   'itemProperties.$.value': "" + yeard + ""
                               }
                               }
                               )

                    self.process_vehicle_item(ucount)

            ucount = ucount + 1


    def build_asset_stack(self,stack_name):

        if stack_name == "Home_contents":
            col = con['homecontent_asset']
            asset_data = col.find_one({'name': 'Home Contents'})
        elif stack_name == "Motor_vehicles":
            col = con['vehicle_asset']
            asset_data = col.find_one({'name': 'Vehicles'})
        elif stack_name == "Building":
            col = con['vehicle_asset']
            asset_data = col.find_one({'name': 'Vehicles'})
        elif stack_name == "AllRisks":
            col = con['allrisks_asset']
            asset_data = col.find_one({'name': 'All Risks'})


        del asset_data['_id']

        col = con['asset_api']

        col.update({'quoteHeader.srsId': 'SRS_ID'},
                   {'$set': {
                       'sections': []
                   }
                   }
                   )

        col.update({'quoteHeader.srsId': 'SRS_ID'},
                   {'$set': {
                       'sections.0': asset_data
                   }
                   }
                   )

        asset_req = col.find_one({"quoteHeader.srsId" : "SRS_ID"})

        del asset_req['_id']

        asset_req = json.dumps(asset_req, indent=5)
        return asset_req




    def process_homecontent_item(self,ucount):
        col = con['homecontent_items']
        build_item = col.find_one({"itemType":"HomeContent"})

        del build_item['_id']

        self.asset_content(build_item,ucount)


    def process_vehicle_item(self,ucount):
        col = con['vehicle_item']
        build_item = col.find_one({'itemType': 'Vehicle'})

        del build_item['_id']

        self.asset_vehicle(build_item,ucount)

    def process_allrisks_item(self,ucount):
        col = con['allrisks_item']
        build_item = col.find_one({'itemType': 'AllRisk'})

        del build_item['_id']

        self.asset_allrisks(build_item,ucount)


    def asset_content(self,build_item,ucount):

        col = con['homecontent_asset']

        if ucount == 0:
            col.update({'name': 'Home Contents'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name': 'Home Contents'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )
    def asset_allrisks(self,build_item,ucount):

        col = con['allrisks_asset']

        if ucount == 0:
            col.update({'name': 'All Risks'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name': 'All Risks'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )

    def asset_vehicle(self,build_item,ucount):

        col = con['vehicle_asset']

        if ucount == 0:
            col.update({'name':'Vehicles'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name':'Vehicles'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )

class gateway_process():

    def __init__(self,func):
        global req_url,head
        funcp = func
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        if funcp == "asset_api":
            req_url = 'http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/Process'
        elif funcp == "calculate_prorata":
            req_url = 'http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/CalculateProRata'
        elif funcp == "convert_to_policy":
            req_url = "http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy/"

    def api_exec(self,api_req):
        do_req = api_req
        response = requests.post(req_url, data=do_req, headers=head)

        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp

    def convtop_exec(self,policy_n):
        req_url = "http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy/"
        req_url = req_url + policy_n
        response = requests.post(req_url,headers=head)

        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp




class test_rating_db(Asset_stack):

    def __init__(self,tconnect):
        global col,logger
        db = MongoClient()
        con = db['test_data']
        if tconnect == "rate_home_contents":
            col = con['rate_home_contents']
            print("Connected to --rate_home_contents--- test DB")
            glog = log_builder('Assetapi_homecontent')
            logger = glog.set_log('INFO', 'noformat')
        elif tconnect == 'rate_vehicles':
            col = con['rate_vehicles']
            print("Connected to --rate_vehicles--- test DB")
        elif tconnect == 'rate_allrisks':
            col = con['rate_allrisks']
            print("Connected to --rate_allrisks--- test DB")


    def get_rating_factors(self,caseval,testcase,tinfo):

        global precount

        if testcase == "asset_homecontent":
            tab_title = "rate_contents"
        elif testcase == "asset_vehicle":
            tab_title = "rate_vehicles"
        elif testcase == "asset_allrisks":
            tab_title = "rate_allrisks"

        rtcont = col.find_one({"title": "" + tab_title + ""})

        del rtcont['_id']
        rcfact = rtcont['ratingfactors']
        datak = rcfact.keys()
        print(datak)
        datal = list(datak)
        kcount = 0
        while kcount < len(datal):
            print("key count is", kcount)
            if datal[kcount] == caseval:
                print("found!!!!")
                print(datal[kcount])

                testkey = datal[kcount]

                print(rcfact[testkey])
                logger.info(rcfact[testkey])
                testfact = rcfact[testkey]
                precount = len(testfact)

                print(precount)

                """Process the request json in mongodb using
                   1.testkey  - datatype - char (eg: "ControlledAccess")
                   2.testfact - datatype - dict (eg:{"key":"value".....}) 
                   3.precount - datatype - int  (eg: total number for updates to perform and add)
                """
                break
            kcount = kcount + 1
        else:
            print("Test_Rating_factor Key does not exist in test DB..Test case failed")

        assetops = Asset_stack()

        if tab_title == "rate_contents":
            assetops.update_homecontent_item(testkey, testfact, precount,tinfo)

        if tab_title == "rate_vehicles":
            assetops.update_vehicle_item(testkey, testfact, precount,tinfo)

        if tab_title == "rate_allrisks":
            assetops.update_allrisks_item(testkey,testfact,precount,tinfo)


class All_safe(test_rating_db):
    def __init__(self):
        pass

    def test_all_safe(self,saftyp,cont):
        global  logfil,report_file
        print('Entering AllSafe - chamber....')

        if saftyp == 'file':
            logfil = cont
        elif saftyp == 'report':
            report_file = cont
        elif saftyp == "getfile":
            return logfil
        elif saftyp == "getreport":
            return report_file


    def checkoutput(self,asset_resp):

        asset_resp = json.loads(asset_resp)
        ikey = precount
        itemp = asset_resp['items']

        print("item_key expected: ",ikey)
        print("item_key from response: ", itemp)

        """
        print('counter is',ikey)
        print('asset response length is..',len(storesp))

        quotn = storesp['quoteNumber']
        print('quote number is..',quotn)
        itemp = storesp['items']

        print('length of item premium..',len(itemp))
        """
        try:
            assert len(asset_resp) > 1

            assert asset_resp['quoteNumber']
            quotn = asset_resp['quoteNumber']
            assert len(quotn) > 5

            itemp = asset_resp['items']


            assert len(itemp) == ikey

            print("am PASS")
            return 'PASS'

        except:
            return 'FAIL'

        finally:

            print('api response - validation completed...')


class report_builder():

    def __init__(self, logsuit):
        global logcol, unid

        logdb = MongoClient()
        logcon = logdb['test_data']
        logcol = logcon['test_report']

        if logsuit != 'handover':

            if logsuit == 'asset_homecontent':
                test_suite = '﻿Home contents Rating Factors - Asset API'
            elif logsuit == 'asset_vehicle':
                test_suite = 'Vehicles Rating Factors - Asset API'
            elif logsuit == 'asset_allrisks':
                test_suite = 'AllRisks Rating Factors - Asset API'

            unid = uuid.uuid4()
            unid = str(unid)
            logcol.insert({
                '_id': '' + unid + '',
                'test_suite': '' + logsuit + ''
            })
        else:
            pass

    def log_repdata(self, logdat, logres):

        if logres == 'testsuite':
            tcdat = logdat['testc']
            logcol.update({
                '_id': '' + unid + ''
            },
                {
                    '$set': {
                        'test_cases': tcdat,
                        'time_taken': logdat['time_taken'],
                        'start_time': logdat['start_time'],
                        'end_time': logdat['end_time']
                    }
                }
            )

    def report_handover(self, func):
        trept = logcol.find_one({'_id': '' + unid + ''})
        if func == 'handover':
            print("handover initiated....")
            gs = All_safe()
            gs.test_all_safe('report', trept)


class log_builder():

    def __init__(self, logfile):

        global tfilename, logapi, chin

        logapi = logfile
        curr_time = datetime.datetime.now().isoformat()
        if logfile == 'Assetapi_homecontent':
            tfilename = 'log_asset_homecont_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'
        elif logfile == 'asset_vehicle':
            tfilename = 'log_asset_vehicle_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'asset_allrisks':
            tfilename = 'log_asset_allrisks_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'
        elif logfile == 'asset_api':
            tfilename = 'create_quote_log_'+ curr_time
            tfilename = tfilename + '.json'

        elif logfile == 'asset_api_calcpror':
            tfilename = 'calc_prorata_log_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'asset_api_conv_to_policy_':
            tfilename = 'conv_to_policy_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        dir = os.path.join('testapi/test_chamber')
        chin = logging.FileHandler(os.path.join(dir, tfilename), "a")

    def return_file(self):
        print(tfilename)
        return tfilename

    def set_log(self, loglevl, format):

        if format == 'format':
            format = '%(levelname)s - %(name)s - %(message)s - %(asctime)s'
        elif format == 'noformat':
            format = ''

        global logger
        logger = logging.getLogger(logapi)
        if loglevl == 'DEBUG':
            logger.setLevel(logging.DEBUG)
            chin.setLevel(logging.DEBUG)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'INFO':
            logger.setLevel(logging.INFO)
            chin.setLevel(logging.INFO)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'WARNING':
            logger.setLevel(logging.WARNING)
            chin.setLevel(logging.WARNING)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'ERROR':
            logger.setLevel(logging.ERROR)
            chin.setLevel(logging.ERROR)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger

    def file_handover(self, func):
        if func == 'handover':
            gs = All_safe()
            gs.test_all_safe('file', tfilename)


"""
if __name__ == '__main__':
    print("main")

    assetops = Homecontent_asset()
    #assetops.update_homecontent_item()
    assetops.process_homecontent_item()

    #contfact = test_rating_db()
    #contfact.get_rating_factors("home_contents")
    
"""