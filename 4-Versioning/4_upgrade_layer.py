import json
import re


with open("data/layers/older_layer.json", "r") as f:
    layer = json.load(f)

techniques = layer["techniques"]

with open("data/stix_data/enterprise-attack.json", "r") as f:
    stix_data = json.load(f)

new_technique_ids = []

for technique in techniques:
    technique_id = technique["techniqueID"]

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
                ext_id = external_reference.get("external_id")

        if technique_id != ext_id:
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

        new_technique_ids += updated_technique_ids

new_technique_ids = list(set(new_technique_ids))  # remove duplicates

new_layer_techniques = []
for new_t_id in new_technique_ids:
    new_layer_technique = {"techniqueID": new_t_id, "score": 1, "enabled": True}
    new_layer_techniques.append(new_layer_technique)

layer["techniques"] = new_layer_techniques
layer["versions"] = {"attack": "11", "navigator": "4.6.6", "layer": "4.3"}
layer["name"] = "Older (updated) layer"
layer["description"] = "Updated the older layer with the current techniques"

with open("data/layers/updated_older_layer.json", "w") as f:
    json.dump(layer, f, indent=2)
