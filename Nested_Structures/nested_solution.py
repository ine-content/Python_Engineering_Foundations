# nested_solution.py
# Python Nested Structures — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answer for each task below
# 2. Run nested_grading.py to check your answers:
#    python3 nested_grading.py

# ─────────────────────────────────────────────────────────────────────────────
# DATA — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
NETWORK = {
    "NYC": {
        "region": "us-east",
        "devices": [
            {
                "hostname": "nyc-rtr-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "up"},
                    {"name": "Gi0/2", "vlan": 30, "state": "down"},
                ],
            },
            {
                "hostname": "nyc-sw-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 40, "state": "up"},
                ],
            },
        ],
    },
    "LON": {
        "region": "eu-west",
        "devices": [
            {
                "hostname": "lon-sw-01",
                "platform": "NX-OS",
                "status":   "down",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "down"},
                ],
            },
            {
                "hostname": "lon-fw-01",
                "platform": "ASA",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 30, "state": "up"},
                    {"name": "Gi0/1", "vlan": 50, "state": "up"},
                ],
            },
        ],
    },
    "SIN": {
        "region": "ap-southeast",
        "devices": [
            {
                "hostname": "sin-rtr-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "up"},
                    {"name": "Gi0/2", "vlan": 50, "state": "up"},
                ],
            },
        ],
    },
}

RECORDS = [
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 20, "state": "up"},
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/2", "vlan": 30, "state": "down"},
    {"site": "NYC", "hostname": "nyc-sw-01",  "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "NYC", "hostname": "nyc-sw-01",  "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 40, "state": "up"},
    {"site": "LON", "hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "LON", "hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/1", "vlan": 20, "state": "down"},
    {"site": "LON", "hostname": "lon-fw-01",  "platform": "ASA",    "iface": "Gi0/0", "vlan": 30, "state": "up"},
    {"site": "LON", "hostname": "lon-fw-01",  "platform": "ASA",    "iface": "Gi0/1", "vlan": 50, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 20, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/2", "vlan": 50, "state": "up"},
]

# ─────────────────────────────────────────────────────────────────────────────
# YOUR ANSWERS
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Extract all hostnames


# Task 2 — Count devices per site


# Task 3 — Extract all interface names


# Task 4 — Map hostname to site


# Task 5 — Find interfaces that are DOWN


# Task 6 — Map VLAN to hostnames that use it


# Task 7 — Count interfaces per device


# Task 8 — List unique VLANs per site


# Task 9 — Find devices where ALL interfaces are UP


# Task 10 — Rebuild nested structure from flat RECORDS


# Task 11 — Summarise interfaces per site


# Task 12 — Build a VLAN report