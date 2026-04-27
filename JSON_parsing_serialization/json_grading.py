# json_grading.py
# JSON Parsing & Serialization — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in json_solution.py
# 2. Run this script: python3 json_grading.py
# 3. Fix any hints and re-run until you get Good Job!

import os
import sys
import json
import copy
import traceback
from datetime import datetime

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
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
    },
]

NXOS_INTERFACES_STR = json.dumps({
    "TABLE_interface": {
        "ROW_interface": [
            {"interface": "Ethernet1/1", "state": "up",   "vlan": "10", "eth_ip_addr": "10.0.0.1"},
            {"interface": "Ethernet1/2", "state": "down", "vlan": "20", "eth_ip_addr": "10.0.1.1"},
            {"interface": "Ethernet1/3", "state": "up",   "vlan": "30", "eth_ip_addr": "10.0.2.1"},
            {"interface": "Ethernet1/4", "state": "down", "vlan": "10", "eth_ip_addr": "10.0.3.1"},
        ]
    }
})

NESTED_INVENTORY_STR = json.dumps({
    "sites": {
        "NYC": {
            "region": "us-east",
            "devices": [
                {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30]},
                {"hostname": "nyc-sw-01",  "platform": "IOS-XE", "status": "up",   "vlans": [10, 20]},
            ],
        },
        "LON": {
            "region": "eu-west",
            "devices": [
                {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10, 20]},
                {"hostname": "lon-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30, 40]},
            ],
        },
        "SIN": {
            "region": "ap-southeast",
            "devices": [
                {"hostname": "sin-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 50]},
            ],
        },
    }
})

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "json_solution.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        sys.exit()

    namespace = {
        "json":                  json,
        "copy":                  copy,
        "datetime":              datetime,
        "INVENTORY":             INVENTORY,
        "GLOBAL_NTP":            GLOBAL_NTP,
        "NXOS_INTERFACES_STR":   NXOS_INTERFACES_STR,
        "NESTED_INVENTORY_STR":  NESTED_INVENTORY_STR,
    }
    try:
        with open(filename) as f:
            code = f.read()
        import textwrap
        code = textwrap.dedent(code)
        exec(compile(code, filename, "exec"), namespace)
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
print(f"{BOLD}         JSON PARSING & SERIALIZATION — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your json_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    exp_inv_json      = json.dumps(INVENTORY, indent=2, sort_keys=True)
    exp_inv_json_type = str

    # Task 2
    devices_json = '[{"hostname":"nyc-rtr-01","platform":"IOS-XE","active":true,"backup":null},{"hostname":"lon-sw-01","platform":"NX-OS","active":false,"backup":null},{"hostname":"sin-fw-01","platform":"ASA","active":true,"backup":null}]'
    exp_active = ["nyc-rtr-01", "sin-fw-01"]

    # Task 3
    exp_compact = json.dumps(INVENTORY, separators=(",", ":"))

    # Task 4
    exp_round_trip = json.loads(json.dumps(INVENTORY))

    # Task 5
    nxos_parsed = json.loads(NXOS_INTERFACES_STR)
    rows = nxos_parsed["TABLE_interface"]["ROW_interface"]
    exp_up_ifaces = [
        {"name": i["interface"], "vlan": int(i["vlan"]), "ip": i["eth_ip_addr"]}
        for i in rows if i["state"] == "up"
    ]

    # Task 6
    nested_parsed = json.loads(NESTED_INVENTORY_STR)
    exp_all_devices = [
        {**device, "site": site}
        for site, cfg in nested_parsed["sites"].items()
        for device in cfg["devices"]
    ]

    # Task 7
    exp_site_vlans = {}
    for d in exp_all_devices:
        exp_site_vlans.setdefault(d["site"], set())
        for v in d["vlans"]:
            exp_site_vlans[d["site"]].add(v)
    exp_site_vlans = {k: sorted(v) for k, v in exp_site_vlans.items()}

    # Task 8
    def _dt_default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Cannot serialize {type(obj)}")

    enriched = copy.deepcopy(INVENTORY)
    for d in enriched:
        d["checked_at"] = datetime(2024, 1, 15, 10, 30)
    exp_safe_parsed = json.loads(json.dumps(enriched, default=_dt_default))

    safe_json = ns.get("safe_json")
    safe_parsed = None
    if safe_json:
        try:
            safe_parsed = json.loads(safe_json)
        except Exception:
            pass

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_inv_json = [
        ("json.dumps with indent and sort_keys",
         ["inv_json      = json.dumps(INVENTORY, indent=2, sort_keys=True)",
          "inv_json_type = type(inv_json)"]),
    ]

    ways_active = [
        ("json.loads then list comprehension",
         ["devices_json = '[{\"hostname\":\"nyc-rtr-01\",\"active\":true}, ...]'",
          "parsed_devices   = json.loads(devices_json)",
          "active_hostnames = [d['hostname'] for d in parsed_devices if d['active']]"]),
    ]

    ways_compact = [
        ("json.dumps with separators",
         ["compact_json = json.dumps(INVENTORY, separators=(',', ':'))"]),
    ]

    ways_round_trip = [
        ("json.loads(json.dumps(...))",
         ["round_trip = json.loads(json.dumps(INVENTORY))"]),
    ]

    ways_up_ifaces = [
        ("json.loads then filter with int conversion",
         ["data = json.loads(NXOS_INTERFACES_STR)",
          "rows = data['TABLE_interface']['ROW_interface']",
          "up_interfaces = [",
          "    {'name': i['interface'], 'vlan': int(i['vlan']), 'ip': i['eth_ip_addr']}",
          "    for i in rows if i['state'] == 'up'",
          "]"]),
    ]

    ways_all_devices = [
        ("json.loads then nested comprehension with site key",
         ["data = json.loads(NESTED_INVENTORY_STR)",
          "all_devices = [",
          "    {**device, 'site': site}",
          "    for site, cfg in data['sites'].items()",
          "    for device in cfg['devices']",
          "]"]),
        ("For loop version",
         ["data = json.loads(NESTED_INVENTORY_STR)",
          "all_devices = []",
          "for site, cfg in data['sites'].items():",
          "    for device in cfg['devices']:",
          "        all_devices.append({**device, 'site': site})"]),
    ]

    ways_site_vlans = [
        ("setdefault with set then sorted",
         ["site_vlan_summary = {}",
          "for d in all_devices:",
          "    site_vlan_summary.setdefault(d['site'], set())",
          "    for v in d['vlans']:",
          "        site_vlan_summary[d['site']].add(v)",
          "site_vlan_summary = {k: sorted(v) for k, v in site_vlan_summary.items()}"]),
    ]

    ways_safe_json = [
        ("copy.deepcopy + datetime field + custom default",
         ["def dt_default(obj):",
          "    if isinstance(obj, datetime):",
          "        return obj.isoformat()",
          "    raise TypeError(f'Cannot serialize {type(obj)}')",
          "",
          "enriched = copy.deepcopy(INVENTORY)",
          "for d in enriched:",
          "    d['checked_at'] = datetime(2024, 1, 15, 10, 30)",
          "safe_json = json.dumps(enriched, default=dt_default)"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task 1", "inv_json — INVENTORY as indented sorted JSON string",
         (ns.get("inv_json"), ns.get("inv_json_type")),
         (exp_inv_json, exp_inv_json_type),
         "json.dumps(INVENTORY, indent=2, sort_keys=True). type(inv_json) should be str.",
         ways_inv_json, "(inv_json, inv_json_type)"),
        ("Task 2", "active_hostnames — hostnames where active is True",
         ns.get("active_hostnames"), exp_active,
         "json.loads(devices_json), then [d['hostname'] for d in parsed if d['active']].",
         ways_active, "active_hostnames"),
        ("Task 3", "compact_json — INVENTORY as compact JSON string",
         ns.get("compact_json"), exp_compact,
         "json.dumps(INVENTORY, separators=(',', ':')).",
         ways_compact, "compact_json"),
        ("Task 4", "round_trip — serialize then parse back equals INVENTORY",
         ns.get("round_trip"), exp_round_trip,
         "json.loads(json.dumps(INVENTORY)).",
         ways_round_trip, "round_trip"),
        ("Task 5", "up_interfaces — up interfaces with int vlan from NX-OS JSON",
         ns.get("up_interfaces"), exp_up_ifaces,
         "json.loads(NXOS_INTERFACES_STR), navigate TABLE→ROW, filter state=='up', int(i['vlan']).",
         ways_up_ifaces, "up_interfaces"),
        ("Task 6", "all_devices — flattened list with site key from nested JSON",
         ns.get("all_devices"), exp_all_devices,
         "json.loads(NESTED_INVENTORY_STR), flatten with nested loop, add 'site' key.",
         ways_all_devices, "all_devices"),
        ("Task 7", "site_vlan_summary — site → sorted unique VLANs",
         ns.get("site_vlan_summary"), exp_site_vlans,
         "Group VLANs from all_devices by site, use set() for uniqueness, then sorted().",
         ways_site_vlans, "site_vlan_summary"),
        ("Task 8", "safe_json — INVENTORY enriched with datetime, serialized with default=",
         safe_parsed, exp_safe_parsed,
         "copy.deepcopy, add datetime field, json.dumps with default= that calls .isoformat().",
         ways_safe_json, "json.loads(safe_json)"),
    ], ns=ns)

pause()