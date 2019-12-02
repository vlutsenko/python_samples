import json
import requests
import urllib3
urllib3.disable_warnings()

url = "https://10.101.195.16:9182/vnms/sdwan/workflow/orgs/org"

headers = {
    'Authorization': "Basic QWRtaW5pc3RyYXRvcjpWZXJzYTEyM0A=",
    'Content-Type': "application/json",
    'Accept': "application/json"
    }
for x in range(3, 251):

    strX =  "%s" % (x)
    print (strX)

    payload = "{\r\n\t\"versanms.sdwan-org-workflow\": {\r\n\t\t\"orgName\": \"ORG-"+strX+"\",\r\n\t\t\"globalId\": \""+strX+"\",\r\n\t\t\"parentOrg\": \"Netcracker\",\r\n\t\t\"ikeAuthType\": \"psk\",\r\n\t\t\"sharedControlPlane\": false,\r\n\t\t\"controllers\": [\"Controller-2\", \"Controller-1\"],\r\n\t\t\"vrfs\": [{\r\n\t\t\t\"name\": \"ORG-"+strX+"-LAN-VR\",\r\n\t\t\t\"description\": \"\",\r\n\t\t\t\"id\":"+strX+",\r\n\t\t\t\"enableVPN\": \"true\"\r\n\t\t}],\r\n\t\t\"analyticsClusters\": [\"VAN-HA\"],\r\n\t\t\"supportedRoles\": []\r\n\t}\r\n}"
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload, verify = False)
    print(response.text)


