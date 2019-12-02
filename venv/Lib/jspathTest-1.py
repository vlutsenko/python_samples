import json
from jsonpath_ng import jsonpath, parse
from jsonpath_rw import jsonpath
from jsonpath_rw_ext import parse
import jsonpath_rw_ext as jp

# read file from disk
json_file = open("vlans.json")
json_data=json.load(json_file)

##select info about vlan 123
for vlan in jp.match("$..[?(@.value==123)]",json_data):
    print(format(vlan))

#print(json_data)