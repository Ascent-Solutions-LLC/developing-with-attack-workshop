# Read a (local copy of) enterprise stix data from MITRE
import json


with open("stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        print(json.dumps(object, indent=2))
