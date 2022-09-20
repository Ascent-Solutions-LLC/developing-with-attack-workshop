from stix2 import TAXIICollectionSource, Filter
from taxii2client.v20 import Collection, Server


MITRE_TAXII_SERVER_URL = "https://cti-taxii.mitre.org/"

server = Server(f"{MITRE_TAXII_SERVER_URL}/taxii")
api_root = server.api_roots[0]

for collection in api_root.collections:
    if collection.title == "Enterprise ATT&CK":
        enterprise_id = collection.id

enterprise_collection = Collection(
    f"{MITRE_TAXII_SERVER_URL}/stix/collections/{enterprise_id}"
)
collection_source = TAXIICollectionSource(enterprise_collection)

groups_filter = Filter("type", "=", "intrusion-set")
group_name_filter = Filter("name", "contains", "APT29")
groups = collection_source.query([groups_filter, group_name_filter])

applicable_group = groups[0]

relationships_filter = Filter("type", "=", "relationship")
group_relationships = Filter("source_ref", "=", applicable_group.id)
to_techniques = Filter("target_ref", "contains", "attack-pattern")
relationships = collection_source.query([relationships_filter, group_relationships])
print(len(relationships))

technique_filter = Filter("type", "=", "attack-pattern")
applicable_techniques = Filter("id", "in", [r.target_ref for r in relationships])
active = Filter("x_mitre_deprecated", "=", False)
current = Filter("revoked", "=", False)
techniques = collection_source.query(
    [technique_filter, applicable_techniques, active, current]
)

for technique in techniques:
    print(technique.id)
