from difflib import SequenceMatcher
import yaml


with open("6-Real-World/lapsus_ir_scenario.yml", "r") as f:
    data = yaml.safe_load(f)

interesting_technique_ids = data["techniques"]

with open("6-Real-World/group-techniques.yml", "r") as f:
    group_data = yaml.safe_load(f)

similarity = {}

for group in group_data:
    group_technique_ids = group["techniques"]
    ratio = SequenceMatcher(None, group_technique_ids, interesting_technique_ids).ratio()
    similarity[group["name"]] = ratio

output = dict(sorted(similarity.items(), key=lambda item: item[1], reverse=True))
for k in output:
    percent = round(output[k] * 100, 2)
    if percent > 0:
        print(f"{k}: {percent}%")
