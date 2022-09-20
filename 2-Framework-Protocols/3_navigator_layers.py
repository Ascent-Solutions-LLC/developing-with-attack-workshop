import json


with open("data/layers/G0016-enterprise-layer.json", "r") as f:
    layer = json.load(f)

name = layer["name"]
print(name)

description = layer["description"]
print(description)

techniques = layer["techniques"]
for technique in techniques:
    technique["score"] = technique["score"] * 5

with open("data/layers/G0016-enterprise-layer-updated.json", "w") as f:
    json.dump(layer, f, indent=2)
