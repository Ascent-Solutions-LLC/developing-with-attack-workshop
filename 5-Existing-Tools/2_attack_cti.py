from attackcti import attack_client


lift = attack_client()

print()
print("Getting techniques by the Internet Scan Data Source")
print()
techniques = lift.get_techniques_by_data_sources("Internet Scan")
print()
for t in techniques:
    print(t.name)
