# yaml_challenges.py
# YAML Parsing — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

import os
import sys
import yaml
import json
import shutil
import tempfile
import traceback

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

def copyable(text):
    print(f"{CYAN}{text}{RESET}")

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

def challenge_header(num, title, difficulty):
    stars = {"Easy": "★☆☆", "Medium": "★★☆"}
    bar = "█" * 62
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    print()
    print(f"{BOLD}  CHALLENGE {num} — {title}{RESET}")
    print(f"{BOLD}  Difficulty: {difficulty}  {stars[difficulty]}{RESET}")
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    blank()

# ─────────────────────────────────────────────────────────────────────────────
# SHARED TEST DATA
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

# YAML strings used as test data
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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num, work_dir):
    filename = f"yaml_solution_ch{challenge_num}.py"
    if not os.path.exists(filename):
        blank()
        print(f"    {RED}✘  File '{filename}' not found.{RESET}")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        explain(f"  Do not move on to the next challenge until this")
        explain(f"  one is complete.")
        blank()
        sys.exit()

    namespace = {
        "yaml":                  yaml,
        "json":                  json,
        "os":                    os,
        "INVENTORY":             INVENTORY,
        "GLOBAL_NTP":            GLOBAL_NTP,
        "INVENTORY_YAML_STR":    INVENTORY_YAML_STR,
        "MULTI_DOC_YAML_STR":    MULTI_DOC_YAML_STR,
        "WORK_DIR":              work_dir,
    }
    try:
        with open(filename) as f:
            code = f.read()
        import textwrap
        code = textwrap.dedent(code)
        old_cwd = os.getcwd()
        os.chdir(work_dir)
        try:
            exec(compile(code, filename, "exec"), namespace)
        finally:
            os.chdir(old_cwd)
        return namespace
    except Exception:
        blank()
        print(f"    {RED}✘  Your script raised an error:{RESET}")
        print()
        traceback.print_exc()
        blank()
        return None


def check(task_label, label, actual, expected, hint_text, solution_code, var_name):
    if actual == expected:
        print(f"    {GREEN}✔  {task_label}: {label}{RESET}")
        return True
    else:
        print(f"    {RED}✘  {task_label}: {label}{RESET}")
        blank()
        print(f"    {YELLOW}💡 Hint: {hint_text}{RESET}")
        blank()
        print(f"    {YELLOW}Solution:{RESET}")
        for line in solution_code.split("\n"):
            print(f"    {CYAN}>>> {line}{RESET}")
        blank()
        print(f"    {YELLOW}What you should see when it is correct:{RESET}")
        print(f"    {CYAN}>>> print({var_name}){RESET}")
        if isinstance(expected, list) and len(expected) > 4:
            for item in expected:
                print(f"    {GREEN}{item}{RESET}")
        elif isinstance(expected, dict) and len(expected) > 4:
            for k, v in expected.items():
                print(f"    {GREEN}{k!r}: {v!r}{RESET}")
        else:
            print(f"    {GREEN}{expected}{RESET}")
        blank()
        print(f"    {RED}What your code produced:{RESET}")
        print(f"    {CYAN}>>> print({var_name}){RESET}")
        print(f"    {RED}{actual}{RESET}")
        blank()
        return False


def grade(challenge_num, checks_list):
    blank()
    section("Grading your solution...")
    passed = 0
    for args in checks_list:
        if check(*args):
            passed += 1
    blank()
    total = len(checks_list)
    if passed == total:
        bar = "█" * 62
        print(f"{BOLD}{GREEN}{bar}{RESET}")
        print(f"{BOLD}{GREEN}{bar}{RESET}")
        print()
        print(f"{BOLD}{GREEN}    ✔  GOOD JOB! All {total} checks passed.{RESET}")
        print()
        print(f"{BOLD}{GREEN}{bar}{RESET}")
        print(f"{BOLD}{GREEN}{bar}{RESET}")
        return True
    else:
        print(f"{BOLD}{RED}{'─' * 62}{RESET}")
        print(f"{BOLD}{RED}  {passed} of {total} checks passed. Fix the hints above and try again.{RESET}")
        print(f"{BOLD}{RED}{'─' * 62}{RESET}")
        return False


# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         YAML PARSING — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have two challenges — Easy and Medium.")
explain("Each one parses and produces real IaC YAML structures.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → yaml_solution_ch1.py")
explain("  Challenge 2 (Medium) → yaml_solution_ch2.py")
blank()
explain("HOW GRADING WORKS:")
explain("  Some tasks use file I/O — your script runs in a")
explain("  temporary working directory. Use relative paths.")
explain("  Some tasks work with YAML strings directly.")
blank()
explain("These are available in your solution files:")
explain("  yaml, json, os, INVENTORY, GLOBAL_NTP")
explain("  INVENTORY_YAML_STR  — YAML string of all 8 devices")
explain("  MULTI_DOC_YAML_STR  — multi-document YAML string")
blank()
explain("IMPORTANT: Copy the data shown on the next screen")
explain("into the TOP of each solution file.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Copy this into the TOP of each solution file.")
blank()
copyable("import yaml, json, os")
blank()
copyable("GLOBAL_NTP = '10.0.0.100'")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
copyable(f"INVENTORY_YAML_STR = {repr(INVENTORY_YAML_STR)}")
blank()
copyable(f"MULTI_DOC_YAML_STR = {repr(MULTI_DOC_YAML_STR)}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Basic YAML Parsing and Writing", "Easy")

explain("Parse YAML strings and write YAML files using INVENTORY.")
blank()

pause()

section("Task A")
explain("Parse INVENTORY_YAML_STR using yaml.safe_load().")
explain("Produce a list called 'devices' containing just the")
explain("device dicts from the 'devices' key.")
explain("Then produce 'up_hostnames' — a list of hostnames")
explain("whose status is 'up', in original order.")
blank()
header(">>> print(up_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task B")
explain("From the parsed INVENTORY_YAML_STR, extract the")
explain("global NTP server (under 'global' → 'ntp') into a")
explain("variable called 'global_ntp'.")
explain("Then produce 'custom_ntp_hosts' — a list of hostnames")
explain("whose config.ntp differs from global_ntp.")
blank()
header(">>> print(global_ntp)")
header("'10.0.0.100'")
blank()
header(">>> print(custom_ntp_hosts)")
header("['lon-sw-01', 'tok-sw-01', 'mum-rtr-01']")
blank()

pause()

section("Task C")
explain("Serialize INVENTORY to a YAML string called 'inv_yaml'")
explain("using yaml.dump() with default_flow_style=False")
explain("and sort_keys=False.")
explain("Then store the TYPE of inv_yaml in 'inv_yaml_type'.")
blank()
header(">>> print(inv_yaml_type)")
header("<class 'str'>")
blank()
header(">>> print(inv_yaml[:60])")
header("- hostname: nyc-rtr-01\n  platform: IOS-XE\n  status: up")
blank()

pause()

section("Task D")
explain("Write INVENTORY to a YAML file called 'inventory.yaml'")
explain("using yaml.dump() with default_flow_style=False.")
explain("Then read it back and produce a list called 'reloaded'")
explain("containing the Python objects from the file.")
explain("reloaded must equal INVENTORY.")
blank()
header(">>> print(reloaded == INVENTORY)")
header("True")
blank()
header(">>> print(type(reloaded))")
header("<class 'list'>")
blank()

pause()

explain("Write your solution in: yaml_solution_ch1.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — yaml.safe_load(INVENTORY_YAML_STR)['devices']. Ch 3.1.")
explain("  Task B — parsed['global']['ntp'] for global_ntp. Ch 5.1.")
explain("  Task C — yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False).")
explain("  Task D — open('inventory.yaml','w') + yaml.dump, then open + yaml.safe_load.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
work_dir_1 = tempfile.mkdtemp(prefix="yaml_ch1_")
ns = run_solution(1, work_dir_1)
if ns:
    parsed_full = yaml.safe_load(INVENTORY_YAML_STR)
    exp_devices      = parsed_full["devices"]
    exp_up           = [d["hostname"] for d in exp_devices if d["status"] == "up"]
    exp_global_ntp   = str(parsed_full["global"]["ntp"])
    exp_custom_ntp   = [d["hostname"] for d in exp_devices
                        if str(d["config"]["ntp"]) != exp_global_ntp]
    exp_inv_yaml_type = str
    exp_inv_yaml      = yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False)
    exp_reloaded      = INVENTORY

    yaml_path = os.path.join(work_dir_1, "inventory.yaml")
    reloaded = None
    if os.path.exists(yaml_path):
        with open(yaml_path) as f:
            reloaded = yaml.safe_load(f)

    grade(1, [
        (
            "Task A", "up_hostnames — 5 hostnames with status 'up'",
            ns.get("up_hostnames"), exp_up,
            "See Chapter 3.1/5.1 — yaml.safe_load(INVENTORY_YAML_STR)['devices'], filter status=='up'.",
            "parsed = yaml.safe_load(INVENTORY_YAML_STR)\ndevices = parsed['devices']\nup_hostnames = [d['hostname'] for d in devices if d['status']=='up']",
            "up_hostnames",
        ),
        (
            "Task B", "global_ntp + custom_ntp_hosts",
            (ns.get("global_ntp"), ns.get("custom_ntp_hosts")),
            (exp_global_ntp, exp_custom_ntp),
            "See Chapter 5.1 — parsed['global']['ntp'] for global_ntp, then filter d['config']['ntp'] != global_ntp.",
            "global_ntp = str(parsed['global']['ntp'])\ncustom_ntp_hosts = [d['hostname'] for d in devices if str(d['config']['ntp']) != global_ntp]",
            "(global_ntp, custom_ntp_hosts)",
        ),
        (
            "Task C", "inv_yaml — INVENTORY as YAML string, inv_yaml_type is str",
            (ns.get("inv_yaml"), ns.get("inv_yaml_type")),
            (exp_inv_yaml, exp_inv_yaml_type),
            "See Chapter 3.3 — yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False).",
            "inv_yaml = yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False)\ninv_yaml_type = type(inv_yaml)",
            "(inv_yaml, inv_yaml_type)",
        ),
        (
            "Task D", "reloaded — inventory.yaml read back equals INVENTORY",
            reloaded, exp_reloaded,
            "See Chapter 3.2/7.2 — write with yaml.dump, read back with yaml.safe_load.",
            "with open('inventory.yaml','w') as f:\n    yaml.dump(INVENTORY, f, default_flow_style=False)\nwith open('inventory.yaml') as f:\n    reloaded = yaml.safe_load(f)",
            "reloaded",
        ),
    ])

