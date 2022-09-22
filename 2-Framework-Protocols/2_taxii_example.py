from stix2 import TAXIICollectionSource, Filter
from taxii2client.v20 import Collection, Server


MITRE_TAXII_SERVER_URL = "https://cti-taxii.mitre.org/"

server = Server(f"{MITRE_TAXII_SERVER_URL}/taxii")

print("API Roots:")
for api_root in server.api_roots:
    print(api_root.title)

api_root = server.api_roots[0]

print()
print("Collections:")
for collection in api_root.collections:
    print(collection.title)

print()

for collection in api_root.collections:
    if collection.title == "Enterprise ATT&CK":
        enterprise_id = collection.id

enterprise_collection = Collection(
    f"{MITRE_TAXII_SERVER_URL}/stix/collections/{enterprise_id}"
)
collection_source = TAXIICollectionSource(enterprise_collection)
technique_filter = Filter("type", "=", "attack-pattern")
techniques = collection_source.query(technique_filter)
technique = techniques[0]
print(f"<Technique: {technique.id} Name: {technique.name} Description: {technique.description}>")
