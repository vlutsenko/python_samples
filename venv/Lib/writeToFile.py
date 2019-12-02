import json

##main credentials
fileName = "testData.json"

##define file payload
data = {
    "president": [{
        "name":"Joy Con",
        "country": "Bosvana"
    },
        {
            "name": "Toy Bon",
            "country": "Venesuela"
        }
    ]
}

##write to file

with open(fileName,"w") as write_file:
    json.dump(data,write_file)




