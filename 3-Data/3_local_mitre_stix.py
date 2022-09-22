# Read a (local copy of) enterprise stix data from MITRE
import json
from stix2 import parse

with open("data/stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        stix_object = parse(object, allow_custom=True)
        break

print(type(stix_object))
print(stix_object.id)
print(stix_object.name)
print(stix_object.description)
