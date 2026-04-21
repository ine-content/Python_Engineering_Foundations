# json_challenges.py
# JSON Parsing & Serialization — Student Challenges
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
    stars = {"Easy": "★☆☆", "Medium": "★★☆", "Hard": "★★★"}
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

# The standard INVENTORY list
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

GLOBAL_NTP = "10.0.0.100"

# NX-OS style show interfaces response string
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

# Nested site inventory JSON string
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
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"json_solution_ch{challenge_num}.py"
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
        "json":                   json,
        "copy":                   copy,
        "datetime":               datetime,
        "INVENTORY":              INVENTORY,
        "GLOBAL_NTP":             GLOBAL_NTP,
        "NXOS_INTERFACES_STR":    NXOS_INTERFACES_STR,
        "NESTED_INVENTORY_STR":   NESTED_INVENTORY_STR,
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
print(f"{BOLD}         JSON PARSING & SERIALIZATION — CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have two challenges — Easy and Medium.")
explain("Each one works with JSON strings and Python objects.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → json_solution_ch1.py")
explain("  Challenge 2 (Medium) → json_solution_ch2.py")
blank()
explain("These variables are available in all solution files:")
explain("  INVENTORY, GLOBAL_NTP")
explain("  NXOS_INTERFACES_STR   — JSON string of NX-OS interface data")
explain("  NESTED_INVENTORY_STR  — JSON string of nested site inventory")
explain("  json, copy, datetime  — already imported")
blank()
explain("IMPORTANT: Copy the data shown on the next screen")
explain("into the TOP of your solution file.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Copy this into the TOP of each solution file.")
blank()
copyable("import json, copy")
copyable("from datetime import datetime")
blank()
copyable("GLOBAL_NTP = '10.0.0.100'")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
copyable(f"NXOS_INTERFACES_STR = {repr(NXOS_INTERFACES_STR)}")
blank()
copyable(f"NESTED_INVENTORY_STR = {repr(NESTED_INVENTORY_STR)}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Basic Parsing and Serialization", "Easy")

explain("Parse JSON strings and serialize Python objects.")
blank()

pause()

section("Task A")
explain("Serialize INVENTORY to a JSON string called 'inv_json'")
explain("using json.dumps() with indent=2 and sort_keys=True.")
explain("Then store the TYPE of the result in 'inv_json_type'.")
blank()
header(">>> print(inv_json_type)")
header("<class 'str'>")
blank()
header(">>> print(inv_json[:60])")
header('[\n  {\n    "config": {\n      "dns": "8.8.8.8",\n      "ntp"')
blank()

pause()

section("Task B")
explain("Parse the JSON string below and produce a list called")
explain("'parsed_devices' containing the Python objects.")
blank()
header("devices_json = '[")
header('  {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "active": true,  "backup": null},')
header('  {"hostname": "lon-sw-01",  "platform": "NX-OS",  "active": false, "backup": null},')
header('  {"hostname": "sin-fw-01",  "platform": "ASA",    "active": true,  "backup": null}')
header("]'")
blank()
explain("After parsing, produce 'active_hostnames' — a list of")
explain("hostnames where 'active' is True.")
blank()
header(">>> print(active_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01']")
blank()

pause()

section("Task C")
explain("Produce a variable called 'compact_json' — INVENTORY")
explain("serialized as a compact JSON string (no spaces).")
explain("Use separators=(',', ':').")
blank()
header(">>> print(compact_json[:60])")
header('[{"hostname":"nyc-rtr-01","platform":"IOS-XE","status":"up"')
blank()

pause()

section("Task D")
explain("Produce a variable called 'round_trip' that proves")
explain("a round-trip works: serialize INVENTORY to JSON and")
explain("immediately parse it back.")
explain("round_trip must equal INVENTORY (same content).")
blank()
header(">>> print(round_trip == INVENTORY)")
header("True")
blank()
header(">>> print(type(round_trip))")
header("<class 'list'>")
blank()

pause()

