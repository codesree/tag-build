from pymongo import MongoClient
import json

"""
db = MongoClient()
con = db['test_data']
col = con['test_report']

dat = col.find_one({"_id" : "b7867f27-4106-474f-9836-06a95c460d36"})
"""

a = {
     "quoteNumber": "SHL000011219",
     "items": [{'a':1}
]}

ab = json.dumps(a, indent=5)

ab = json.loads(ab)

one = ['data1']
two = ['data2']
three = None

try:
       assert one and two is not None
       print("hello")


except:
       print('error')
finally:
       print("final destination")

motor = []
content = []
allrisk = []

asset_dict = {'motor':motor,
               'content':content,
               }
try:
       assert(content != [] or motor != [] or allrisk != [])
       print("asset :",asset_dict)
except:
       print("asset empty")

db = MongoClient()
con = db['test_data']
col = con['rate_vehicles']

vehid = col.find_one({"title": "rate_vehicles"})

carsd = vehid['ratingfactors']['CARS']

ulist = ['TAZZ 130','HILUX 2.4 GD P/U S/C']
print(len(ulist))

print('----------------------------------')

asset = {"allrisk_list": []}

print(len(asset["allrisk_list"]))



try:
       assert asset['allrisk_list'] is not []
       print("allrisk update processing ....")

except:
       print("no updates for all risks")
try:
       assert len(ulist)>1
       motor_ul = []
       ui = 0
       for ui in ulist:
              for cl in carsd:
                     if cl['model'] == ui:
                            motor_ul.append(cl)
       print("List:",motor_ul)

except:
       print("error at try block")
       for cl in carsd:
              if cl['model'] == ulist[0]:
                     print("found!!", cl)




tcs = [{'testcase': 'test_content_asset_with_Alarm', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_ApplianceBreakdown', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_BuildingUsage', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_BurglarBarType', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_ControlledAccess', 'status': 'FAIL'},
       {'testcase': 'test_content_asset_with_HighWallCode', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_HomeArea', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_HomeType', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_NCB', 'status': 'FAIL'},
       {'testcase': 'test_content_asset_with_RoofType', 'status': 'FAIL'},
       {'testcase': 'test_content_asset_with_WallType', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_itemStatus', 'status': 'PASS'},
       {'testcase': 'test_content_asset_with_ppolFrequency', 'status': 'FAIL'}]

ck = 0
ps = 0
fl = 0
for td in tcs:
       ck = ck + 1
       if td['status'] == 'PASS':
              ps = ps + 1
       elif td['status'] == 'FAIL':
              fl = fl + 1

print('no of tests executed :',ck,'\n'
      'no of tests passed   :',ps,'\n'
      'no of tests failed   :',fl)
