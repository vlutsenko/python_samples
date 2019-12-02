import json
import requests
import urllib3
urllib3.disable_warnings()

url = "https://10.101.164.17:9182/api/config/nms/provider/organizations"

headers = {
    'Authorization': "Basic QWRtaW5pc3RyYXRvcjpWZXJzYTEyM0A=",
    'Content-Type': "application/json",
    'Accept': "application/json"
    }

response = requests.request("GET", url, headers=headers, verify = False)

print(response.text)
