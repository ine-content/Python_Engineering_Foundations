# file_io_solution.py
# Python File I/O — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answer for each task below
# 2. Run file_io_grading.py to check your answers:
#    python3 file_io_grading.py
#
# IMPORTANT:
# - Use RELATIVE paths (e.g. 'hostnames.txt', not '/home/user/hostnames.txt')
# - The grader runs your script from a temporary working directory
# - os, csv, and json are pre-injected — no need to import them

# ─────────────────────────────────────────────────────────────────────────────
# DATA — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
GLOBAL_NTP = "10.0.0.100"

INVENTORY = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.0.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.1.0.1", "vlans": [10, 20],
     "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"}},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
     "ip": "10.2.0.1", "vlans": [30, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
     "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.4.0.1", "vlans": [20, 30],
     "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"}},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.5.0.1", "vlans": [10, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
     "ip": "10.6.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
     "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"}},
]

# ─────────────────────────────────────────────────────────────────────────────
# YOUR ANSWERS
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Write hostnames to a text file


# Task 2 — Read hostnames back from the text file


# Task 3 — Parse a structured device list file


# Task 4 — Write one config file per device


# Task 5 — Write INVENTORY to a CSV file


# Task 6 — Read CSV and filter UP devices


# Task 7 — Write and read INVENTORY as JSON


# Task 8 — Enrich JSON, write back, and build a summary dict