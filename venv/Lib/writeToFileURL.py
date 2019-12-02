import json
import requests
import urllib3
urllib3.disable_warnings()


##main credentials
fileName = "testDataURL.json"

## get peyload from URL

URL = "http://json-schema.org/schema"

data = requests.request("GET", URL, verify = False)

##write to file

with open(fileName,"w") as write_file:
    json.dump(data.text,write_file)