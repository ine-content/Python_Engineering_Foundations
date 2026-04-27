# yaml_solution.py
# YAML Parsing — Your Solution File
# Cisco IaC Perspective
#
# HOW TO USE:
# 1. Write your answer for each task below
# 2. Run yaml_grading.py to check your answers:
#    python3 yaml_grading.py
#
# IMPORTANT:
# - Tasks 4 and 6 involve file I/O — use RELATIVE paths
# - The grader runs your script from a temporary working directory

# ─────────────────────────────────────────────────────────────────────────────
# DATA — do not edit this
# ─────────────────────────────────────────────────────────────────────────────
import yaml
import json
import os

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

INVENTORY_YAML_STR = """\
---
global:
  ntp: '10.0.0.100'
  dns: 8.8.8.8
  domain: corp.net

devices:
  - hostname: nyc-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.0.0.1
    vlans:    [10, 20, 30]
    config:
      ntp: '10.0.0.100'
      dns: 8.8.8.8

  - hostname: lon-sw-01
    platform: NX-OS
    status:   down
    ip:       10.1.0.1
    vlans:    [10, 20]
    config:
      ntp: '10.1.0.100'
      dns: 8.8.8.8

  - hostname: sin-fw-01
    platform: ASA
    status:   up
    ip:       10.2.0.1
    vlans:    [30, 40, 50]
    config:
      ntp: '10.0.0.100'
      dns: 8.8.8.8

  - hostname: ams-rtr-02
    platform: IOS-XE
    status:   up
    ip:       10.3.0.1
    vlans:    [10, 20, 30, 40]
    config:
      ntp: '10.0.0.100'
      dns: 8.8.8.8

  - hostname: tok-sw-01
    platform: NX-OS
    status:   down
    ip:       10.4.0.1
    vlans:    [20, 30]
    config:
      ntp: '10.4.0.100'
      dns: 8.8.8.8

  - hostname: syd-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.5.0.1
    vlans:    [10, 40, 50]
    config:
      ntp: '10.0.0.100'
      dns: 8.8.8.8

  - hostname: dub-fw-01
    platform: ASA
    status:   down
    ip:       10.6.0.1
    vlans:    [10, 20, 30]
    config:
      ntp: '10.0.0.100'
      dns: 8.8.8.8

  - hostname: mum-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.7.0.1
    vlans:    [20, 30, 40, 50]
    config:
      ntp: '10.7.0.100'
      dns: 8.8.8.8
"""

MULTI_DOC_YAML_STR = """\
---
hostname: nyc-rtr-01
platform: IOS-XE
status:   up
vlans:    [10, 20, 30]
---
hostname: lon-sw-01
platform: NX-OS
status:   down
vlans:    [10, 20]
---
hostname: sin-fw-01
platform: ASA
status:   up
vlans:    [30, 40, 50]
---
hostname: ams-rtr-02
platform: IOS-XE
status:   up
vlans:    [10, 20, 30, 40]
---
hostname: tok-sw-01
platform: NX-OS
status:   down
vlans:    [20, 30]
"""

# ─────────────────────────────────────────────────────────────────────────────
# YOUR ANSWERS
# ─────────────────────────────────────────────────────────────────────────────

# Task 1 — Parse YAML string and filter UP devices


# Task 2 — Extract global NTP and find custom NTP devices


# Task 3 — Serialize INVENTORY to a YAML string


# Task 4 — Write INVENTORY to a YAML file and read it back


# Task 5 — Parse a multi-document YAML string


# Task 6 — Write per-device host_vars YAML files


# Task 7 — Convert YAML devices to JSON


# Task 8 — Build a VLAN-to-devices map from multi-doc YAML