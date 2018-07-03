import json

"""dicter = {
     "QuoteNumber": 0,
     "Items": 0,
     "bSuccess":'',
     "ErrorMessage": "VehicleID: 77c84869-9e7c-4a53-8547-3b41f84deeb6 has no risk address associated with it.\r\n 00:00:00.0378360",
     "ErrorCode": 0
}

do_it = json.loads(dicter)
print(type(do_it))
print(type(dicter))
print(dicter["bSuccess"])

if dicter['bSuccess'] == 'false':
    print('am ok')"""
ddata =  { "BankingDetails": [
    {
      "BankingID": "0d20d84d-b6f4-4337-bb61-afcbc54d04ed",
		"AccountNumber": "3084",
		"AccountHolderName": "M",
		"AccountHolderSurname": "MOTUPA",
		"AccountHolderInitials": "SP",
		"AccountHolderIDNumber": "7809225675088",
		"AccountHolderBranchCode": "051001",
		"AccountType": "CHEQUE",
		"AVSDone": True,
		"AVSResponse": "string"
    }
  ]}

#data = False
print(type(ddata))

bankid = ddata["BankingDetails"][0]["BankingID"]
accnum = ddata["BankingDetails"][0]["AccountNumber"]
accnam = ddata["BankingDetails"][0]["AccountHolderName"]
accsur = ddata["BankingDetails"][0]["AccountHolderSurname"]
accini = ddata["BankingDetails"][0]["AccountHolderInitials"]
accidn = ddata["BankingDetails"][0]["AccountHolderIDNumber"]
accibt = ddata["BankingDetails"][0]["AccountHolderBranchCode"]
acctyp = ddata["BankingDetails"][0]["AccountType"]
accavs = ddata["BankingDetails"][0]["AVSDone"]
accrsp = ddata["BankingDetails"][0]["AVSResponse"]

print(bankid,accavs,accibt,accidn,accini,accnam,accnum,accrsp,accsur,acctyp)



#if ddata == False:
#    print('am ok')