explain("Write your solution in: json_solution_ch1.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — json.dumps(INVENTORY, indent=2, sort_keys=True). Ch 6.")
explain("  Task B — json.loads(devices_json), then filter where d['active']. Ch 2.1.")
explain("  Task C — json.dumps(INVENTORY, separators=(',',':')). Ch 6.3.")
explain("  Task D — json.loads(json.dumps(INVENTORY)). Ch 2.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    devices_json = '[{"hostname":"nyc-rtr-01","platform":"IOS-XE","active":true,"backup":null},{"hostname":"lon-sw-01","platform":"NX-OS","active":false,"backup":null},{"hostname":"sin-fw-01","platform":"ASA","active":true,"backup":null}]'

    exp_inv_json      = json.dumps(INVENTORY, indent=2, sort_keys=True)
    exp_inv_json_type = str
    exp_active        = ["nyc-rtr-01", "sin-fw-01"]
    exp_compact       = json.dumps(INVENTORY, separators=(",", ":"))
    exp_round_trip    = json.loads(json.dumps(INVENTORY))

    grade(1, [
        (
            "Task A", "inv_json — INVENTORY as indented sorted JSON string",
            (ns.get("inv_json"), ns.get("inv_json_type")),
            (exp_inv_json, exp_inv_json_type),
            "See Chapter 6.1/6.2 — json.dumps(INVENTORY, indent=2, sort_keys=True).",
            "inv_json = json.dumps(INVENTORY, indent=2, sort_keys=True)\ninv_json_type = type(inv_json)",
            "(inv_json, inv_json_type)",
        ),
        (
            "Task B", "active_hostnames — hostnames where active is True",
            ns.get("active_hostnames"), exp_active,
            "See Chapter 2.1 and 4.3 — json.loads(devices_json), then filter d['active'].",
            f"devices_json = '{devices_json}'\nparsed_devices = json.loads(devices_json)\nactive_hostnames = [d['hostname'] for d in parsed_devices if d['active']]",
            "active_hostnames",
        ),
        (
            "Task C", "compact_json — INVENTORY as compact JSON string",
            ns.get("compact_json"), exp_compact,
            "See Chapter 6.3 — json.dumps(INVENTORY, separators=(',', ':')).",
            "compact_json = json.dumps(INVENTORY, separators=(',', ':'))",
            "compact_json",
        ),
        (
            "Task D", "round_trip — serialize then parse back equals INVENTORY",
            ns.get("round_trip"), exp_round_trip,
            "See Chapter 2 — json.loads(json.dumps(INVENTORY)).",
            "round_trip = json.loads(json.dumps(INVENTORY))",
            "round_trip",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Navigating and Transforming JSON", "Medium")

explain("Parse real-style device JSON responses and transform them.")
blank()

pause()

section("Task A")
explain("NXOS_INTERFACES_STR is a JSON string containing a NX-OS")
explain("'show interfaces' style response.")
explain("Parse it and produce a list called 'up_interfaces'")
explain("containing dicts for interfaces whose state is 'up'.")
explain("Each dict: {'name': ..., 'vlan': int, 'ip': ...}")
explain("The vlan field must be converted to int (it's a string in the JSON).")
blank()
header(">>> print(up_interfaces)")
header("[{'name': 'Ethernet1/1', 'vlan': 10, 'ip': '10.0.0.1'},")
header(" {'name': 'Ethernet1/3', 'vlan': 30, 'ip': '10.0.2.1'}]")
blank()

pause()

section("Task B")
explain("NESTED_INVENTORY_STR is a JSON string with a nested")
explain("site → devices structure. Parse it and produce a flat")
explain("list called 'all_devices' — one dict per device across")
explain("all sites. Add a 'site' key to each dict.")
blank()
header(">>> for d in all_devices: print(d['site'], d['hostname'])")
header("NYC nyc-rtr-01")
header("NYC nyc-sw-01")
header("LON lon-sw-01")
header("LON lon-fw-01")
header("SIN sin-rtr-01")
blank()

pause()

section("Task C")
explain("Using the parsed nested inventory from Task B,")
explain("produce a dict called 'site_vlan_summary' mapping")
explain("each site name to a sorted list of unique VLANs across")
explain("all its devices.")
blank()
header(">>> print(site_vlan_summary)")
header("{'NYC': [10, 20, 30], 'LON': [10, 20, 30, 40], 'SIN': [10, 20, 50]}")
blank()

pause()

section("Task D")
explain("Serialize INVENTORY to a JSON string called 'safe_json'")
explain("but first enrich each device with a 'checked_at' field")
explain("set to datetime(2024, 1, 15, 10, 30).")
explain("Use a custom default= function to handle the datetime.")
explain("The datetime must appear as its ISO format string.")
blank()
header(">>> import json")
header(">>> data = json.loads(safe_json)")
header(">>> print(data[0]['checked_at'])")
header("'2024-01-15T10:30:00'")
blank()
header(">>> print(data[0]['hostname'])")
header("'nyc-rtr-01'")
blank()

pause()

explain("Write your solution in: json_solution_ch2.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — json.loads(NXOS_INTERFACES_STR), navigate TABLE→ROW,")
explain("           filter state=='up', int(i['vlan']). Ch 4, 5.2.")
explain("  Task B — json.loads(NESTED_INVENTORY_STR), flatten with nested loop,")
explain("           add 'site' key. Ch 9.2.")
explain("  Task C — group VLANs by site from all_devices. Ch 9.")
explain("  Task D — copy.deepcopy(INVENTORY), add datetime field,")
explain("           json.dumps with default= function. Ch 7.2.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    # Task A
    nxos_parsed = json.loads(NXOS_INTERFACES_STR)
    rows = nxos_parsed["TABLE_interface"]["ROW_interface"]
    exp_up_ifaces = [
        {"name": i["interface"], "vlan": int(i["vlan"]), "ip": i["eth_ip_addr"]}
        for i in rows if i["state"] == "up"
    ]

    # Task B
    nested_parsed = json.loads(NESTED_INVENTORY_STR)
    exp_all_devices = [
        {**device, "site": site}
        for site, cfg in nested_parsed["sites"].items()
        for device in cfg["devices"]
    ]

    # Task C
    exp_site_vlans = {}
    for d in exp_all_devices:
        site = d["site"]
        exp_site_vlans.setdefault(site, set())
        for v in d["vlans"]:
            exp_site_vlans[site].add(v)
    exp_site_vlans = {k: sorted(v) for k, v in exp_site_vlans.items()}

    # Task D
    def _dt_default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Cannot serialize {type(obj)}")

    enriched = copy.deepcopy(INVENTORY)
    for d in enriched:
        d["checked_at"] = datetime(2024, 1, 15, 10, 30)
    exp_safe_json = json.dumps(enriched, default=_dt_default)
    exp_safe_parsed = json.loads(exp_safe_json)

    safe_json = ns.get("safe_json")
    safe_parsed = json.loads(safe_json) if safe_json else None

    grade(2, [
        (
            "Task A", "up_interfaces — up interfaces with int vlan from NX-OS JSON",
            ns.get("up_interfaces"), exp_up_ifaces,
            "See Chapter 5.2 — json.loads(NXOS_INTERFACES_STR), then filter state=='up', int(i['vlan']).",
            "data = json.loads(NXOS_INTERFACES_STR)\nrows = data['TABLE_interface']['ROW_interface']\nup_interfaces = [{'name':i['interface'],'vlan':int(i['vlan']),'ip':i['eth_ip_addr']} for i in rows if i['state']=='up']",
            "up_interfaces",
        ),
        (
            "Task B", "all_devices — flattened list with site key from nested JSON",
            ns.get("all_devices"), exp_all_devices,
            "See Chapter 9.2 — json.loads(NESTED_INVENTORY_STR), flatten with nested loop, add site key.",
            "data = json.loads(NESTED_INVENTORY_STR)\nall_devices = [{**d,'site':site} for site,cfg in data['sites'].items() for d in cfg['devices']]",
            "all_devices",
        ),
        (
            "Task C", "site_vlan_summary — site → sorted unique VLANs",
            ns.get("site_vlan_summary"), exp_site_vlans,
            "See Chapter 9 — group VLANs from all_devices by site, use set for uniqueness, sorted().",
            "svs = {}\nfor d in all_devices:\n    svs.setdefault(d['site'], set())\n    for v in d['vlans']: svs[d['site']].add(v)\nsite_vlan_summary = {k: sorted(v) for k,v in svs.items()}",
            "site_vlan_summary",
        ),
        (
            "Task D", "safe_json — INVENTORY enriched with datetime, serialized with default=",
            safe_parsed, exp_safe_parsed,
            "See Chapter 7.2 — copy.deepcopy, add datetime field, json.dumps with default= function.",
            "def dt_default(obj):\n    if isinstance(obj, datetime): return obj.isoformat()\n    raise TypeError()\nenriched = copy.deepcopy(INVENTORY)\nfor d in enriched: d['checked_at'] = datetime(2024,1,15,10,30)\nsafe_json = json.dumps(enriched, default=dt_default)",
            "json.loads(safe_json)",
        ),
    ])

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