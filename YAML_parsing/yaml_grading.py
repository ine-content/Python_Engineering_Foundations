# yaml_grading.py
# YAML Parsing — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in yaml_solution.py
# 2. Run this script: python3 yaml_grading.py
# 3. Fix any hints and re-run until you get Good Job!

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

def fail(text):
    print(f"    {RED}✘  {text}{RESET}")

def hint(text):
    print(f"    {YELLOW}💡 Hint: {text}{RESET}")

def explain(text):
    print(f"  {WHITE}{text}{RESET}")

def blank():
    print()

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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(work_dir):
    filename = "yaml_solution.py"
    solution_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    if not os.path.exists(solution_path):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
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
        with open(solution_path) as f:
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
        fail("Your script raised an error:")
        print()
        traceback.print_exc()
        blank()
        return None


def show_task_review(task_label, label, passed, actual, expected, hint_text, solution_ways, var_name):
    status = f"{GREEN}✔  PASSED{RESET}" if passed else f"{RED}✘  FAILED{RESET}"
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {task_label}: {label}{RESET}")
    print(f"  {status}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

    if not passed:
        hint(hint_text)
        blank()
        print(f"    {YELLOW}What your code produced:{RESET}")
        print(f"    {CYAN}>>> print({var_name}){RESET}")
        print(f"    {RED}{actual}{RESET}")
        blank()

    print(f"    {YELLOW}Ways to write the solution:{RESET}")
    for way_label, way_code in solution_ways:
        print(f"    {YELLOW}  ▸ {way_label}{RESET}")
        for line in way_code:
            print(f"    {CYAN}    {line}{RESET}")
        blank()

    print(f"    {YELLOW}Correct output:{RESET}")
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


def grade(checks, ns=None):
    total = len(checks)

    results = []
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        if expected is None and ns is not None:
            student_defined = var_name.strip("()") in ns
            ok = student_defined and (actual == expected)
        else:
            ok = (actual == expected)
        if ok:
            passed += 1
        results.append((task_label, label, ok, actual, expected, hint_text, solution_ways, var_name))

    blank()
    bar = "█" * 62
    score_color = GREEN if passed >= 6 else YELLOW if passed >= 4 else RED
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    print()
    print(f"{BOLD}  YOUR SCORE:  {score_color}{passed} / {total}{RESET}")
    print()
    for task_label, label, ok, *_ in results:
        mark = f"{GREEN}✔{RESET}" if ok else f"{RED}✘{RESET}"
        print(f"    {mark}  {task_label}: {label}")
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")

    blank()
    explain("Press ENTER to review each task — solutions are shown for all tasks.")
    for task_label, label, ok, actual, expected, hint_text, solution_ways, var_name in results:
        pause()
        show_task_review(task_label, label, ok, actual, expected, hint_text, solution_ways, var_name)

    blank()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    print()
    if passed >= 6:
        print(f"{BOLD}{GREEN}  ✔  GOOD JOB! You scored {passed}/{total}.{RESET}")
        print()
        print(f"{BOLD}{GREEN}  You may move on to the next topic.{RESET}")
        print(f"{BOLD}{GREEN}  Or run this script again to aim for a perfect score.{RESET}")
    else:
        print(f"{BOLD}{RED}  You scored {passed}/{total}.{RESET}")
        print()
        print(f"{BOLD}{YELLOW}  We recommend trying again before moving on.{RESET}")
        print(f"{BOLD}{YELLOW}  Review the solutions above, fix your file, and re-run.{RESET}")
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    return passed >= 6


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         YAML PARSING — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your yaml_solution.py ...")
blank()

work_dir = tempfile.mkdtemp(prefix="yaml_")
ns = run_solution(work_dir)

if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    parsed_full = yaml.safe_load(INVENTORY_YAML_STR)
    exp_devices = parsed_full["devices"]

    # Task 1
    exp_up = [d["hostname"] for d in exp_devices if d["status"] == "up"]

    # Task 2
    exp_global_ntp   = str(parsed_full["global"]["ntp"])
    exp_custom_ntp   = [d["hostname"] for d in exp_devices
                        if str(d["config"]["ntp"]) != exp_global_ntp]

    # Task 3
    exp_inv_yaml      = yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False)
    exp_inv_yaml_type = str

    # Task 4 — check file
    yaml_path = os.path.join(work_dir, "inventory.yaml")
    reloaded = None
    if os.path.exists(yaml_path):
        with open(yaml_path) as f:
            reloaded = yaml.safe_load(f)

    # Task 5
    exp_multi   = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))
    exp_pcounts = {}
    for d in exp_multi:
        p = d["platform"]
        exp_pcounts[p] = exp_pcounts.get(p, 0) + 1

    # Task 6 — check files
    PLATFORM_MAP = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa"}
    exp_hv_files = sorted(f"{d['hostname']}.yaml" for d in INVENTORY)
    nyc_path = os.path.join(work_dir, "host_vars", "nyc-rtr-01.yaml")
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

    # Task 7
    exp_dj_parsed = json.loads(json.dumps(exp_devices, indent=2))
    devices_json = ns.get("devices_json")
    devices_json_parsed = None
    if devices_json:
        try:
            devices_json_parsed = json.loads(devices_json)
        except Exception:
            pass

    # Task 8
    exp_v2d = {}
    for d in exp_multi:
        for v in d["vlans"]:
            exp_v2d.setdefault(v, set()).add(d["hostname"])
    exp_v2d = {k: sorted(v) for k, v in exp_v2d.items()}

    host_var_files = ns.get("host_var_files")

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_up = [
        ("yaml.safe_load then filter",
         ["parsed = yaml.safe_load(INVENTORY_YAML_STR)",
          "devices = parsed['devices']",
          "up_hostnames = [d['hostname'] for d in devices if d['status'] == 'up']"]),
    ]

    ways_ntp = [
        ("extract global ntp then filter",
         ["parsed = yaml.safe_load(INVENTORY_YAML_STR)",
          "devices = parsed['devices']",
          "global_ntp = str(parsed['global']['ntp'])",
          "custom_ntp_hosts = [d['hostname'] for d in devices",
          "                    if str(d['config']['ntp']) != global_ntp]"]),
    ]

    ways_inv_yaml = [
        ("yaml.dump with options",
         ["inv_yaml      = yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False)",
          "inv_yaml_type = type(inv_yaml)"]),
    ]

    ways_reloaded = [
        ("write then read back",
         ["with open('inventory.yaml', 'w') as f:",
          "    yaml.dump(INVENTORY, f, default_flow_style=False)",
          "with open('inventory.yaml') as f:",
          "    reloaded = yaml.safe_load(f)"]),
    ]

    ways_multi = [
        ("yaml.safe_load_all + counter",
         ["multi_devices = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))",
          "platform_counts = {}",
          "for d in multi_devices:",
          "    p = d['platform']",
          "    platform_counts[p] = platform_counts.get(p, 0) + 1"]),
    ]

    ways_hv = [
        ("makedirs + yaml.dump per device + listdir",
         ["PLATFORM_MAP = {'IOS-XE': 'ios', 'NX-OS': 'nxos', 'ASA': 'asa'}",
          "os.makedirs('host_vars', exist_ok=True)",
          "for d in INVENTORY:",
          "    data = {",
          "        'ansible_host':       d['ip'],",
          "        'ansible_network_os': PLATFORM_MAP[d['platform']],",
          "        'ntp':                d['config']['ntp'],",
          "        'vlans':              d['vlans'],",
          "    }",
          "    with open(f\"host_vars/{d['hostname']}.yaml\", 'w') as f:",
          "        yaml.dump(data, f, default_flow_style=False)",
          "host_var_files = sorted(os.listdir('host_vars'))"]),
    ]

    ways_dj = [
        ("yaml.safe_load then json.dumps",
         ["parsed = yaml.safe_load(INVENTORY_YAML_STR)",
          "devices_json = json.dumps(parsed['devices'], indent=2)"]),
    ]

    ways_v2d = [
        ("safe_load_all then nested loop with setdefault",
         ["docs = list(yaml.safe_load_all(MULTI_DOC_YAML_STR))",
          "vlan_to_devices = {}",
          "for d in docs:",
          "    for v in d['vlans']:",
          "        vlan_to_devices.setdefault(v, set()).add(d['hostname'])",
          "vlan_to_devices = {k: sorted(v) for k, v in vlan_to_devices.items()}"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task 1", "up_hostnames — 5 hostnames with status 'up'",
         ns.get("up_hostnames"), exp_up,
         "yaml.safe_load(INVENTORY_YAML_STR)['devices'], then filter status == 'up'.",
         ways_up, "up_hostnames"),
        ("Task 2", "global_ntp + custom_ntp_hosts",
         (ns.get("global_ntp"), ns.get("custom_ntp_hosts")),
         (exp_global_ntp, exp_custom_ntp),
         "parsed['global']['ntp'] for global_ntp. Compare as str() when filtering.",
         ways_ntp, "(global_ntp, custom_ntp_hosts)"),
        ("Task 3", "inv_yaml — INVENTORY as YAML string, inv_yaml_type is str",
         (ns.get("inv_yaml"), ns.get("inv_yaml_type")),
         (exp_inv_yaml, exp_inv_yaml_type),
         "yaml.dump(INVENTORY, default_flow_style=False, sort_keys=False).",
         ways_inv_yaml, "(inv_yaml, inv_yaml_type)"),
        ("Task 4", "reloaded — inventory.yaml read back equals INVENTORY",
         reloaded, INVENTORY,
         "open write + yaml.dump, then open + yaml.safe_load.",
         ways_reloaded, "reloaded"),
        ("Task 5", "multi_devices (5 docs) and platform_counts",
         (ns.get("multi_devices"), ns.get("platform_counts")),
         (exp_multi, exp_pcounts),
         "list(yaml.safe_load_all(MULTI_DOC_YAML_STR)) to get all 5 documents.",
         ways_multi, "(multi_devices, platform_counts)"),
        ("Task 6", "host_var_files list + nyc-rtr-01.yaml correct content",
         (host_var_files, nyc_data),
         (exp_hv_files, exp_nyc),
         "os.makedirs('host_vars', exist_ok=True), map platform, yaml.dump per device.",
         ways_hv, "(host_var_files, nyc-rtr-01.yaml contents)"),
        ("Task 7", "devices_json — YAML devices converted to JSON string",
         devices_json_parsed, exp_dj_parsed,
         "yaml.safe_load(INVENTORY_YAML_STR)['devices'], then json.dumps with indent=2.",
         ways_dj, "json.loads(devices_json)"),
        ("Task 8", "vlan_to_devices — vlan → sorted hostnames from multi-doc",
         ns.get("vlan_to_devices"), exp_v2d,
         "safe_load_all, nested loop over vlans, setdefault+add, then sorted().",
         ways_v2d, "vlan_to_devices"),
    ], ns=ns)

shutil.rmtree(work_dir, ignore_errors=True)
pause()