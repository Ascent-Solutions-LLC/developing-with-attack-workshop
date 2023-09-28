import json
from stix2 import parse


with open("data/stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)

objects = data.get("objects")

for object in objects:
    if object.get("id") == "x-mitre-tactic--daa4cbb1-b4f4-4723-a824-7f1efd6e0592":
        stix_object = parse(object, allow_custom=True)
        print("Example Tactic")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()

    elif object.get("id") == "attack-pattern--120d5519-3098-4e1c-9191-2aa61232f073":
        stix_object = parse(object, allow_custom=True)
        print("Example Technique")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()

    elif (
        object.get("id") == "x-mitre-data-source--d6188aac-17db-4861-845f-57c369f9b4c8"
    ):
        stix_object = parse(object, allow_custom=True)
        print("Example Data Source")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()

    elif object.get("id") == "course-of-action--f9f9e6ef-bc0a-41ad-ba11-0924e5e84c4c":
        stix_object = parse(object, allow_custom=True)
        print("Example Mitigation")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()

    elif object.get("id") == "intrusion-set--16ade1aa-0ea1-4bb7-88cc-9079df2ae756":
        stix_object = parse(object, allow_custom=True)
        print("Example Group")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()

    elif object.get("id") == "malware--7bec698a-7e20-4fd3-bb6a-12787770fb1a":
        stix_object = parse(object, allow_custom=True)
        print("Example Software")
        print(f'Object type: {object.get("type")}')
        print(f"STIX Object Type: {type(stix_object)}")
        print(f'ID: {object.get("id")}')
        print(f'Name: {object.get("name")}')
        print(
            f'MITRE ID: {object.get("external_references", [])[0].get("external_id")}'
        )
        print()
