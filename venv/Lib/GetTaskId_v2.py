import json
import requests
import urllib3
import re
import sys
urllib3.disable_warnings()

url = "https://10.101.164.17:9182/vnms/tasks/task/702"

headers = {
    'Authorization': "Basic QWRtaW5pc3RyYXRvcjpWZXJzYTEyM0A=",
    'Content-Type': "application/json",
    'Accept': "application/json"
    }

exp_result = "COMPLETED"
unexp_result = "FAILED"
val = ""

while True:
    response = requests.request("GET", url, headers=headers, verify=False)
    val = response.text
    if exp_result in val:
            print(exp_result)
            break

    elif unexp_result in val:
            print(unexp_result)
            break
