# file_io_challenges.py
# Python File I/O — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: file_io_solution.py
# 3. Run file_io_grading.py to check your answers

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

GLOBAL_NTP = "10.0.0.100"

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         FILE I/O — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("8 tasks — Easy and Medium — all in one challenge.")
explain("Each task involves reading and writing real files.")
explain("Read each task, write your solution in file_io_solution.py,")
explain("then run file_io_grading.py to check it.")
blank()
explain("HOW FILE GRADING WORKS:")
explain("  Your script runs in a temporary working directory.")
explain("  Use RELATIVE paths — just 'devices.txt', not a full path.")
explain("  The grader reads the files your script creates and")
explain("  checks their contents.")
blank()
explain("INVENTORY, GLOBAL_NTP, os, csv, and json are all")
explain("pre-injected — no need to import or redefine them.")
explain("(But you can import them again — no harm done.)")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Write hostnames to a text file", "Easy")
explain("Goal:  Write the hostname of every device in INVENTORY")
explain("       to a file called 'hostnames.txt', one per line.")
blank()
explain("Rules:")
explain("  • Use relative path: 'hostnames.txt'")
explain("  • One hostname per line, no extra blank lines.")
blank()
explain("Expected contents of hostnames.txt:")
blank()
header("nyc-rtr-01")
header("lon-sw-01")
header("sin-fw-01")
header("ams-rtr-02")
header("tok-sw-01")
header("syd-rtr-01")
header("dub-fw-01")
header("mum-rtr-01")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Read hostnames back from the text file", "Easy")
explain("Goal:  Read 'hostnames.txt' back and produce a list called")
explain("       'read_hostnames' containing each hostname as a string.")
blank()
explain("Rules:")
explain("  • Strip trailing newlines from each line.")
explain("  • Skip any blank lines.")
blank()
explain("Variable name:  read_hostnames")
blank()
header(">>> print(read_hostnames)")
header("['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02',")
header(" 'tok-sw-01',  'syd-rtr-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Parse a structured device list file", "Easy")
explain("Goal:  Read a pre-created file called 'device_list.txt'")
explain("       and produce a list called 'parsed_devices' — one")
explain("       dict per device line.")
blank()
explain("Rules:")
explain("  • The grader creates 'device_list.txt' for you with this content:")
blank()
header("# hostname        platform   ip")
header("nyc-rtr-01        IOS-XE     10.0.0.1")
header("lon-sw-01         NX-OS      10.1.0.1")
header("sin-fw-01         ASA        10.2.0.1")
blank()
explain("  • Skip lines that start with '#' or are blank.")
explain("  • Split each valid line on whitespace to get 3 fields.")
explain("  • Each dict: {'hostname': ..., 'platform': ..., 'ip': ...}")
blank()
explain("Variable name:  parsed_devices")
blank()
header(">>> print(parsed_devices)")
header("[{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'},")
header(" {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'ip': '10.1.0.1'},")
header(" {'hostname': 'sin-fw-01',  'platform': 'ASA',    'ip': '10.2.0.1'}]")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Write one config file per device", "Easy")
explain("Goal:  Create a folder called 'configs' and write one")
explain("       config file per device in INVENTORY.")
blank()
explain("Rules:")
explain("  • Folder:   configs/")
explain("  • Filename: configs/<hostname>.cfg")
explain("  • Content — exactly 3 lines:")
blank()
header("hostname <hostname>")
header("ntp server <ntp from config>")
header("ip name-server <dns from config>")
blank()
explain("  • After writing, store the SORTED list of .cfg filenames")
explain("    (just the filename, not the full path) in 'cfg_files'.")
blank()
explain("Variable name:  cfg_files")
blank()
header(">>> print(cfg_files)")
header("['ams-rtr-02.cfg', 'dub-fw-01.cfg', 'lon-sw-01.cfg',")
header(" 'mum-rtr-01.cfg', 'nyc-rtr-01.cfg', 'sin-fw-01.cfg',")
header(" 'syd-rtr-01.cfg', 'tok-sw-01.cfg']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Write INVENTORY to a CSV file", "Medium")
explain("Goal:  Write INVENTORY to a CSV file called 'inventory.csv'")
explain("       using csv.DictWriter.")
blank()
explain("Rules:")
explain("  • Include these columns in this exact order:")
explain("      hostname, platform, status, ip")
explain("  • Include a header row.")
explain("  • Use newline='' when opening the file.")
blank()
explain("Expected contents of inventory.csv:")
blank()
header("hostname,platform,status,ip")
header("nyc-rtr-01,IOS-XE,up,10.0.0.1")
header("lon-sw-01,NX-OS,down,10.1.0.1")
header("... (8 rows total)")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Read CSV and filter UP devices", "Medium")
explain("Goal:  Read 'inventory.csv' back using csv.DictReader")
explain("       and produce a list called 'csv_devices' containing")
explain("       only devices whose status is 'up'.")
blank()
explain("Rules:")
explain("  • Each item is a dict with keys: hostname, platform, status, ip.")
explain("  • Only include rows where status == 'up'.")
blank()
explain("Variable name:  csv_devices")
blank()
header(">>> print(csv_devices)")
header("[{'hostname':'nyc-rtr-01','platform':'IOS-XE','status':'up','ip':'10.0.0.1'},")
header(" {'hostname':'sin-fw-01', 'platform':'ASA',   'status':'up','ip':'10.2.0.1'},")
header(" {'hostname':'ams-rtr-02','platform':'IOS-XE','status':'up','ip':'10.3.0.1'},")
header(" {'hostname':'syd-rtr-01','platform':'IOS-XE','status':'up','ip':'10.5.0.1'},")
header(" {'hostname':'mum-rtr-01','platform':'IOS-XE','status':'up','ip':'10.7.0.1'}]")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Write and read INVENTORY as JSON", "Medium")
explain("Goal:  Write INVENTORY to a JSON file called 'inventory.json'")
explain("       using json.dump(), then read it back using json.load()")
explain("       and store the result in 'json_inventory'.")
blank()
explain("Rules:")
explain("  • Use indent=2 when writing.")
explain("  • json_inventory must be a list of 8 dicts.")
explain("  • Nested fields (vlans, config) must be preserved.")
blank()
explain("Variable name:  json_inventory")
blank()
header(">>> print(type(json_inventory))")
header("<class 'list'>")
blank()
header(">>> print(len(json_inventory))")
header("8")
blank()
header(">>> print(json_inventory[0]['hostname'])")
header("'nyc-rtr-01'")
blank()
header(">>> print(json_inventory[0]['vlans'])")
header("[10, 20, 30]")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Enrich JSON, write back, and build a summary dict", "Medium")
explain("Goal:  Load 'inventory.json', add a 'vlan_count' field to")
explain("       each device, write the enriched data back to")
explain("       'inventory.json', then read it back and build a")
explain("       dict called 'vlan_counts' mapping hostname → vlan_count.")
blank()
explain("Rules:")
explain("  • 'vlan_count' = len(d['vlans']) for each device.")
explain("  • Write the enriched list back to 'inventory.json' with indent=2.")
explain("  • Read the final JSON and build vlan_counts from it.")
blank()
explain("Variable name:  vlan_counts")
blank()
header(">>> print(vlan_counts)")
header("{'nyc-rtr-01': 3, 'lon-sw-01': 2, 'sin-fw-01': 3,")
header(" 'ams-rtr-02': 4, 'tok-sw-01': 2, 'syd-rtr-01': 3,")
header(" 'dub-fw-01': 3,  'mum-rtr-01': 4}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: file_io_solution.py")
explain("Use RELATIVE paths — the grader runs your script from")
explain("a temporary working directory.")
blank()
explain("Tips by task:")
explain("  Task 1 — open('hostnames.txt', 'w') then f.write(h + '\\n') for each")
explain("  Task 2 — open read, [line.strip() for line in f if line.strip()]")
explain("  Task 3 — skip lines starting with '#' or blank, parts = line.split()")
explain("  Task 4 — os.makedirs('configs', exist_ok=True), write 3 lines per device")
explain("           sorted(os.listdir('configs')) for the file list")
explain("  Task 5 — csv.DictWriter with fieldnames=[...], writeheader(), writerows()")
explain("           use newline='' when opening the file")
explain("  Task 6 — csv.DictReader, filter rows where row['status'] == 'up'")
explain("  Task 7 — json.dump(INVENTORY, f, indent=2), then json.load(f)")
explain("  Task 8 — load, add vlan_count, write back, reload, build dict")

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
print(f"{BOLD}{CYAN}    file_io_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 file_io_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()