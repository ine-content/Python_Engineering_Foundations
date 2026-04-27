# mapping_challenges.py
# Mapping Data to Infrastructure Use Cases — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

import os
import sys
import json
import yaml
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
# SHARED DATA
# ─────────────────────────────────────────────────────────────────────────────
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

GLOBAL_NTP    = "10.0.0.100"
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

PLATFORM_OS = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa", "IOS-XR": "iosxr"}

VLAN_INTENT = {
    10: {"name": "MGMT",    "svi_ip": "10.10.0.1/24"},
    20: {"name": "USERS",   "svi_ip": "10.20.0.1/24"},
    30: {"name": "VOICE",   "svi_ip": "10.30.0.1/24"},
    40: {"name": "SERVERS", "svi_ip": "10.40.0.1/24"},
    50: {"name": "DMZ",     "svi_ip": "10.50.0.1/24"},
}

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num, work_dir):
    filename = f"mapping_solution_ch{challenge_num}.py"
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
        "json":           json,
        "yaml":           yaml,
        "os":             os,
        "INVENTORY":      INVENTORY,
        "GLOBAL_NTP":     GLOBAL_NTP,
        "RESERVED_VLANS": RESERVED_VLANS,
        "PLATFORM_OS":    PLATFORM_OS,
        "VLAN_INTENT":    VLAN_INTENT,
        "WORK_DIR":       work_dir,
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
print(f"{BOLD}         MAPPING DATA — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Two challenges — Easy and Medium.")
explain("Both build things real Cisco IaC pipelines produce.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → mapping_solution_ch1.py")
explain("  Challenge 2 (Medium) → mapping_solution_ch2.py")
blank()
explain("Available in all solution files:")
explain("  json, yaml, os")
explain("  INVENTORY, GLOBAL_NTP, RESERVED_VLANS")
explain("  PLATFORM_OS  — {'IOS-XE':'ios','NX-OS':'nxos','ASA':'asa',...}")
explain("  VLAN_INTENT  — {10:{name,svi_ip}, 20:{...}, ...}")
blank()
explain("Some tasks use file I/O — your script runs in a")
explain("temporary working directory. Use relative paths.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Copy this into the TOP of each solution file.")
blank()
copyable("import json, yaml, os")
blank()
copyable("GLOBAL_NTP     = '10.0.0.100'")
copyable("RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
copyable("PLATFORM_OS    = {'IOS-XE':'ios','NX-OS':'nxos','ASA':'asa','IOS-XR':'iosxr'}")
blank()
copyable("VLAN_INTENT = {")
for k, v in VLAN_INTENT.items():
    copyable(f"    {k}: {v},")
copyable("}")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Config Generation and Ansible Inventory", "Easy")

explain("Build the two most fundamental IaC outputs —")
explain("an Ansible hosts.yaml and per-device config files.")
blank()

pause()

section("Task A")
explain("Build an Ansible inventory dict called 'ansible_inv'")
explain("from INVENTORY. Structure must match exactly:")
blank()
header("{'all': {'hosts': {")
header("  'nyc-rtr-01': {'ansible_host':'10.0.0.1','ansible_network_os':'ios','ansible_user':'admin'},")
header("  'lon-sw-01':  {'ansible_host':'10.1.0.1','ansible_network_os':'nxos','ansible_user':'admin'},")
header("  ...}}")
blank()
explain("Use PLATFORM_OS to map platform → ansible_network_os.")
explain("All devices use ansible_user='admin'.")
blank()
header(">>> print(ansible_inv['all']['hosts']['nyc-rtr-01'])")
header("{'ansible_host': '10.0.0.1', 'ansible_network_os': 'ios', 'ansible_user': 'admin'}")
blank()

pause()

section("Task B")
explain("Write ansible_inv to a YAML file called 'hosts.yaml'")
explain("using yaml.dump() with default_flow_style=False.")
explain("Then read it back and produce 'reloaded_inv' — a dict.")
blank()
header(">>> print(reloaded_inv['all']['hosts']['sin-fw-01'])")
header("{'ansible_host': '10.2.0.1', 'ansible_network_os': 'asa', 'ansible_user': 'admin'}")
blank()

pause()

section("Task C")
explain("Write a function called 'gen_base_config(device)'")
explain("that returns a config string with these lines:")
blank()
header("hostname <hostname>")
header("ntp server <config.ntp>")
header("ip name-server <config.dns>")
blank()
explain("Then produce 'base_configs' — a dict mapping each")
explain("hostname to its base config string.")
blank()
header(">>> print(base_configs['nyc-rtr-01'])")
header("'hostname nyc-rtr-01\\nntp server 10.0.0.100\\nip name-server 8.8.8.8'")
blank()

pause()

section("Task D")
explain("Create a folder called 'configs' and write one file")
explain("per device in INVENTORY.")
explain("Filename: configs/<hostname>.cfg")
explain("Content: gen_base_config(device)")
explain("After writing, store the sorted list of .cfg filenames")
explain("in 'cfg_files'.")
blank()
header(">>> print(cfg_files)")
header("['ams-rtr-02.cfg','dub-fw-01.cfg','lon-sw-01.cfg','mum-rtr-01.cfg',")
header(" 'nyc-rtr-01.cfg','sin-fw-01.cfg','syd-rtr-01.cfg','tok-sw-01.cfg']")
blank()
explain("Also verify nyc-rtr-01.cfg content is correct.")
blank()

pause()

explain("Write your solution in: mapping_solution_ch1.py")
blank()
explain("Tips:")
explain("  Task A — {d['hostname']: {'ansible_host':d['ip'],...} for d in INVENTORY}. Ch 2.")
explain("  Task B — yaml.dump(ansible_inv, f), yaml.safe_load(f). Ch 2.3.")
explain("  Task C — def gen_base_config(d): return '\\n'.join([...]). Ch 3.1.")
explain("  Task D — makedirs, open per device, yaml.dump. Ch 3.3.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
work_dir_1 = tempfile.mkdtemp(prefix="map_ch1_")
ns = run_solution(1, work_dir_1)
if ns:
    # Task A
    exp_hosts = {
        d["hostname"]: {
            "ansible_host":       d["ip"],
            "ansible_network_os": PLATFORM_OS[d["platform"]],
            "ansible_user":       "admin",
        }
        for d in INVENTORY
    }
    exp_ansible_inv = {"all": {"hosts": exp_hosts}}

    # Task B
    hosts_path = os.path.join(work_dir_1, "hosts.yaml")
    reloaded   = None
    if os.path.exists(hosts_path):
        with open(hosts_path) as f:
            reloaded = yaml.safe_load(f)

    # Task C
    def _gen_base(d):
        return (f"hostname {d['hostname']}\n"
                f"ntp server {d['config']['ntp']}\n"
                f"ip name-server {d['config']['dns']}")
    exp_base_configs = {d["hostname"]: _gen_base(d) for d in INVENTORY}

    # Task D
    exp_cfg_files = sorted(f"{d['hostname']}.cfg" for d in INVENTORY)
    nyc_cfg_path  = os.path.join(work_dir_1, "configs", "nyc-rtr-01.cfg")
    nyc_cfg       = None
    if os.path.exists(nyc_cfg_path):
        with open(nyc_cfg_path) as f:
            nyc_cfg = f.read().strip()
    exp_nyc_cfg = _gen_base(next(d for d in INVENTORY if d["hostname"] == "nyc-rtr-01"))

    grade(1, [
        (
            "Task A", "ansible_inv — all 8 devices with correct ansible_ keys",
            ns.get("ansible_inv"), exp_ansible_inv,
            "See Chapter 2.2 — {'all':{'hosts':{d['hostname']:{'ansible_host':d['ip'],...} for d in INVENTORY}}}.",
            "ansible_inv = {'all': {'hosts': {d['hostname']: {'ansible_host': d['ip'], 'ansible_network_os': PLATFORM_OS[d['platform']], 'ansible_user': 'admin'} for d in INVENTORY}}}",
            "ansible_inv",
        ),
        (
            "Task B", "reloaded_inv — hosts.yaml written and read back correctly",
            reloaded, exp_ansible_inv,
            "See Chapter 2.3 — yaml.dump(ansible_inv, f, default_flow_style=False), then yaml.safe_load(f).",
            "with open('hosts.yaml','w') as f:\n    yaml.dump(ansible_inv, f, default_flow_style=False)\nwith open('hosts.yaml') as f:\n    reloaded_inv = yaml.safe_load(f)",
            "reloaded_inv",
        ),
        (
            "Task C", "base_configs — hostname → 3-line config string",
            ns.get("base_configs"), exp_base_configs,
            "See Chapter 3.1 — def gen_base_config(d): return f'hostname {d[\"hostname\"]}\\nntp server {d[\"config\"][\"ntp\"]}\\nip name-server {d[\"config\"][\"dns\"]}'.",
            "def gen_base_config(d):\n    return f'hostname {d[\"hostname\"]}\\nntp server {d[\"config\"][\"ntp\"]}\\nip name-server {d[\"config\"][\"dns\"]}'\nbase_configs = {d['hostname']: gen_base_config(d) for d in INVENTORY}",
            "base_configs",
        ),
        (
            "Task D", "cfg_files list + nyc-rtr-01.cfg correct content",
            (ns.get("cfg_files"), nyc_cfg),
            (exp_cfg_files, exp_nyc_cfg),
            "See Chapter 3.3 — makedirs('configs'), write gen_base_config(d) per device, sorted(os.listdir('configs')).",
            "os.makedirs('configs',exist_ok=True)\nfor d in INVENTORY:\n    with open(f\"configs/{d['hostname']}.cfg\",'w') as f: f.write(gen_base_config(d))\ncfg_files = sorted(os.listdir('configs'))",
            "(cfg_files, nyc-rtr-01.cfg content)",
        ),
    ])

shutil.rmtree(work_dir_1, ignore_errors=True)
pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Compliance, Change Planning, and Full Pipeline", "Medium")

explain("Build a compliance checker, a change diff engine,")
explain("and run a full IaC pipeline producing real output files.")
blank()

pause()

section("Task A")
explain("Write a function called 'run_compliance(inventory)'")
explain("that checks every device against these rules:")
blank()
explain("  status_up    — status must be 'up'")
explain("  standard_ntp — config.ntp must equal GLOBAL_NTP")
explain("  has_vlans    — vlans list must not be empty")
blank()
explain("Return a list called 'compliance_report' — one dict per device:")
explain("  {'hostname': ..., 'overall': 'PASS'|'FAIL',")
explain("   'checks': {'status_up':bool, 'standard_ntp':bool, 'has_vlans':bool}}")
blank()
header(">>> for r in compliance_report: print(r['overall'], r['hostname'])")
header("FAIL nyc-rtr-01  ← fails standard_ntp? No — should PASS")
blank()
explain("Expected overall results:")
blank()
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

section("Task B")
explain("Write a function called 'build_change_plan(before, after)'")
explain("that diffs two device lists and returns a list of changes.")
explain("Each entry: {'hostname':..., 'changes':{...}}")
explain("Only include devices that actually have changes.")
blank()
explain("Changes to detect per device:")
explain("  vlans_add    — VLANs in after but not in before")
explain("  vlans_remove — VLANs in before but not in after")
explain("  ntp          — {'old':..., 'new':...} if NTP changed")
blank()
explain("Test with:")
blank()
header("before = [")
header("  {'hostname':'nyc-rtr-01','vlans':[10,20],'ntp':'10.0.0.100'},")
header("  {'hostname':'lon-sw-01', 'vlans':[10,20,99],'ntp':'10.9.0.1'},")
header("  {'hostname':'sin-fw-01', 'vlans':[30,40,50],'ntp':'10.0.0.100'},")
header("]")
header("after = [")
header("  {'hostname':'nyc-rtr-01','vlans':[10,20,30],'ntp':'10.0.0.100'},")
header("  {'hostname':'lon-sw-01', 'vlans':[10,20],   'ntp':'10.0.0.100'},")
header("  {'hostname':'sin-fw-01', 'vlans':[30,40,50],'ntp':'10.0.0.100'},")
header("]")
blank()
header(">>> print(change_plan)")
header("[{'hostname':'nyc-rtr-01','changes':{'vlans_add':[30]}},")
header(" {'hostname':'lon-sw-01', 'changes':{'vlans_remove':[99],'ntp':{'old':'10.9.0.1','new':'10.0.0.100'}}}]")
blank()

pause()

section("Task C")
explain("Run a complete IaC pipeline on INVENTORY:")
blank()
explain("  1. Filter: keep only up devices on IOS-XE or NX-OS")
explain("  2. Generate a config string per device:")
explain("       'hostname <hostname>'")
explain("       'ntp server <config.ntp>'")
explain("       'ip name-server <config.dns>'")
explain("       For each vlan: 'vlan <n>'")
explain("  3. Write each config to 'pipeline/<hostname>.cfg'")
explain("  4. Write a JSON report to 'pipeline_report.json'")
explain("     — one entry per device: {hostname, status, vlan_count, cfg_file}")
blank()
explain("After the pipeline, produce:")
explain("  'pipeline_hostnames' — sorted list of written hostnames")
blank()
header(">>> print(pipeline_hostnames)")
header("['ams-rtr-02', 'nyc-rtr-01', 'syd-rtr-01']")
blank()
explain("(Only 3 devices — up AND IOS-XE or NX-OS)")
blank()

pause()

section("Task D")
explain("Build a RESTCONF-style NTP payload for every device")
explain("in INVENTORY whose status is 'up'.")
explain("Produce a dict called 'ntp_payloads' mapping")
explain("each hostname to its payload dict.")
blank()
explain("Each payload structure:")
blank()
header("{'Cisco-IOS-XE-native:ntp': {")
header("  'server': {")
header("    'server-list': [{'ip-address': '<ntp_server>'}]")
header("  }}")
header("}")
blank()
header(">>> print(ntp_payloads['nyc-rtr-01'])")
header("{'Cisco-IOS-XE-native:ntp': {'server': {'server-list': [{'ip-address': '10.0.0.100'}]}}}")
blank()
explain("Produce also 'ntp_payloads_json' — the full dict")
explain("serialized as a compact JSON string (no spaces).")
blank()

pause()

explain("Write your solution in: mapping_solution_ch2.py")
blank()
explain("Tips:")
explain("  Task A — lambda checks per rule, all() for overall. Ch 7.")
explain("  Task B — before_map by hostname, set diff for vlans. Ch 8.")
explain("  Task C — filter, gen config, makedirs, write files, json.dump report. Ch 10.")
explain("  Task D — {d['hostname']: payload for d in INVENTORY if d['status']=='up'}. Ch 6.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
work_dir_2 = tempfile.mkdtemp(prefix="map_ch2_")
ns = run_solution(2, work_dir_2)
if ns:
    # Task A
    def _check_device(d):
        checks = {
            "status_up":    d["status"] == "up",
            "standard_ntp": d["config"]["ntp"] == GLOBAL_NTP,
            "has_vlans":    bool(d["vlans"]),
        }
        overall = "PASS" if all(checks.values()) else "FAIL"
        return {"hostname": d["hostname"], "overall": overall, "checks": checks}
    exp_compliance = [_check_device(d) for d in INVENTORY]

    # Task B
    before = [
        {"hostname": "nyc-rtr-01", "vlans": [10, 20],      "ntp": "10.0.0.100"},
        {"hostname": "lon-sw-01",  "vlans": [10, 20, 99],   "ntp": "10.9.0.1"},
        {"hostname": "sin-fw-01",  "vlans": [30, 40, 50],   "ntp": "10.0.0.100"},
    ]
    after = [
        {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30],   "ntp": "10.0.0.100"},
        {"hostname": "lon-sw-01",  "vlans": [10, 20],        "ntp": "10.0.0.100"},
        {"hostname": "sin-fw-01",  "vlans": [30, 40, 50],    "ntp": "10.0.0.100"},
    ]
    def _diff(b_list, a_list):
        bm = {d["hostname"]: d for d in b_list}
        plan = []
        for ad in a_list:
            bd = bm.get(ad["hostname"], {})
            changes = {}
            add_v = set(ad["vlans"]) - set(bd.get("vlans", []))
            rem_v = set(bd.get("vlans", [])) - set(ad["vlans"])
            if add_v: changes["vlans_add"]    = sorted(add_v)
            if rem_v: changes["vlans_remove"] = sorted(rem_v)
            if ad["ntp"] != bd.get("ntp"):
                changes["ntp"] = {"old": bd.get("ntp"), "new": ad["ntp"]}
            if changes:
                plan.append({"hostname": ad["hostname"], "changes": changes})
        return plan
    exp_change_plan = _diff(before, after)

    # Task C
    valid = [d for d in INVENTORY
             if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS")]
    exp_pipeline_hostnames = sorted(d["hostname"] for d in valid)

    pipe_report_path = os.path.join(work_dir_2, "pipeline_report.json")
    pipe_report = None
    if os.path.exists(pipe_report_path):
        with open(pipe_report_path) as f:
            pipe_report = json.load(f)
    exp_pipe_report = [
        {"hostname": d["hostname"], "status": d["status"],
         "vlan_count": len(d["vlans"]),
         "cfg_file": f"pipeline/{d['hostname']}.cfg"}
        for d in valid
    ]

    # Task D
    up_devices = [d for d in INVENTORY if d["status"] == "up"]
    def _ntp_payload(d):
        return {"Cisco-IOS-XE-native:ntp": {"server": {"server-list": [{"ip-address": d["config"]["ntp"]}]}}}
    exp_ntp_payloads = {d["hostname"]: _ntp_payload(d) for d in up_devices}
    exp_ntp_json     = json.dumps(exp_ntp_payloads, separators=(",", ":"))

    grade(2, [
        (
            "Task A", "compliance_report — PASS/FAIL per device with check details",
            ns.get("compliance_report"), exp_compliance,
            "See Chapter 7.2 — check status=='up', ntp==GLOBAL_NTP, bool(vlans). overall='PASS' if all pass.",
            "def run_compliance(inv):\n    return [{'hostname':d['hostname'],'overall':'PASS' if all([d['status']=='up',d['config']['ntp']==GLOBAL_NTP,bool(d['vlans'])]) else 'FAIL','checks':{'status_up':d['status']=='up','standard_ntp':d['config']['ntp']==GLOBAL_NTP,'has_vlans':bool(d['vlans'])}} for d in inv]\ncompliance_report=run_compliance(INVENTORY)",
            "compliance_report",
        ),
        (
            "Task B", "change_plan — diffs between before and after states",
            ns.get("change_plan"), exp_change_plan,
            "See Chapter 8.2 — before_map by hostname, set diff for vlans, compare ntp.",
            "def build_change_plan(b,a):\n    bm={d['hostname']:d for d in b}\n    plan=[]\n    for ad in a:\n        bd=bm.get(ad['hostname'],{})\n        ch={}\n        add_v=set(ad['vlans'])-set(bd.get('vlans',[]))\n        rem_v=set(bd.get('vlans',[]))-set(ad['vlans'])\n        if add_v: ch['vlans_add']=sorted(add_v)\n        if rem_v: ch['vlans_remove']=sorted(rem_v)\n        if ad['ntp']!=bd.get('ntp'): ch['ntp']={'old':bd.get('ntp'),'new':ad['ntp']}\n        if ch: plan.append({'hostname':ad['hostname'],'changes':ch})\n    return plan\nchange_plan=build_change_plan(before,after)",
            "change_plan",
        ),
        (
            "Task C", "pipeline_hostnames + pipeline_report.json content",
            (ns.get("pipeline_hostnames"), pipe_report),
            (exp_pipeline_hostnames, exp_pipe_report),
            "See Chapter 10 — filter up+IOS-XE/NX-OS, gen config, makedirs('pipeline'), write files, json.dump report.",
            "valid=[d for d in INVENTORY if d['status']=='up' and d['platform'] in ('IOS-XE','NX-OS')]\nos.makedirs('pipeline',exist_ok=True)\nreport=[]\nfor d in valid:\n    cfg='\\n'.join([f'hostname {d[\"hostname\"]}',f'ntp server {d[\"config\"][\"ntp\"]}',f'ip name-server {d[\"config\"][\"dns\"]}']+[f'vlan {v}' for v in d['vlans']])\n    with open(f\"pipeline/{d['hostname']}.cfg\",'w') as f: f.write(cfg)\n    report.append({'hostname':d['hostname'],'status':d['status'],'vlan_count':len(d['vlans']),'cfg_file':f\"pipeline/{d['hostname']}.cfg\"})\nwith open('pipeline_report.json','w') as f: json.dump(report,f,indent=2)\npipeline_hostnames=sorted(d['hostname'] for d in valid)",
            "(pipeline_hostnames, pipeline_report.json)",
        ),
        (
            "Task D", "ntp_payloads + ntp_payloads_json",
            (ns.get("ntp_payloads"), ns.get("ntp_payloads_json")),
            (exp_ntp_payloads, exp_ntp_json),
            "See Chapter 6.2 — {'Cisco-IOS-XE-native:ntp':{'server':{'server-list':[{'ip-address':d['config']['ntp']}]}}} per up device.",
            "up=[d for d in INVENTORY if d['status']=='up']\nntp_payloads={d['hostname']:{'Cisco-IOS-XE-native:ntp':{'server':{'server-list':[{'ip-address':d['config']['ntp']}]}}} for d in up}\nntp_payloads_json=json.dumps(ntp_payloads,separators=(',',':'))",
            "(ntp_payloads, ntp_payloads_json)",
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
print(f"{BOLD}   Course complete — you can now map any data{RESET}")
print(f"{BOLD}   to any infrastructure target.{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()