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
exp_result = "COMPLETED"
unexp_result = "FAILED"

for x in range(3, 251):
    #time.sleep(20)
    strX =  "%s" % (x)
    print (strX)
    url_post = "https://10.101.195.16:9182/vnms/sdwan/workflow/orgs/org/deploy/ORG-"+strX

    response_post = requests.request("POST", url_post, data=payload, headers=headers, verify = False)
    response_post_val = response_post.text
    json_a = json.loads(response_post_val)
    taskid = "%s" % (json_a["TaskResponse"]["task-id"])
    url_get = "https://10.101.195.16:9182/vnms/tasks/task/"+taskid
    while True:
        response_get = requests.request("GET", url_get, headers=headers, verify=False)
        val = response_get.text
        if exp_result in val:
            print(exp_result)
            break

        elif unexp_result in val:
            print(unexp_result)
            break
        print("In process, retry in 10s")
        time.sleep(10)







