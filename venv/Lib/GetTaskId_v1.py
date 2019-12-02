import json
import requests
import urllib3
import re
urllib3.disable_warnings()

url = "https://10.101.164.17:9182/vnms/tasks/task/702"

headers = {
    'Authorization': "Basic QWRtaW5pc3RyYXRvcjpWZXJzYTEyM0A=",
    'Content-Type': "application/json",
    'Accept': "application/json"
    }

exp_result = "COMPLETED"
unexp_result = "NOT COMPLETED"

response = requests.request("GET", url, headers=headers, verify = False)

print(response.text)







