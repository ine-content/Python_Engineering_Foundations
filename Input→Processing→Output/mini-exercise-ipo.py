####################Bad Way####################

# devices = [
#     {"name": "R1", "status": "up"},
#     {"name": "R2", "status": "down"},
#     {"name": "R3", "status": "up"}
# ]
# print("Operational devices:")
# print(" - R1")
# print(" - R3")
# print("Non-operational devices:")
# print(" - R2")

###################Good Way###################
# Input
devices = [
    {"name": "R1", "status": "up"},
    {"name": "R2", "status": "down"},
    {"name": "R3", "status": "up"},
    {"name": "R4", "status": "down"}
]

# Processing
operational_devices = []
non_operational_devices = []

for device in devices:
    if device["status"] == "up":
        operational_devices.append(device["name"])
    else:
        non_operational_devices.append(device["name"])

# Output
print("Operational devices:")
for device in operational_devices:
    print(f" - {device}")

print("Non-operational devices:")
for device in non_operational_devices:
    print(f" - {device}")