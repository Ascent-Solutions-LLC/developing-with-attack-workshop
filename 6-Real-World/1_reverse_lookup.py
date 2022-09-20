from dataclasses import dataclass, field
import json
from typing import List
import yaml


@dataclass
class Technique:
    stix_data: dict

    @property
    def id(self):
        return self.stix_data.get("id")

    def __str__(self):
        return f"<Technique {self.mitre_id}>"

    @property
    def mitre_id(self):
        ext_refs = self.stix_data.get("external_references")
        for er in ext_refs:
            if er.get("source_name") == "mitre-attack":
                return er.get("external_id")


@dataclass
class Tool:
    stix_data: dict

    @property
    def id(self):
        return self.stix_data.get("id")

    @property
    def mitre_id(self):
        ext_refs = self.stix_data.get("external_references")
        for er in ext_refs:
            if er.get("source_name") == "mitre-attack":
                return er.get("external_id")

    @property
    def name(self):
        return self.stix_data.get("name")


@dataclass
class Group:
    stix_data: dict
    techniques: List[Technique] = field(default_factory=lambda: [])

    @property
    def id(self):
        return self.stix_data.get("id")

    @property
    def mitre_id(self):
        ext_refs = self.stix_data.get("external_references")
        for er in ext_refs:
            if er.get("source_name") == "mitre-attack":
                return er.get("external_id")

    @property
    def name(self):
        return self.stix_data.get("name")


@dataclass
class Relationship:
    group: Group
    technique: Technique
    stix_data: dict

    @property
    def id(self):
        return self.stix_data.get("id")


with open("stix_data/enterprise-attack.json", "r") as f:
    data = json.load(f)


objects = data["objects"]

groups = {}
for object in objects:
    if object.get("type") == "intrusion-set":
        group = Group(stix_data=object)
        groups[group.id] = group


techniques = {}
for object in objects:
    if object.get("type") == "attack-pattern":
        deprecated = object.get("x_mitre_deprecated")
        if deprecated:
            continue
        deprecated = object.get("x_mitre_deprecated")
        if deprecated:
            continue
        revoked = object.get("revoked")
        if revoked:
            continue
        domains = object.get("x_mitre_domains", [])
        if "enterprise-attack" not in domains:
            continue
        technique = Technique(stix_data=object)
        techniques[technique.id] = technique


software = {}
for object in objects:
    if object.get("type") == "tool":
        tool = Tool(stix_data=object)
        software[tool.id] = tool


relationships = {}
for object in objects:
    if object.get("type") == "relationship":
        source = object.get("source_ref")
        if source is None:
            continue
        target = object.get("target_ref")
        if target is None:
            continue
        if "intrusion-set" not in source:
            continue
        if "attack-pattern" not in target:
            continue
        relationship_type = object.get("relationship_type")
        if relationship_type != "uses":
            continue
        if source == "intrusion-set--899ce53f-13a0-479b-a0e4-67d46e241542":
            print(object.get("id"))
        group = groups[source]
        technique = techniques.get(target)
        if not technique:
            continue  # deprecated or revoked
        group.techniques.append(technique)

group_techniques = []
for group in groups:
    technique_ids = [t.mitre_id for t in groups[group].techniques]
    technique_ids.sort()
    group_id = groups[group].mitre_id
    name = groups[group].name
    d = {"name": name, "id": group_id, "techniques": technique_ids}
    group_techniques.append(d)


tool_techniques = []


with open("group-techniques.yml", "w") as f:
    yaml.dump(group_techniques, f)
