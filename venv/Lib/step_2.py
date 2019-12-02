import json
import time
import requests
import urllib3
import re


text = "1998 was the year when the film titanic was released"
if re.search(r"^1998", text):
    print("Match found")
else:
    print("Match not found")

