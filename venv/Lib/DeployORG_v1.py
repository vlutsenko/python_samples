import json
import time
import requests
import urllib3
urllib3.disable_warnings()

headers = {
    'Authorization': "Basic QWRtaW5pc3RyYXRvcjpWZXJzYTEyM0A=",
    'Content-Type': "application/json",
    'Accept': "application/json"
    }
payload = ""

for x in range(88, 90):
    #time.sleep(20)
    strX =  "%s" % (x)
    print (strX)
    url = "https://10.101.164.17:9182/vnms/sdwan/workflow/orgs/org/deploy/ORG-"+strX

    response = requests.request("POST", url, data=payload, headers=headers, verify = False)
    print(response.text)


