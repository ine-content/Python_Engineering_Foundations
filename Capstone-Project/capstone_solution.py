# capstone_solution.py
# Python IaC Capstone Lab — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answers for each part below
# 2. Run capstone_grading.py to check:
#    python3 capstone_grading.py
#
# IMPORTANT:
# - Parts 7 and 8c involve file I/O — use RELATIVE paths
# - The grader runs your script from a temporary working directory

# ─────────────────────────────────────────────────────────────────────────────
# DATA — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
import json
import yaml
import os

GLOBAL_NTP      = "10.0.0.100"
RESERVED_VLANS  = {1, 1002, 1003, 1004, 1005}
PLATFORM_OS     = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa", "IOS-XR": "iosxr"}

VLAN_INTENT = {
    10: {"name": "MGMT",    "svi_ip": "10.10.0.1/24"},
    20: {"name": "USERS",   "svi_ip": "10.20.0.1/24"},
    30: {"name": "VOICE",   "svi_ip": "10.30.0.1/24"},
    40: {"name": "SERVERS", "svi_ip": "10.40.0.1/24"},
    50: {"name": "DMZ",     "svi_ip": "10.50.0.1/24"},
}

INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "NYC", "role": "core", "ip": "10.0.0.1",
        "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65001, "neighbors": ["10.3.0.1"]},
    },
    {
        "hostname": "lon-sw-01", "platform": "NX-OS", "status": "down",
        "site": "LON", "role": "distribution", "ip": "10.1.0.1",
        "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "sin-fw-01", "platform": "ASA", "status": "up",
        "site": "SIN", "role": "firewall", "ip": "10.2.0.1",
        "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "site": "AMS", "role": "core", "ip": "10.3.0.1",
        "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65002, "neighbors": ["10.0.0.1"]},
    },
    {
        "hostname": "tok-sw-01", "platform": "NX-OS", "status": "down",
        "site": "TOK", "role": "access", "ip": "10.4.0.1",
        "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "SYD", "role": "core", "ip": "10.5.0.1",
        "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65003, "neighbors": ["10.7.0.1"]},
    },
    {
        "hostname": "dub-fw-01", "platform": "ASA", "status": "down",
        "site": "DUB", "role": "firewall", "ip": "10.6.0.1",
        "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "MUM", "role": "core", "ip": "10.7.0.1",
        "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65004, "neighbors": ["10.5.0.1"]},
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# PART 1 — Lists & Dicts
# ─────────────────────────────────────────────────────────────────────────────

# 1a — List of hostnames where status == 'up'
up_hostnames = None

# 1b — Dict mapping hostname → ip for all 8 devices
hostname_to_ip = None

# 1c — Dict mapping platform → count
platform_counts = None

# 1d — Sorted list of unique VLAN IDs across all devices
all_vlans = None


# ─────────────────────────────────────────────────────────────────────────────
# PART 2 — Nested Structures
# ─────────────────────────────────────────────────────────────────────────────

# 2a — Dict mapping site → sorted list of hostnames at that site
site_hostnames = None

# 2b — Sorted list of hostnames that have a non-None 'bgp' key
bgp_devices = None

# 2c — Dict mapping ntp_server_ip → sorted list of hostnames using it
ntp_map = None


# ─────────────────────────────────────────────────────────────────────────────
# PART 3 — Functions
# ─────────────────────────────────────────────────────────────────────────────

# 3a — Returns 'router', 'switch', 'firewall', or 'unknown'


# 3b — Returns a 3-line config string for a device


# 3c — Returns sorted list of hostnames with the given role


# ─────────────────────────────────────────────────────────────────────────────
# PART 4 — Conditionals & Loops
# ─────────────────────────────────────────────────────────────────────────────

# 4a — Hostname of first 'up' device with more than 3 VLANs (use for + break)
first_large_up_device = None

# 4b — List of label strings: 'OFFLINE/FIREWALL/CORE/OTHER: <hostname>'
device_labels = None

# 4c — List of hostnames whose NTP differs from GLOBAL_NTP
custom_ntp_hosts = None


# ─────────────────────────────────────────────────────────────────────────────
# PART 5 — Exceptions
# ─────────────────────────────────────────────────────────────────────────────

# 5a — Define DeviceOfflineError(Exception)


# 5b — def safe_connect(device)


# 5c — def batch_connect(inventory) → {connected, offline, errors}


# ─────────────────────────────────────────────────────────────────────────────
# PART 6 — JSON & YAML
# ─────────────────────────────────────────────────────────────────────────────

# 6a — Ansible inventory dict: {'all': {'hosts': {...}}}
ansible_inv = None

# 6b — ansible_inv serialized to YAML string
ansible_inv_yaml = None

# 6c — INVENTORY serialized to JSON and immediately parsed back
inv_json_roundtrip = None


# ─────────────────────────────────────────────────────────────────────────────
# PART 7 — File I/O  (use relative paths)
# ─────────────────────────────────────────────────────────────────────────────

# 7a — Write ansible_inv to 'hosts.yaml'


# 7b — Write one .cfg file per device to 'configs/<hostname>.cfg'
#      Store sorted filenames in cfg_files
cfg_files = None

# 7c — Write INVENTORY to 'inventory.json' (indent=2), read back into json_inventory
json_inventory = None


# ─────────────────────────────────────────────────────────────────────────────
# PART 8 — Compliance & Pipeline
# ─────────────────────────────────────────────────────────────────────────────

# 8a — List of {hostname, overall, status_up, standard_ntp, has_vlans} for all 8 devices
compliance_report = None

# 8b — Filter: up devices on IOS-XE or NX-OS only
#      pipeline_report: list of {hostname, status, vlan_count, connect_result}
#      pipeline_hostnames: sorted list of their hostnames
pipeline_report    = None
pipeline_hostnames = None

# 8c — Write pipeline_report to 'pipeline_report.json' (indent=2)