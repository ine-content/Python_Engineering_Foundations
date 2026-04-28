# mapping_challenges.py
# Mapping Data to Infrastructure Use Cases — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: mapping_solution.py
# 3. Run mapping_grading.py to check your answers

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
PLATFORM_OS    = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa", "IOS-XR": "iosxr"}

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
        "site": "NYC", "role": "core",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65001, "neighbors": ["10.3.0.1"]},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "site": "LON", "role": "distribution",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "site": "SIN", "role": "firewall",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "site": "AMS", "role": "core",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65002, "neighbors": ["10.0.0.1"]},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "site": "TOK", "role": "access",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "SYD", "role": "core",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65003, "neighbors": ["10.7.0.1"]},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "site": "DUB", "role": "firewall",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "MUM", "role": "core",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
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
print(f"{BOLD}         MAPPING DATA — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("8 tasks — Easy and Medium — all in one challenge.")
explain("Both sections build real Cisco IaC pipeline outputs.")
explain("Read each task, write your solution in mapping_solution.py,")
explain("then run mapping_grading.py to check it.")
blank()
explain("HOW FILE GRADING WORKS:")
explain("  Some tasks involve file I/O. Your script runs in a")
explain("  temporary working directory — use RELATIVE paths.")
blank()
explain("The data is already pasted at the top of")
explain("mapping_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Build an Ansible inventory dict", "Easy")
explain("Goal:  Build a dict called 'ansible_inv' that represents")
explain("       an Ansible inventory in the standard hosts.yaml format.")
blank()
explain("Rules:")
explain("  • Structure: {'all': {'hosts': { hostname: {...}, ... }}}")
explain("  • Each host dict must have exactly three keys:")
explain("      'ansible_host'       — the device IP")
explain("      'ansible_network_os' — from PLATFORM_OS lookup")
explain("      'ansible_user'       — always 'admin'")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  ansible_inv")
blank()
header(">>> print(ansible_inv['all']['hosts']['nyc-rtr-01'])")
header("{'ansible_host': '10.0.0.1', 'ansible_network_os': 'ios', 'ansible_user': 'admin'}")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Write Ansible inventory to hosts.yaml and read it back", "Easy")
explain("Goal:  Write ansible_inv to a YAML file called 'hosts.yaml',")
explain("       then read it back and store the result in 'reloaded_inv'.")
blank()
explain("Rules:")
explain("  • Use relative path: 'hosts.yaml'")
explain("  • Use yaml.dump() with default_flow_style=False to write.")
explain("  • Use yaml.safe_load() to read back.")
blank()
explain("Variable name:  reloaded_inv")
blank()
header(">>> print(reloaded_inv['all']['hosts']['sin-fw-01'])")
header("{'ansible_host': '10.2.0.1', 'ansible_network_os': 'asa', 'ansible_user': 'admin'}")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Generate a base config string per device", "Easy")
explain("Goal:  Write a function called 'gen_base_config(device)'")
explain("       that returns a 3-line config string for a device.")
explain("       Then produce 'base_configs' — a dict mapping each")
explain("       hostname to its config string.")
blank()
explain("Rules:")
explain("  • Config format (3 lines joined with \\n):")
explain("      hostname <hostname>")
explain("      ntp server <config.ntp>")
explain("      ip name-server <config.dns>")
blank()
explain("Variable name:  base_configs")
blank()
header(">>> print(base_configs['nyc-rtr-01'])")
header("'hostname nyc-rtr-01\\nntp server 10.0.0.100\\nip name-server 8.8.8.8'")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Write one config file per device", "Easy")
explain("Goal:  Create a folder called 'configs' and write one .cfg")
explain("       file per device using gen_base_config().")
blank()
explain("Rules:")
explain("  • Filename: configs/<hostname>.cfg")
explain("  • Content: the result of gen_base_config(device)")
explain("  • After writing, store the sorted list of .cfg filenames")
explain("    in 'cfg_files' (just filenames, not full paths).")
blank()
explain("Variable name:  cfg_files")
blank()
header(">>> print(cfg_files)")
header("['ams-rtr-02.cfg', 'dub-fw-01.cfg', 'lon-sw-01.cfg', 'mum-rtr-01.cfg',")
header(" 'nyc-rtr-01.cfg', 'sin-fw-01.cfg', 'syd-rtr-01.cfg', 'tok-sw-01.cfg']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Run a compliance check on the inventory", "Medium")
explain("Goal:  Write a function called 'run_compliance(inventory)'")
explain("       that checks every device against three rules and")
explain("       returns a list called 'compliance_report'.")
blank()
explain("Rules to check per device:")
explain("  • status_up    — status must be 'up'")
explain("  • standard_ntp — config.ntp must equal GLOBAL_NTP")
explain("  • has_vlans    — vlans list must not be empty")
blank()
explain("Each dict in the report:")
explain("  {'hostname': ..., 'overall': 'PASS' or 'FAIL',")
explain("   'checks': {'status_up': bool, 'standard_ntp': bool, 'has_vlans': bool}}")
explain("  overall is 'PASS' only if ALL three checks are True.")
blank()
explain("Variable name:  compliance_report")
blank()
header("Expected overall results:")
header("PASS nyc-rtr-01")
header("FAIL lon-sw-01   (down, custom ntp)")
header("PASS sin-fw-01")
header("PASS ams-rtr-02")
header("FAIL tok-sw-01   (down, custom ntp)")
header("PASS syd-rtr-01")
header("FAIL dub-fw-01   (down)")
header("FAIL mum-rtr-01  (custom ntp)")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Build a change plan by diffing two device states", "Medium")
explain("Goal:  Write a function called 'build_change_plan(before, after)'")
explain("       that compares two device lists and returns a list of")
explain("       changes called 'change_plan'.")
blank()
explain("Rules:")
explain("  • Only include devices that have at least one change.")
explain("  • Changes to detect per device:")
explain("      vlans_add    — VLANs in after but not in before (sorted list)")
explain("      vlans_remove — VLANs in before but not in after (sorted list)")
explain("      ntp          — {'old': ..., 'new': ...} if NTP changed")
blank()
explain("Test with this data in your solution file:")
blank()
header("before = [")
header("  {'hostname': 'nyc-rtr-01', 'vlans': [10, 20],    'ntp': '10.0.0.100'},")
header("  {'hostname': 'lon-sw-01',  'vlans': [10, 20, 99], 'ntp': '10.9.0.1'},")
header("  {'hostname': 'sin-fw-01',  'vlans': [30, 40, 50], 'ntp': '10.0.0.100'},")
header("]")
header("after = [")
header("  {'hostname': 'nyc-rtr-01', 'vlans': [10, 20, 30], 'ntp': '10.0.0.100'},")
header("  {'hostname': 'lon-sw-01',  'vlans': [10, 20],      'ntp': '10.0.0.100'},")
header("  {'hostname': 'sin-fw-01',  'vlans': [30, 40, 50],  'ntp': '10.0.0.100'},")
header("]")
blank()
explain("Variable name:  change_plan")
blank()
header(">>> print(change_plan)")
header("[{'hostname': 'nyc-rtr-01', 'changes': {'vlans_add': [30]}},")
header(" {'hostname': 'lon-sw-01',  'changes': {'vlans_remove': [99], 'ntp': {'old': '10.9.0.1', 'new': '10.0.0.100'}}}]")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Run a full IaC pipeline", "Medium")
explain("Goal:  Run a complete IaC pipeline on INVENTORY and")
explain("       produce output files plus a summary list.")
blank()
explain("Pipeline steps:")
explain("  1. Filter: keep only 'up' devices on IOS-XE or NX-OS")
explain("  2. Generate a config string per device with these lines:")
explain("       hostname <hostname>")
explain("       ntp server <config.ntp>")
explain("       ip name-server <config.dns>")
explain("       vlan <n>   (one line per VLAN)")
explain("  3. Write each config to 'pipeline/<hostname>.cfg'")
explain("  4. Write a JSON report to 'pipeline_report.json'")
explain("     One entry per device: {hostname, status, vlan_count, cfg_file}")
blank()
explain("Variable name:  pipeline_hostnames")
blank()
header(">>> print(pipeline_hostnames)")
header("['ams-rtr-02', 'nyc-rtr-01', 'syd-rtr-01']")
blank()
explain("(Only 3 devices pass the filter — up AND IOS-XE or NX-OS)")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Build RESTCONF NTP payloads", "Medium")
explain("Goal:  Build a dict called 'ntp_payloads' mapping each")
explain("       UP device hostname to a RESTCONF-style NTP payload.")
explain("       Also produce 'ntp_payloads_json' — the full dict")
explain("       as a compact JSON string (no spaces).")
blank()
explain("Rules:")
explain("  • Only include devices with status 'up'.")
explain("  • Each payload structure:")
blank()
header("{'Cisco-IOS-XE-native:ntp': {")
header("  'server': {")
header("    'server-list': [{'ip-address': '<config.ntp>'}]")
header("  }}")
header("}")
blank()
explain("Variable names:  ntp_payloads  /  ntp_payloads_json")
blank()
header(">>> print(ntp_payloads['nyc-rtr-01'])")
header("{'Cisco-IOS-XE-native:ntp': {'server': {'server-list': [{'ip-address': '10.0.0.100'}]}}}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: mapping_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task 1 — {d['hostname']: {'ansible_host': d['ip'], ...} for d in INVENTORY}")
explain("           wrap in {'all': {'hosts': ...}}")
explain("  Task 2 — yaml.dump(ansible_inv, f, default_flow_style=False)")
explain("           yaml.safe_load(f) to read back")
explain("  Task 3 — def gen_base_config(d): return '\\n'.join([...])")
explain("  Task 4 — os.makedirs('configs', exist_ok=True), write per device")
explain("           sorted(os.listdir('configs')) for the file list")
explain("  Task 5 — check each rule as a bool, all([...]) for overall")
explain("  Task 6 — before_map = {d['hostname']: d for d in before}")
explain("           set diff for vlans, compare ntp string")
explain("  Task 7 — filter, gen config with vlan lines, makedirs('pipeline'),")
explain("           write files, json.dump report, sorted hostnames list")
explain("  Task 8 — {d['hostname']: payload for d in INVENTORY if d['status']=='up'}")
explain("           json.dumps(ntp_payloads, separators=(',', ':'))")

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
print(f"{BOLD}{CYAN}    mapping_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 mapping_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()