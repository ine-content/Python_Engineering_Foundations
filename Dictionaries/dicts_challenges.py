# dicts_challenges.py
# Python Dicts — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: dicts_solution.py
# 3. Run dicts_grading.py to check your answers

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

def copyable(text):
    print(f"{CYAN}{text}{RESET}")

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
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
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
print(f"{BOLD}         PYTHON DICTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same INVENTORY and GLOBAL_NTP.")
explain("Read each task, write your solution in dicts_solution.py,")
explain("then run dicts_grading.py to check it.")
blank()
explain("The INVENTORY and GLOBAL_NTP are already pasted at the")
explain("top of dicts_solution.py — just write your answers below them.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Map hostname to IP", "Easy")
explain("Goal:  Build a dict mapping each hostname to its IP address.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Key = hostname, Value = ip.")
blank()
explain("Variable name:  hostname_to_ip")
blank()
header(">>> print(hostname_to_ip)")
header("{'nyc-rtr-01': '10.0.0.1', 'lon-sw-01': '10.1.0.1',")
header(" 'sin-fw-01': '10.2.0.1',  'ams-rtr-02': '10.3.0.1',")
header(" 'tok-sw-01': '10.4.0.1',  'syd-rtr-01': '10.5.0.1',")
header(" 'dub-fw-01': '10.6.0.1',  'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Map hostname to platform", "Easy")
explain("Goal:  Build a dict mapping each hostname to its platform.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Key = hostname, Value = platform.")
blank()
explain("Variable name:  hostname_to_platform")
blank()
header(">>> print(hostname_to_platform)")
header("{'nyc-rtr-01': 'IOS-XE', 'lon-sw-01': 'NX-OS',")
header(" 'sin-fw-01': 'ASA',     'ams-rtr-02': 'IOS-XE',")
header(" 'tok-sw-01': 'NX-OS',   'syd-rtr-01': 'IOS-XE',")
header(" 'dub-fw-01': 'ASA',     'mum-rtr-01': 'IOS-XE'}")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Count devices by status", "Easy")
explain("Goal:  Build a dict with two keys — 'up' and 'down' —")
explain("       each holding the count of devices with that status.")
blank()
explain("Rules:")
explain("  • Dict must have exactly two keys: 'up' and 'down'.")
explain("  • Values are integers.")
blank()
explain("Variable name:  status_count")
blank()
header(">>> print(status_count)")
header("{'up': 5, 'down': 3}")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Map hostname to IP for UP devices only", "Easy")
explain("Goal:  Build a dict mapping hostname to IP,")
explain("       but only for devices whose status is 'up'.")
blank()
explain("Rules:")
explain("  • Skip any device with status 'down'.")
explain("  • Key = hostname, Value = ip.")
blank()
explain("Variable name:  up_devices")
blank()
header(">>> print(up_devices)")
header("{'nyc-rtr-01': '10.0.0.1', 'sin-fw-01': '10.2.0.1',")
header(" 'ams-rtr-02': '10.3.0.1', 'syd-rtr-01': '10.5.0.1',")
header(" 'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Group hostnames by platform", "Medium")
explain("Goal:  Build a dict mapping each platform to a sorted")
explain("       list of hostnames that use it.")
blank()
explain("Rules:")
explain("  • Key = platform, Value = sorted list of hostnames.")
explain("  • Sort each list alphabetically.")
blank()
explain("Variable name:  platform_groups")
blank()
header(">>> print(platform_groups)")
header("{'IOS-XE': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01'],")
header(" 'NX-OS':  ['lon-sw-01', 'tok-sw-01'],")
header(" 'ASA':    ['dub-fw-01', 'sin-fw-01']}")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Map hostname to its config dict", "Medium")
explain("Goal:  Build a dict mapping each hostname to its")
explain("       nested 'config' dict.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = the config dict.")
explain("  • Each config dict has keys: ntp, dns, domain.")
blank()
explain("Variable name:  hostname_to_config")
blank()
header(">>> print(hostname_to_config['nyc-rtr-01'])")
header("{'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()
header(">>> print(hostname_to_config['lon-sw-01'])")
header("{'ntp': '10.1.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Map hostname to VLAN count", "Medium")
explain("Goal:  Build a dict mapping each hostname to the")
explain("       number of VLANs it has.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = integer count of vlans.")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  vlan_count_map")
blank()
header(">>> print(vlan_count_map)")
header("{'nyc-rtr-01': 3, 'lon-sw-01': 2, 'sin-fw-01': 3,")
header(" 'ams-rtr-02': 4, 'tok-sw-01': 2, 'syd-rtr-01': 3,")
header(" 'dub-fw-01': 3,  'mum-rtr-01': 4}")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Group hostnames by NTP server", "Medium")
explain("Goal:  Build a dict mapping each unique NTP server")
explain("       to a sorted list of hostnames using it.")
blank()
explain("Rules:")
explain("  • Each device's NTP is at d['config']['ntp'].")
explain("  • Key = NTP server IP, Value = sorted list of hostnames.")
blank()
explain("Variable name:  ntp_to_hostnames")
blank()
header(">>> print(ntp_to_hostnames)")
header("{'10.0.0.100': ['ams-rtr-02', 'dub-fw-01', 'nyc-rtr-01', 'sin-fw-01', 'syd-rtr-01'],")
header(" '10.1.0.100': ['lon-sw-01'],")
header(" '10.4.0.100': ['tok-sw-01'],")
header(" '10.7.0.100': ['mum-rtr-01']}")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Merge BASE config with each device config", "Hard")
explain("Goal:  Build a dict mapping each hostname to a merged")
explain("       config — BASE defaults overridden by the device's")
explain("       own config values.")
blank()
explain("Rules:")
explain("  • Start with this BASE dict for every device:")
explain("      BASE = {'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public'}")
explain("  • Merge each device's config on top — device values win.")
explain("  • Key = hostname, Value = merged config dict.")
blank()
explain("Variable name:  merged_configs")
blank()
header(">>> print(merged_configs['nyc-rtr-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.0.0.100'}")
blank()
header(">>> print(merged_configs['lon-sw-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.1.0.100'}")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Invert IP to hostname", "Hard")
explain("Goal:  Build a dict mapping each IP address to its hostname.")
blank()
explain("Rules:")
explain("  • This is the reverse of Task 1.")
explain("  • Key = ip, Value = hostname.")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  inverted_ip")
blank()
header(">>> print(inverted_ip)")
header("{'10.0.0.1': 'nyc-rtr-01', '10.1.0.1': 'lon-sw-01',")
header(" '10.2.0.1': 'sin-fw-01',  '10.3.0.1': 'ams-rtr-02',")
header(" '10.4.0.1': 'tok-sw-01',  '10.5.0.1': 'syd-rtr-01',")
header(" '10.6.0.1': 'dub-fw-01',  '10.7.0.1': 'mum-rtr-01'}")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Count devices per platform", "Hard")
explain("Goal:  Build a dict mapping each platform to the number")
explain("       of devices using it.")
blank()
explain("Rules:")
explain("  • Key = platform, Value = count of devices (int).")
explain("  • Use the .get(key, 0) + 1 counting pattern.")
blank()
explain("Variable name:  platform_count")
blank()
header(">>> print(platform_count)")
header("{'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Find devices with non-standard NTP", "Hard")
explain("Goal:  Build a dict mapping hostname to NTP server,")
explain("       but ONLY for devices whose NTP differs from GLOBAL_NTP.")
blank()
explain("Rules:")
explain(f"  • GLOBAL_NTP = '{GLOBAL_NTP}'")
explain("  • Skip any device whose NTP matches GLOBAL_NTP.")
explain("  • Key = hostname, Value = that device's NTP server IP.")
blank()
explain("Variable name:  ntp_diff")
blank()
header(">>> print(ntp_diff)")
header("{'lon-sw-01':  '10.1.0.100',")
header(" 'tok-sw-01':  '10.4.0.100',")
header(" 'mum-rtr-01': '10.7.0.100'}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: dicts_solution.py")
explain("Remember to paste INVENTORY and GLOBAL_NTP at the top.")
blank()
explain("Tips by task:")
explain("  Task  1 — dict comprehension: {d['hostname']: d['ip'] for d in INVENTORY}")
explain("  Task  2 — same pattern, value is d['platform']")
explain("  Task  3 — sum() with generator expression for each status")
explain("  Task  4 — add if clause: if d['status'] == 'up'")
explain("  Task  5 — .setdefault(platform, []) then .append() and .sort()")
explain("  Task  6 — value is d['config'] directly")
explain("  Task  7 — value is len(d['vlans'])")
explain("  Task  8 — key is d['config']['ntp'], same grouping pattern as Task 5")
explain("  Task  9 — use {**BASE, **d['config']} to merge")
explain("  Task 10 — swap key/value: {d['ip']: d['hostname'] ...}")
explain("  Task 11 — use .get(platform, 0) + 1 counting pattern from Ch 9.1")
explain("  Task 12 — filter: if d['config']['ntp'] != GLOBAL_NTP")

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
print(f"{BOLD}{CYAN}    dicts_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 dicts_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()