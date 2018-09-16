import unittest
import pprint
from .test_gate import test_rating_db,Asset_stack,gateway_process
import logging
import uuid
from pymongo import MongoClient
import time,datetime
import os
from .test_gate import All_safe,log_builder,report_builder


class asset_homecontent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb,test_case,rlog,logdat,stsec,start_time,dof,tlog
        test_case = "asset_homecontent"
        testdb = test_rating_db("rate_home_contents")

        #Intializing the report builder

        rlog = report_builder('asset_homecontent')
        logdat = {
                    'testc':[],
                    'time_taken':'',
                    'start_time':'',
                    'end_time':''
                 }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        #Intializing the log builder

        tlog = log_builder('Assetapi_homecontent')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    #@unittest.skip('done')
    def test_content_asset_with_ControlledAccess(self):
        caseval = "ControlledAccess"
        tinfo = "rate_keys"
        tclist = {'testcase':'test_content_asset_with_ControlledAccess'}

        logger = tlog.set_log('INFO','format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO','noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval,test_case,tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)


        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_Alarm(self):
        caseval = "Alarm"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_content_asset_with_Alarm'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")

        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        #validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)


        tclist['status'] = itemc

        logdat['testc'].append(tclist)


    def test_content_asset_with_HighWallCode(self):
        caseval = "HighWallCode"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_content_asset_with_HighWallCode'}
        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)


    def test_content_asset_with_ApplianceBreakdown(self):
        caseval = "ApplianceBreakdown"
        tinfo = "rate_enums"

        tclist = {'testcase': 'test_content_asset_with_ApplianceBreakdown'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()


        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)


    def test_content_asset_with_BurglarBarType(self):
        caseval = "BurglarBarType"
        tinfo = "rate_enums"

        tclist = {'testcase': 'test_content_asset_with_BurglarBarType'}
        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_NCB(self):
        caseval = "NCB"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_NCB'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)



    def test_content_asset_with_RoofType(self):
        caseval = "RoofType"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_RoofType'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_WallType(self):
        caseval = "WallType"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_WallType'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_HomeArea(self):
        caseval = "HomeArea"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_HomeArea'}
        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_HomeType(self):
        caseval = "HomeType"
        tinfo = "rate_enums"


        tclist = {'testcase': 'test_content_asset_with_HomeType'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_ppolFrequency(self):
        caseval = "ppolFrequency"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_ppolFrequency'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)


    def test_content_asset_with_itemStatus(self):
        caseval = "itemStatus"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_itemStatus'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_content_asset_with_BuildingUsage(self):
        caseval = "BuildingUsage"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_content_asset_with_BuildingUsage'}
        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Home_contents")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):

        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat,'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')


class asset_vehicle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_vehicle"
        testdb = test_rating_db("rate_vehicles")


        # Intializing the report builder

        rlog = report_builder('asset_vehicle')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_vehicle')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    def test_vehicle_asset_with_CARS(self):
        caseval = "CARS"
        tinfo = "cars"
        tclist = {'testcase': 'test_vehicle_asset_with_CARS'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_vehicle_asset_with_Usage(self):
        caseval = "Usage"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_Usage'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_vehicle_asset_with_ExcessWaiver(self):
        caseval = "ExcessWaiver"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_vehicle_asset_with_ExcessWaiver'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_vehicle_asset_with_Cover(self):
        caseval = "Cover"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_Cover'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_VehicleRebuilt(self):
        caseval = "VehicleRebuilt"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_vehicle_asset_with_VehicleRebuilt'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_hasImmobiliser(self):
        caseval = "hasImmobiliser"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_hasImmobiliser'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_AlarmType(self):
        caseval = "AlarmType"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_AlarmType'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_Financed(self):
        caseval = "Financed"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_vehicle_asset_with_Financed'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_CarHireOption(self):
        caseval = "CarHireOption"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_CarHireOption'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_NewVehicle(self):
        caseval = "NewVehicle"
        tinfo = "rate_enums"
        tclist = {'testcase': 'test_vehicle_asset_with_NewVehicle'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_vehicle_asset_with_ParkedOvernight(self):
        caseval = "ParkedOvernight"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_vehicle_asset_with_ParkedOvernight'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("Motor_vehicles")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')


class asset_allrisks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb,test_case,rlog,logdat,stsec,start_time,dof,tlog
        test_case = "asset_allrisks"
        testdb = test_rating_db("rate_allrisks")

        #Intializing the report builder

        rlog = report_builder('asset_allrisks')
        logdat = {
                    'testc':[],
                    'time_taken':'',
                    'start_time':'',
                    'end_time':''
                 }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        #Intializing the log builder

        tlog = log_builder('asset_allrisks')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    #@unittest.skip('bypass test method')
    def test_allrisks_asset_with_subsection(self):
        caseval = "subsection"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_subsection'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_allrisks_asset_with_ppolFrequency(self):
        caseval = "ppolFrequency"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_ppolFrequency'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_allrisks_asset_with_discountType(self):
        caseval = "discountType"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_discountType'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_allrisks_asset_with_discountLoading(self):
        caseval = "discountLoading"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_discountLoading'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_allrisks_asset_with_itemStatus(self):
        caseval = "itemStatus"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_itemStatus'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    #@unittest.skip('bypass test method')
    def test_allrisks_asset_with_storageLocation(self):
        caseval = "storageLocation"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_allrisks_asset_with_storageLocation'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)
        assetops = Asset_stack()
        asset_req = assetops.build_asset_stack("AllRisks")
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(asset_resp)

        logger.info("-----------}")

        # validate response
        goky = All_safe()
        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')


















