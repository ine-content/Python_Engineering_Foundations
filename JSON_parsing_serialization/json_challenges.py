# json_challenges.py
# JSON Parsing & Serialization — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: json_solution.py
# 3. Run json_grading.py to check your answers

import os
import json
import copy
from datetime import datetime

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

def task_section(num, title, difficulty):
    stars = {"Easy": "★☆☆", "Medium": "★★☆", "Hard": "★★★"}
    label = f"Task {num:02d} — {title}  |  {difficulty} {stars[difficulty]}"
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {label}{RESET}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

def section(title):
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         JSON PARSING & SERIALIZATION — CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("8 tasks — Easy and Medium — all in one challenge.")
explain("All tasks work with JSON strings and Python objects.")
explain("Read each task, write your solution in json_solution.py,")
explain("then run json_grading.py to check it.")
blank()
explain("The data is already pasted at the top of")
explain("json_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Serialize INVENTORY to an indented JSON string", "Easy")
explain("Goal:  Serialize INVENTORY to a JSON string called 'inv_json'")
explain("       using json.dumps() with indent=2 and sort_keys=True.")
explain("       Also store the type of the result in 'inv_json_type'.")
blank()
explain("Variable names:  inv_json  /  inv_json_type")
blank()
header(">>> print(inv_json_type)")
header("<class 'str'>")
blank()
header(">>> print(inv_json[:60])")
header('[\n  {\n    "config": {\n      "dns": "8.8.8.8",\n      "ntp"')
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Parse a JSON string and filter active devices", "Easy")
explain("Goal:  Parse the JSON string below, then produce a list")
explain("       called 'active_hostnames' — hostnames where 'active' is True.")
blank()
explain("Use this string in your solution file:")
blank()
header("devices_json = '[")
header('  {\"hostname\": \"nyc-rtr-01\", \"platform\": \"IOS-XE\", \"active\": true,  \"backup\": null},')
header('  {\"hostname\": \"lon-sw-01\",  \"platform\": \"NX-OS\",  \"active\": false, \"backup\": null},')
header('  {\"hostname\": \"sin-fw-01\",  \"platform\": \"ASA\",    \"active\": true,  \"backup\": null}')
header("]'")
blank()
explain("Variable name:  active_hostnames")
blank()
header(">>> print(active_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Serialize INVENTORY as a compact JSON string", "Easy")
explain("Goal:  Serialize INVENTORY to a compact JSON string called")
explain("       'compact_json' with no extra spaces.")
blank()
explain("Rules:")
explain("  • Use separators=(',', ':')")
blank()
explain("Variable name:  compact_json")
blank()
header(">>> print(compact_json[:60])")
header('[{"hostname":"nyc-rtr-01","platform":"IOS-XE","status":"up"')
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Prove a JSON round-trip works", "Easy")
explain("Goal:  Serialize INVENTORY to JSON and immediately parse")
explain("       it back. Store the result in 'round_trip'.")
blank()
explain("Rules:")
explain("  • round_trip must equal INVENTORY (same content).")
explain("  • round_trip must be a list.")
blank()
explain("Variable name:  round_trip")
blank()
header(">>> print(round_trip == INVENTORY)")
header("True")
blank()
header(">>> print(type(round_trip))")
header("<class 'list'>")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Parse NX-OS interface JSON and filter UP interfaces", "Medium")
explain("Goal:  Parse NXOS_INTERFACES_STR and produce a list called")
explain("       'up_interfaces' containing dicts for interfaces")
explain("       whose state is 'up'.")
blank()
explain("Rules:")
explain("  • Navigate: data['TABLE_interface']['ROW_interface']")
explain("  • Only include interfaces where state == 'up'.")
explain("  • Each dict must have exactly three keys:")
explain("      'name' — the interface name")
explain("      'vlan' — the VLAN number as an INTEGER (not string)")
explain("      'ip'   — the IP address")
blank()
explain("Variable name:  up_interfaces")
blank()
header(">>> print(up_interfaces)")
header("[{'name': 'Ethernet1/1', 'vlan': 10, 'ip': '10.0.0.1'},")
header(" {'name': 'Ethernet1/3', 'vlan': 30, 'ip': '10.0.2.1'}]")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Flatten nested site inventory JSON", "Medium")
explain("Goal:  Parse NESTED_INVENTORY_STR and produce a flat list")
explain("       called 'all_devices' — one dict per device across")
explain("       all sites.")
blank()
explain("Rules:")
explain("  • Navigate: data['sites'][site]['devices']")
explain("  • Add a 'site' key to each device dict.")
explain("  • Order: site iteration order, then device order within each site.")
blank()
explain("Variable name:  all_devices")
blank()
header(">>> for d in all_devices: print(d['site'], d['hostname'])")
header("NYC nyc-rtr-01")
header("NYC nyc-sw-01")
header("LON lon-sw-01")
header("LON lon-fw-01")
header("SIN sin-rtr-01")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Build a site VLAN summary from parsed JSON", "Medium")
explain("Goal:  Using the parsed nested inventory from Task 6,")
explain("       produce a dict called 'site_vlan_summary' mapping")
explain("       each site name to a sorted list of unique VLANs")
explain("       across all its devices.")
blank()
explain("Variable name:  site_vlan_summary")
blank()
header(">>> print(site_vlan_summary)")
header("{'NYC': [10, 20, 30], 'LON': [10, 20, 30, 40], 'SIN': [10, 20, 50]}")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Serialize a datetime field using a custom default function", "Medium")
explain("Goal:  Enrich each device in INVENTORY with a 'checked_at'")
explain("       field set to datetime(2024, 1, 15, 10, 30), then")
explain("       serialize the enriched list to a JSON string called")
explain("       'safe_json' using a custom default= function.")
blank()
explain("Rules:")
explain("  • Use copy.deepcopy(INVENTORY) so you don't modify the original.")
explain("  • The custom default function must convert datetime to ISO format string.")
explain("  • Use datetime.isoformat() for the conversion.")
blank()
explain("Variable name:  safe_json")
blank()
header(">>> import json")
header(">>> data = json.loads(safe_json)")
header(">>> print(data[0]['checked_at'])")
header("'2024-01-15T10:30:00'")
blank()
header(">>> print(data[0]['hostname'])")
header("'nyc-rtr-01'")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: json_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task 1 — json.dumps(INVENTORY, indent=2, sort_keys=True)")
explain("  Task 2 — json.loads(devices_json), filter where d['active'] is True")
explain("  Task 3 — json.dumps(INVENTORY, separators=(',', ':'))")
explain("  Task 4 — json.loads(json.dumps(INVENTORY))")
explain("  Task 5 — json.loads(NXOS_INTERFACES_STR), navigate TABLE→ROW,")
explain("           filter state=='up', convert int(i['vlan'])")
explain("  Task 6 — json.loads(NESTED_INVENTORY_STR), flatten with nested loop,")
explain("           add 'site' key to each device")
explain("  Task 7 — group VLANs by site from all_devices, use set for uniqueness")
explain("  Task 8 — copy.deepcopy, add datetime field, json.dumps with default=")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# DONE
# ═════════════════════════════════════════════════════════════════════════════
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}  All tasks read. Now write your solution in:{RESET}")
print()
print(f"{BOLD}{CYAN}    json_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 json_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()