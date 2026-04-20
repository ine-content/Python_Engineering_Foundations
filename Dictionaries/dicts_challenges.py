# dicts_challenges.py
# Python Dicts — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

import os
import sys
import copy
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

def header(text):
    print(f"    {CYAN}{text}{RESET}")

def copyable(text):
    """Print with no indentation so student can copy directly."""
    print(f"{CYAN}{text}{RESET}")

def success(text):
    print(f"    {GREEN}✔  {text}{RESET}")

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
# DATA — shared across all challenges
# ─────────────────────────────────────────────────────────────────────────────
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

GLOBAL_NTP = "10.0.0.100"

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"dict_solution_ch{challenge_num}.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        explain(f"  Do not move on to the next challenge until this")
        explain(f"  one is complete.")
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
        fail(f"Your script raised an error:")
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
        hint(hint_text)
        blank()
        print(f"    {YELLOW}Solution:{RESET}")
        print(f"    {CYAN}>>> {solution_code}{RESET}")
        blank()
        print(f"    {YELLOW}What you should see when it is correct:{RESET}")
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
        print(f"    {RED}What your code produced:{RESET}")
        print(f"    {CYAN}>>> print({var_name}){RESET}")
        print(f"    {RED}{actual}{RESET}")
        blank()
        return False


def grade(challenge_num, checks):
    blank()
    section("Grading your solution...")
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_code, var_name in checks:
        if check(task_label, label, actual, expected, hint_text, solution_code, var_name):
            passed += 1
    blank()
    total = len(checks)
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
print(f"{BOLD}         PYTHON DICTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses the same INVENTORY and GLOBAL_NTP.")
explain("Read the challenge, write your solution in the")
explain("correct file, then run this script to check it.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → dict_solution_ch1.py")
explain("  Challenge 2 (Medium) → dict_solution_ch2.py")
explain("  Challenge 3 (Hard)   → dict_solution_ch3.py")
blank()
explain("IMPORTANT: Copy INVENTORY and GLOBAL_NTP shown on")
explain("the next screen into the TOP of each solution file.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Copy this entire block into the TOP of each solution file.")
explain("It is printed with NO indentation so you can copy it directly.")
blank()
copyable("GLOBAL_NTP = '10.0.0.100'")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
explain("Your solution file should start like this:")
blank()
copyable("# dict_solution_ch1.py")
copyable("")
copyable("GLOBAL_NTP = '10.0.0.100'")
copyable("")
copyable("INVENTORY = [")
copyable("    {'hostname': 'nyc-rtr-01', ...},")
copyable("    ...")
copyable("]")
copyable("")
copyable("# your code below")
copyable("hostname_to_ip = {...}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Dict Basics", "Easy")

explain("Using INVENTORY, produce the following dicts.")
blank()

pause()

