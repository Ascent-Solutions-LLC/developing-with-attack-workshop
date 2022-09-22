from attackcti import attack_client


lift = attack_client()

techniques = lift.get_techniques()
print(f"Number of techniques: {len(techniques)}")
