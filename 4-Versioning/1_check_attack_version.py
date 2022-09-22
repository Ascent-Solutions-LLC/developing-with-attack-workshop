import json

print("Processing ATT&CK v6 ...")
with open("data/stix_data/enterprise-attack-6.0.json", "r") as f:
    data = json.load(f)

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--6aabc5ec-eae6-422c-8311-38d45ee9838a":
        print(f'Name: {object.get("name")}')
        print(f'Description: {object.get("description")}')
        print(f'Deprecated? {object.get("x_mitre_deprecated")}')

print()
print("Processing ATT&CK current version ...")
with open("data/stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)

objects = data["objects"]

for object in objects:
    if object.get("id") == "attack-pattern--6aabc5ec-eae6-422c-8311-38d45ee9838a":
        print(f'Name: {object.get("name")}')
        print(f'Description: {object.get("description")}')
        print(f'Deprecated? {object.get("x_mitre_deprecated")}')
