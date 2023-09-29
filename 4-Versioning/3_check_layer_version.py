import json


with open("data/layers/older_layer.json", "r") as f:
    layer = json.load(f)

versions = layer.get("versions")
print(json.dumps(versions, indent=2))


with open("data/layers/example_layer.json", "r") as f:
    layer = json.load(f)

versions = layer.get("versions")
print(json.dumps(versions, indent=2))
