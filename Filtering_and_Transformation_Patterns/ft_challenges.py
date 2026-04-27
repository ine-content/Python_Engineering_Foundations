# filtering_transformation_challenges.py
# Filtering and Transformation Patterns — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: ft_solution.py
# 3. Run ft_grading.py to check your answers

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
GLOBAL_NTP     = "10.0.0.100"
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "up"},
            {"name": "Gi0/3", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "down"},
            {"name": "Gi0/1", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
            {"name": "Gi0/2", "vlan": 50, "state": "down"},
        ],
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "up"},
            {"name": "Gi0/1", "vlan": 30, "state": "up"},
            {"name": "Gi0/2", "vlan": 40, "state": "up"},
            {"name": "Gi0/3", "vlan": 50, "state": "up"},
        ],
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
print(f"{BOLD}         FILTERING & TRANSFORMATION — CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use INVENTORY, GLOBAL_NTP, and RESERVED_VLANS.")
explain("Read each task, write your solution in ft_solution.py,")
explain("then run ft_grading.py to check it.")
blank()
explain("The data is already pasted at the top of")
explain("ft_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Extract IPs of UP devices", "Easy")
explain("Goal:  Build a list called 'up_ips' containing the IP")
explain("       address of every device whose status is 'up'.")
blank()
explain("Rules:")
explain("  • Include only devices with status 'up'.")
explain("  • Keep INVENTORY order.")
blank()
explain("Variable name:  up_ips")
blank()
header(">>> print(up_ips)")
header("['10.0.0.1', '10.2.0.1', '10.3.0.1', '10.5.0.1', '10.7.0.1']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Build enriched device list", "Easy")
explain("Goal:  Build a list called 'enriched' — one dict per device")
explain("       with a subset of fields plus a computed vlan_count.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Each dict must have exactly four keys:")
explain("      'hostname'   — the hostname")
explain("      'platform'   — the platform")
explain("      'vlan_count' — len(d['vlans'])")
explain("      'status'     — the status")
blank()
explain("Variable name:  enriched")
blank()
header(">>> print(enriched[0])")
header("{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'vlan_count': 3, 'status': 'up'}")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Map hostname to NTP server", "Easy")
explain("Goal:  Build a dict called 'hostname_to_ntp' mapping")
explain("       each hostname to its NTP server.")
blank()
explain("Rules:")
explain("  • NTP is at d['config']['ntp'].")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  hostname_to_ntp")
blank()
header(">>> print(hostname_to_ntp)")
header("{'nyc-rtr-01': '10.0.0.100', 'lon-sw-01': '10.1.0.100',")
header(" 'sin-fw-01':  '10.0.0.100', 'ams-rtr-02': '10.0.0.100',")
header(" 'tok-sw-01':  '10.4.0.100', 'syd-rtr-01': '10.0.0.100',")
header(" 'dub-fw-01':  '10.0.0.100', 'mum-rtr-01': '10.7.0.100'}")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Find devices with custom NTP", "Easy")
explain("Goal:  Build a list called 'custom_ntp_hosts' containing")
explain("       the hostname of every device whose NTP server")
explain("       differs from GLOBAL_NTP.")
blank()
explain("Rules:")
explain("  • GLOBAL_NTP = '10.0.0.100'")
explain("  • Keep INVENTORY order.")
blank()
explain("Variable name:  custom_ntp_hosts")
blank()
header(">>> print(custom_ntp_hosts)")
header("['lon-sw-01', 'tok-sw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Partition devices into push-ready and skip", "Medium")
explain("Goal:  Partition INVENTORY into two lists of hostnames:")
explain("       'push_ready' and 'skip_devices'.")
blank()
explain("Rules:")
explain("  • push_ready  — devices that are 'up' AND platform is 'IOS-XE' or 'NX-OS'")
explain("  • skip_devices — everything else")
blank()
explain("Variable names:  push_ready  /  skip_devices")
blank()
header(">>> print(push_ready)")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(skip_devices)")
header("['lon-sw-01', 'sin-fw-01', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Group hostnames by platform", "Medium")
explain("Goal:  Build a dict called 'platform_groups' mapping each")
explain("       platform to a sorted list of hostnames using it.")
blank()
explain("Rules:")
explain("  • Key = platform, Value = sorted list of hostnames.")
blank()
explain("Variable name:  platform_groups")
blank()
header(">>> print(platform_groups)")
header("{'ASA':    ['dub-fw-01', 'sin-fw-01'],")
header(" 'IOS-XE': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01'],")
header(" 'NX-OS':  ['lon-sw-01', 'tok-sw-01']}")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Compute platform statistics", "Medium")
explain("Goal:  Build a dict called 'platform_stats' mapping each")
explain("       platform to a summary dict with three keys.")
blank()
explain("Rules:")
explain("  • Key = platform name.")
explain("  • Value = dict with exactly these three keys:")
explain("      'total'     — number of devices on that platform")
explain("      'up_count'  — number of those that are 'up'")
explain("      'avg_vlans' — average number of VLANs (as a float)")
blank()
explain("Variable name:  platform_stats")
blank()
header(">>> print(platform_stats['IOS-XE'])")
header("{'total': 4, 'up_count': 4, 'avg_vlans': 3.5}")
blank()
header(">>> print(platform_stats['NX-OS'])")
header("{'total': 2, 'up_count': 0, 'avg_vlans': 2.0}")
blank()
header(">>> print(platform_stats['ASA'])")
header("{'total': 2, 'up_count': 1, 'avg_vlans': 2.5}")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Build VLAN usage report", "Medium")
explain("Goal:  Build a list called 'vlan_usage' — one dict per")
explain("       unique VLAN across all devices, sorted by vlan ascending.")
blank()
explain("Rules:")
explain("  • Each dict must have exactly three keys:")
explain("      'vlan'         — the VLAN number")
explain("      'device_count' — number of devices that have it")
explain("      'hostnames'    — sorted list of those hostnames")
blank()
explain("Variable name:  vlan_usage")
blank()
header(">>> for v in vlan_usage: print(v)")
header("{'vlan': 10, 'device_count': 5, 'hostnames': ['ams-rtr-02','dub-fw-01','lon-sw-01','nyc-rtr-01','syd-rtr-01']}")
header("{'vlan': 20, 'device_count': 5, 'hostnames': ['ams-rtr-02','lon-sw-01','mum-rtr-01','nyc-rtr-01','tok-sw-01']}")
header("{'vlan': 30, 'device_count': 5, 'hostnames': ['ams-rtr-02','dub-fw-01','mum-rtr-01','nyc-rtr-01','sin-fw-01']}")
header("{'vlan': 40, 'device_count': 4, 'hostnames': ['ams-rtr-02','mum-rtr-01','sin-fw-01','syd-rtr-01']}")
header("{'vlan': 50, 'device_count': 3, 'hostnames': ['mum-rtr-01','sin-fw-01','syd-rtr-01']}")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Run a 4-step filtering pipeline", "Hard")
explain("Goal:  Build a list called 'pipeline_result' by running")
explain("       INVENTORY through four steps in sequence.")
blank()
explain("Rules (apply in order):")
explain("  Step 1 — Keep only devices that are 'up'")
explain("  Step 2 — Remove reserved VLANs from each device's vlan list")
explain("           RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
explain("  Step 3 — Keep only devices that still have at least one VLAN")
explain("           after reserved removal")
explain("  Step 4 — Transform each device to:")
explain("           {'hostname', 'platform', 'clean_vlans'}")
blank()
explain("Variable name:  pipeline_result")
blank()
header(">>> for r in pipeline_result: print(r)")
header("{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [10, 20, 30]}")
header("{'hostname': 'sin-fw-01',  'platform': 'ASA',    'clean_vlans': [30, 40, 50]}")
header("{'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'clean_vlans': [10, 20, 30, 40]}")
header("{'hostname': 'syd-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [10, 40, 50]}")
header("{'hostname': 'mum-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [20, 30, 40, 50]}")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Build a full device report with interface breakdown", "Hard")
explain("Goal:  Build a list called 'device_report' — one dict")
explain("       per device with a full interface breakdown.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Each dict must have exactly five keys:")
explain("      'hostname'        — the hostname")
explain("      'status'          — the status")
explain("      'up_interfaces'   — list of interface names that are 'up'")
explain("      'down_interfaces' — list of interface names that are 'down'")
explain("      'all_up'          — True if ALL interfaces are 'up', else False")
blank()
explain("Variable name:  device_report")
blank()
header(">>> print(device_report[0])")
header("{'hostname': 'nyc-rtr-01', 'status': 'up',")
header(" 'up_interfaces': ['Gi0/0', 'Gi0/1'],")
header(" 'down_interfaces': ['Gi0/2'],")
header(" 'all_up': False}")
blank()
header(">>> print(device_report[3])")
header("{'hostname': 'ams-rtr-02', 'status': 'up',")
header(" 'up_interfaces': ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3'],")
header(" 'down_interfaces': [],")
header(" 'all_up': True}")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Flatten UP interfaces across all devices", "Hard")
explain("Goal:  Build a list called 'interface_flat' — one dict per")
explain("       interface across ALL devices, flattened.")
blank()
explain("Rules:")
explain("  • Only include interfaces whose state is 'up'.")
explain("  • Each dict must have exactly four keys:")
explain("      'hostname' — the device hostname")
explain("      'iface'    — the interface name")
explain("      'vlan'     — the VLAN number")
explain("      'platform' — the device platform")
explain("  • Outer loop follows INVENTORY order.")
explain("  • Inner loop follows each device's interfaces order.")
blank()
explain("Variable name:  interface_flat")
blank()
header(">>> print(interface_flat[0])")
header("{'hostname': 'nyc-rtr-01', 'iface': 'Gi0/0', 'vlan': 10, 'platform': 'IOS-XE'}")
blank()
header(">>> print(len(interface_flat))")
header("15")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Map VLANs to platforms via UP interfaces only", "Hard")
explain("Goal:  Build a dict called 'vlan_platform_map' mapping each")
explain("       unique VLAN to a sorted list of unique platforms that")
explain("       have that VLAN on at least one UP interface.")
blank()
explain("Rules:")
explain("  • Only count interfaces whose state is 'up'.")
explain("  • Key = VLAN number, Value = sorted list of platform names.")
blank()
explain("Variable name:  vlan_platform_map")
blank()
header(">>> print(vlan_platform_map)")
header("{10: ['ASA', 'IOS-XE', 'NX-OS'],")
header(" 20: ['IOS-XE', 'NX-OS'],")
header(" 30: ['ASA', 'IOS-XE'],")
header(" 40: ['IOS-XE'],")
header(" 50: ['IOS-XE']}")
blank()
explain("Note: tok-sw-01 (NX-OS) has vlans 20 and 30 but both")
explain("interfaces are DOWN — so NX-OS should NOT appear for")
explain("vlans 20 or 30 in this output.")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: ft_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task  1 — [d['ip'] for d in INVENTORY if d['status'] == 'up']")
explain("  Task  2 — {'hostname': d['hostname'], 'platform': ..., 'vlan_count': len(d['vlans']), 'status': ...}")
explain("  Task  3 — {d['hostname']: d['config']['ntp'] for d in INVENTORY}")
explain("  Task  4 — filter where d['config']['ntp'] != GLOBAL_NTP")
explain("  Task  5 — two comprehensions with different conditions")
explain("  Task  6 — get unique platforms, then {p: sorted([...]) for p in platforms}")
explain("  Task  7 — filter per platform, compute total/up_count/avg_vlans")
explain("  Task  8 — collect unique vlans with set(), sort, build one dict per vlan")
explain("  Task  9 — 4 separate steps using list comprehensions")
explain("  Task 10 — [i['name'] for i in d['interfaces'] if i['state'] == 'up']")
explain("  Task 11 — nested comprehension: for d in INVENTORY for i in d['interfaces'] if i['state'] == 'up'")
explain("  Task 12 — collect (platform, vlan) pairs from UP interfaces, then group by vlan")

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
print(f"{BOLD}{CYAN}    ft_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 ft_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()