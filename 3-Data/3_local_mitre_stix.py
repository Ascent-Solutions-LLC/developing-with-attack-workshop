# Read a (local copy of) enterprise stix data from MITRE
import json
from stix2 import parse

with open("stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        print(json.dumps(object, indent=2))

for object in objects:
    if object.get("id") == "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236":
        # Let's also parse this into a stix object
        stix_object = parse(object, allow_custom=True)
        print(stix_object)
