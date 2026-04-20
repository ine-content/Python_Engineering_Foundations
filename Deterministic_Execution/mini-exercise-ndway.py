devices = ["R1", "R2", "R3", "R4", "R3"]
# Converting to set removes duplicates but loses order
devices = list(set(devices))                
if "R3" in devices:
    devices.remove("R3")
print(devices)