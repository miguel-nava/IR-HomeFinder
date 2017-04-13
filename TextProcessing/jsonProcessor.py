import json

with open('Data1.json') as f:
    Data = json.load(f)

for prop in Data:
    zipcode = prop["link"][-5:]
    if zipcode.isnumeric():
        prop["Zip Code"] = zipcode
    else:
        prop["Zip Code"] = ""

with open('Data2.json', 'w') as output:
    json.dump(Data, output)



