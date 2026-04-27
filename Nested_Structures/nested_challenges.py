# nested_challenges.py
# Python Nested Structures — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: nested_solution.py
# 3. Run nested_grading.py to check your answers

import os

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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         NESTED STRUCTURES — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same NETWORK and RECORDS data.")
explain("Read each task, write your solution in nested_solution.py,")
explain("then run nested_grading.py to check it.")
blank()
explain("The NETWORK and RECORDS are already pasted at the top of")
explain("nested_solution.py — just write your answers below them.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# DATA OVERVIEW
# ═════════════════════════════════════════════════════════════════════════════
section("Data Structure Overview")
explain("NETWORK — three-level nested dict:")
explain("  NETWORK[site]['devices'] → list of device dicts")
explain("  Each device has: hostname, platform, status, interfaces")
explain("  Each interface has: name, vlan, state")
blank()
explain("RECORDS — same data as a flat list of dicts:")
explain("  Each record has: site, hostname, platform, iface, vlan, state")
blank()
explain("Both are already in nested_solution.py — do not retype them.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Extract all hostnames", "Easy")
explain("Goal:  Build a list of every hostname across all sites,")
explain("       in NETWORK iteration order.")
blank()
explain("Rules:")
explain("  • Loop: site → devices.")
explain("  • Include all 5 devices.")
blank()
explain("Variable name:  all_hostnames")
blank()
header(">>> print(all_hostnames)")
header("['nyc-rtr-01', 'nyc-sw-01', 'lon-sw-01', 'lon-fw-01', 'sin-rtr-01']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Count devices per site", "Easy")
explain("Goal:  Build a dict mapping each site name to the")
explain("       number of devices it has.")
blank()
explain("Rules:")
explain("  • Key = site name, Value = integer count.")
blank()
explain("Variable name:  site_device_count")
blank()
header(">>> print(site_device_count)")
header("{'NYC': 2, 'LON': 2, 'SIN': 1}")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Extract all interface names", "Easy")
explain("Goal:  Build a list of every interface name across all")
explain("       devices and all sites.")
blank()
explain("Rules:")
explain("  • Loop order: site → device → interface.")
explain("  • Keep duplicates — 'Gi0/0' appears many times.")
blank()
explain("Variable name:  all_interface_names")
blank()
header(">>> print(all_interface_names)")
header("['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/0', 'Gi0/1',")
header(" 'Gi0/0', 'Gi0/1', 'Gi0/0', 'Gi0/1',")
header(" 'Gi0/0', 'Gi0/1', 'Gi0/2']")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Map hostname to site", "Easy")
explain("Goal:  Build a dict mapping each hostname to the")
explain("       site it belongs to.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = site name.")
explain("  • Include all 5 devices.")
blank()
explain("Variable name:  hostname_to_site")
blank()
header(">>> print(hostname_to_site)")
header("{'nyc-rtr-01': 'NYC', 'nyc-sw-01': 'NYC',")
header(" 'lon-sw-01':  'LON', 'lon-fw-01': 'LON',")
header(" 'sin-rtr-01': 'SIN'}")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Find interfaces that are DOWN", "Medium")
explain("Goal:  Build a list of tuples — one per interface")
explain("       whose state is 'down'.")
blank()
explain("Rules:")
explain("  • Each tuple: (site, hostname, interface_name).")
explain("  • Order matches NETWORK iteration order.")
blank()
explain("Variable name:  down_interfaces")
blank()
header(">>> print(down_interfaces)")
header("[('NYC', 'nyc-rtr-01', 'Gi0/2'),")
header(" ('LON', 'lon-sw-01',  'Gi0/1')]")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Map VLAN to hostnames that use it", "Medium")
explain("Goal:  Build a dict mapping each VLAN number to a")
explain("       sorted list of hostnames that have that VLAN")
explain("       on at least one interface.")
blank()
explain("Rules:")
explain("  • Key = VLAN number, Value = sorted list of hostnames.")
explain("  • Each hostname appears only once per VLAN.")
blank()
explain("Variable name:  vlan_usage")
blank()
header(">>> print(vlan_usage)")
header("{10: ['lon-sw-01', 'nyc-rtr-01', 'nyc-sw-01', 'sin-rtr-01'],")
header(" 20: ['lon-sw-01', 'nyc-rtr-01', 'sin-rtr-01'],")
header(" 30: ['lon-fw-01', 'nyc-rtr-01'],")
header(" 40: ['nyc-sw-01'],")
header(" 50: ['lon-fw-01', 'sin-rtr-01']}")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Count interfaces per device", "Medium")
explain("Goal:  Build a dict mapping each hostname to the")
explain("       number of interfaces it has.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = integer count.")
explain("  • Include all 5 devices.")
blank()
explain("Variable name:  device_interface_count")
blank()
header(">>> print(device_interface_count)")
header("{'nyc-rtr-01': 3, 'nyc-sw-01': 2,")
header(" 'lon-sw-01':  2, 'lon-fw-01': 2,")
header(" 'sin-rtr-01': 3}")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "List unique VLANs per site", "Medium")
explain("Goal:  Build a dict mapping each site to a sorted list")
explain("       of unique VLANs used across all its devices.")
blank()
explain("Rules:")
explain("  • Key = site name, Value = sorted list of unique VLAN numbers.")
blank()
explain("Variable name:  site_vlan_summary")
blank()
header(">>> print(site_vlan_summary)")
header("{'NYC': [10, 20, 30, 40],")
header(" 'LON': [10, 20, 30, 50],")
header(" 'SIN': [10, 20, 50]}")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Find devices where ALL interfaces are UP", "Hard")
explain("Goal:  Build a list of hostnames where every single")
explain("       interface has state 'up'.")
blank()
explain("Rules:")
explain("  • Skip any device that has even one 'down' interface.")
explain("  • Order matches NETWORK iteration order.")
blank()
explain("Variable name:  devices_all_up")
blank()
header(">>> print(devices_all_up)")
header("['nyc-sw-01', 'lon-fw-01', 'sin-rtr-01']")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Rebuild nested structure from flat RECORDS", "Hard")
explain("Goal:  Using RECORDS (the flat list), build a dict")
explain("       called 'rebuilt' mapping each hostname to a")
explain("       dict with its platform, site, and interfaces.")
blank()
explain("Rules:")
explain("  • Use RECORDS — not NETWORK — as your source.")
explain("  • Key = hostname.")
explain("  • Value = {'platform': ..., 'site': ..., 'interfaces': [...]}")
explain("  • Each interface: {'name': ..., 'vlan': ..., 'state': ...}")
explain("  • Interface order must match order in RECORDS.")
blank()
explain("Variable name:  rebuilt")
blank()
header(">>> print(rebuilt['nyc-rtr-01'])")
header("{'platform': 'IOS-XE', 'site': 'NYC',")
header(" 'interfaces': [{'name': 'Gi0/0', 'vlan': 10, 'state': 'up'},")
header("                {'name': 'Gi0/1', 'vlan': 20, 'state': 'up'},")
header("                {'name': 'Gi0/2', 'vlan': 30, 'state': 'down'}]}")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Summarise interfaces per site", "Hard")
explain("Goal:  Build a dict mapping each site to a summary")
explain("       dict with four keys.")
blank()
explain("Rules:")
explain("  • Key = site name.")
explain("  • Value = dict with exactly these four keys:")
explain("      'device_count'     — total devices in that site")
explain("      'total_interfaces' — total interfaces across all devices")
explain("      'up_count'         — interfaces with state 'up'")
explain("      'down_count'       — interfaces with state 'down'")
blank()
explain("Variable name:  site_summary")
blank()
header(">>> print(site_summary['NYC'])")
header("{'device_count': 2, 'total_interfaces': 5, 'up_count': 4, 'down_count': 1}")
blank()
header(">>> print(site_summary['LON'])")
header("{'device_count': 2, 'total_interfaces': 4, 'up_count': 3, 'down_count': 1}")
blank()
header(">>> print(site_summary['SIN'])")
header("{'device_count': 1, 'total_interfaces': 3, 'up_count': 3, 'down_count': 0}")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Build a VLAN report", "Hard")
explain("Goal:  Build a list called 'vlan_report' — one dict")
explain("       per unique VLAN across all sites and devices.")
blank()
explain("Rules:")
explain("  • Each dict must have exactly four keys:")
explain("      'vlan'            — the VLAN number")
explain("      'sites'           — sorted list of sites where it appears")
explain("      'device_count'    — number of devices that have it")
explain("      'interface_count' — number of interfaces using it")
explain("  • Sort the list by vlan number ascending.")
blank()
explain("Variable name:  vlan_report")
blank()
header(">>> for r in vlan_report: print(r)")
header("{'vlan': 10, 'sites': ['LON','NYC','SIN'], 'device_count': 4, 'interface_count': 4}")
header("{'vlan': 20, 'sites': ['LON','NYC','SIN'], 'device_count': 3, 'interface_count': 3}")
header("{'vlan': 30, 'sites': ['LON','NYC'],       'device_count': 2, 'interface_count': 2}")
header("{'vlan': 40, 'sites': ['NYC'],             'device_count': 1, 'interface_count': 1}")
header("{'vlan': 50, 'sites': ['LON','SIN'],       'device_count': 2, 'interface_count': 2}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: nested_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task  1 — two nested loops: site → devices")
explain("  Task  2 — {site: len(cfg['devices']) for site, cfg in NETWORK.items()}")
explain("  Task  3 — three nested loops: site → device → interfaces")
explain("  Task  4 — {d['hostname']: site for site, cfg in NETWORK.items() for d in cfg['devices']}")
explain("  Task  5 — 3-level comprehension with if iface['state'] == 'down'")
explain("  Task  6 — setdefault(vlan, set()).add(hostname), then sort each value")
explain("  Task  7 — {d['hostname']: len(d['interfaces']) for all devices}")
explain("  Task  8 — {site: sorted(set(vlan for d ... for i ...)) for site, cfg ...}")
explain("  Task  9 — all(i['state'] == 'up' for i in d['interfaces'])")
explain("  Task 10 — setdefault(hostname, {platform, site, interfaces:[]}) then .append()")
explain("  Task 11 — one dict per site with four sum() expressions")
explain("  Task 12 — collect unique VLANs first, then build one dict per VLAN")

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
print(f"{BOLD}{CYAN}    nested_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 nested_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()