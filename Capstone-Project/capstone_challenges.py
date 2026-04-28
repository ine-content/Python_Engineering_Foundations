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
explain("This is the capstone lab. One big realistic challenge")
explain("that covers every topic from the course — at Easy and")
explain("Medium difficulty only.")
blank()
explain("Write your solution in:  capstone_solution.py")
explain("Check your answers with:  python3 capstone_grading.py")
blank()
explain("All data is already pasted at the top of")
explain("capstone_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SCENARIO
# ═════════════════════════════════════════════════════════════════════════════
section("The Scenario")

explain("You are a network automation engineer at a global firm.")
explain("You have an INVENTORY of 8 devices across 6 sites.")
explain("Your job is to build the full IaC automation pipeline:")
blank()
explain("  1. Filter and summarise the inventory")
explain("  2. Query nested structures")
explain("  3. Write helper functions")
explain("  4. Apply conditionals and loops")
explain("  5. Handle exceptions safely")
explain("  6. Serialize data to JSON and YAML")
explain("  7. Write output files")
explain("  8. Run compliance checks and produce reports")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 1 — LISTS & DICTS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 1 — Lists & Dicts  ★☆☆ Easy")

explain("1a. Build a list called 'up_hostnames' containing the")
explain("    hostname of every device whose status is 'up'.")
blank()
explain("1b. Build a dict called 'hostname_to_ip' mapping every")
explain("    hostname to its IP address. Include all 8 devices.")
blank()
explain("1c. Build a dict called 'platform_counts' mapping each")
explain("    platform name to how many devices use it.")
blank()
explain("1d. Build a sorted list called 'all_vlans' of every unique")
explain("    VLAN ID across all devices. No duplicates.")
blank()
header("Expected:")
header("up_hostnames    → ['nyc-rtr-01','sin-fw-01','ams-rtr-02','syd-rtr-01','mum-rtr-01']")
header("hostname_to_ip  → {'nyc-rtr-01':'10.0.0.1', ...}  (8 entries)")
header("platform_counts → {'IOS-XE':4, 'NX-OS':2, 'ASA':2}")
header("all_vlans       → [10, 20, 30, 40, 50]")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 2 — NESTED STRUCTURES
# ═════════════════════════════════════════════════════════════════════════════
section("Part 2 — Nested Structures  ★★☆ Medium")

explain("2a. Build a dict called 'site_hostnames' mapping each site")
explain("    name to a sorted list of hostnames at that site.")
blank()
explain("2b. Build a list called 'bgp_devices' containing the")
explain("    hostnames of devices that have a non-None 'bgp' key.")
explain("    Sort the list alphabetically.")
blank()
explain("2c. Build a dict called 'ntp_map' mapping each unique NTP")
explain("    server IP to a sorted list of hostnames using it.")
blank()
header("Expected:")
header("site_hostnames → {'NYC':['nyc-rtr-01'], 'LON':['lon-sw-01'], ...}")
header("bgp_devices    → ['ams-rtr-02','mum-rtr-01','nyc-rtr-01','syd-rtr-01']")
header("ntp_map        → {'10.0.0.100':['ams-rtr-02','dub-fw-01',...],")
header("                   '10.1.0.100':['lon-sw-01'],")
header("                   '10.4.0.100':['tok-sw-01'],")
header("                   '10.7.0.100':['mum-rtr-01']}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 3 — FUNCTIONS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 3 — Functions  ★★☆ Medium")

explain("3a. Write a function 'classify_device(hostname)' that")
explain("    returns 'router', 'switch', 'firewall', or 'unknown'")
explain("    based on whether the hostname contains 'rtr','sw','fw'.")
blank()
explain("3b. Write a function 'gen_base_config(device)' that returns")
explain("    a multi-line config string with exactly these 3 lines:")
explain("      hostname <hostname>")
explain("      ntp server <config.ntp>")
explain("      ip name-server <config.dns>")
blank()
explain("3c. Write a function 'get_devices_by_role(inventory, role)'")
explain("    that returns a sorted list of hostnames with that role.")
blank()
header("Expected:")
header("classify_device('nyc-rtr-01') → 'router'")
header("classify_device('lon-sw-01')  → 'switch'")
header("classify_device('sin-fw-01')  → 'firewall'")
header("gen_base_config(INVENTORY[0]) →")
header("  'hostname nyc-rtr-01")
header("   ntp server 10.0.0.100")
header("   ip name-server 8.8.8.8'")
header("get_devices_by_role(INVENTORY,'core') →")
header("  ['ams-rtr-02','mum-rtr-01','nyc-rtr-01','syd-rtr-01']")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 4 — CONDITIONALS & LOOPS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 4 — Conditionals & Loops  ★★☆ Medium")

explain("4a. Using a for loop with break, find the FIRST device in")
explain("    INVENTORY that is 'up' AND has more than 3 VLANs.")
explain("    Store the hostname in 'first_large_up_device'.")
explain("    If none found, store None.")
blank()
explain("4b. Build a list called 'device_labels' — one string per")
explain("    device using this priority order (first match wins):")
explain("      status 'down'                    → 'OFFLINE: <hostname>'")
explain("      platform 'ASA' and status 'up'   → 'FIREWALL: <hostname>'")
explain("      role 'core' and status 'up'      → 'CORE: <hostname>'")
explain("      anything else                    → 'OTHER: <hostname>'")
blank()
explain("4c. Build a list called 'custom_ntp_hosts' containing the")
explain("    hostname of every device whose NTP differs from GLOBAL_NTP.")
blank()
header("Expected:")
header("first_large_up_device → 'ams-rtr-02'")
header("device_labels → ['CORE: nyc-rtr-01','OFFLINE: lon-sw-01',")
header("                  'FIREWALL: sin-fw-01','CORE: ams-rtr-02',")
header("                  'OFFLINE: tok-sw-01','CORE: syd-rtr-01',")
header("                  'OFFLINE: dub-fw-01','CORE: mum-rtr-01']")
header("custom_ntp_hosts → ['lon-sw-01','tok-sw-01','mum-rtr-01']")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 5 — EXCEPTIONS
# ═════════════════════════════════════════════════════════════════════════════
section("Part 5 — Exceptions  ★★☆ Medium")

explain("5a. Define a custom exception class 'DeviceOfflineError'")
explain("    that inherits from Exception.")
blank()
explain("5b. Write a function 'safe_connect(device)' that:")
explain("      raises DeviceOfflineError if status == 'down'")
explain("      returns 'connected: <hostname>' if status == 'up'")
blank()
explain("5c. Write a function 'batch_connect(inventory)' that calls")
explain("    safe_connect() on every device and returns a dict with")
explain("    three keys: 'connected', 'offline', and 'errors'.")
explain("    Each key maps to a list of hostnames.")
blank()
header("Expected:")
header("batch_connect(INVENTORY)['connected'] →")
header("  ['nyc-rtr-01','sin-fw-01','ams-rtr-02','syd-rtr-01','mum-rtr-01']")
header("batch_connect(INVENTORY)['offline']   →")
header("  ['lon-sw-01','tok-sw-01','dub-fw-01']")
header("batch_connect(INVENTORY)['errors']    → []")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 6 — JSON & YAML
# ═════════════════════════════════════════════════════════════════════════════
section("Part 6 — JSON & YAML  ★★☆ Medium")

explain("6a. Build a dict called 'ansible_inv' in Ansible hosts.yaml")
explain("    format using PLATFORM_OS to map platform names:")
explain("      {'all': {'hosts': {")
explain("        hostname: {ansible_host, ansible_network_os, ansible_user: 'admin'}}}}")
blank()
explain("6b. Serialize ansible_inv to a YAML string called")
explain("    'ansible_inv_yaml' using yaml.dump() with")
explain("    default_flow_style=False.")
blank()
explain("6c. Build a dict called 'inv_json_roundtrip' by serializing")
explain("    INVENTORY to a JSON string and immediately parsing it")
explain("    back. It must equal INVENTORY.")
blank()
header("Expected:")
header("ansible_inv['all']['hosts']['nyc-rtr-01'] →")
header("  {'ansible_host':'10.0.0.1',")
header("   'ansible_network_os':'ios',")
header("   'ansible_user':'admin'}")
header("ansible_inv_yaml → YAML string starting with 'all:\\n'")
header("inv_json_roundtrip == INVENTORY → True")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 7 — FILE I/O
# ═════════════════════════════════════════════════════════════════════════════
section("Part 7 — File I/O  ★★☆ Medium")

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
explain("    'json_inventory'. It must equal INVENTORY.")
blank()
header("Expected:")
header("hosts.yaml     → valid YAML, ansible_inv structure")
header("cfg_files      → ['ams-rtr-02.cfg','dub-fw-01.cfg',...]  8 files")
header("json_inventory → equals INVENTORY, type list")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PART 8 — COMPLIANCE & PIPELINE
# ═════════════════════════════════════════════════════════════════════════════
section("Part 8 — Compliance & Pipeline  ★★☆ Medium")

explain("8a. Build a list called 'compliance_report' — one dict per")
explain("    device. Check three rules and set overall to 'PASS' only")
explain("    if ALL three pass:")
explain("      status_up    — status must be 'up'")
explain("      standard_ntp — config.ntp must equal GLOBAL_NTP")
explain("      has_vlans    — vlans list must not be empty")
explain("    Each dict: {hostname, overall: 'PASS'|'FAIL',")
explain("                status_up: bool, standard_ntp: bool, has_vlans: bool}")
blank()
explain("8b. Filter INVENTORY to only 'up' devices on IOS-XE or NX-OS.")
explain("    Build a list called 'pipeline_report' — one dict per")
explain("    filtered device:")
explain("      {hostname, status, vlan_count, connect_result}")
explain("    connect_result = the return value of safe_connect(device)")
explain("    Store the sorted hostnames in 'pipeline_hostnames'.")
blank()
explain("8c. Write pipeline_report to 'pipeline_report.json' (indent=2).")
blank()
header("Expected:")
header("compliance_report → 8 dicts.")
header("  overall='PASS' for: nyc-rtr-01, sin-fw-01, ams-rtr-02, syd-rtr-01")
header("  overall='FAIL' for: lon-sw-01, tok-sw-01, dub-fw-01, mum-rtr-01")
header("pipeline_report   → 3 dicts (nyc-rtr-01, ams-rtr-02, syd-rtr-01)")
header("pipeline_hostnames → ['ams-rtr-02','nyc-rtr-01','syd-rtr-01']")

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