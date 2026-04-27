# lists_solution.py
# Python Lists — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Read the hint comment above each task
# 2. Replace the None with your actual code
# 3. Run lists_grading.py to check your answers:
#    python3 lists_grading.py

# ─────────────────────────────────────────────────────────────────────────────
# INVENTORY — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
INVENTORY = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30],      "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10, 20],           "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30, 40, 50],       "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30, 40],  "ip": "10.3.0.1"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [20, 30],           "ip": "10.4.0.1"},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 40, 50],       "ip": "10.5.0.1"},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down", "vlans": [10, 20, 30],       "ip": "10.6.0.1"},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [20, 30, 40, 50],  "ip": "10.7.0.1"},
]

# ─────────────────────────────────────────────────────────────────────────────
# YOUR ANSWERS — replace None with your code
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Extract all hostnames
# Hint: [d["..."] for d in INVENTORY]
all_hostnames = None

# Task 2 — Filter devices that are UP
# Hint: [d["..."] for d in INVENTORY if d["..."] == "..."]
up_hostnames = None

# Task 3 — Count devices that are DOWN
# Hint: sum(1 for d in INVENTORY if d["..."] == "...")
down_count = None

# Task 4 — Extract platforms in UPPERCASE
# Hint: [d["..."].upper() for d in INVENTORY]
platforms = None

# Task 5 — Flatten all VLANs into one list
# Hint: [v for d in INVENTORY for v in d["..."]]
all_vlans = None

# Task 6 — List unique VLANs in ascending order
# Hint: sorted(set(all_vlans))
unique_vlans = None

# Task 7 — Find devices carrying VLAN 30
# Hint: [d["..."] for d in INVENTORY if 30 in d["..."]]
vlan_30_devices = None

# Task 8 — Summarise devices with more than 2 VLANs
# Hint: sorted([{"hostname": d["..."], "vlan_count": len(d["..."])} for d in INVENTORY if len(d["..."]) > 2],
#              key=lambda x: x["..."], reverse=True)
vlan_summary = None

# Task 9 — Generate IOS-XE config blocks
# Hint: [f"hostname {d['...']}\n ntp server 10.0.0.100\n ip domain-name corp.net"
#        for d in INVENTORY if d["..."] == "..." and d["..."] == "..."]
config_blocks = None

# Task 10 — Build IP to hostname pairs sorted by hostname
# Hint: sorted([f"{d['...'"]} --> {d['...']}" for d in INVENTORY],
#              key=lambda s: s.split(" --> ")[1])
ip_hostname_pairs = None

# Task 11 — Number every device in the inventory
# Hint: [f"{i}. {d['...']} ({d['...']}) — {d['...']}"
#        for i, d in enumerate(INVENTORY, start=1)]
numbered_inventory = None

# Task 12 — Group devices by platform
# Hint: platforms_unique = sorted(set(d["..."] for d in INVENTORY))
#       platform_groups = [{"platform": p,
#                           "count":    sum(1 for d in INVENTORY if d["..."] == p),
#                           "up_count": sum(1 for d in INVENTORY if d["..."] == p and d["..."] == "...")}
#                          for p in platforms_unique]
platform_groups = None