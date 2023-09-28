import json


with open("data/layers/example_layer.json", "r") as f:
    layer = json.load(f)

name = layer["name"]
print(name)

description = layer["description"]
print(description)

techniques = layer["techniques"]
for technique in techniques:
    technique["score"] = technique.get("score", 0) * 5

with open("data/layers/example_layer_updated.json", "w") as f:
    json.dump(layer, f, indent=2)
