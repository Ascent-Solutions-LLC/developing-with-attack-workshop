from difflib import SequenceMatcher
import json

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

top_matches = "Top matches:\n"
for i, k in enumerate(output):
    percent = round(output[k] * 100, 2)
    top_matches += f"{k}: {percent}%\n"
    if i >= 5:
        break  # Only add top 5


layer_techniques = []
for technique in interesting_technique_ids:
    layer_technique = {
        "techniqueID": technique,
        "score": 1,
        "enabled": True
    }
    layer_techniques.append(layer_technique)

layer_data = {
    "name": "Lapsus IR Scenario",
    "description": top_matches,
    "techniques": layer_techniques,
    "versions": {
		"attack": "11",
		"navigator": "4.6.6",
		"layer": "4.3"
	},
	"domain": "enterprise-attack",
	"description": top_matches,
	"filters": {
		"platforms": [
			"Linux",
			"macOS",
			"Windows",
			"PRE",
			"Containers",
			"Network",
			"Office 365",
			"SaaS",
			"Google Workspace",
			"IaaS",
			"Azure AD"
		]
	},
	"sorting": 0,
	"layout": {
		"layout": "side",
		"aggregateFunction": "average",
		"showID": False,
		"showName": True,
		"showAggregateScores": False,
		"countUnscored": False
	},
	"hideDisabled": False,
	"gradient": {
		"colors": [
			"#ff6666ff",
			"#ffe766ff",
			"#8ec843ff"
		],
		"minValue": 0,
		"maxValue": 100
	},
	"legendItems": [],
	"metadata": [],
	"links": [],
	"showTacticRowBackground": False,
	"tacticRowBackground": "#dddddd",
	"selectTechniquesAcrossTactics": False,
	"selectSubtechniquesWithParent": False
}

with open("6-Real-World/lapsus_layer.json", "w") as f:
    json.dump(layer_data, f, indent=2)
