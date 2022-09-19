import json

import requests


response = requests.get("https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-11.3.json")

data = response.json()

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        print(json.dumps(object, indent=2))
