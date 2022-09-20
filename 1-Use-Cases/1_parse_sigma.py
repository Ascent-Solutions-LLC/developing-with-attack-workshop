import yaml


# Read the rule
with open("1-Use-Cases/dns_query_remote_access_software_domains.yml", "r") as f:
    sigma_rule = yaml.safe_load(f)

# The technique IDs are located inside of the `tags` property
tags = sigma_rule.get("tags")

technique_ids = []
for tag in tags:
    # Try to find the techniques (vs tactics)
    if "attack.t" in tag:
        technique_id = "".join(tag.split(".")[1:]).upper()
        technique_ids.append(technique_id)

print(technique_ids)
