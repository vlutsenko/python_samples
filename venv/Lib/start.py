from jnpr.junos import Device
import json
import requests
import urllib3
urllib3.disable_warnings()

URL = "http://json-schema.org/schema"

response = requests.request("GET", URL, verify = False)
print(response.text)

#dev = Device(host="10.101.164.44", user="root", password="root123")
#dev.open()
#print(dev.facts)
#dev.close()