shutil.rmtree(work_dir_1, ignore_errors=True)
pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Multi-doc, host_vars, and YAML↔JSON", "Medium")

explain("Work with multi-document YAML, write per-device")
explain("host_vars files, and convert between YAML and JSON.")
blank()

pause()

section("Task A")
explain("Parse MULTI_DOC_YAML_STR using yaml.safe_load_all().")
explain("It contains 5 device documents separated by ---.")
explain("Produce a list called 'multi_devices' containing all 5.")
explain("Then produce 'platform_counts' — a dict mapping each")
explain("platform to how many devices use it.")
blank()
header(">>> print(len(multi_devices))")
header("5")
blank()
header(">>> print(platform_counts)")
header("{'IOS-XE': 2, 'NX-OS': 2, 'ASA': 1}")
blank()

pause()

section("Task B")
explain("Create a folder called 'host_vars' and write one YAML")
explain("file per device in INVENTORY.")
explain("Filename: host_vars/<hostname>.yaml")
explain("Each file must contain:")
blank()
header("ansible_host: <ip>")
header("ansible_network_os: <mapped platform>")
header("ntp: <config.ntp>")
header("vlans: <vlans list>")
blank()
explain("Platform mapping:")
explain("  IOS-XE → ios")
explain("  NX-OS  → nxos")
explain("  ASA    → asa")
blank()
explain("After writing, store the sorted list of .yaml filenames")
explain("in 'host_var_files' (just filenames, not full paths).")
blank()
header(">>> print(host_var_files)")
header("['ams-rtr-02.yaml', 'dub-fw-01.yaml', 'lon-sw-01.yaml',")
header(" 'mum-rtr-01.yaml', 'nyc-rtr-01.yaml', 'sin-fw-01.yaml',")
header(" 'syd-rtr-01.yaml', 'tok-sw-01.yaml']")
blank()
explain("Verify nyc-rtr-01.yaml contains:")
blank()
header("ansible_host: 10.0.0.1")
header("ansible_network_os: ios")
header("ntp: '10.0.0.100'")
header("vlans:")
header("- 10")
header("- 20")
header("- 30")
blank()

pause()

section("Task C")
explain("Convert INVENTORY_YAML_STR to JSON format.")
explain("Parse the YAML string, extract just the 'devices' list,")
explain("and serialize it to a JSON string called 'devices_json'")
explain("with indent=2.")
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

section("Task D")
explain("Using MULTI_DOC_YAML_STR, produce a dict called")
explain("'vlan_to_devices' mapping each unique VLAN number to")
explain("a sorted list of hostnames that have that VLAN.")
explain("Parse MULTI_DOC_YAML_STR to get the 5 devices.")
blank()
header(">>> print(vlan_to_devices)")
header("{10: ['lon-sw-01', 'nyc-rtr-01'],")
header(" 20: ['ams-rtr-02', 'lon-sw-01', 'nyc-rtr-01', 'tok-sw-01'],")
header(" 30: ['ams-rtr-02', 'nyc-rtr-01', 'sin-fw-01'],")
header(" 40: ['ams-rtr-02', 'sin-fw-01'],")
header(" 50: ['sin-fw-01']}")
blank()

pause()

