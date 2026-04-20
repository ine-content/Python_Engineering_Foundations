# filtering_transformation_challenges.py
# Filtering and Transformation Patterns — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
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
# DATA
# ─────────────────────────────────────────────────────────────────────────────
INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "up"},
            {"name": "Gi0/3", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "down"},
            {"name": "Gi0/1", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
            {"name": "Gi0/2", "vlan": 50, "state": "down"},
        ],
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "up"},
            {"name": "Gi0/1", "vlan": 30, "state": "up"},
            {"name": "Gi0/2", "vlan": 40, "state": "up"},
            {"name": "Gi0/3", "vlan": 50, "state": "up"},
        ],
    },
]

GLOBAL_NTP     = "10.0.0.100"
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"ft_solution_ch{challenge_num}.py"
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
        "INVENTORY":      INVENTORY,
        "GLOBAL_NTP":     GLOBAL_NTP,
        "RESERVED_VLANS": RESERVED_VLANS,
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
print(f"{BOLD}         FILTERING & TRANSFORMATION — CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses INVENTORY, GLOBAL_NTP, and RESERVED_VLANS.")
explain("Read the challenge, write your solution in the")
explain("correct file, then run this script to check it.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → ft_solution_ch1.py")
explain("  Challenge 2 (Medium) → ft_solution_ch2.py")
explain("  Challenge 3 (Hard)   → ft_solution_ch3.py")
blank()
explain("IMPORTANT: Copy the data shown on the next screen")
explain("into the TOP of each solution file.")
explain("It is printed with NO indentation — copy directly.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Copy this entire block into the TOP of each solution file.")
blank()
copyable("GLOBAL_NTP     = '10.0.0.100'")
copyable("RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
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
challenge_header(1, "Basic Filtering and Transformation", "Easy")

explain("Use list and dict comprehensions to filter and")
explain("transform INVENTORY into the following outputs.")
blank()

pause()

section("Task A")
explain("Create a list called 'up_ips' containing the IP")
explain("address of every device whose status is 'up'.")
blank()
header(">>> print(up_ips)")
header("['10.0.0.1', '10.2.0.1', '10.3.0.1', '10.5.0.1', '10.7.0.1']")
blank()

pause()

section("Task B")
explain("Create a list called 'enriched' — one dict per device.")
explain("Each dict must have:")
explain("  'hostname'   → the hostname")
explain("  'platform'   → the platform")
explain("  'vlan_count' → the number of VLANs")
explain("  'status'     → the status")
blank()
header(">>> print(enriched[0])")
header("{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'vlan_count': 3, 'status': 'up'}")
blank()
header(">>> print(len(enriched))")
header("8")
blank()

pause()

section("Task C")
explain("Create a dict called 'hostname_to_ntp' mapping each")
explain("hostname to its NTP server (from d['config']['ntp']).")
blank()
header(">>> print(hostname_to_ntp)")
header("{'nyc-rtr-01': '10.0.0.100', 'lon-sw-01': '10.1.0.100',")
header(" 'sin-fw-01': '10.0.0.100',  'ams-rtr-02': '10.0.0.100',")
header(" 'tok-sw-01': '10.4.0.100',  'syd-rtr-01': '10.0.0.100',")
header(" 'dub-fw-01': '10.0.0.100',  'mum-rtr-01': '10.7.0.100'}")
blank()

pause()

section("Task D")
explain("Create a list called 'custom_ntp_hosts' containing")
explain("the hostname of every device whose NTP server differs")
explain("from GLOBAL_NTP.")
blank()
header(">>> print(custom_ntp_hosts)")
header("['lon-sw-01', 'tok-sw-01', 'mum-rtr-01']")
blank()

pause()

explain("Write your solution in: ft_solution_ch1.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — [d['ip'] for d in INVENTORY if d['status']=='up']. Ch 2.1.")
explain("  Task B — [{**d fields, 'vlan_count': len(d['vlans'])} ...]. Ch 3.3.")
explain("  Task C — {d['hostname']: d['config']['ntp'] for d in INVENTORY}. Ch 3.1.")
explain("  Task D — filter where d['config']['ntp'] != GLOBAL_NTP. Ch 2.3.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    exp_up_ips = [d["ip"] for d in INVENTORY if d["status"] == "up"]

    exp_enriched = [
        {
            "hostname":   d["hostname"],
            "platform":   d["platform"],
            "vlan_count": len(d["vlans"]),
            "status":     d["status"],
        }
        for d in INVENTORY
    ]

    exp_h2ntp = {d["hostname"]: d["config"]["ntp"] for d in INVENTORY}

    exp_custom_ntp = [
        d["hostname"] for d in INVENTORY
        if d["config"]["ntp"] != GLOBAL_NTP
    ]

    grade(1, [
        (
            "Task A", "up_ips — IPs of all 'up' devices",
            ns.get("up_ips"), exp_up_ips,
            "See Chapter 2.1 — [d['ip'] for d in INVENTORY if d['status']=='up'].",
            "[d['ip'] for d in INVENTORY if d['status'] == 'up']",
            "up_ips",
        ),
        (
            "Task B", "enriched — all 8 devices with hostname/platform/vlan_count/status",
            ns.get("enriched"), exp_enriched,
            "See Chapter 3.3 — use len(d['vlans']) as vlan_count, keep only the 4 required fields.",
            "[{'hostname': d['hostname'], 'platform': d['platform'], 'vlan_count': len(d['vlans']), 'status': d['status']} for d in INVENTORY]",
            "enriched",
        ),
        (
            "Task C", "hostname_to_ntp — hostname → ntp server",
            ns.get("hostname_to_ntp"), exp_h2ntp,
            "See Chapter 3.1 — {d['hostname']: d['config']['ntp'] for d in INVENTORY}.",
            "{d['hostname']: d['config']['ntp'] for d in INVENTORY}",
            "hostname_to_ntp",
        ),
        (
            "Task D", "custom_ntp_hosts — hostnames with non-standard NTP",
            ns.get("custom_ntp_hosts"), exp_custom_ntp,
            "See Chapter 2.3 — filter where d['config']['ntp'] != GLOBAL_NTP.",
            "[d['hostname'] for d in INVENTORY if d['config']['ntp'] != GLOBAL_NTP]",
            "custom_ntp_hosts",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Grouping and Aggregation", "Medium")

explain("Use grouping, partitioning, and aggregation patterns")
explain("to analyse INVENTORY in deeper ways.")
blank()

pause()

section("Task A")
explain("Partition INVENTORY into two lists:")
explain("  'push_ready'    — up devices on IOS-XE or NX-OS")
explain("  'skip_devices'  — everything else")
explain("Each list contains only the hostnames (not full dicts).")
blank()
header(">>> print(push_ready)")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(skip_devices)")
header("['lon-sw-01', 'sin-fw-01', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

section("Task B")
explain("Create a dict called 'platform_groups' mapping each")
explain("platform to a sorted list of hostnames using it.")
blank()
header(">>> print(platform_groups)")
header("{'ASA':    ['dub-fw-01', 'sin-fw-01'],")
header(" 'IOS-XE': ['ams-rtr-02', 'mum-rtr-01', 'nyc-rtr-01', 'syd-rtr-01'],")
header(" 'NX-OS':  ['lon-sw-01', 'tok-sw-01']}")
blank()

pause()

section("Task C")
explain("Create a dict called 'platform_stats' mapping each")
explain("platform to a dict with:")
explain("  'total'    → number of devices on that platform")
explain("  'up_count' → number of those devices that are 'up'")
explain("  'avg_vlans'→ average number of VLANs (as a float)")
blank()
header(">>> print(platform_stats['IOS-XE'])")
header("{'total': 4, 'up_count': 4, 'avg_vlans': 3.5}")
blank()
header(">>> print(platform_stats['NX-OS'])")
header("{'total': 2, 'up_count': 0, 'avg_vlans': 2.0}")
blank()
header(">>> print(platform_stats['ASA'])")
header("{'total': 2, 'up_count': 1, 'avg_vlans': 2.5}")
blank()

pause()

section("Task D")
explain("Create a list called 'vlan_usage' — one dict per")
explain("unique VLAN across all devices, sorted by vlan ascending.")
explain("Each dict has:")
explain("  'vlan'         → the VLAN number")
explain("  'device_count' → number of devices that have it")
explain("  'hostnames'    → sorted list of those hostnames")
blank()
header(">>> for v in vlan_usage: print(v)")
header("{'vlan': 10, 'device_count': 5, 'hostnames': ['ams-rtr-02','dub-fw-01','lon-sw-01','nyc-rtr-01','syd-rtr-01']}")
header("{'vlan': 20, 'device_count': 5, 'hostnames': ['ams-rtr-02','lon-sw-01','mum-rtr-01','nyc-rtr-01','tok-sw-01']}")
header("{'vlan': 30, 'device_count': 5, 'hostnames': ['ams-rtr-02','dub-fw-01','mum-rtr-01','nyc-rtr-01','sin-fw-01']}")
header("{'vlan': 40, 'device_count': 4, 'hostnames': ['ams-rtr-02','mum-rtr-01','sin-fw-01','syd-rtr-01']}")
header("{'vlan': 50, 'device_count': 3, 'hostnames': ['mum-rtr-01','sin-fw-01','syd-rtr-01']}")
blank()

pause()

explain("Write your solution in: ft_solution_ch2.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — two separate comprehensions with different conditions. Ch 7.1.")
explain("  Task B — setdefault() + append() + sort, or comprehension over sorted platforms. Ch 7.2.")
explain("  Task C — get unique platforms first, then build one dict per platform. Ch 8.2.")
explain("  Task D — collect unique vlans with set(), sort, then build one dict per vlan. Ch 8.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    exp_push = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS")
    ]
    exp_skip = [
        d["hostname"] for d in INVENTORY
        if not (d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS"))
    ]

    platforms_u = sorted(set(d["platform"] for d in INVENTORY))
    exp_pg = {
        p: sorted(d["hostname"] for d in INVENTORY if d["platform"] == p)
        for p in platforms_u
    }

    exp_ps = {}
    for p in platforms_u:
        devices_p = [d for d in INVENTORY if d["platform"] == p]
        exp_ps[p] = {
            "total":     len(devices_p),
            "up_count":  sum(1 for d in devices_p if d["status"] == "up"),
            "avg_vlans": sum(len(d["vlans"]) for d in devices_p) / len(devices_p),
        }

    all_vlans = sorted(set(v for d in INVENTORY for v in d["vlans"]))
    exp_vu = [
        {
            "vlan":         v,
            "device_count": sum(1 for d in INVENTORY if v in d["vlans"]),
            "hostnames":    sorted(d["hostname"] for d in INVENTORY if v in d["vlans"]),
        }
        for v in all_vlans
    ]

    grade(2, [
        (
            "Task A", "push_ready and skip_devices — correct partition",
            (ns.get("push_ready"), ns.get("skip_devices")),
            (exp_push, exp_skip),
            "See Chapter 7.1 — two comprehensions: one with 'up and IOS-XE/NX-OS', one negated.",
            "push_ready  = [d['hostname'] for d in INVENTORY if d['status']=='up' and d['platform'] in ('IOS-XE','NX-OS')]\nskip_devices = [d['hostname'] for d in INVENTORY if not (d['status']=='up' and d['platform'] in ('IOS-XE','NX-OS'))]",
            "(push_ready, skip_devices)",
        ),
        (
            "Task B", "platform_groups — platform → sorted list of hostnames",
            ns.get("platform_groups"), exp_pg,
            "See Chapter 7.2 — get unique platforms, then {p: sorted([...]) for p in platforms}.",
            "platforms = sorted(set(d['platform'] for d in INVENTORY))\nplatform_groups = {p: sorted(d['hostname'] for d in INVENTORY if d['platform']==p) for p in platforms}",
            "platform_groups",
        ),
        (
            "Task C", "platform_stats — platform → {total, up_count, avg_vlans}",
            ns.get("platform_stats"), exp_ps,
            "See Chapter 8.2 — filter per platform, then compute total/up_count/avg_vlans.",
            "platforms = sorted(set(d['platform'] for d in INVENTORY))\nplatform_stats = {p: {'total': sum(1 for d in INVENTORY if d['platform']==p), 'up_count': sum(1 for d in INVENTORY if d['platform']==p and d['status']=='up'), 'avg_vlans': sum(len(d['vlans']) for d in INVENTORY if d['platform']==p) / sum(1 for d in INVENTORY if d['platform']==p)} for p in platforms}",
            "platform_stats",
        ),
        (
            "Task D", "vlan_usage — sorted list of {vlan, device_count, hostnames}",
            ns.get("vlan_usage"), exp_vu,
            "See Chapter 8 — collect unique vlans with set(), sort, build one dict per vlan.",
            "all_vlans = sorted(set(v for d in INVENTORY for v in d['vlans']))\nvlan_usage = [{'vlan': v, 'device_count': sum(1 for d in INVENTORY if v in d['vlans']), 'hostnames': sorted(d['hostname'] for d in INVENTORY if v in d['vlans'])} for v in all_vlans]",
            "vlan_usage",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Pipelines and Nested Transformation", "Hard")

explain("Combine chaining, nested filtering, and transformation")
explain("pipelines to solve complex IaC analysis tasks.")
blank()

pause()

section("Task A")
explain("Build a multi-step pipeline. Starting from INVENTORY:")
blank()
explain("  Step 1 — Keep only devices that are 'up'")
explain("  Step 2 — Remove reserved VLANs from each device's vlan list")
explain("           RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
explain("  Step 3 — Keep only devices that still have at least one VLAN")
explain("           after reserved removal")
explain("  Step 4 — Transform each to: {'hostname', 'platform', 'clean_vlans'}")
blank()
explain("Store the final result in 'pipeline_result'.")
blank()
header(">>> for r in pipeline_result: print(r)")
header("{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [10, 20, 30]}")
header("{'hostname': 'sin-fw-01',  'platform': 'ASA',    'clean_vlans': [30, 40, 50]}")
header("{'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'clean_vlans': [10, 20, 30, 40]}")
header("{'hostname': 'syd-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [10, 40, 50]}")
header("{'hostname': 'mum-rtr-01', 'platform': 'IOS-XE', 'clean_vlans': [20, 30, 40, 50]}")
blank()

pause()

section("Task B")
explain("Using nested filtering and transformation, create a")
explain("list called 'device_report' — one dict per device.")
explain("Each dict has:")
explain("  'hostname'        → the hostname")
explain("  'status'          → the status")
explain("  'up_interfaces'   → list of interface names that are 'up'")
explain("  'down_interfaces' → list of interface names that are 'down'")
explain("  'all_up'          → True if ALL interfaces are 'up', else False")
blank()
header(">>> print(device_report[0])")
header("{'hostname': 'nyc-rtr-01', 'status': 'up',")
header(" 'up_interfaces': ['Gi0/0', 'Gi0/1'],")
header(" 'down_interfaces': ['Gi0/2'],")
header(" 'all_up': False}")
blank()
header(">>> print(device_report[3])")
header("{'hostname': 'ams-rtr-02', 'status': 'up',")
header(" 'up_interfaces': ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3'],")
header(" 'down_interfaces': [],")
header(" 'all_up': True}")
blank()

pause()

section("Task C")
explain("Create a list called 'interface_flat' — one dict per")
explain("interface across ALL devices (flatten the nested structure).")
explain("Only include interfaces whose state is 'up'.")
explain("Each dict has: 'hostname', 'iface', 'vlan', 'platform'")
explain("Order: outer loop follows INVENTORY, inner follows interfaces.")
blank()
header(">>> print(interface_flat[0])")
header("{'hostname': 'nyc-rtr-01', 'iface': 'Gi0/0', 'vlan': 10, 'platform': 'IOS-XE'}")
blank()
header(">>> print(len(interface_flat))")
header("15")
blank()

pause()

section("Task D")
explain("Create a dict called 'vlan_platform_map' mapping each")
explain("unique VLAN to a sorted list of UNIQUE platforms that")
explain("have that VLAN on at least one UP interface.")
explain("Only count interfaces whose state is 'up'.")
blank()
header(">>> print(vlan_platform_map)")
header("{10: ['ASA', 'IOS-XE', 'NX-OS'],")
header(" 20: ['IOS-XE', 'NX-OS'],")
header(" 30: ['ASA', 'IOS-XE'],")
header(" 40: ['IOS-XE'],")
header(" 50: ['IOS-XE']}")
blank()
explain("Note: tok-sw-01 (NX-OS) has vlans 20 and 30 but both")
explain("interfaces are DOWN — so NX-OS should NOT appear for")
explain("vlans 20 or 30 in this output.")
blank()

pause()

explain("Write your solution in: ft_solution_ch3.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — 4 separate steps using list comprehensions. Ch 6.1.")
explain("  Task B — [i['name'] for i in d['interfaces'] if i['state']=='up']. Ch 9.1.")
explain("  Task C — flatten with nested comprehension, filter state=='up'. Ch 9.2.")
explain("  Task D — collect unique vlans from UP interfaces only,")
explain("           then for each vlan collect unique platforms. Ch 9.2.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    # Task A
    step1 = [d for d in INVENTORY if d["status"] == "up"]
    step2 = [{**d, "vlans": [v for v in d["vlans"] if v not in RESERVED_VLANS]}
             for d in step1]
    step3 = [d for d in step2 if d["vlans"]]
    exp_pipeline = [
        {"hostname": d["hostname"], "platform": d["platform"], "clean_vlans": d["vlans"]}
        for d in step3
    ]

    # Task B
    exp_report = [
        {
            "hostname":        d["hostname"],
            "status":          d["status"],
            "up_interfaces":   [i["name"] for i in d["interfaces"] if i["state"] == "up"],
            "down_interfaces": [i["name"] for i in d["interfaces"] if i["state"] == "down"],
            "all_up":          all(i["state"] == "up" for i in d["interfaces"]),
        }
        for d in INVENTORY
    ]

    # Task C
    exp_flat = [
        {
            "hostname": d["hostname"],
            "iface":    i["name"],
            "vlan":     i["vlan"],
            "platform": d["platform"],
        }
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "up"
    ]

    # Task D
    up_ifaces = [
        (d["platform"], i["vlan"])
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "up"
    ]
    unique_vlans_d = sorted(set(vlan for _, vlan in up_ifaces))
    exp_vpm = {
        v: sorted(set(p for p, vlan in up_ifaces if vlan == v))
        for v in unique_vlans_d
    }

    grade(3, [
        (
            "Task A", "pipeline_result — 4-step filtered and transformed list",
            ns.get("pipeline_result"), exp_pipeline,
            "See Chapter 6.1 — 4 separate steps: filter up, remove reserved vlans, filter non-empty, reshape.",
            "step1 = [d for d in INVENTORY if d['status']=='up']\nstep2 = [{**d,'vlans':[v for v in d['vlans'] if v not in RESERVED_VLANS]} for d in step1]\nstep3 = [d for d in step2 if d['vlans']]\npipeline_result = [{'hostname':d['hostname'],'platform':d['platform'],'clean_vlans':d['vlans']} for d in step3]",
            "pipeline_result",
        ),
        (
            "Task B", "device_report — all 8 devices with up/down interface lists and all_up flag",
            ns.get("device_report"), exp_report,
            "See Chapter 9.1 — build up_interfaces and down_interfaces with inner comprehensions.",
            "[{'hostname':d['hostname'],'status':d['status'],'up_interfaces':[i['name'] for i in d['interfaces'] if i['state']=='up'],'down_interfaces':[i['name'] for i in d['interfaces'] if i['state']=='down'],'all_up':all(i['state']=='up' for i in d['interfaces'])} for d in INVENTORY]",
            "device_report",
        ),
        (
            "Task C", "interface_flat — flattened up-only interfaces across all devices",
            ns.get("interface_flat"), exp_flat,
            "See Chapter 9.2 — nested comprehension: for d in INVENTORY for i in d['interfaces'] if i['state']=='up'.",
            "[{'hostname':d['hostname'],'iface':i['name'],'vlan':i['vlan'],'platform':d['platform']} for d in INVENTORY for i in d['interfaces'] if i['state']=='up']",
            "interface_flat",
        ),
        (
            "Task D", "vlan_platform_map — vlan → sorted unique platforms on UP interfaces only",
            ns.get("vlan_platform_map"), exp_vpm,
            "See Chapter 9.2 — collect (platform, vlan) pairs from UP interfaces only, then group by vlan.",
            "up_ifaces = [(d['platform'],i['vlan']) for d in INVENTORY for i in d['interfaces'] if i['state']=='up']\nvlans = sorted(set(v for _,v in up_ifaces))\nvlan_platform_map = {v: sorted(set(p for p,vlan in up_ifaces if vlan==v)) for v in vlans}",
            "vlan_platform_map",
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