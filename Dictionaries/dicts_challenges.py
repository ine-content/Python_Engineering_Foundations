# dicts_challenges.py
# Python Dicts — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: dicts_solution.py
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

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

def header(text):
    print(f"    {CYAN}{text}{RESET}")

def copyable(text):
    print(f"{CYAN}{text}{RESET}")

def fail(text):
    print(f"    {RED}✘  {text}{RESET}")

def hint(text):
    print(f"    {YELLOW}💡 Hint: {text}{RESET}")

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
# GRADER
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

    # ── Step 1: run all checks silently ───────────────────────────────────────
    results = []
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        ok = (actual == expected)
        if ok:
            passed += 1
        results.append((task_label, label, ok, actual, expected, hint_text, solution_ways, var_name))

    # ── Step 2: show score first ───────────────────────────────────────────────
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

    # ── Step 3: walk through each task review one by one ──────────────────────
    blank()
    explain("Press ENTER to review each task — solutions are shown for all tasks.")
    for task_label, label, ok, actual, expected, hint_text, solution_ways, var_name in results:
        pause()
        show_task_review(task_label, label, ok, actual, expected, hint_text, solution_ways, var_name)

    # ── Step 4: final message based on score ──────────────────────────────────
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
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON DICTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same INVENTORY and GLOBAL_NTP.")
explain("Read each task, write your solution in the file below,")
explain("then run this script to check it.")
blank()
explain("File to create:  dicts_solution.py")
blank()
explain("IMPORTANT: Copy INVENTORY and GLOBAL_NTP shown on the")
explain("next screen into the TOP of your solution file.")
explain("Your solution will not work without it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")
explain("Copy this entire block into the TOP of your solution file.")
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
copyable("# dicts_solution.py")
copyable("")
copyable("GLOBAL_NTP = '10.0.0.100'")
copyable("")
copyable("INVENTORY = [")
copyable("    {'hostname': 'nyc-rtr-01', ...},")
copyable("    ...")
copyable("]")
copyable("")
copyable("# your answers below — one variable per task")
copyable("hostname_to_ip = {...}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Map hostname to IP", "Easy")
explain("Goal:  Build a dict mapping each hostname to its IP address.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Key = hostname, Value = ip.")
blank()
explain("Variable name:  hostname_to_ip")
blank()
header(">>> print(hostname_to_ip)")
header("{'nyc-rtr-01': '10.0.0.1', 'lon-sw-01': '10.1.0.1',")
header(" 'sin-fw-01': '10.2.0.1',  'ams-rtr-02': '10.3.0.1',")
header(" 'tok-sw-01': '10.4.0.1',  'syd-rtr-01': '10.5.0.1',")
header(" 'dub-fw-01': '10.6.0.1',  'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Map hostname to platform", "Easy")
explain("Goal:  Build a dict mapping each hostname to its platform.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Key = hostname, Value = platform.")
blank()
explain("Variable name:  hostname_to_platform")
blank()
header(">>> print(hostname_to_platform)")
header("{'nyc-rtr-01': 'IOS-XE', 'lon-sw-01': 'NX-OS',")
header(" 'sin-fw-01': 'ASA',     'ams-rtr-02': 'IOS-XE',")
header(" 'tok-sw-01': 'NX-OS',   'syd-rtr-01': 'IOS-XE',")
header(" 'dub-fw-01': 'ASA',     'mum-rtr-01': 'IOS-XE'}")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Count devices by status", "Easy")
explain("Goal:  Build a dict with two keys — 'up' and 'down' —")
explain("       each holding the count of devices with that status.")
blank()
explain("Rules:")
explain("  • Dict must have exactly two keys: 'up' and 'down'.")
explain("  • Values are integers.")
blank()
explain("Variable name:  status_count")
blank()
header(">>> print(status_count)")
header("{'up': 5, 'down': 3}")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Map hostname to IP for UP devices only", "Easy")
explain("Goal:  Build a dict mapping hostname to IP,")
explain("       but only for devices whose status is 'up'.")
blank()
explain("Rules:")
explain("  • Skip any device with status 'down'.")
explain("  • Key = hostname, Value = ip.")
blank()
explain("Variable name:  up_devices")
blank()
header(">>> print(up_devices)")
header("{'nyc-rtr-01': '10.0.0.1', 'sin-fw-01': '10.2.0.1',")
header(" 'ams-rtr-02': '10.3.0.1', 'syd-rtr-01': '10.5.0.1',")
header(" 'mum-rtr-01': '10.7.0.1'}")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Group hostnames by platform", "Medium")
explain("Goal:  Build a dict mapping each platform to a sorted")
explain("       list of hostnames that use it.")
blank()
explain("Rules:")
explain("  • Key = platform, Value = sorted list of hostnames.")
explain("  • Sort each list alphabetically.")
blank()
explain("Variable name:  platform_groups")
blank()
header(">>> print(platform_groups)")
header("{'IOS-XE': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01'],")
header(" 'NX-OS':  ['lon-sw-01', 'tok-sw-01'],")
header(" 'ASA':    ['dub-fw-01', 'sin-fw-01']}")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Map hostname to its config dict", "Medium")
explain("Goal:  Build a dict mapping each hostname to its")
explain("       nested 'config' dict.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = the config dict.")
explain("  • Each config dict has keys: ntp, dns, domain.")
blank()
explain("Variable name:  hostname_to_config")
blank()
header(">>> print(hostname_to_config['nyc-rtr-01'])")
header("{'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()
header(">>> print(hostname_to_config['lon-sw-01'])")
header("{'ntp': '10.1.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Map hostname to VLAN count", "Medium")
explain("Goal:  Build a dict mapping each hostname to the")
explain("       number of VLANs it has.")
blank()
explain("Rules:")
explain("  • Key = hostname, Value = integer count of vlans.")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  vlan_count_map")
blank()
header(">>> print(vlan_count_map)")
header("{'nyc-rtr-01': 3, 'lon-sw-01': 2, 'sin-fw-01': 3,")
header(" 'ams-rtr-02': 4, 'tok-sw-01': 2, 'syd-rtr-01': 3,")
header(" 'dub-fw-01': 3,  'mum-rtr-01': 4}")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Group hostnames by NTP server", "Medium")
explain("Goal:  Build a dict mapping each unique NTP server")
explain("       to a sorted list of hostnames using it.")
blank()
explain("Rules:")
explain("  • Each device's NTP is at d['config']['ntp'].")
explain("  • Key = NTP server IP, Value = sorted list of hostnames.")
blank()
explain("Variable name:  ntp_to_hostnames")
blank()
header(">>> print(ntp_to_hostnames)")
header("{'10.0.0.100': ['ams-rtr-02', 'dub-fw-01', 'nyc-rtr-01', 'sin-fw-01', 'syd-rtr-01'],")
header(" '10.1.0.100': ['lon-sw-01'],")
header(" '10.4.0.100': ['tok-sw-01'],")
header(" '10.7.0.100': ['mum-rtr-01']}")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Merge BASE config with each device config", "Hard")
explain("Goal:  Build a dict mapping each hostname to a merged")
explain("       config — BASE defaults overridden by the device's")
explain("       own config values.")
blank()
explain("Rules:")
explain("  • Start with this BASE dict for every device:")
explain("      BASE = {'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public'}")
explain("  • Merge each device's config on top — device values win.")
explain("  • Key = hostname, Value = merged config dict.")
blank()
explain("Variable name:  merged_configs")
blank()
header(">>> print(merged_configs['nyc-rtr-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.0.0.100'}")
blank()
header(">>> print(merged_configs['lon-sw-01'])")
header("{'dns': '8.8.8.8', 'domain': 'corp.net', 'snmp': 'public', 'ntp': '10.1.0.100'}")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Invert IP to hostname", "Hard")
explain("Goal:  Build a dict mapping each IP address to its hostname.")
blank()
explain("Rules:")
explain("  • This is the reverse of Task 1.")
explain("  • Key = ip, Value = hostname.")
explain("  • Include all 8 devices.")
blank()
explain("Variable name:  inverted_ip")
blank()
header(">>> print(inverted_ip)")
header("{'10.0.0.1': 'nyc-rtr-01', '10.1.0.1': 'lon-sw-01',")
header(" '10.2.0.1': 'sin-fw-01',  '10.3.0.1': 'ams-rtr-02',")
header(" '10.4.0.1': 'tok-sw-01',  '10.5.0.1': 'syd-rtr-01',")
header(" '10.6.0.1': 'dub-fw-01',  '10.7.0.1': 'mum-rtr-01'}")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Summarise devices by platform", "Hard")
explain("Goal:  Build a dict mapping each platform to a summary")
explain("       dict with three keys.")
blank()
explain("Rules:")
explain("  • Key = platform name.")
explain("  • Value = dict with exactly these three keys:")
explain("      'count'     — total number of devices on that platform")
explain("      'up_count'  — number of those devices that are 'up'")
explain("      'hostnames' — sorted list of all hostnames on that platform")
blank()
explain("Variable name:  platform_summary")
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

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Find devices with non-standard NTP", "Hard")
explain("Goal:  Build a dict mapping hostname to NTP server,")
explain("       but ONLY for devices whose NTP differs from GLOBAL_NTP.")
blank()
explain("Rules:")
explain(f"  • GLOBAL_NTP = '{GLOBAL_NTP}'")
explain("  • Skip any device whose NTP matches GLOBAL_NTP.")
explain("  • Key = hostname, Value = that device's NTP server IP.")
blank()
explain("Variable name:  ntp_diff")
blank()
header(">>> print(ntp_diff)")
header("{'lon-sw-01':  '10.1.0.100',")
header(" 'tok-sw-01':  '10.4.0.100',")
header(" 'mum-rtr-01': '10.7.0.100'}")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: dicts_solution.py")
explain("Remember to paste INVENTORY and GLOBAL_NTP at the top.")
blank()
explain("Tips by task:")
explain("  Task  1 — dict comprehension: {d['hostname']: d['ip'] for d in INVENTORY}")
explain("  Task  2 — same pattern, value is d['platform']")
explain("  Task  3 — sum() with generator expression for each status")
explain("  Task  4 — add if clause: if d['status'] == 'up'")
explain("  Task  5 — .setdefault(platform, []) then .append() and .sort()")
explain("  Task  6 — value is d['config'] directly")
explain("  Task  7 — value is len(d['vlans'])")
explain("  Task  8 — key is d['config']['ntp'], same grouping pattern as Task 5")
explain("  Task  9 — use {**BASE, **d['config']} to merge")
explain("  Task 10 — swap key/value: {d['ip']: d['hostname'] ...}")
explain("  Task 11 — unique platforms with set(), then build one summary dict each")
explain("  Task 12 — filter: if d['config']['ntp'] != GLOBAL_NTP")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# GRADE
# ═════════════════════════════════════════════════════════════════════════════
ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Tasks 1–4
    exp_h2ip   = {d["hostname"]: d["ip"] for d in INVENTORY}
    exp_h2plat = {d["hostname"]: d["platform"] for d in INVENTORY}
    exp_status = {
        "up":   sum(1 for d in INVENTORY if d["status"] == "up"),
        "down": sum(1 for d in INVENTORY if d["status"] == "down"),
    }
    exp_up = {d["hostname"]: d["ip"] for d in INVENTORY if d["status"] == "up"}

    # Tasks 5–8
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

    # Tasks 9–12
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

    # ── Run grade ──────────────────────────────────────────────────────────────
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