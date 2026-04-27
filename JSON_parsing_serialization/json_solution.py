# json_solution.py
# JSON Parsing & Serialization — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answer for each task below
# 2. Run json_grading.py to check your answers:
#    python3 json_grading.py

# ─────────────────────────────────────────────────────────────────────────────
# DATA — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
import json
import copy
from datetime import datetime

GLOBAL_NTP = "10.0.0.100"

INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
    },
]

NXOS_INTERFACES_STR = json.dumps({
    "TABLE_interface": {
        "ROW_interface": [
            {"interface": "Ethernet1/1", "state": "up",   "vlan": "10", "eth_ip_addr": "10.0.0.1"},
            {"interface": "Ethernet1/2", "state": "down", "vlan": "20", "eth_ip_addr": "10.0.1.1"},
            {"interface": "Ethernet1/3", "state": "up",   "vlan": "30", "eth_ip_addr": "10.0.2.1"},
            {"interface": "Ethernet1/4", "state": "down", "vlan": "10", "eth_ip_addr": "10.0.3.1"},
        ]
    }
})

NESTED_INVENTORY_STR = json.dumps({
    "sites": {
        "NYC": {
            "region": "us-east",
            "devices": [
                {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30]},
                {"hostname": "nyc-sw-01",  "platform": "IOS-XE", "status": "up",   "vlans": [10, 20]},
            ],
        },
        "LON": {
            "region": "eu-west",
            "devices": [
                {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10, 20]},
                {"hostname": "lon-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30, 40]},
            ],
        },
        "SIN": {
            "region": "ap-southeast",
            "devices": [
                {"hostname": "sin-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 50]},
            ],
        },
    }
})

# ─────────────────────────────────────────────────────────────────────────────
# YOUR ANSWERS
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Serialize INVENTORY to an indented JSON string


# Task 2 — Parse a JSON string and filter active devices


# Task 3 — Serialize INVENTORY as a compact JSON string


# Task 4 — Prove a JSON round-trip works


# Task 5 — Parse NX-OS interface JSON and filter UP interfaces


# Task 6 — Flatten nested site inventory JSON


# Task 7 — Build a site VLAN summary from parsed JSON


# Task 8 — Serialize a datetime field using a custom default function