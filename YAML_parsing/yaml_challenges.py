# yaml_challenges.py
# YAML Parsing — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: yaml_solution.py
# 3. Run yaml_grading.py to check your answers

import os
import yaml
import json

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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         YAML PARSING — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("8 tasks — Easy and Medium — all in one challenge.")
explain("Each task parses or produces real IaC YAML structures.")
explain("Read each task, write your solution in yaml_solution.py,")
explain("then run yaml_grading.py to check it.")
blank()
explain("HOW FILE GRADING WORKS:")
explain("  Some tasks involve file I/O. Your script runs in a")
explain("  temporary working directory — use RELATIVE paths.")
blank()
explain("The data is already pasted at the top of")
explain("yaml_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Parse YAML string and filter UP devices", "Easy")
explain("Goal:  Parse INVENTORY_YAML_STR using yaml.safe_load().")
explain("       Produce a list called 'up_hostnames' — hostnames")
explain("       of devices whose status is 'up', in original order.")
blank()
explain("Rules:")
explain("  • The devices are under the 'devices' key.")
explain("  • Only include devices with status == 'up'.")
blank()
explain("Variable name:  up_hostnames")
blank()
header(">>> print(up_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Extract global NTP and find custom NTP devices", "Easy")
explain("Goal:  From the parsed INVENTORY_YAML_STR, extract the")
explain("       global NTP server into 'global_ntp', then build")
explain("       'custom_ntp_hosts' — hostnames whose config.ntp")
explain("       differs from global_ntp.")
blank()
explain("Rules:")
explain("  • global_ntp is at parsed['global']['ntp'].")
explain("  • Compare as strings.")
blank()
explain("Variable names:  global_ntp  /  custom_ntp_hosts")
blank()
header(">>> print(global_ntp)")
header("'10.0.0.100'")
blank()
header(">>> print(custom_ntp_hosts)")
header("['lon-sw-01', 'tok-sw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Serialize INVENTORY to a YAML string", "Easy")
explain("Goal:  Serialize INVENTORY to a YAML string called 'inv_yaml'")
explain("       using yaml.dump(). Also store the type in 'inv_yaml_type'.")
blank()
explain("Rules:")
explain("  • Use default_flow_style=False and sort_keys=False.")
blank()
explain("Variable names:  inv_yaml  /  inv_yaml_type")
blank()
header(">>> print(inv_yaml_type)")
header("<class 'str'>")
blank()
header(">>> print(inv_yaml[:60])")
header("- hostname: nyc-rtr-01\n  platform: IOS-XE\n  status: up")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Write INVENTORY to a YAML file and read it back", "Easy")
explain("Goal:  Write INVENTORY to a YAML file called 'inventory.yaml'")
explain("       then read it back and store the result in 'reloaded'.")
blank()
explain("Rules:")
explain("  • Use relative path: 'inventory.yaml'")
explain("  • Use yaml.dump() to write, yaml.safe_load() to read.")
explain("  • reloaded must equal INVENTORY.")
blank()
explain("Variable name:  reloaded")
blank()
header(">>> print(reloaded == INVENTORY)")
header("True")
blank()
header(">>> print(type(reloaded))")
header("<class 'list'>")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Parse a multi-document YAML string", "Medium")
explain("Goal:  Parse MULTI_DOC_YAML_STR using yaml.safe_load_all().")
explain("       It contains 5 device documents separated by ---.")
explain("       Produce a list called 'multi_devices' with all 5.")
explain("       Then produce 'platform_counts' — a dict mapping")
explain("       each platform to how many devices use it.")
blank()
explain("Variable names:  multi_devices  /  platform_counts")
blank()
header(">>> print(len(multi_devices))")
header("5")
blank()
header(">>> print(platform_counts)")
header("{'IOS-XE': 2, 'NX-OS': 2, 'ASA': 1}")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Write per-device host_vars YAML files", "Medium")
explain("Goal:  Create a folder called 'host_vars' and write one")
explain("       YAML file per device in INVENTORY.")
blank()
explain("Rules:")
explain("  • Filename: host_vars/<hostname>.yaml")
explain("  • Each file must contain these four keys:")
explain("      ansible_host:       <ip>")
explain("      ansible_network_os: <mapped platform>")
explain("      ntp:                <config.ntp>")
explain("      vlans:              <vlans list>")
explain("  • Platform mapping:")
explain("      IOS-XE → ios    NX-OS → nxos    ASA → asa")
explain("  • After writing, store the sorted list of .yaml filenames")
explain("    in 'host_var_files' (just filenames, not full paths).")
blank()
explain("Variable name:  host_var_files")
blank()
header(">>> print(host_var_files)")
header("['ams-rtr-02.yaml', 'dub-fw-01.yaml', 'lon-sw-01.yaml',")
header(" 'mum-rtr-01.yaml', 'nyc-rtr-01.yaml', 'sin-fw-01.yaml',")
header(" 'syd-rtr-01.yaml', 'tok-sw-01.yaml']")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Convert YAML devices to JSON", "Medium")
explain("Goal:  Parse INVENTORY_YAML_STR, extract just the 'devices'")
explain("       list, and serialize it to a JSON string called")
explain("       'devices_json' with indent=2.")
blank()
explain("Variable name:  devices_json")
blank()
header(">>> import json")
header(">>> data = json.loads(devices_json)")
header(">>> print(type(data))")
header("<class 'list'>")
blank()
header(">>> print(len(data))")
header("8")
blank()
header(">>> print(data[0]['hostname'])")
header("'nyc-rtr-01'")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Build a VLAN-to-devices map from multi-doc YAML", "Medium")
explain("Goal:  Parse MULTI_DOC_YAML_STR and produce a dict called")
explain("       'vlan_to_devices' mapping each unique VLAN number")
explain("       to a sorted list of hostnames that have that VLAN.")
blank()
explain("Variable name:  vlan_to_devices")
blank()
header(">>> print(vlan_to_devices)")
header("{10: ['lon-sw-01', 'nyc-rtr-01'],")
header(" 20: ['ams-rtr-02', 'lon-sw-01', 'nyc-rtr-01', 'tok-sw-01'],")
header(" 30: ['ams-rtr-02', 'nyc-rtr-01', 'sin-fw-01'],")
header(" 40: ['ams-rtr-02', 'sin-fw-01'],")
header(" 50: ['sin-fw-01']}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: yaml_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task 1 — yaml.safe_load(INVENTORY_YAML_STR)['devices'], filter status=='up'")
explain("  Task 2 — parsed['global']['ntp'], compare as str()")
explain("  Task 3 — yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False)")
explain("  Task 4 — open write + yaml.dump, then open + yaml.safe_load")
explain("  Task 5 — list(yaml.safe_load_all(MULTI_DOC_YAML_STR))")
explain("  Task 6 — os.makedirs('host_vars', exist_ok=True), yaml.dump per device")
explain("           sorted(os.listdir('host_vars')) for the file list")
explain("  Task 7 — yaml.safe_load then json.dumps with indent=2")
explain("  Task 8 — safe_load_all, nested loop over vlans, setdefault+add+sorted")

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
print(f"{BOLD}{CYAN}    yaml_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 yaml_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()