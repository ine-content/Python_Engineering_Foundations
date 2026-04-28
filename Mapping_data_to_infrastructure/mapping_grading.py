# mapping_grading.py
# Mapping Data to Infrastructure Use Cases — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in mapping_solution.py
# 2. Run this script: python3 mapping_grading.py
# 3. Fix any hints and re-run until you get Good Job!

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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(work_dir):
    filename = "mapping_solution.py"
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
print(f"{BOLD}         MAPPING DATA — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your mapping_solution.py ...")
blank()

work_dir = tempfile.mkdtemp(prefix="mapping_")
ns = run_solution(work_dir)

if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    exp_hosts = {
        d["hostname"]: {
            "ansible_host":       d["ip"],
            "ansible_network_os": PLATFORM_OS[d["platform"]],
            "ansible_user":       "admin",
        }
        for d in INVENTORY
    }
    exp_ansible_inv = {"all": {"hosts": exp_hosts}}

    # Task 2 — check file
    hosts_path = os.path.join(work_dir, "hosts.yaml")
    reloaded = None
    if os.path.exists(hosts_path):
        with open(hosts_path) as f:
            reloaded = yaml.safe_load(f)

    # Task 3
    def _gen_base(d):
        return (f"hostname {d['hostname']}\n"
                f"ntp server {d['config']['ntp']}\n"
                f"ip name-server {d['config']['dns']}")
    exp_base_configs = {d["hostname"]: _gen_base(d) for d in INVENTORY}

    # Task 4 — check files
    exp_cfg_files = sorted(f"{d['hostname']}.cfg" for d in INVENTORY)
    nyc_cfg_path  = os.path.join(work_dir, "configs", "nyc-rtr-01.cfg")
    nyc_cfg       = None
    if os.path.exists(nyc_cfg_path):
        with open(nyc_cfg_path) as f:
            nyc_cfg = f.read().strip()
    exp_nyc_cfg = _gen_base(next(d for d in INVENTORY if d["hostname"] == "nyc-rtr-01"))

    # Task 5
    def _check_device(d):
        checks = {
            "status_up":    d["status"] == "up",
            "standard_ntp": d["config"]["ntp"] == GLOBAL_NTP,
            "has_vlans":    bool(d["vlans"]),
        }
        return {
            "hostname": d["hostname"],
            "overall":  "PASS" if all(checks.values()) else "FAIL",
            "checks":   checks,
        }
    exp_compliance = [_check_device(d) for d in INVENTORY]

    # Task 6
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

    # Task 7
    valid = [d for d in INVENTORY
             if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS")]
    exp_pipeline_hostnames = sorted(d["hostname"] for d in valid)

    pipe_report_path = os.path.join(work_dir, "pipeline_report.json")
    pipe_report = None
    if os.path.exists(pipe_report_path):
        with open(pipe_report_path) as f:
            pipe_report = json.load(f)
    exp_pipe_report = [
        {
            "hostname":   d["hostname"],
            "status":     d["status"],
            "vlan_count": len(d["vlans"]),
            "cfg_file":   f"pipeline/{d['hostname']}.cfg",
        }
        for d in valid
    ]

    # Task 8
    up_devices = [d for d in INVENTORY if d["status"] == "up"]
    def _ntp_payload(d):
        return {"Cisco-IOS-XE-native:ntp": {
            "server": {"server-list": [{"ip-address": d["config"]["ntp"]}]}
        }}
    exp_ntp_payloads = {d["hostname"]: _ntp_payload(d) for d in up_devices}
    exp_ntp_json     = json.dumps(exp_ntp_payloads, separators=(",", ":"))

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_ansible_inv = [
        ("Dict comprehension wrapped in all/hosts structure",
         ["ansible_inv = {",
          "    'all': {",
          "        'hosts': {",
          "            d['hostname']: {",
          "                'ansible_host':       d['ip'],",
          "                'ansible_network_os': PLATFORM_OS[d['platform']],",
          "                'ansible_user':       'admin',",
          "            }",
          "            for d in INVENTORY",
          "        }",
          "    }",
          "}"]),
    ]

    ways_reloaded = [
        ("yaml.dump write then yaml.safe_load read",
         ["with open('hosts.yaml', 'w') as f:",
          "    yaml.dump(ansible_inv, f, default_flow_style=False)",
          "with open('hosts.yaml') as f:",
          "    reloaded_inv = yaml.safe_load(f)"]),
    ]

    ways_base_configs = [
        ("Function + dict comprehension",
         ["def gen_base_config(d):",
          "    return (f'hostname {d[\"hostname\"]}\\n'",
          "            f'ntp server {d[\"config\"][\"ntp\"]}\\n'",
          "            f'ip name-server {d[\"config\"][\"dns\"]}')",
          "base_configs = {d['hostname']: gen_base_config(d) for d in INVENTORY}"]),
    ]

    ways_cfg_files = [
        ("makedirs + write per device + listdir",
         ["os.makedirs('configs', exist_ok=True)",
          "for d in INVENTORY:",
          "    with open(f\"configs/{d['hostname']}.cfg\", 'w') as f:",
          "        f.write(gen_base_config(d))",
          "cfg_files = sorted(os.listdir('configs'))"]),
    ]

    ways_compliance = [
        ("Function with dict of checks",
         ["def run_compliance(inventory):",
          "    report = []",
          "    for d in inventory:",
          "        checks = {",
          "            'status_up':    d['status'] == 'up',",
          "            'standard_ntp': d['config']['ntp'] == GLOBAL_NTP,",
          "            'has_vlans':    bool(d['vlans']),",
          "        }",
          "        report.append({",
          "            'hostname': d['hostname'],",
          "            'overall':  'PASS' if all(checks.values()) else 'FAIL',",
          "            'checks':   checks,",
          "        })",
          "    return report",
          "compliance_report = run_compliance(INVENTORY)"]),
    ]

    ways_change_plan = [
        ("before_map + set diff per device",
         ["def build_change_plan(b_list, a_list):",
          "    bm = {d['hostname']: d for d in b_list}",
          "    plan = []",
          "    for ad in a_list:",
          "        bd = bm.get(ad['hostname'], {})",
          "        changes = {}",
          "        add_v = set(ad['vlans']) - set(bd.get('vlans', []))",
          "        rem_v = set(bd.get('vlans', [])) - set(ad['vlans'])",
          "        if add_v: changes['vlans_add']    = sorted(add_v)",
          "        if rem_v: changes['vlans_remove'] = sorted(rem_v)",
          "        if ad['ntp'] != bd.get('ntp'):",
          "            changes['ntp'] = {'old': bd.get('ntp'), 'new': ad['ntp']}",
          "        if changes:",
          "            plan.append({'hostname': ad['hostname'], 'changes': changes})",
          "    return plan",
          "change_plan = build_change_plan(before, after)"]),
    ]

    ways_pipeline = [
        ("Filter, gen config, write files, write report",
         ["valid = [d for d in INVENTORY",
          "         if d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS')]",
          "os.makedirs('pipeline', exist_ok=True)",
          "report = []",
          "for d in valid:",
          "    lines = [",
          "        f'hostname {d[\"hostname\"]}',",
          "        f'ntp server {d[\"config\"][\"ntp\"]}',",
          "        f'ip name-server {d[\"config\"][\"dns\"]}',",
          "    ] + [f'vlan {v}' for v in d['vlans']]",
          "    with open(f\"pipeline/{d['hostname']}.cfg\", 'w') as f:",
          "        f.write('\\n'.join(lines))",
          "    report.append({'hostname': d['hostname'], 'status': d['status'],",
          "                   'vlan_count': len(d['vlans']),",
          "                   'cfg_file': f\"pipeline/{d['hostname']}.cfg\"})",
          "with open('pipeline_report.json', 'w') as f:",
          "    json.dump(report, f, indent=2)",
          "pipeline_hostnames = sorted(d['hostname'] for d in valid)"]),
    ]

    ways_ntp_payloads = [
        ("Dict comprehension for up devices",
         ["up_devices = [d for d in INVENTORY if d['status'] == 'up']",
          "ntp_payloads = {",
          "    d['hostname']: {",
          "        'Cisco-IOS-XE-native:ntp': {",
          "            'server': {",
          "                'server-list': [{'ip-address': d['config']['ntp']}]",
          "            }",
          "        }",
          "    }",
          "    for d in up_devices",
          "}",
          "ntp_payloads_json = json.dumps(ntp_payloads, separators=(',', ':'))"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task 1", "ansible_inv — all 8 devices with correct ansible_ keys",
         ns.get("ansible_inv"), exp_ansible_inv,
         "Wrap the dict comprehension in {'all': {'hosts': {...}}}. Use PLATFORM_OS[d['platform']].",
         ways_ansible_inv, "ansible_inv"),
        ("Task 2", "reloaded_inv — hosts.yaml written and read back correctly",
         reloaded, exp_ansible_inv,
         "yaml.dump(ansible_inv, f, default_flow_style=False), then yaml.safe_load(f).",
         ways_reloaded, "reloaded_inv"),
        ("Task 3", "base_configs — hostname → 3-line config string",
         ns.get("base_configs"), exp_base_configs,
         "def gen_base_config(d): return f-string with \\n between the 3 lines.",
         ways_base_configs, "base_configs"),
        ("Task 4", "cfg_files list + nyc-rtr-01.cfg correct content",
         (ns.get("cfg_files"), nyc_cfg),
         (exp_cfg_files, exp_nyc_cfg),
         "os.makedirs('configs', exist_ok=True), write gen_base_config(d) per device.",
         ways_cfg_files, "(cfg_files, nyc-rtr-01.cfg content)"),
        ("Task 5", "compliance_report — PASS/FAIL per device with check details",
         ns.get("compliance_report"), exp_compliance,
         "Three bool checks per device. overall='PASS' only if all([...]) is True.",
         ways_compliance, "compliance_report"),
        ("Task 6", "change_plan — diffs between before and after states",
         ns.get("change_plan"), exp_change_plan,
         "before_map by hostname. set diff for vlans. compare ntp strings.",
         ways_change_plan, "change_plan"),
        ("Task 7", "pipeline_hostnames + pipeline_report.json content",
         (ns.get("pipeline_hostnames"), pipe_report),
         (exp_pipeline_hostnames, exp_pipe_report),
         "Filter up+IOS-XE/NX-OS, gen config with vlan lines, write files and JSON report.",
         ways_pipeline, "(pipeline_hostnames, pipeline_report.json)"),
        ("Task 8", "ntp_payloads + ntp_payloads_json",
         (ns.get("ntp_payloads"), ns.get("ntp_payloads_json")),
         (exp_ntp_payloads, exp_ntp_json),
         "Only up devices. Nested dict: Cisco-IOS-XE-native:ntp → server → server-list.",
         ways_ntp_payloads, "(ntp_payloads, ntp_payloads_json)"),
    ], ns=ns)

shutil.rmtree(work_dir, ignore_errors=True)
pause()