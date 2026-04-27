# lists_challenges.py
# Python Lists — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: lists_solution.py
# 3. Run lists_grading.py to check your answers

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
INVENTORY = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30],      "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10, 20],           "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30, 40, 50],       "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30, 40],  "ip": "10.3.0.1"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [20, 30],           "ip": "10.4.0.1"},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 40, 50],       "ip": "10.5.0.1"},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down", "vlans": [10, 20, 30],       "ip": "10.6.0.1"},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [20, 30, 40, 50],  "ip": "10.7.0.1"},
]

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON LISTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same device INVENTORY list.")
explain("Read each task, write your solution in the file below,")
explain("then run lists_grading.py to check it.")
blank()
explain("File to create:  lists_solution.py")
blank()
explain("IMPORTANT: Copy the INVENTORY list shown on the next")
explain("screen into the TOP of your solution file.")
explain("Your solution will not work without it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW INVENTORY
# ═════════════════════════════════════════════════════════════════════════════
section("The INVENTORY You Will Work With")
explain("Copy this entire block into the TOP of your solution file.")
explain("It is printed with NO indentation so you can copy it directly.")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
explain("Your solution file should start like this:")
blank()
copyable("# lists_solution.py")
copyable("")
copyable("INVENTORY = [")
copyable("    {'hostname': 'nyc-rtr-01', ...},")
copyable("    ...")
copyable("]")
copyable("")
copyable("# your answers below — one variable per task")
copyable("all_hostnames = [...]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Extract all hostnames", "Easy")
explain("Goal:  Build a list of the hostname of every device.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  all_hostnames")
blank()
header(">>> print(all_hostnames)")
header("['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02',")
header(" 'tok-sw-01', 'syd-rtr-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Filter devices that are UP", "Easy")
explain("Goal:  Build a list of hostnames for devices whose")
explain("       status is 'up' only.")
blank()
explain("Rules:")
explain("  • Skip any device whose status is 'down'.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  up_hostnames")
blank()
header(">>> print(up_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Count devices that are DOWN", "Easy")
explain("Goal:  Count how many devices have status 'down'.")
blank()
explain("Rules:")
explain("  • Store the result as a single integer (not a list).")
blank()
explain("Variable name:  down_count")
blank()
header(">>> print(down_count)")
header("3")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Extract platforms in UPPERCASE", "Easy")
explain("Goal:  Build a list of the platform of every device,")
explain("       converted to UPPERCASE.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Keep the same order as INVENTORY.")
explain("  • Each platform string must be fully uppercase.")
blank()
explain("Variable name:  platforms")
blank()
header(">>> print(platforms)")
header("['IOS-XE', 'NX-OS', 'ASA', 'IOS-XE', 'NX-OS', 'IOS-XE', 'ASA', 'IOS-XE']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Flatten all VLANs into one list", "Medium")
explain("Goal:  Build a single flat list containing every VLAN ID")
explain("       from every device.")
blank()
explain("Rules:")
explain("  • Each device has a 'vlans' key with a list of VLAN IDs.")
explain("  • Outer loop must follow INVENTORY order.")
explain("  • Inner loop must follow each device's vlan list order.")
explain("  • Do NOT remove duplicates — keep every occurrence.")
blank()
explain("Variable name:  all_vlans")
blank()
header(">>> print(all_vlans)")
header("[10, 20, 30, 10, 20, 30, 40, 50, 10, 20, 30, 40, 20, 30,")
header(" 10, 40, 50, 10, 20, 30, 20, 30, 40, 50]")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "List unique VLANs in ascending order", "Medium")
explain("Goal:  Build a sorted list of unique VLAN IDs that")
explain("       appear across the entire inventory.")
blank()
explain("Rules:")
explain("  • Each VLAN ID must appear exactly once.")
explain("  • Sort ascending (lowest number first).")
explain("  • You may use all_vlans from Task 5 as a starting point.")
blank()
explain("Variable name:  unique_vlans")
blank()
header(">>> print(unique_vlans)")
header("[10, 20, 30, 40, 50]")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Find devices carrying VLAN 30", "Medium")
explain("Goal:  Build a list of hostnames for every device")
explain("       that has VLAN 30 in its vlan list.")
blank()
explain("Rules:")
explain("  • Check each device's 'vlans' list for the value 30.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  vlan_30_devices")
blank()
header(">>> print(vlan_30_devices)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Summarise devices with more than 2 VLANs", "Medium")
explain("Goal:  Build a list of dicts — one dict per device that")
explain("       has MORE THAN 2 VLANs — sorted by vlan_count")
explain("       descending (highest count first).")
blank()
explain("Rules:")
explain("  • Only include devices where len(vlans) > 2.")
explain("  • Each dict must have exactly two keys:")
explain("      'hostname'   — the device hostname")
explain("      'vlan_count' — the number of VLANs on that device")
explain("  • Sort by vlan_count descending.")
blank()
explain("Variable name:  vlan_summary")
blank()
header(">>> print(vlan_summary)")
header("[{'hostname': 'mum-rtr-01', 'vlan_count': 4},")
header(" {'hostname': 'ams-rtr-02', 'vlan_count': 4},")
header(" {'hostname': 'sin-fw-01',  'vlan_count': 3},")
header(" {'hostname': 'nyc-rtr-01', 'vlan_count': 3},")
header(" {'hostname': 'syd-rtr-01', 'vlan_count': 3},")
header(" {'hostname': 'dub-fw-01',  'vlan_count': 3}]")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Generate IOS-XE config blocks", "Hard")
explain("Goal:  Build a list of multi-line config strings — one")
explain("       string per device that is BOTH 'up' AND 'IOS-XE'.")
blank()
explain("Rules:")
explain("  • Skip any device that is 'down' or not 'IOS-XE'.")
explain(r"  • Each config string must use \n to separate these three lines:")
blank()
header("  'hostname <hostname>\\n ntp server 10.0.0.100\\n ip domain-name corp.net'")
blank()
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  config_blocks")
blank()
header(">>> for block in config_blocks: print(block)")
header("hostname nyc-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname ams-rtr-02")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname syd-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname mum-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Build IP to hostname pairs sorted by hostname", "Hard")
explain("Goal:  Build a list of strings in the format")
explain("       'ip --> hostname' for ALL 8 devices,")
explain("       sorted alphabetically by hostname.")
blank()
explain("Rules:")
explain("  • Include every device regardless of status or platform.")
explain("  • Format each string exactly as:  'x.x.x.x --> hostname'")
explain("  • Sort the final list by the hostname part (A to Z).")
blank()
explain("Variable name:  ip_hostname_pairs")
blank()
header(">>> print(ip_hostname_pairs)")
header("['10.3.0.1 --> ams-rtr-02', '10.6.0.1 --> dub-fw-01',")
header(" '10.1.0.1 --> lon-sw-01',  '10.7.0.1 --> mum-rtr-01',")
header(" '10.0.0.1 --> nyc-rtr-01', '10.2.0.1 --> sin-fw-01',")
header(" '10.5.0.1 --> syd-rtr-01', '10.4.0.1 --> tok-sw-01']")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Number every device in the inventory", "Hard")
explain("Goal:  Build a list of strings that label each device")
explain("       with a sequential number.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Numbering starts at 1 and follows INVENTORY order.")
explain("  • Format each string exactly as:")
explain("      'N. hostname (platform) \u2014 status'")
explain("    where N is the device's position number.")
blank()
explain("Variable name:  numbered_inventory")
blank()
header(">>> print(numbered_inventory)")
header("['1. nyc-rtr-01 (IOS-XE) \u2014 up',")
header(" '2. lon-sw-01 (NX-OS) \u2014 down',")
header(" '3. sin-fw-01 (ASA) \u2014 up',")
header(" '4. ams-rtr-02 (IOS-XE) \u2014 up',")
header(" '5. tok-sw-01 (NX-OS) \u2014 down',")
header(" '6. syd-rtr-01 (IOS-XE) \u2014 up',")
header(" '7. dub-fw-01 (ASA) \u2014 down',")
header(" '8. mum-rtr-01 (IOS-XE) \u2014 up']")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Group devices by platform", "Hard")
explain("Goal:  Build a list of dicts — one dict per unique platform")
explain("       — summarising the total device count and how many")
explain("       of those devices are currently 'up'.")
blank()
explain("Rules:")
explain("  • One dict per unique platform (3 platforms total).")
explain("  • Sort the list alphabetically by platform name.")
explain("  • Each dict must have exactly three keys:")
explain("      'platform' — the platform name (e.g. 'IOS-XE')")
explain("      'count'    — total devices with that platform")
explain("      'up_count' — devices with that platform AND status 'up'")
blank()
explain("Variable name:  platform_groups")
blank()
header(">>> print(platform_groups)")
header("[{'platform': 'ASA',    'count': 2, 'up_count': 1},")
header(" {'platform': 'IOS-XE', 'count': 4, 'up_count': 4},")
header(" {'platform': 'NX-OS',  'count': 2, 'up_count': 0}]")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: lists_solution.py")
explain("Remember to paste INVENTORY at the top of your file.")
blank()
explain("Tips by task:")
explain("  Task  1 — list comprehension: [d['hostname'] for d in INVENTORY]")
explain("  Task  2 — add an if clause:   [... if d['status'] == 'up']")
explain("  Task  3 — sum() with a generator expression")
explain("  Task  4 — call .upper() inside the comprehension")
explain("  Task  5 — nested comprehension: [v for d in INVENTORY for v in d['vlans']]")
explain("  Task  6 — sorted(set(all_vlans))")
explain("  Task  7 — use 'in' operator: if 30 in d['vlans']")
explain("  Task  8 — build dicts in comprehension, filter > 2, sort with key=lambda")
explain("  Task  9 — double filter: if d['status'] == 'up' and d['platform'] == 'IOS-XE'")
explain("  Task 10 — sorted(..., key=lambda s: s.split(' --> ')[1])")
explain("  Task 11 — enumerate(INVENTORY, start=1)")
explain("  Task 12 — get unique platforms with set(), sort, build one dict per platform")

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
print(f"{BOLD}{CYAN}    lists_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 lists_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()