explain("Write your solution in: yaml_solution_ch2.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — list(yaml.safe_load_all(MULTI_DOC_YAML_STR)). Ch 8.2.")
explain("  Task B — platform map dict, yaml.dump per device. Ch 7.2.")
explain("  Task C — yaml.safe_load(INVENTORY_YAML_STR)['devices'], json.dumps. Ch 9.3.")
explain("  Task D — safe_load_all, nested loop over vlans, setdefault+append+sort. Ch 8.2.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
work_dir_2 = tempfile.mkdtemp(prefix="yaml_ch2_")
ns = run_solution(2, work_dir_2)
if ns:
    # Task A
    exp_multi   = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))
    exp_pcounts = {}
    for d in exp_multi:
        p = d["platform"]
        exp_pcounts[p] = exp_pcounts.get(p, 0) + 1

    # Task B
    PLATFORM_MAP = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa"}
    exp_hv_files = sorted(f"{d['hostname']}.yaml" for d in INVENTORY)

    # Verify nyc-rtr-01.yaml content
    nyc_path = os.path.join(work_dir_2, "host_vars", "nyc-rtr-01.yaml")
    nyc_data = None
    if os.path.exists(nyc_path):
        with open(nyc_path) as f:
            nyc_data = yaml.safe_load(f)
    nyc_inv = next(d for d in INVENTORY if d["hostname"] == "nyc-rtr-01")
    exp_nyc = {
        "ansible_host":       nyc_inv["ip"],
        "ansible_network_os": "ios",
        "ntp":                nyc_inv["config"]["ntp"],
        "vlans":              nyc_inv["vlans"],
    }

    # Task C
    parsed_inv = yaml.safe_load(INVENTORY_YAML_STR)
    exp_dj     = json.dumps(parsed_inv["devices"], indent=2)
    devices_json = ns.get("devices_json")
    devices_json_parsed = json.loads(devices_json) if devices_json else None
    exp_dj_parsed = json.loads(exp_dj)

    # Task D
    exp_v2d = {}
    for d in exp_multi:
        for v in d["vlans"]:
            exp_v2d.setdefault(v, set())
            exp_v2d[v].add(d["hostname"])
    exp_v2d = {k: sorted(v) for k, v in exp_v2d.items()}

    host_var_files = ns.get("host_var_files")

    grade(2, [
        (
            "Task A", "multi_devices (5 docs) and platform_counts",
            (ns.get("multi_devices"), ns.get("platform_counts")),
            (exp_multi, exp_pcounts),
            "See Chapter 8.2 — list(yaml.safe_load_all(MULTI_DOC_YAML_STR)).",
            "multi_devices = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))\nplatform_counts = {}\nfor d in multi_devices:\n    p = d['platform']\n    platform_counts[p] = platform_counts.get(p,0)+1",
            "(multi_devices, platform_counts)",
        ),
        (
            "Task B", "host_var_files list + nyc-rtr-01.yaml correct content",
            (host_var_files, nyc_data),
            (exp_hv_files, exp_nyc),
            "See Chapter 6.2 and 7.2 — makedirs, map platform, yaml.dump per device.",
            "os.makedirs('host_vars',exist_ok=True)\nPM={'IOS-XE':'ios','NX-OS':'nxos','ASA':'asa'}\nfor d in INVENTORY:\n    data={'ansible_host':d['ip'],'ansible_network_os':PM[d['platform']],'ntp':d['config']['ntp'],'vlans':d['vlans']}\n    with open(f\"host_vars/{d['hostname']}.yaml\",'w') as f: yaml.dump(data,f,default_flow_style=False)\nhost_var_files=sorted(os.listdir('host_vars'))",
            "(host_var_files, nyc-rtr-01.yaml contents)",
        ),
        (
            "Task C", "devices_json — YAML devices converted to JSON string",
            devices_json_parsed, exp_dj_parsed,
            "See Chapter 9.3 — yaml.safe_load then json.dumps with indent=2.",
            "parsed = yaml.safe_load(INVENTORY_YAML_STR)\ndevices_json = json.dumps(parsed['devices'], indent=2)",
            "json.loads(devices_json)",
        ),
        (
            "Task D", "vlan_to_devices — vlan → sorted hostnames from multi-doc",
            ns.get("vlan_to_devices"), exp_v2d,
            "See Chapter 8.2 — safe_load_all, nested loop over vlans, setdefault+append+sort.",
            "docs = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))\nv2d = {}\nfor d in docs:\n    for v in d['vlans']: v2d.setdefault(v,set()).add(d['hostname'])\nvlan_to_devices = {k:sorted(v) for k,v in v2d.items()}",
            "vlan_to_devices",
        ),
    ])

shutil.rmtree(work_dir_2, ignore_errors=True)
pause()

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}   Both challenges complete.{RESET}")
print(f"{BOLD}   You are ready for the next topic.{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()