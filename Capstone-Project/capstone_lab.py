# capstone_lab.py
# Python IaC Capstone Lab — Full Challenge
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read this file carefully — there is ONE big task
# 2. Write your solution in: capstone_solution.py
# 3. Run capstone_grading.py to check your answers

import os
import json
import yaml

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
WHITE  = "\033[97m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

def pause():
    input(f"\n{DIM}  [ Press ENTER to continue ]{RESET} ")
    print()

def header(text):
    print(f"    {CYAN}{text}{RESET}")

def explain(text):
    print(f"  {WHITE}{text}{RESET}")

def blank():
    print()

def section(title):
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

# ─────────────────────────────────────────────────────────────────────────────
# DATA — already in capstone_solution.py
# ─────────────────────────────────────────────────────────────────────────────
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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON IaC CAPSTONE LAB{RESET}")
print(f"{BOLD}         Full Challenge — Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("This is the capstone lab. One big realistic task that")
explain("covers every topic from the course.")
explain("")
explain("You will build a complete IaC pipeline from scratch.")
explain("Read every section carefully before writing any code.")
blank()
explain("Write your solution in:  capstone_solution.py")
explain("Check your answers with:  python3 capstone_grading.py")
blank()
explain("The data (INVENTORY, GLOBAL_NTP, etc.) is already")
explain("pasted at the top of capstone_solution.py.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SCENARIO
# ═════════════════════════════════════════════════════════════════════════════
section("The Scenario")

explain("You are a network automation engineer at a global firm.")
explain("You have an INVENTORY of 8 devices across 6 sites.")
explain("Your job is to build the full IaC automation pipeline:")
blank()
explain("  1. Validate and enrich the inventory")
explain("  2. Run compliance checks")
explain("  3. Generate per-device config files")
explain("  4. Build an Ansible inventory")
explain("  5. Process the inventory through a safe pipeline")
explain("  6. Produce a JSON operations report")
blank()
explain("Every deliverable must be a Python variable or function")
explain("that the grader can check.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 1 — DATA STRUCTURES & FILTERING
# ═════════════════════════════════════════════════════════════════════════════
section("Part 1 — Data Structures & Filtering  (Lists, Dicts, Filtering)")

explain("1a. Build a list called 'up_devices' containing the full")
explain("    device dict for every device whose status is 'up'.")
blank()
explain("1b. Build a dict called 'hostname_to_ip' mapping every")
explain("    hostname to its IP address. Include all 8 devices.")
blank()
explain("1c. Build a dict called 'site_hostnames' mapping each")
explain("    site name to a sorted list of hostnames at that site.")
blank()
explain("1d. Build a list called 'all_vlans' — every unique VLAN ID")
explain("    across all devices, sorted ascending. No duplicates.")
blank()
header("Expected:")
header("up_devices      → 5 device dicts (status == 'up')")
header("hostname_to_ip  → {'nyc-rtr-01': '10.0.0.1', ...}  (8 entries)")
header("site_hostnames  → {'NYC': ['nyc-rtr-01'], 'LON': ['lon-sw-01'], ...}")
header("all_vlans       → [10, 20, 30, 40, 50]")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 2 — NESTED STRUCTURES
# ═════════════════════════════════════════════════════════════════════════════
section("Part 2 — Nested Structures")

explain("2a. Build a dict called 'vlan_to_hostnames' mapping each")
explain("    unique VLAN to a sorted list of hostnames that carry it.")
blank()
explain("2b. Build a list called 'bgp_devices' containing just the")
explain("    hostnames of devices that have a non-None 'bgp' key.")
blank()
explain("2c. Build a dict called 'enriched_inventory' mapping each")
explain("    hostname to a new dict with these keys ONLY:")
explain("      site, role, platform, status, vlan_count, has_bgp")
explain("    vlan_count = len(vlans),  has_bgp = bgp is not None")
blank()
header("Expected:")
header("vlan_to_hostnames → {10: ['ams-rtr-02','dub-fw-01',...], ...}")
header("bgp_devices       → ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01']")
header("enriched_inventory → {'nyc-rtr-01': {site, role, platform, status,")
header("                       vlan_count: 3, has_bgp: True}, ...}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 3 — FUNCTIONS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 3 — Functions")

explain("3a. Write a function 'classify_device(hostname)' that")
explain("    returns 'router', 'switch', 'firewall', or 'unknown'")
explain("    based on whether the hostname contains 'rtr', 'sw', 'fw'.")
blank()
explain("3b. Write a function 'gen_base_config(device)' that returns")
explain("    a multi-line config string with exactly these 3 lines:")
explain("      hostname <hostname>")
explain("      ntp server <config.ntp>")
explain("      ip name-server <config.dns>")
blank()
explain("3c. Write a function 'get_devices_by_role(inventory, role)'")
explain("    that returns a list of hostnames with that role.")
blank()
header("Expected:")
header("classify_device('nyc-rtr-01') → 'router'")
header("classify_device('lon-sw-01')  → 'switch'")
header("classify_device('sin-fw-01')  → 'firewall'")
header("gen_base_config(INVENTORY[0]) → 'hostname nyc-rtr-01\\n...")
header("get_devices_by_role(INVENTORY,'core') → ['ams-rtr-02','mum-rtr-01',")
header("                                          'nyc-rtr-01','syd-rtr-01']")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 4 — CONDITIONALS & LOOPS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 4 — Conditionals & Loops")

explain("4a. Using a for loop (not a comprehension), build a dict")
explain("    called 'platform_counts' mapping each platform to")
explain("    the number of devices using it.")
blank()
explain("4b. Using a for loop with break, find the FIRST device")
explain("    in INVENTORY that is 'up' AND has more than 3 VLANs.")
explain("    Store the hostname in 'first_large_up_device'.")
explain("    If none found, store None.")
blank()
explain("4c. Build a list called 'device_labels' — one string per")
explain("    device using this priority logic (first match wins):")
explain("      status 'down'                       → 'OFFLINE: <hostname>'")
explain("      platform 'ASA' and status 'up'      → 'FIREWALL: <hostname>'")
explain("      role 'core' and status 'up'         → 'CORE: <hostname>'")
explain("      anything else                       → 'OTHER: <hostname>'")
blank()
header("Expected:")
header("platform_counts         → {'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
header("first_large_up_device   → 'ams-rtr-02'")
header("device_labels           → ['CORE: nyc-rtr-01', 'OFFLINE: lon-sw-01',")
header("                            'FIREWALL: sin-fw-01', ...]")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 5 — EXCEPTIONS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 5 — Exceptions")

explain("5a. Define a custom exception class 'DeviceOfflineError'")
explain("    that inherits from Exception.")
blank()
explain("5b. Write a function 'safe_connect(device)' that:")
explain("      • raises DeviceOfflineError if status == 'down'")
explain("      • returns 'connected: <hostname>' if status == 'up'")
blank()
explain("5c. Write a function 'batch_connect(inventory)' that calls")
explain("    safe_connect() on every device and returns a dict:")
explain("      {'connected': [...hostnames...],")
explain("       'offline':   [...hostnames...],")
explain("       'errors':    [...hostnames...]}")
blank()
header("Expected:")
header("batch_connect(INVENTORY)['connected'] →")
header("  ['nyc-rtr-01','sin-fw-01','ams-rtr-02','syd-rtr-01','mum-rtr-01']")
header("batch_connect(INVENTORY)['offline']   →")
header("  ['lon-sw-01','tok-sw-01','dub-fw-01']")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 6 — JSON & YAML
# ═════════════════════════════════════════════════════════════════════════════
section("Part 6 — JSON & YAML")

explain("6a. Build a dict called 'ansible_inv' in Ansible hosts.yaml")
explain("    format. Use PLATFORM_OS to map platform names.")
explain("    Structure: {'all': {'hosts': {hostname: {ansible_host,")
explain("    ansible_network_os, ansible_user: 'admin'}, ...}}}")
blank()
explain("6b. Serialize ansible_inv to a YAML string called")
explain("    'ansible_inv_yaml' using yaml.dump() with")
explain("    default_flow_style=False.")
blank()
explain("6c. Build a list called 'ntp_payloads' — one dict per UP")
explain("    device — each in RESTCONF format:")
explain("      {'hostname': ...,")
explain("       'payload': {'Cisco-IOS-XE-native:ntp': {")
explain("         'server': {'server-list': [{'ip-address': <ntp>}]}}}}")
blank()
header("Expected:")
header("ansible_inv['all']['hosts']['nyc-rtr-01'] →")
header("  {'ansible_host':'10.0.0.1','ansible_network_os':'ios','ansible_user':'admin'}")
header("ansible_inv_yaml → starts with 'all:\\n'")
header("ntp_payloads     → list of 5 dicts (up devices only)")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 7 — FILE I/O
# ═════════════════════════════════════════════════════════════════════════════
section("Part 7 — File I/O  (uses relative paths in temp dir)")

explain("The grader runs your script from a temporary working")
explain("directory. Use RELATIVE paths for all file operations.")
blank()
explain("7a. Write ansible_inv to a YAML file called 'hosts.yaml'")
explain("    using yaml.dump() with default_flow_style=False.")
blank()
explain("7b. Create a folder called 'configs' and write one .cfg")
explain("    file per device using gen_base_config(device).")
explain("    Filename: configs/<hostname>.cfg")
explain("    After writing, store the sorted list of .cfg filenames")
explain("    in 'cfg_files' (just filenames, not full paths).")
blank()
explain("7c. Write INVENTORY to a JSON file called 'inventory.json'")
explain("    with indent=2. Then read it back and store in")
explain("    'json_inventory' (must equal INVENTORY).")
blank()
header("Expected:")
header("hosts.yaml      → valid YAML, ansible_inv structure")
header("cfg_files       → ['ams-rtr-02.cfg', 'dub-fw-01.cfg', ...]  8 files")
header("json_inventory  → equal to INVENTORY, type list")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 8 — COMPLIANCE & PIPELINE
# ═════════════════════════════════════════════════════════════════════════════
section("Part 8 — Compliance & Full Pipeline")

explain("8a. Build a list called 'compliance_report' — one dict per")
explain("    device with compliance results. Check three rules:")
explain("      status_up    — status must be 'up'")
explain("      standard_ntp — config.ntp must equal GLOBAL_NTP")
explain("      has_vlans    — vlans list must not be empty")
explain("    Each dict: {hostname, overall: 'PASS'|'FAIL',")
explain("                checks: {status_up, standard_ntp, has_vlans}}")
blank()
explain("8b. Run the full pipeline on INVENTORY:")
explain("    Filter: up devices on IOS-XE or NX-OS only.")
explain("    For each, call batch_connect() and gen_base_config().")
explain("    Build a list called 'pipeline_report' — one dict per")
explain("    filtered device:")
explain("      {hostname, status, vlan_count,")
explain("       connect_result, config_lines: int}")
explain("    config_lines = number of lines in gen_base_config(device)")
blank()
explain("8c. Write pipeline_report to 'pipeline_report.json' (indent=2).")
explain("    Store the sorted list of hostnames in 'pipeline_hostnames'.")
blank()
header("Expected:")
header("compliance_report → 8 dicts, PASS for nyc/sin/ams/syd devices")
header("pipeline_report   → 3 dicts (nyc-rtr-01, ams-rtr-02, syd-rtr-01)")
header("pipeline_hostnames → ['ams-rtr-02', 'nyc-rtr-01', 'syd-rtr-01']")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# DONE
# ═════════════════════════════════════════════════════════════════════════════
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}  All parts read. Now write your solution in:{RESET}")
print()
print(f"{BOLD}{CYAN}    capstone_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 capstone_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()