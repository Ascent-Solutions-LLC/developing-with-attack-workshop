# MITRE maintains a repository of current (and versioned) STIX data

import requests
from stix2 import parse


SOURCE_URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack"
VERSION = "enterprise-attack-11.3"

response = requests.get(f"{SOURCE_URL}/{VERSION}.json")

data = response.json()

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        stix_object = parse(object, allow_custom=True)
        break

print(type(stix_object))
print(stix_object.id)
print(stix_object.name)
print(stix_object.description)
