devices = ["R1", "R2", "R3", "R4", "R3"]
        
for d in devices:
    if d == "R3":
        devices.remove(d)
print(devices)