section("Task A")
explain("Create a dict called 'hostname_to_ip' mapping")
explain("each hostname to its ip address.")
blank()
header(">>> print(hostname_to_ip)")
header("{'nyc-rtr-01': '10.0.0.1', 'lon-sw-01': '10.1.0.1',")
header(" 'sin-fw-01': '10.2.0.1', 'ams-rtr-02': '10.3.0.1',")
header(" 'tok-sw-01': '10.4.0.1', 'syd-rtr-01': '10.5.0.1',")
header(" 'dub-fw-01': '10.6.0.1', 'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

section("Task B")
explain("Create a dict called 'hostname_to_platform' mapping")
explain("each hostname to its platform.")
blank()
header(">>> print(hostname_to_platform)")
header("{'nyc-rtr-01': 'IOS-XE', 'lon-sw-01': 'NX-OS',")
header(" 'sin-fw-01': 'ASA',    'ams-rtr-02': 'IOS-XE',")
header(" 'tok-sw-01': 'NX-OS',  'syd-rtr-01': 'IOS-XE',")
header(" 'dub-fw-01': 'ASA',    'mum-rtr-01': 'IOS-XE'}")
blank()

pause()

section("Task C")
explain("Create a dict called 'status_count' with two keys:")
explain("  'up'   → number of devices with status 'up'")
explain("  'down' → number of devices with status 'down'")
blank()
header(">>> print(status_count)")
header("{'up': 5, 'down': 3}")
blank()

pause()

section("Task D")
explain("Create a dict called 'up_devices' mapping hostname → ip")
explain("but ONLY for devices whose status is 'up'.")
blank()
header(">>> print(up_devices)")
header("{'nyc-rtr-01': '10.0.0.1', 'sin-fw-01': '10.2.0.1',")
header(" 'ams-rtr-02': '10.3.0.1', 'syd-rtr-01': '10.5.0.1',")
header(" 'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

explain("Write your solution in: dict_solution_ch1.py")
explain("Remember to paste INVENTORY and GLOBAL_NTP at the top.")
explain("Use dict comprehensions where possible.")
blank()
explain("Example structure:")
blank()
header("# dict_solution_ch1.py")
header("")
header("hostname_to_ip       = {d['hostname']: ... for d in INVENTORY}")
header("hostname_to_platform = {d['hostname']: ... for d in INVENTORY}")
header("status_count         = {...}")
header("up_devices           = {d['hostname']: ... for d in INVENTORY if ...}")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    exp_h2ip   = {d["hostname"]: d["ip"] for d in INVENTORY}
    exp_h2plat = {d["hostname"]: d["platform"] for d in INVENTORY}
    exp_status = {
        "up":   sum(1 for d in INVENTORY if d["status"] == "up"),
        "down": sum(1 for d in INVENTORY if d["status"] == "down"),
    }
    exp_up = {d["hostname"]: d["ip"] for d in INVENTORY if d["status"] == "up"}

    grade(1, [
        (
            "Task A",
            "hostname_to_ip — 8 hostname→ip pairs",
            ns.get("hostname_to_ip"),
            exp_h2ip,
            "See Chapter 6.3 — dict comprehension: {d['hostname']: d['ip'] for d in INVENTORY}.",
            "hostname_to_ip = {d['hostname']: d['ip'] for d in INVENTORY}",
            "hostname_to_ip",
        ),
        (
            "Task B",
            "hostname_to_platform — 8 hostname→platform pairs",
            ns.get("hostname_to_platform"),
            exp_h2plat,
            "See Chapter 6.3 — {d['hostname']: d['platform'] for d in INVENTORY}.",
            "hostname_to_platform = {d['hostname']: d['platform'] for d in INVENTORY}",
            "hostname_to_platform",
        ),
        (
            "Task C",
            "status_count — {'up': 5, 'down': 3}",
            ns.get("status_count"),
            exp_status,
            "See Chapter 9.1 — count with .get(): counts[s] = counts.get(s, 0) + 1.",
            "status_count = {'up': sum(1 for d in INVENTORY if d['status']=='up'), 'down': sum(1 for d in INVENTORY if d['status']=='down')}",
            "status_count",
        ),
        (
            "Task D",
            "up_devices — hostname→ip for 'up' devices only",
            ns.get("up_devices"),
            exp_up,
            "See Chapter 6.3 — add 'if d[\"status\"] == \"up\"' to the comprehension.",
            "up_devices = {d['hostname']: d['ip'] for d in INVENTORY if d['status'] == 'up'}",
            "up_devices",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Nested Dicts and Grouping", "Medium")

explain("Using INVENTORY, produce the following dicts.")
explain("Each device has a 'config' nested dict with ntp, dns, domain.")
blank()

pause()

section("Task A")
explain("Create a dict called 'platform_groups' mapping each")
explain("platform to a LIST of hostnames that use it.")
explain("Sorted alphabetically within each list.")
blank()
header(">>> print(platform_groups)")
header("{'IOS-XE': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01'],")
header(" 'NX-OS':  ['lon-sw-01', 'tok-sw-01'],")
header(" 'ASA':    ['dub-fw-01', 'sin-fw-01']}")
blank()

pause()

section("Task B")
explain("Create a dict called 'hostname_to_config' mapping")
explain("each hostname to its nested 'config' dict.")
blank()
header(">>> print(hostname_to_config['nyc-rtr-01'])")
header("{'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()
header(">>> print(hostname_to_config['lon-sw-01'])")
header("{'ntp': '10.1.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()

pause()

section("Task C")
explain("Create a dict called 'vlan_count_map' mapping")
explain("each hostname to the NUMBER of VLANs it has.")
blank()
header(">>> print(vlan_count_map)")
header("{'nyc-rtr-01': 3, 'lon-sw-01': 2, 'sin-fw-01': 3,")
header(" 'ams-rtr-02': 4, 'tok-sw-01': 2, 'syd-rtr-01': 3,")
header(" 'dub-fw-01': 3,  'mum-rtr-01': 4}")
blank()

pause()

section("Task D")
explain("Create a dict called 'ntp_to_hostnames' mapping each")
explain("unique NTP server to a LIST of hostnames using it.")
explain("Each device's NTP is in d['config']['ntp'].")
explain("Lists sorted alphabetically.")
blank()
header(">>> print(ntp_to_hostnames)")
header("{'10.0.0.100': ['ams-rtr-02', 'dub-fw-01', 'nyc-rtr-01', 'sin-fw-01', 'syd-rtr-01'],")
header(" '10.1.0.100': ['lon-sw-01'],")
header(" '10.4.0.100': ['tok-sw-01'],")
header(" '10.7.0.100': ['mum-rtr-01']}")
blank()

pause()

explain("Write your solution in: dict_solution_ch2.py")
explain("Remember to paste INVENTORY and GLOBAL_NTP at the top.")
blank()
explain("Tips:")
explain("  Task A — .setdefault(platform, []) then .append(). See Ch 4.3 and 9.2.")
explain("  Task B — dict comprehension: {d['hostname']: d['config'] ...}. See Ch 6.3.")
explain("  Task C — use len(d['vlans']) as the value. See Ch 6.3.")
explain("  Task D — same pattern as Task A but key is d['config']['ntp']. See Ch 7.3.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    # Task A
    exp_pg = {}
    for d in INVENTORY:
        exp_pg.setdefault(d["platform"], [])
        exp_pg[d["platform"]].append(d["hostname"])
    for k in exp_pg:
        exp_pg[k].sort()

    # Task B
    exp_h2cfg = {d["hostname"]: d["config"] for d in INVENTORY}

    # Task C
    exp_vcm = {d["hostname"]: len(d["vlans"]) for d in INVENTORY}

    # Task D
    exp_ntp = {}
    for d in INVENTORY:
        ntp = d["config"]["ntp"]
        exp_ntp.setdefault(ntp, [])
        exp_ntp[ntp].append(d["hostname"])
    for k in exp_ntp:
        exp_ntp[k].sort()

    grade(2, [
        (
            "Task A",
            "platform_groups — platform → sorted list of hostnames",
            ns.get("platform_groups"),
            exp_pg,
            "See Chapter 4.3 and 9.2 — use .setdefault(platform, []) then .append() and .sort().",
            "groups = {}  →  for d in INVENTORY: groups.setdefault(d['platform'], []).append(d['hostname'])  →  sort each list",
            "platform_groups",
        ),
        (
            "Task B",
            "hostname_to_config — hostname → config dict",
            ns.get("hostname_to_config"),
            exp_h2cfg,
            "See Chapter 6.3 — {d['hostname']: d['config'] for d in INVENTORY}.",
            "hostname_to_config = {d['hostname']: d['config'] for d in INVENTORY}",
            "hostname_to_config",
        ),
        (
            "Task C",
            "vlan_count_map — hostname → number of vlans",
            ns.get("vlan_count_map"),
            exp_vcm,
            "See Chapter 6.3 — use len(d['vlans']) as the value.",
            "vlan_count_map = {d['hostname']: len(d['vlans']) for d in INVENTORY}",
            "vlan_count_map",
        ),
        (
            "Task D",
            "ntp_to_hostnames — ntp_server → sorted list of hostnames",
            ns.get("ntp_to_hostnames"),
            exp_ntp,
            "See Chapter 7.3 — key is d['config']['ntp'], use .setdefault() and .append().",
            "ntp = {}  →  for d in INVENTORY: ntp.setdefault(d['config']['ntp'], []).append(d['hostname'])  →  sort each list",
            "ntp_to_hostnames",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Advanced Dict Patterns", "Hard")

explain("Using INVENTORY and GLOBAL_NTP, produce the following.")
explain("This challenge combines nested access, merging,")
explain("grouping, and filtering.")
blank()

pause()

section("Task A")
explain("Create a dict called 'merged_configs' mapping each")
explain("hostname to a MERGED config dict.")
explain("Start with these base defaults:")
blank()
header("BASE = {'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public'}")
blank()
explain("Then merge each device's own config on top.")
explain("Device config values override BASE values.")
explain("Device-specific fields (ntp) are added on top.")
blank()
header(">>> print(merged_configs['nyc-rtr-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.0.0.100'}")
blank()
header(">>> print(merged_configs['lon-sw-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.1.0.100'}")
blank()

pause()

section("Task B")
explain("Create a dict called 'inverted_ip' mapping each")
explain("ip address to its hostname.")
blank()
header(">>> print(inverted_ip)")
header("{'10.0.0.1': 'nyc-rtr-01', '10.1.0.1': 'lon-sw-01',")
header(" '10.2.0.1': 'sin-fw-01',  '10.3.0.1': 'ams-rtr-02',")
header(" '10.4.0.1': 'tok-sw-01',  '10.5.0.1': 'syd-rtr-01',")
header(" '10.6.0.1': 'dub-fw-01',  '10.7.0.1': 'mum-rtr-01'}")
blank()

pause()

section("Task C")
explain("Create a dict called 'platform_summary' mapping each")
explain("platform to a summary dict with three keys:")
explain("  'count'     → total number of devices")
explain("  'up_count'  → number of devices that are 'up'")
explain("  'hostnames' → sorted list of all hostnames")
blank()
header(">>> print(platform_summary['IOS-XE'])")
header("{'count': 4, 'up_count': 4, 'hostnames': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01']}")
blank()
header(">>> print(platform_summary['NX-OS'])")
header("{'count': 2, 'up_count': 0, 'hostnames': ['lon-sw-01', 'tok-sw-01']}")
blank()
header(">>> print(platform_summary['ASA'])")
header("{'count': 2, 'up_count': 1, 'hostnames': ['dub-fw-01', 'sin-fw-01']}")
blank()

pause()

section("Task D")
explain("Create a dict called 'ntp_diff' mapping hostname → ntp")
explain("but ONLY for devices whose NTP differs from GLOBAL_NTP.")
explain(f"GLOBAL_NTP = '{GLOBAL_NTP}'")
blank()
header(">>> print(ntp_diff)")
header("{'lon-sw-01':  '10.1.0.100',")
header(" 'tok-sw-01':  '10.4.0.100',")
header(" 'mum-rtr-01': '10.7.0.100'}")
blank()

pause()

explain("Write your solution in: dict_solution_ch3.py")
explain("Remember to paste INVENTORY and GLOBAL_NTP at the top.")
blank()
explain("Tips:")
explain("  Task A — use {**BASE, **d['config']} to merge. See Ch 8.1.")
explain("  Task B — invert with {d['ip']: d['hostname'] ...}. See Ch 6.3.")
explain("  Task C — build per-platform with sorted hostnames. See Ch 9.")
explain("  Task D — filter where d['config']['ntp'] != GLOBAL_NTP. See Ch 6.3.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    # Task A
    BASE = {"dns": "8.8.8.8", "domain": "corp.net", "snmp": "public"}
    exp_merged = {
        d["hostname"]: {**BASE, **d["config"]}
        for d in INVENTORY
    }

    # Task B
    exp_inverted = {d["ip"]: d["hostname"] for d in INVENTORY}

    # Task C
    platforms_unique = sorted(set(d["platform"] for d in INVENTORY))
    exp_summary = {
        p: {
            "count":     sum(1 for d in INVENTORY if d["platform"] == p),
            "up_count":  sum(1 for d in INVENTORY if d["platform"] == p and d["status"] == "up"),
            "hostnames": sorted(d["hostname"] for d in INVENTORY if d["platform"] == p),
        }
        for p in platforms_unique
    }

    # Task D
    exp_diff = {
        d["hostname"]: d["config"]["ntp"]
        for d in INVENTORY
        if d["config"]["ntp"] != GLOBAL_NTP
    }

    grade(3, [
        (
            "Task A",
            "merged_configs — hostname → BASE merged with device config",
            ns.get("merged_configs"),
            exp_merged,
            "See Chapter 8.1 — use {**BASE, **d['config']} to merge dicts.",
            "merged_configs = {d['hostname']: {**BASE, **d['config']} for d in INVENTORY}",
            "merged_configs",
        ),
        (
            "Task B",
            "inverted_ip — ip → hostname",
            ns.get("inverted_ip"),
            exp_inverted,
            "See Chapter 6.3 — swap key and value: {d['ip']: d['hostname'] for d in INVENTORY}.",
            "inverted_ip = {d['ip']: d['hostname'] for d in INVENTORY}",
            "inverted_ip",
        ),
        (
            "Task C",
            "platform_summary — platform → {count, up_count, hostnames}",
            ns.get("platform_summary"),
            exp_summary,
            "See Chapter 9 — get unique platforms with set(), then build one summary dict per platform.",
            "platforms = sorted(set(d['platform'] for d in INVENTORY))\nplatform_summary = {p: {'count': sum(1 for d in INVENTORY if d['platform']==p), 'up_count': sum(1 for d in INVENTORY if d['platform']==p and d['status']=='up'), 'hostnames': sorted(d['hostname'] for d in INVENTORY if d['platform']==p)} for p in platforms}",
            "platform_summary",
        ),
        (
            "Task D",
            "ntp_diff — hostname → ntp for devices not using GLOBAL_NTP",
            ns.get("ntp_diff"),
            exp_diff,
            "See Chapter 6.3 — filter with 'if d[\"config\"][\"ntp\"] != GLOBAL_NTP'.",
            "ntp_diff = {d['hostname']: d['config']['ntp'] for d in INVENTORY if d['config']['ntp'] != GLOBAL_NTP}",
            "ntp_diff",
        ),
    ])

pause()

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}   All challenges complete.{RESET}")
print(f"{BOLD}   You are ready for the next topic.{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()