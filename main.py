import json
from pprint import pprint


with open("test.json","r") as file:
    
    data=json.load(file)
    
# print(data)

pprint(data)


