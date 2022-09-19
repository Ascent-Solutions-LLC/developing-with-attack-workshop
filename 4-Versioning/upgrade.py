import json
import re


# An example of a deprecated technique: T1108, attack-pattern--6aabc5ec-eae6-422c-8311-38d45ee9838a
example_technique_id = "T1108"

with open("stix_data/enterprise-attack.json", "r") as f:
    stix_data = json.load(f)

for item in stix_data["objects"]:
    item_type = item.get("type")
    if not item_type:
        continue  # type not present, skip it

    if item_type != "attack-pattern":
        continue  # not a technique, skip it

    external_references = item.get("external_references")
    if not external_references:
        continue  # not present, skip it

    for external_reference in external_references:
        source_name = external_reference.get("source_name")
        if source_name == "mitre-attack":
            technique_id = external_reference.get("external_id")

    if technique_id != example_technique_id:
        continue  # not matched, skip it

    deprecated = item.get("x_mitre_deprecated")
    if not deprecated:
        continue  # Not deprecated, skip it

    description = item.get("description")
    if not description:
        continue  # doesn't have a description, skip it

    pattern = r"\*\*This technique has been deprecated. Please use (.*)\.\*\*"
    matched = re.match(pattern, description)
    if not matched:
        continue  # Not deprecated, skip it
    
    updates = matched.groups()[0]
    print()
    print(f'Found deprecated item:')
    print()
    print(f'ID: {item["id"]}')
    print(f'Name: {item.get("name")}')
    print(f'Description: {description}')
    break


# Do some fancy regexing
pattern = r"\[([^][]+)\](\(((?:[^()]+|(?:2))+)\))"
matched = re.findall(pattern, updates)
links = []
if matched:
    for match in matched:
        links.append(match[2])

updated_technique_ids = []
# MOAR regexing
for link in links:
    pattern = r"(T\d{4}.*)"
    found = re.search(pattern, link)
    if found:
        path = found.groups()[0]
        t_id = path.replace("/", ".")
        updated_technique_ids.append(t_id)

print()
print(f"Potential updates: {updated_technique_ids}")
