from stix2 import AttackPattern, IntrusionSet, Relationship

# Create a "group"
custom_intrusion_set = IntrusionSet(
    id="intrusion-set--a6274981-97a6-46bf-9487-2ceeab525362",
    name="APT-TBD",
    description="An example instrusion set",
    aliases=["APT-00", "Example Bear"]
)


# Create a "technique"
custom_pattern = AttackPattern(
    id="attack-pattern--d5274981-97a6-46bf-9487-2ceeab525351",
    name="Example Attack Pattern",
    description="This is an example pattern which attackers may use",
    revoked=False,
)


# Connect the two together
custom_relationship = Relationship(
    id="relationship--c7274981-97a6-46bf-9487-2ceeab525373",
    relationship_type="Uses",
    source_ref=custom_intrusion_set.id,
    target_ref=custom_pattern.id,
)

print(custom_relationship)
