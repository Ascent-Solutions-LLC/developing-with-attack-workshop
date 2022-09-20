from difflib import SequenceMatcher
import json
import random
import yaml


# Read in a layer we are interested in: intrusion-set--899ce53f-13a0-479b-a0e4-67d46e241542
with open("data/layers/G0016-enterprise-layer.json", "r") as f:
    layer = json.load(f)

layer_techniques = layer.get("techniques")

layer_technique_ids = []
for technique in layer_techniques:
    layer_technique_ids.append(technique["techniqueID"])

layer_technique_ids.remove(random.choice(layer_technique_ids))

layer_technique_ids.sort()
print(layer_technique_ids)

with open("6-Real-World/group-techniques.yml", "r") as f:
    group_data = yaml.safe_load(f)

similarity = {}

for group in group_data:
    group_technique_ids = group["techniques"]
    ratio = SequenceMatcher(None, group_technique_ids, layer_technique_ids).ratio()
    similarity[group["name"]] = ratio

output = dict(sorted(similarity.items(), key=lambda item: item[1], reverse=True))
for k in output:
    percent = round(output[k] * 100, 2)
    print(f"{k}: {percent}%")

# Remove sub techniques

for group in group_data:
    group_technique_ids = [t_id for t_id in group["techniques"] if "." not in t_id]
    ratio = SequenceMatcher(None, group_technique_ids, layer_technique_ids).ratio()
    similarity[group["name"]] = ratio

output = dict(sorted(similarity.items(), key=lambda item: item[1], reverse=True))
for k in output:
    percent = round(output[k] * 100, 2)
    if percent > 0:
        print(f"{k}: {percent}%")
