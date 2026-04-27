# loops_challenges.py
# Python Loops — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: loops_solution.py
# 3. Run loops_grading.py to check your answers

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
INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
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
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "down"},
            {"name": "Gi0/1", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
            {"name": "Gi0/2", "vlan": 50, "state": "down"},
        ],
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
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
print(f"{BOLD}         LOOPS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same INVENTORY list.")
explain("Read each task, write your solution in loops_solution.py,")
explain("then run loops_grading.py to check it.")
blank()
explain("The INVENTORY is already pasted at the top of")
explain("loops_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Count devices by platform", "Easy")
explain("Goal:  Using a for loop and a counter, build a dict called")
explain("       'platform_counts' mapping each platform to how")
explain("       many devices use it.")
blank()
explain("Rules:")
explain("  • Use a for loop — not a comprehension.")
explain("  • Use .get() to safely increment the count.")
blank()
explain("Variable name:  platform_counts")
blank()
header(">>> print(platform_counts)")
header("{'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Number devices with enumerate()", "Easy")
explain("Goal:  Using enumerate(), build a list called 'numbered'")
explain("       — one string per device, numbered from 1.")
blank()
explain("Rules:")
explain("  • Format: 'N. hostname (platform)'")
explain("  • Numbering starts at 1.")
blank()
explain("Variable name:  numbered")
blank()
header(">>> print(numbered)")
header("['1. nyc-rtr-01 (IOS-XE)', '2. lon-sw-01 (NX-OS)',")
header(" '3. sin-fw-01 (ASA)',     '4. ams-rtr-02 (IOS-XE)',")
header(" '5. tok-sw-01 (NX-OS)',   '6. syd-rtr-01 (IOS-XE)',")
header(" '7. dub-fw-01 (ASA)',     '8. mum-rtr-01 (IOS-XE)']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Collect all unique VLANs", "Easy")
explain("Goal:  Using a for loop, collect all unique VLAN IDs")
explain("       across all devices into a sorted list called 'all_vlans'.")
blank()
explain("Rules:")
explain("  • Each device has a 'vlans' key with a list of VLAN IDs.")
explain("  • Use a set to deduplicate, then sorted().")
blank()
explain("Variable name:  all_vlans")
blank()
header(">>> print(all_vlans)")
header("[10, 20, 30, 40, 50]")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Pair devices with regions using zip()", "Easy")
explain("Goal:  Using zip(), pair each device with a region and")
explain("       build a list called 'device_regions' — one string per pair.")
blank()
explain("Rules:")
explain("  • Format: 'hostname → region'")
explain("  • Use this regions list in your solution file:")
blank()
header("regions = ['us-east', 'eu-west', 'ap-se', 'eu-central',")
header("           'ap-ne',   'au-east', 'eu-west', 'ap-south']")
blank()
explain("Variable name:  device_regions")
blank()
header(">>> print(device_regions)")
header("['nyc-rtr-01 → us-east', 'lon-sw-01 → eu-west',")
header(" 'sin-fw-01 → ap-se',    'ams-rtr-02 → eu-central',")
header(" 'tok-sw-01 → ap-ne',    'syd-rtr-01 → au-east',")
header(" 'dub-fw-01 → eu-west',  'mum-rtr-01 → ap-south']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Report all DOWN interfaces", "Medium")
explain("Goal:  Using nested loops, build a list called 'down_report'")
explain("       — one string per interface that is 'down' across")
explain("       ALL devices.")
blank()
explain("Rules:")
explain("  • Format: 'hostname | iface_name | vlan'")
explain("  • Outer loop follows INVENTORY order.")
explain("  • Inner loop follows each device's interfaces order.")
blank()
explain("Variable name:  down_report")
blank()
header(">>> print(down_report)")
header("['nyc-rtr-01 | Gi0/2 | 30',")
header(" 'lon-sw-01  | Gi0/1 | 20',")
header(" 'tok-sw-01  | Gi0/0 | 20',")
header(" 'tok-sw-01  | Gi0/1 | 30',")
header(" 'syd-rtr-01 | Gi0/2 | 50',")
header(" 'dub-fw-01  | Gi0/1 | 20']")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Find first NX-OS device that is UP", "Medium")
explain("Goal:  Using a for loop with break and for...else,")
explain("       find the FIRST device in INVENTORY whose platform")
explain("       is 'NX-OS' and status is 'up'.")
blank()
explain("Rules:")
explain("  • Store the hostname in 'first_nxos_up'.")
explain("  • If no such device exists, store None.")
blank()
explain("Variable name:  first_nxos_up")
blank()
header(">>> print(first_nxos_up)")
header("None")
blank()
explain("(All NX-OS devices in INVENTORY are currently down.)")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Summarise UP interfaces with VLAN > 20", "Medium")
explain("Goal:  Using nested loops with continue, build a list called")
explain("       'interface_summary' — one dict per interface that is")
explain("       'up' AND whose vlan is greater than 20.")
blank()
explain("Rules:")
explain("  • Skip all other interfaces using continue.")
explain("  • Each dict: {'hostname': ..., 'iface': ..., 'vlan': ...}")
blank()
explain("Variable name:  interface_summary")
blank()
header(">>> print(interface_summary)")
header("[{'hostname': 'nyc-rtr-01', 'iface': 'Gi0/2', 'vlan': 30},")
header(" {'hostname': 'sin-fw-01',  'iface': 'Gi0/0', 'vlan': 30},")
header(" {'hostname': 'sin-fw-01',  'iface': 'Gi0/1', 'vlan': 40},")
header(" {'hostname': 'ams-rtr-02', 'iface': 'Gi0/2', 'vlan': 30},")
header(" {'hostname': 'ams-rtr-02', 'iface': 'Gi0/3', 'vlan': 40},")
header(" {'hostname': 'syd-rtr-01', 'iface': 'Gi0/1', 'vlan': 40},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/1', 'vlan': 30},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/2', 'vlan': 40},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/3', 'vlan': 50}]")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Find device with most interfaces", "Medium")
explain("Goal:  Using a for loop and a running max tracker,")
explain("       find the device with the MOST interfaces.")
blank()
explain("Rules:")
explain("  • Store the hostname in 'most_interfaces_host'.")
explain("  • Store the count in 'most_interfaces_count'.")
blank()
explain("Variable names:  most_interfaces_host  /  most_interfaces_count")
blank()
header(">>> print(most_interfaces_host)")
header("'ams-rtr-02'")
blank()
header(">>> print(most_interfaces_count)")
header("4")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Chunk INVENTORY into batches of 3", "Hard")
explain("Goal:  Using a for loop with range(), chunk INVENTORY")
explain("       hostnames into batches of 3.")
blank()
explain("Rules:")
explain("  • Store the result in 'batches'.")
explain("  • Each item in 'batches' is a list of hostnames.")
explain("  • The last batch may have fewer than 3 items.")
blank()
explain("Variable name:  batches")
blank()
header(">>> print(batches)")
header("[['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01'],")
header(" ['ams-rtr-02', 'tok-sw-01', 'syd-rtr-01'],")
header(" ['dub-fw-01',  'mum-rtr-01']]")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Deduplicate a VLAN feed preserving order", "Hard")
explain("Goal:  Using a for loop with a 'seen' set, deduplicate")
explain("       the following list while PRESERVING the original order.")
blank()
explain("Rules:")
explain("  • Use this vlan_feed list in your solution file:")
blank()
header("vlan_feed = [10, 30, 10, 20, 50, 30, 40, 20, 10, 50]")
blank()
explain("  • Store the result in 'unique_vlans_ordered'.")
blank()
explain("Variable name:  unique_vlans_ordered")
blank()
header(">>> print(unique_vlans_ordered)")
header("[10, 30, 20, 50, 40]")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Simulate a connection retry with while loop", "Hard")
explain("Goal:  Using a while loop, simulate a retry mechanism")
explain("       that processes a queue of devices.")
blank()
explain("Rules:")
explain("  • Use this queue in your solution file:")
blank()
header("queue = ['lon-sw-01', 'nyc-rtr-01', 'sin-fw-01', 'nyc-sw-01']")
blank()
explain("  • Each iteration pops the first device off the queue.")
explain("  • If the device name starts with 'nyc' → success.")
explain("  • Otherwise → failure.")
explain("  • Stop when the queue is empty.")
explain("  • Store results in 'failed_devices' and 'success_devices'.")
blank()
explain("Variable names:  failed_devices  /  success_devices")
blank()
header(">>> print(failed_devices)")
header("['lon-sw-01', 'sin-fw-01']")
blank()
header(">>> print(success_devices)")
header("['nyc-rtr-01', 'nyc-sw-01']")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Build a VLAN gap report with sliding window", "Hard")
explain("Goal:  Using a sliding window (consecutive pairs), build")
explain("       a list called 'vlan_gaps' — one dict per adjacent")
explain("       pair of VLANs.")
blank()
explain("Rules:")
explain("  • Use this sorted_vlans list in your solution file:")
blank()
header("sorted_vlans = [10, 20, 30, 40, 50, 100, 200]")
blank()
explain("  • Each dict has exactly three keys:")
explain("      'from_vlan' — first VLAN in the pair")
explain("      'to_vlan'   — second VLAN in the pair")
explain("      'gap'       — difference between them")
blank()
explain("Variable name:  vlan_gaps")
blank()
header(">>> for g in vlan_gaps: print(g)")
header("{'from_vlan': 10,  'to_vlan': 20,  'gap': 10}")
header("{'from_vlan': 20,  'to_vlan': 30,  'gap': 10}")
header("{'from_vlan': 30,  'to_vlan': 40,  'gap': 10}")
header("{'from_vlan': 40,  'to_vlan': 50,  'gap': 10}")
header("{'from_vlan': 50,  'to_vlan': 100, 'gap': 50}")
header("{'from_vlan': 100, 'to_vlan': 200, 'gap': 100}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: loops_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task  1 — counts[p] = counts.get(p, 0) + 1")
explain("  Task  2 — enumerate(INVENTORY, start=1)")
explain("  Task  3 — build a set(), nested loop over d['vlans'], then sorted()")
explain("  Task  4 — zip(INVENTORY, regions)")
explain("  Task  5 — nested for: for d in INVENTORY, for iface in d['interfaces']")
explain("  Task  6 — for loop + if + break. Initialise first_nxos_up = None before loop")
explain("  Task  7 — nested loops, continue if state != 'up' or vlan <= 20")
explain("  Task  8 — track max_count and max_host in loop with if len(...) > max_count")
explain("  Task  9 — range(0, len(INVENTORY), 3), slice hostnames[i:i+3]")
explain("  Task 10 — seen=set(), if v not in seen: append(v) and seen.add(v)")
explain("  Task 11 — while queue: device = queue.pop(0), then if/else")
explain("  Task 12 — range(len(sorted_vlans)-1), access [i] and [i+1]")

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
print(f"{BOLD}{CYAN}    loops_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 loops_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()