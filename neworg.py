from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from googleapiclient import _auth
import urllib
import json
import base64
import http
import re
import os
import sys
# import subprocess
from pprint import pprint
from time import sleep
from urllib.parse import urlencode
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/chronicle-backstory', 'https://www.googleapis.com/auth/malachite-ingestion']
#@markdown Please make sure you select the appopriate region below.
region_prefix = "me-west1" #@param ["North America", "Europe", "Asia", "United Kingdom"]



# The apikeys-demo.json file contains the customer's OAuth 2 credentials.
# SERVICE_ACCOUNT_FILE is the full path to the apikeys-demo.json file
# ToDo: Replace this with the full path to your OAuth2 credentials

#os.system(f"rm supplied_key.json")



# Create a credential using Google Developer Service Account Credential and Chronicle API
# Scope.
#sh=json.loads("KeySecured.json")
credentials = service_account.Credentials.from_service_account_file("KeySecured.json", scopes=SCOPES)

# Build an HTTP client to make authorized OAuth requests.
http_client = _auth.authorized_http(credentials)
session = AuthorizedSession(credentials)

#@title Create Customer
#@markdown Creates a customer and associates this customer with the partner. This API fully provisions a customer in Chronicle. The response includes the customer ID.
customer_name = "moep-kar_pri" #@param {type: "string"}
customer_code =  "karpriisr" #@param {type: "string"}
customer_subdomains = "kar-pri-me-west1"  #@param {type: "string"}
#@markdown Select whether to upload the SSO file or specify a local filename. If uploading the sso_config_file variable doesn't matter

#req_body = {
    #"customer_name" : customer_name,
    #"customer_code" : customer_code,
    #"customer_subdomains" : customer_subdomains,
    #"retention_duration" : "ONE_YEAR"

   # }
with open("GoogleIDPMetadata.xml", "rb") as file_to_read:
    sso_config_file = base64.b64encode(file_to_read.read()).decode('ascii')

#req_body = {

  
    #"customer_code" : customer_code,
    #"sso_config": sso_config_file ,
    #"customer_subdomain": customer_subdomains,
    #"update_v2_only": "true"


#}

req_body = {
    "customer_code" : customer_code,
    "state": True
    
}


  
 # with open(sso_config_filename, "rb") as file_to_read:
  #  sso_config_file = base64.b64encode(file_to_read.read()).decode('ascii')

 

#uri_to_post = f"https://{region_prefix}-backstory.googleapis.com/v1/partner/customer/createcustomer"
#uri_to_patch = f"https://{region_prefix}-backstory.googleapis.com/v1/partner/customer/updatessoconfig"
uri_to_ui = f"https://{region_prefix}-backstory.googleapis.com/v1/partner/customer/setuistate:state"
# send the request and process the response
print("Attempting to create customer. This may take several minutes and there will be no output during this time.")
# extend http timeout to 20 minutes since this is a long call
#http_client.timeout = 1200

#resp = http_client.request(uri_to_patch, "PATCH", body=json.dumps(req_body))
# return timeout back to default 1 minute
#http_client.timeout = 60
#json_resp = json.loads(resp[1])
#if resp[0].status != http.HTTPStatus.OK:
 # pprint(json_resp.get('error').get('message'))
#else:
 # pprint(json_resp)
#http_client.timeout = 600
#resp = http_client.request(uri_to_patch, "PATCH", body=json.dumps(req_body))
#http_client.timeout = 60
#json_resp = json.loads(resp[1])
#if resp[0].status != http.HTTPStatus.OK:
  #pprint(json_resp.get('error').get('message'))
#else:
 # pprint(json_resp)
http_client.timeout = 600
resp = http_client.request(uri_to_ui, "POST", body=json.dumps(req_body))
http_client.timeout = 60
json_resp = json.loads(resp[1])
if resp[0].status != http.HTTPStatus.OK:
  pprint(json_resp.get('error').get('message'))
else:
 pprint(json_resp)
