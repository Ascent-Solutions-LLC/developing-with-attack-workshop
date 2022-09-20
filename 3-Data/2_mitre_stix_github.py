# MITRE maintains a repository of current (and versioned) STIX data


import json

import requests


SOURCE_URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack"
VERSION = "enterprise-attack-11.3"

response = requests.get(f"{SOURCE_URL}/{VERSION}.json")

data = response.json()

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        print(json.dumps(object, indent=2))
