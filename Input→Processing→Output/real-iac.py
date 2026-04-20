
# Input (YAML/JSON-style)

devices = [
    {"name": "R1", "role": "core"},
    {"name": "R2", "role": "access"},
    {"name": "R3", "role": "core"},
    {"name": "R4", "role": "access"},
    {"name": "R5", "role": "core"},
    {"name": "R6", "role": "distribution"},
    {"name": "R7", "role": "distribution"}
]

# Processing

core_devices = []
distribution_devices = []
access_devices = []

for d in devices:
    if d["role"] == "core":
        core_devices.append(d["name"])
    elif d["role"] == "distribution":
        distribution_devices.append(d["name"])
    elif d["role"] == "access":
        access_devices.append(d["name"])

# Output

print(f"Core devices: {core_devices}")
print(f"Distribution devices: {distribution_devices}")
print(f"Access devices: {access_devices}")

