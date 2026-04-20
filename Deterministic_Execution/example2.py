devices = ["R1", "R2", "R3"]

filtered = []

for d in devices:
    if d != "R2":
        filtered.append(d)

print(filtered)