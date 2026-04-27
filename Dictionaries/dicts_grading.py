# dicts_grading.py
# Python Dicts — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in dicts_solution.py
# 2. Run this script: python3 dicts_grading.py
# 3. Fix any hints and re-run until you get Good Job!

import os
import sys
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
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8", "domain": "corp.net"},
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "dicts_solution.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        sys.exit()

    namespace = {"INVENTORY": INVENTORY, "GLOBAL_NTP": GLOBAL_NTP}
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
    if isinstance(expected, dict):
        for k, v in expected.items():
            print(f"    {GREEN}{k!r}: {v!r}{RESET}")
    elif isinstance(expected, list) and len(expected) > 4:
        for item in expected:
            print(f"    {GREEN}{item}{RESET}")
    else:
        print(f"    {GREEN}{expected}{RESET}")
    blank()


def grade(checks):
    total = len(checks)

    results = []
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        ok = (actual == expected)
        if ok:
            passed += 1
        results.append((task_label, label, ok, actual, expected, hint_text, solution_ways, var_name))

    blank()
    bar = "█" * 62
    score_color = GREEN if passed >= 8 else YELLOW if passed >= 5 else RED
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
    if passed >= 8:
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
    return passed >= 8


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON DICTS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your dicts_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────
    exp_h2ip   = {d["hostname"]: d["ip"] for d in INVENTORY}
    exp_h2plat = {d["hostname"]: d["platform"] for d in INVENTORY}
    exp_status = {
        "up":   sum(1 for d in INVENTORY if d["status"] == "up"),
        "down": sum(1 for d in INVENTORY if d["status"] == "down"),
    }
    exp_up = {d["hostname"]: d["ip"] for d in INVENTORY if d["status"] == "up"}

    exp_pg = {}
    for d in INVENTORY:
        exp_pg.setdefault(d["platform"], [])
        exp_pg[d["platform"]].append(d["hostname"])
    for k in exp_pg:
        exp_pg[k].sort()

    exp_h2cfg = {d["hostname"]: d["config"] for d in INVENTORY}
    exp_vcm   = {d["hostname"]: len(d["vlans"]) for d in INVENTORY}

    exp_ntp = {}
    for d in INVENTORY:
        ntp = d["config"]["ntp"]
        exp_ntp.setdefault(ntp, [])
        exp_ntp[ntp].append(d["hostname"])
    for k in exp_ntp:
        exp_ntp[k].sort()

    BASE = {"dns": "8.8.8.8", "domain": "corp.net", "snmp": "public"}
    exp_merged   = {d["hostname"]: {**BASE, **d["config"]} for d in INVENTORY}
    exp_inverted = {d["ip"]: d["hostname"] for d in INVENTORY}

    platforms_unique = sorted(set(d["platform"] for d in INVENTORY))
    exp_summary = {
        p: {
            "count":     sum(1 for d in INVENTORY if d["platform"] == p),
            "up_count":  sum(1 for d in INVENTORY if d["platform"] == p and d["status"] == "up"),
            "hostnames": sorted(d["hostname"] for d in INVENTORY if d["platform"] == p),
        }
        for p in platforms_unique
    }

    exp_diff = {
        d["hostname"]: d["config"]["ntp"]
        for d in INVENTORY
        if d["config"]["ntp"] != GLOBAL_NTP
    }

    # ── Solution ways ──────────────────────────────────────────────────────────
    ways_h2ip = [
        ("Dict comprehension",
         ["hostname_to_ip = {d['hostname']: d['ip'] for d in INVENTORY}"]),
        ("For loop",
         ["hostname_to_ip = {}",
          "for d in INVENTORY:",
          "    hostname_to_ip[d['hostname']] = d['ip']"]),
    ]
    ways_h2plat = [
        ("Dict comprehension",
         ["hostname_to_platform = {d['hostname']: d['platform'] for d in INVENTORY}"]),
        ("For loop",
         ["hostname_to_platform = {}",
          "for d in INVENTORY:",
          "    hostname_to_platform[d['hostname']] = d['platform']"]),
    ]
    ways_status = [
        ("Two sum() expressions",
         ["status_count = {",
          "    'up':   sum(1 for d in INVENTORY if d['status'] == 'up'),",
          "    'down': sum(1 for d in INVENTORY if d['status'] == 'down'),",
          "}"]),
        ("For loop with .get()",
         ["status_count = {}",
          "for d in INVENTORY:",
          "    s = d['status']",
          "    status_count[s] = status_count.get(s, 0) + 1"]),
    ]
    ways_up = [
        ("Dict comprehension with filter",
         ["up_devices = {d['hostname']: d['ip'] for d in INVENTORY if d['status'] == 'up'}"]),
        ("For loop with if",
         ["up_devices = {}",
          "for d in INVENTORY:",
          "    if d['status'] == 'up':",
          "        up_devices[d['hostname']] = d['ip']"]),
    ]
    ways_pg = [
        (".setdefault() + .append() + .sort()",
         ["platform_groups = {}",
          "for d in INVENTORY:",
          "    platform_groups.setdefault(d['platform'], []).append(d['hostname'])",
          "for k in platform_groups:",
          "    platform_groups[k].sort()"]),
        ("defaultdict",
         ["from collections import defaultdict",
          "platform_groups = defaultdict(list)",
          "for d in INVENTORY:",
          "    platform_groups[d['platform']].append(d['hostname'])",
          "for k in platform_groups:",
          "    platform_groups[k].sort()",
          "platform_groups = dict(platform_groups)"]),
    ]
    ways_h2cfg = [
        ("Dict comprehension",
         ["hostname_to_config = {d['hostname']: d['config'] for d in INVENTORY}"]),
        ("For loop",
         ["hostname_to_config = {}",
          "for d in INVENTORY:",
          "    hostname_to_config[d['hostname']] = d['config']"]),
    ]
    ways_vcm = [
        ("Dict comprehension",
         ["vlan_count_map = {d['hostname']: len(d['vlans']) for d in INVENTORY}"]),
        ("For loop",
         ["vlan_count_map = {}",
          "for d in INVENTORY:",
          "    vlan_count_map[d['hostname']] = len(d['vlans'])"]),
    ]
    ways_ntp = [
        (".setdefault() + .append() + .sort()",
         ["ntp_to_hostnames = {}",
          "for d in INVENTORY:",
          "    ntp = d['config']['ntp']",
          "    ntp_to_hostnames.setdefault(ntp, []).append(d['hostname'])",
          "for k in ntp_to_hostnames:",
          "    ntp_to_hostnames[k].sort()"]),
        ("defaultdict",
         ["from collections import defaultdict",
          "ntp_to_hostnames = defaultdict(list)",
          "for d in INVENTORY:",
          "    ntp_to_hostnames[d['config']['ntp']].append(d['hostname'])",
          "for k in ntp_to_hostnames:",
          "    ntp_to_hostnames[k].sort()",
          "ntp_to_hostnames = dict(ntp_to_hostnames)"]),
    ]
    ways_merged = [
        ("Dict comprehension with ** unpacking",
         ["BASE = {'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public'}",
          "merged_configs = {d['hostname']: {**BASE, **d['config']} for d in INVENTORY}"]),
        ("For loop with .update()",
         ["BASE = {'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public'}",
          "merged_configs = {}",
          "for d in INVENTORY:",
          "    merged = dict(BASE)",
          "    merged.update(d['config'])",
          "    merged_configs[d['hostname']] = merged"]),
    ]
    ways_inverted = [
        ("Dict comprehension",
         ["inverted_ip = {d['ip']: d['hostname'] for d in INVENTORY}"]),
        ("For loop",
         ["inverted_ip = {}",
          "for d in INVENTORY:",
          "    inverted_ip[d['ip']] = d['hostname']"]),
    ]
    ways_summary = [
        ("set() + dict comprehension",
         ["platforms_unique = sorted(set(d['platform'] for d in INVENTORY))",
          "platform_summary = {",
          "    p: {",
          "        'count':     sum(1 for d in INVENTORY if d['platform'] == p),",
          "        'up_count':  sum(1 for d in INVENTORY if d['platform'] == p and d['status'] == 'up'),",
          "        'hostnames': sorted(d['hostname'] for d in INVENTORY if d['platform'] == p),",
          "    }",
          "    for p in platforms_unique",
          "}"]),
        ("For loop building dict of dicts",
         ["platform_summary = {}",
          "for d in INVENTORY:",
          "    p = d['platform']",
          "    if p not in platform_summary:",
          "        platform_summary[p] = {'count': 0, 'up_count': 0, 'hostnames': []}",
          "    platform_summary[p]['count'] += 1",
          "    if d['status'] == 'up':",
          "        platform_summary[p]['up_count'] += 1",
          "    platform_summary[p]['hostnames'].append(d['hostname'])",
          "for k in platform_summary:",
          "    platform_summary[k]['hostnames'].sort()"]),
    ]
    ways_diff = [
        ("Dict comprehension with filter",
         ["ntp_diff = {",
          "    d['hostname']: d['config']['ntp']",
          "    for d in INVENTORY",
          "    if d['config']['ntp'] != GLOBAL_NTP",
          "}"]),
        ("For loop with if",
         ["ntp_diff = {}",
          "for d in INVENTORY:",
          "    if d['config']['ntp'] != GLOBAL_NTP:",
          "        ntp_diff[d['hostname']] = d['config']['ntp']"]),
    ]

    grade([
        ("Task  1", "hostname_to_ip — 8 hostname→ip pairs",
         ns.get("hostname_to_ip"), exp_h2ip,
         "See Chapter 6.3 — dict comprehension: {d['hostname']: d['ip'] for d in INVENTORY}.",
         ways_h2ip, "hostname_to_ip"),
        ("Task  2", "hostname_to_platform — 8 hostname→platform pairs",
         ns.get("hostname_to_platform"), exp_h2plat,
         "See Chapter 6.3 — same pattern, value is d['platform'].",
         ways_h2plat, "hostname_to_platform"),
        ("Task  3", "status_count — {'up': 5, 'down': 3}",
         ns.get("status_count"), exp_status,
         "See Chapter 9.1 — use sum() with a generator for each key.",
         ways_status, "status_count"),
        ("Task  4", "up_devices — hostname→ip for 'up' devices only",
         ns.get("up_devices"), exp_up,
         "See Chapter 6.3 — add 'if d[\"status\"] == \"up\"' to the comprehension.",
         ways_up, "up_devices"),
        ("Task  5", "platform_groups — platform→sorted list of hostnames",
         ns.get("platform_groups"), exp_pg,
         "See Chapter 9.2 — use .setdefault(platform, []) then .append() and .sort().",
         ways_pg, "platform_groups"),
        ("Task  6", "hostname_to_config — hostname→config dict",
         ns.get("hostname_to_config"), exp_h2cfg,
         "See Chapter 6.3 — value is d['config'] directly.",
         ways_h2cfg, "hostname_to_config"),
        ("Task  7", "vlan_count_map — hostname→number of vlans",
         ns.get("vlan_count_map"), exp_vcm,
         "See Chapter 6.3 — value is len(d['vlans']).",
         ways_vcm, "vlan_count_map"),
        ("Task  8", "ntp_to_hostnames — ntp_server→sorted list of hostnames",
         ns.get("ntp_to_hostnames"), exp_ntp,
         "See Chapter 7.3 — key is d['config']['ntp'], use .setdefault() and .append().",
         ways_ntp, "ntp_to_hostnames"),
        ("Task  9", "merged_configs — hostname→BASE merged with device config",
         ns.get("merged_configs"), exp_merged,
         "See Chapter 8.1 — use {**BASE, **d['config']} to merge dicts.",
         ways_merged, "merged_configs"),
        ("Task 10", "inverted_ip — ip→hostname",
         ns.get("inverted_ip"), exp_inverted,
         "See Chapter 6.3 — swap key and value: {d['ip']: d['hostname'] for d in INVENTORY}.",
         ways_inverted, "inverted_ip"),
        ("Task 11", "platform_summary — platform→{count, up_count, hostnames}",
         ns.get("platform_summary"), exp_summary,
         "See Chapter 9 — get unique platforms with set(), then build one summary dict per platform.",
         ways_summary, "platform_summary"),
        ("Task 12", "ntp_diff — hostname→ntp for devices not using GLOBAL_NTP",
         ns.get("ntp_diff"), exp_diff,
         "See Chapter 6.3 — filter with 'if d[\"config\"][\"ntp\"] != GLOBAL_NTP'.",
         ways_diff, "ntp_diff"),
    ])

pause()