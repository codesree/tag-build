import requests
import json

head = {'Content-Type': 'application/json','Accept': 'application/json'}

api_req ="""{
  "RequestType": "C",
  "QuoteNumber": "string",
  "Persons": [
    {
      "PersonID": "00000000-0000-0000-0000-000000000000",
      "BankingIDS": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "ContactIDS": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "AddressIDS": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "FirstName": "string",
      "Surname": "string",
      "Initials": "string",
      "Title": "NOTITLE",
      "Gender": "MALE",
      "DOB": "2018-06-18T08:32:15.219Z",
      "IdentityDocumentType": "SAIDENTITYDOCUMENT",
      "ClientIDNo": "string",
      "Age": 0,
      "MaritalStatus": "SINGLE",
      "Pensioner": true,
      "CommunicationMethod": "EMAIL",
      "LicenseType": "LEARNERS",
      "LicenceCode": "A",
      "LicenceDateObtained": "2018-06-18T08:32:15.219Z",
      "InsuranceDeclinedPreviously": true,
      "Judgement": true,
      "FraudCriminalOffence": true,
      "POPIConsentIndicator": true,
      "MarketingConsentIndicator": true,
      "PolicyHolderIndicator": true
    }
  ],
  "QuoteDetails": {
    "Vehicle": [
      {
        "VehicleID": "00000000-0000-0000-0000-000000000000",
        "Make": "string",
        "Model": "string",
        "MMCode": "string",
        "Year": 0,
        "SumInsured": "string",
        "EngineNo": "string",
        "VINNo": "string",
        "VehicleLicenseDiskNumber": "string",
        "VehicleRegisterNumber": "string",
        "LicensePlateNumber": "string",
        "Colour": "string",
        "ExcessWaiver": true,
        "Financed": true,
        "LoanAmount": 0,
        "VoluntaryExcess": 0,
        "CoverOption": "MARKET",
        "AlarmType": "OTHER",
        "hasImmobiliser": true,
        "VehicleRebuilt": true,
        "Cover": "COMPREHENSIVE",
        "Usage": "BUSINESSREPRESENTATIVE",
        "CarHireOption": "CLASSA",
        "NewVehicle": true,
        "HasTrackingDevice": true,
        "ParkedOvernight": "UNKNOWN",
        "CoverEffectiveDate": "2018-06-18T08:32:15.219Z",
        "MotorAccessories": [
          {
            "AccessoryID": "00000000-0000-0000-0000-000000000000",
            "AccessoryType": "ABSBRAKES",
            "AccessoryOtherDesc": "string",
            "SumInsured": 0
          }
        ],
        "ClaimsHistory": {
          "NoOfClaims0to12": 0,
          "NoOfClaims13to24": 0,
          "NoOfClaims25to36": 0
        },
        "Parking": {
          "DayParkingAddressID": "00000000-0000-0000-0000-000000000000",
          "NightParkingAddressID": "00000000-0000-0000-0000-000000000000"
        },
        "Drivers": [
          {
            "PersonID": "00000000-0000-0000-0000-000000000000",
            "DriverType": "PRIMARY"
          }
        ]
      }
    ]
  },
  "ITCDetails": {
    "ITCConsent": true,
    "ITCEffectiveDate": "2018-06-18T08:32:15.219Z",
    "ITCLapse": 0,
    "ITCLoss": 0,
    "ITCScore": 0,
    "ITCLapseBand": "string",
    "ITCLossBand": "string",
    "ITCVersion": 0
  },
  "Contacts": [
    {
      "ContactID": "00000000-0000-0000-0000-000000000000",
      "ContactType": "MOBILENO",
      "Text": "string"
    }
  ],
  "BankingDetails": [
    {
      "BankingID": "00000000-0000-0000-0000-000000000000",
      "AccountNumber": "string",
      "AccountHolderName": "string",
      "AccountHolderSurname": "string",
      "AccountHolderInitials": "string",
      "AccountHolderIDNumber": "string",
      "AccountHolderBranchCode": "string",
      "AccountType": "CHEQUE",
      "AVSDone": true,
      "AVSResponse": "string"
    }
  ],
  "Addressses": [
    {
      "AddressID": "00000000-0000-0000-0000-000000000000",
      "AddressType": "POSTALADDRESS",
      "RiskAddLine1": "string",
      "RiskAddLine2": "string",
      "RiskAddLine3": "string",
      "RiskAddLine4": "string",
      "RiskPostCode": "string",
      "Province": "string",
      "StreetNum": 0
    }
  ],
  "SystemID": "string",
  "SystemUserID": "string",
  "CompanyID": "string"
}"""


do_req = api_req
#data = json.dumps(do_req)
#print(type(data))

response = requests.post("http://19289dabtst002v/Quotes/quotes",data=do_req,headers=head)
do_resp = response.json()

print("Response from API Gateway",response.status_code)
print(do_resp)

print(type(do_resp))

do_resp = json.dumps(do_resp,indent=5)
print(do_resp)
