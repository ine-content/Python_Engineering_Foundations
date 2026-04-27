# lists_solution.py
# Python Lists — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answer for each task below
# 2. Run lists_grading.py to check your answers:
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
# YOUR ANSWERS
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Extract all hostnames


# Task 2 — Filter devices that are UP


# Task 3 — Count devices that are DOWN


# Task 4 — Extract platforms in UPPERCASE


# Task 5 — Flatten all VLANs into one list


# Task 6 — List unique VLANs in ascending order


# Task 7 — Find devices carrying VLAN 30


# Task 8 — Summarise devices with more than 2 VLANs


# Task 9 — Generate IOS-XE config blocks


# Task 10 — Build IP to hostname pairs sorted by hostname


# Task 11 — Number every device in the inventory


# Task 12 — Group devices by platform