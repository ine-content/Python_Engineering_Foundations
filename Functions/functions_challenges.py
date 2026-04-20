# functions_challenges.py
# Python Functions — Student Challenges
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
    filename = f"functions_solution_ch{challenge_num}.py"
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
print(f"{BOLD}         FUNCTIONS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses INVENTORY, GLOBAL_NTP, and RESERVED_VLANS.")
explain("You will write FUNCTIONS — not just variables.")
explain("The grader calls your functions with test data.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → functions_solution_ch1.py")
explain("  Challenge 2 (Medium) → functions_solution_ch2.py")
explain("  Challenge 3 (Hard)   → functions_solution_ch3.py")
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
challenge_header(1, "Basic Functions", "Easy")

explain("Write the following four functions.")
explain("The grader will call each one and check the result.")
blank()

pause()

section("Task A")
explain("Write a function called 'classify_device(hostname)'")
explain("that takes a hostname string and returns:")
blank()
explain("  'router'   if 'rtr' is in the hostname")
explain("  'switch'   if 'sw'  is in the hostname")
explain("  'firewall' if 'fw'  is in the hostname")
explain("  'unknown'  otherwise")
blank()
header(">>> print(classify_device('nyc-rtr-01'))")
header("'router'")
blank()
header(">>> print(classify_device('lon-sw-01'))")
header("'switch'")
blank()
header(">>> print(classify_device('sin-fw-01'))")
header("'firewall'")
blank()

pause()

section("Task B")
explain("Write a function called 'get_up_devices(inventory)'")
explain("that takes a list of device dicts and returns a list")
explain("of hostnames whose status is 'up'.")
blank()
header(">>> print(get_up_devices(INVENTORY))")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task C")
explain("Write a function called 'count_by_platform(inventory)'")
explain("that takes a list of device dicts and returns a dict")
explain("mapping each platform to how many devices use it.")
blank()
header(">>> print(count_by_platform(INVENTORY))")
header("{'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
blank()

pause()

section("Task D")
explain("Write a function called 'enrich_device(device)'")
explain("that takes a single device dict and returns a NEW dict")
explain("with all original fields PLUS these computed fields:")
blank()
explain("  'vlan_count'  → number of VLANs")
explain("  'iface_count' → number of interfaces")
explain("  'device_type' → result of classify_device(hostname)")
blank()
header(">>> print(enrich_device(INVENTORY[0]))")
header("{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up',")
header(" 'ip': '10.0.0.1', 'vlans': [10,20,30], 'config': {...},")
header(" 'interfaces': [...],")
header(" 'vlan_count': 3, 'iface_count': 3, 'device_type': 'router'}")
blank()

pause()

explain("Write your solution in: functions_solution_ch1.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — def classify_device(hostname): if/elif/else on 'rtr' in hostname.")
explain("  Task B — def get_up_devices(inventory): list comprehension with filter.")
explain("  Task C — def count_by_platform(inventory): counter dict pattern.")
explain("  Task D — def enrich_device(device): return {**device, 'vlan_count': ...}")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    classify_fn  = ns.get("classify_device")
    get_up_fn    = ns.get("get_up_devices")
    count_fn     = ns.get("count_by_platform")
    enrich_fn    = ns.get("enrich_device")

    # Task A — test classify_device
    classify_results = None
    if classify_fn:
        classify_results = [
            classify_fn("nyc-rtr-01"),
            classify_fn("lon-sw-01"),
            classify_fn("sin-fw-01"),
            classify_fn("ams-rtr-02"),
            classify_fn("abc-xyz-01"),
        ]
    exp_classify = ["router", "switch", "firewall", "router", "unknown"]

    # Task B — test get_up_devices
    get_up_results = get_up_fn(INVENTORY) if get_up_fn else None
    exp_up = [d["hostname"] for d in INVENTORY if d["status"] == "up"]

    # Task C — test count_by_platform
    count_results = count_fn(INVENTORY) if count_fn else None
    exp_counts = {}
    for d in INVENTORY:
        exp_counts[d["platform"]] = exp_counts.get(d["platform"], 0) + 1

    # Task D — test enrich_device
    def _enrich(device):
        h = device["hostname"]
        if "rtr" in h:    dtype = "router"
        elif "sw" in h:   dtype = "switch"
        elif "fw" in h:   dtype = "firewall"
        else:             dtype = "unknown"
        return {
            **device,
            "vlan_count":  len(device["vlans"]),
            "iface_count": len(device["interfaces"]),
            "device_type": dtype,
        }

    enrich_results = enrich_fn(INVENTORY[0]) if enrich_fn else None
    exp_enrich     = _enrich(INVENTORY[0])

    grade(1, [
        (
            "Task A", "classify_device — router/switch/firewall/unknown",
            classify_results, exp_classify,
            "See Chapter 1.2 — if 'rtr' in hostname: return 'router' elif 'sw' ... elif 'fw' ...",
            "def classify_device(hostname):\n    if 'rtr' in hostname: return 'router'\n    elif 'sw' in hostname: return 'switch'\n    elif 'fw' in hostname: return 'firewall'\n    return 'unknown'",
            "classify_device results",
        ),
        (
            "Task B", "get_up_devices — list of hostnames with status 'up'",
            get_up_results, exp_up,
            "See Chapter 2.2 — return [d['hostname'] for d in inventory if d['status']=='up'].",
            "def get_up_devices(inventory):\n    return [d['hostname'] for d in inventory if d['status'] == 'up']",
            "get_up_devices(INVENTORY)",
        ),
        (
            "Task C", "count_by_platform — platform → count dict",
            count_results, exp_counts,
            "See Chapter 3 — use counts.get(p, 0) + 1 pattern inside a loop.",
            "def count_by_platform(inventory):\n    counts = {}\n    for d in inventory:\n        p = d['platform']\n        counts[p] = counts.get(p, 0) + 1\n    return counts",
            "count_by_platform(INVENTORY)",
        ),
        (
            "Task D", "enrich_device — original dict + vlan_count, iface_count, device_type",
            enrich_results, exp_enrich,
            "See Chapter 3.3 — return {**device, 'vlan_count': len(device['vlans']), ...}",
            "def enrich_device(device):\n    return {**device, 'vlan_count': len(device['vlans']), 'iface_count': len(device['interfaces']), 'device_type': classify_device(device['hostname'])}",
            "enrich_device(INVENTORY[0])",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Parameters and Return Values", "Medium")

explain("Write functions that use default parameters,")
explain("return multiple values, and use guard clauses.")
blank()

pause()

section("Task A")
explain("Write a function called 'get_devices_by_platform'")
explain("with this signature:")
blank()
header("def get_devices_by_platform(inventory, platform, status=None):")
blank()
explain("Returns a list of hostnames where platform matches.")
explain("If 'status' is provided, also filter by status.")
explain("If 'status' is None (default), return all for that platform.")
blank()
header(">>> print(get_devices_by_platform(INVENTORY, 'IOS-XE'))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(get_devices_by_platform(INVENTORY, 'IOS-XE', status='up'))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(get_devices_by_platform(INVENTORY, 'NX-OS', status='down'))")
header("['lon-sw-01', 'tok-sw-01']")
blank()

pause()

section("Task B")
explain("Write a function called 'validate_device'")
explain("with this signature:")
blank()
header("def validate_device(device, global_ntp=GLOBAL_NTP):")
blank()
explain("Use guard clauses (early return). Check in order:")
explain("  1. status != 'up'                → (False, 'device is down')")
explain("  2. platform not in supported list → (False, 'unsupported platform')")
explain("     supported: IOS-XE, NX-OS, ASA, IOS-XR")
explain("  3. no vlans configured            → (False, 'no vlans')")
explain("  4. ntp differs from global_ntp   → (False, 'custom ntp')")
explain("  all pass                          → (True,  'valid')")
blank()
header(">>> print(validate_device(INVENTORY[0]))")
header("(True, 'valid')")
blank()
header(">>> print(validate_device(INVENTORY[1]))")
header("(False, 'device is down')")
blank()
header(">>> print(validate_device(INVENTORY[7]))")
header("(False, 'custom ntp')")
blank()

pause()

section("Task C")
explain("Write a function called 'partition_by_status(inventory)'")
explain("that returns TWO lists as a tuple:")
explain("  (up_hostnames, down_hostnames)")
blank()
header(">>> up, down = partition_by_status(INVENTORY)")
header(">>> print(up)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(down)")
header("['lon-sw-01', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

section("Task D")
explain("Write a function called 'generate_ntp_config'")
explain("with this signature:")
blank()
header("def generate_ntp_config(hostname, *ntp_servers, prefer_first=True):")
blank()
explain("Returns a multi-line config string.")
explain("Each NTP server gets a line: 'ntp server <ip>'")
explain("If prefer_first=True, add ' prefer' to the first server only.")
blank()
header(">>> print(generate_ntp_config('nyc-rtr-01', '10.0.0.100', '10.0.0.101'))")
header("ntp server 10.0.0.100 prefer")
header("ntp server 10.0.0.101")
blank()
header(">>> print(generate_ntp_config('lon-sw-01', '10.0.0.100', prefer_first=False))")
header("ntp server 10.0.0.100")
blank()

pause()

explain("Write your solution in: functions_solution_ch2.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — def func(inventory, platform, status=None): then filter.")
explain("  Task B — def validate_device(device, global_ntp=GLOBAL_NTP): guard clauses.")
explain("  Task C — def partition(...): return up_list, down_list (tuple).")
explain("  Task D — def func(hostname, *ntp_servers, prefer_first=True): iterate servers.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    by_plat_fn   = ns.get("get_devices_by_platform")
    validate_fn  = ns.get("validate_device")
    partition_fn = ns.get("partition_by_status")
    ntp_cfg_fn   = ns.get("generate_ntp_config")

    # Task A
    byp_all  = by_plat_fn(INVENTORY, "IOS-XE") if by_plat_fn else None
    byp_up   = by_plat_fn(INVENTORY, "IOS-XE", status="up") if by_plat_fn else None
    byp_down = by_plat_fn(INVENTORY, "NX-OS",  status="down") if by_plat_fn else None
    byp_result = (byp_all, byp_up, byp_down)

    exp_byp_all  = [d["hostname"] for d in INVENTORY if d["platform"] == "IOS-XE"]
    exp_byp_up   = [d["hostname"] for d in INVENTORY if d["platform"] == "IOS-XE" and d["status"] == "up"]
    exp_byp_down = [d["hostname"] for d in INVENTORY if d["platform"] == "NX-OS"  and d["status"] == "down"]
    exp_byp = (exp_byp_all, exp_byp_up, exp_byp_down)

    # Task B
    def _validate(device, global_ntp=GLOBAL_NTP):
        if device["status"] != "up":                                  return (False, "device is down")
        if device["platform"] not in ("IOS-XE","NX-OS","ASA","IOS-XR"): return (False, "unsupported platform")
        if not device.get("vlans"):                                   return (False, "no vlans")
        if device.get("config", {}).get("ntp") != global_ntp:        return (False, "custom ntp")
        return (True, "valid")

    val_results = None
    if validate_fn:
        val_results = [validate_fn(d) for d in INVENTORY]
    exp_val = [_validate(d) for d in INVENTORY]

    # Task C
    part_result = None
    if partition_fn:
        part_result = partition_fn(INVENTORY)
    exp_up   = [d["hostname"] for d in INVENTORY if d["status"] == "up"]
    exp_down = [d["hostname"] for d in INVENTORY if d["status"] == "down"]
    exp_part = (exp_up, exp_down)

    # Task D
    ntp_r1 = ntp_cfg_fn("nyc-rtr-01", "10.0.0.100", "10.0.0.101") if ntp_cfg_fn else None
    ntp_r2 = ntp_cfg_fn("lon-sw-01",  "10.0.0.100", prefer_first=False) if ntp_cfg_fn else None
    ntp_result = (ntp_r1, ntp_r2)
    exp_ntp1 = "ntp server 10.0.0.100 prefer\nntp server 10.0.0.101"
    exp_ntp2 = "ntp server 10.0.0.100"
    exp_ntp  = (exp_ntp1, exp_ntp2)

    grade(2, [
        (
            "Task A", "get_devices_by_platform — with optional status filter",
            byp_result, exp_byp,
            "See Chapter 3.3 — def func(inventory, platform, status=None): filter on platform and optionally status.",
            "def get_devices_by_platform(inventory, platform, status=None):\n    return [d['hostname'] for d in inventory if d['platform']==platform and (status is None or d['status']==status)]",
            "(all_iosxe, up_iosxe, down_nxos)",
        ),
        (
            "Task B", "validate_device — guard clauses returning (bool, msg)",
            val_results, exp_val,
            "See Chapter 5.3 — def validate_device(device, global_ntp=GLOBAL_NTP): early returns.",
            "def validate_device(device, global_ntp=GLOBAL_NTP):\n    if device['status']!='up': return (False,'device is down')\n    if device['platform'] not in ('IOS-XE','NX-OS','ASA','IOS-XR'): return (False,'unsupported platform')\n    if not device.get('vlans'): return (False,'no vlans')\n    if device.get('config',{}).get('ntp')!=global_ntp: return (False,'custom ntp')\n    return (True,'valid')",
            "[validate_device(d) for d in INVENTORY]",
        ),
        (
            "Task C", "partition_by_status — returns (up_list, down_list) tuple",
            part_result, exp_part,
            "See Chapter 5.2 — return up, down as a tuple.",
            "def partition_by_status(inventory):\n    up   = [d['hostname'] for d in inventory if d['status']=='up']\n    down = [d['hostname'] for d in inventory if d['status']=='down']\n    return up, down",
            "partition_by_status(INVENTORY)",
        ),
        (
            "Task D", "generate_ntp_config — *args servers, prefer_first keyword",
            ntp_result, exp_ntp,
            "See Chapter 4.1/4.3 — *ntp_servers collects all IPs, prefer_first=True adds ' prefer' to first.",
            "def generate_ntp_config(hostname, *ntp_servers, prefer_first=True):\n    lines = []\n    for i, s in enumerate(ntp_servers):\n        line = f'ntp server {s}'\n        if prefer_first and i == 0: line += ' prefer'\n        lines.append(line)\n    return '\\n'.join(lines)",
            "(ntp_result1, ntp_result2)",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "First-Class Functions and Pipelines", "Hard")

explain("Write functions that accept other functions as arguments,")
explain("build a processing pipeline, and use **kwargs for")
explain("flexible config generation.")
blank()

pause()

section("Task A")
explain("Write a function called 'apply_filter'")
explain("with this signature:")
blank()
header("def apply_filter(inventory, *filter_fns):")
blank()
explain("Apply ALL provided filter functions to the inventory.")
explain("A device is included only if it passes EVERY filter.")
explain("Returns a list of hostnames of matching devices.")
blank()
header(">>> is_up    = lambda d: d['status'] == 'up'")
header(">>> is_iosxe = lambda d: d['platform'] == 'IOS-XE'")
header(">>> has_vlans = lambda d: len(d['vlans']) > 2")
blank()
header(">>> print(apply_filter(INVENTORY, is_up))")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(apply_filter(INVENTORY, is_up, is_iosxe))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(apply_filter(INVENTORY, is_up, is_iosxe, has_vlans))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task B")
explain("Write a function called 'build_config'")
explain("with this signature:")
blank()
header("def build_config(hostname, **settings):")
blank()
explain("Returns a multi-line config string.")
explain("First line is always 'hostname <hostname>'.")
explain("Each keyword argument adds a line: '<key> <value>'")
explain("Keys with underscores are converted to spaces.")
explain("  e.g.  ip_domain_name='corp.net'  →  'ip domain-name corp.net'")
explain("  (replace _ with space, replace - with - as-is)")
blank()
header(">>> print(build_config('nyc-rtr-01', ntp='10.0.0.100', ip_domain_name='corp.net'))")
header("hostname nyc-rtr-01")
header("ntp 10.0.0.100")
header("ip domain-name corp.net")
blank()

pause()

section("Task C")
explain("Write a function called 'run_pipeline'")
explain("with this signature:")
blank()
header("def run_pipeline(data, *steps):")
blank()
explain("Apply each step function in sequence.")
explain("Each step receives the output of the previous step.")
explain("Returns the final result.")
blank()
header(">>> def step_filter_up(inv):")
header("...     return [d for d in inv if d['status'] == 'up']")
blank()
header(">>> def step_enrich(inv):")
header("...     return [{**d, 'vlan_count': len(d['vlans'])} for d in inv]")
blank()
header(">>> def step_hostnames(inv):")
header("...     return [d['hostname'] for d in inv]")
blank()
header(">>> result = run_pipeline(INVENTORY, step_filter_up, step_enrich, step_hostnames)")
header(">>> print(result)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task D")
explain("Write a function called 'make_sorter'")
explain("with this signature:")
blank()
header("def make_sorter(key_field, reverse=False):")
blank()
explain("Returns a NEW function that sorts a list of dicts")
explain("by the given key_field, in the given direction.")
explain("This is a function that RETURNS a function.")
blank()
header(">>> sort_by_hostname = make_sorter('hostname')")
header(">>> sort_by_vlans    = make_sorter('vlan_count', reverse=True)")
blank()
header(">>> enriched = [{**d, 'vlan_count': len(d['vlans'])} for d in INVENTORY]")
blank()
header(">>> sorted_names = sort_by_hostname(INVENTORY)")
header(">>> print([d['hostname'] for d in sorted_names])")
header("['ams-rtr-02', 'dub-fw-01', 'lon-sw-01', 'mum-rtr-01',")
header(" 'nyc-rtr-01', 'sin-fw-01', 'syd-rtr-01', 'tok-sw-01']")
blank()
header(">>> sorted_vlans = sort_by_vlans(enriched)")
header(">>> print([(d['hostname'], d['vlan_count']) for d in sorted_vlans])")
header("[('ams-rtr-02',4),('mum-rtr-01',4),('nyc-rtr-01',3),('sin-fw-01',3),")
header(" ('syd-rtr-01',3),('dub-fw-01',3),('lon-sw-01',2),('tok-sw-01',2)]")
blank()

pause()

explain("Write your solution in: functions_solution_ch3.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — def apply_filter(inventory, *filter_fns): all() with fns. Ch 4.1.")
explain("  Task B — def build_config(hostname, **settings): iterate settings.items(). Ch 4.2.")
explain("            key.replace('_', ' ') for the key formatting.")
explain("  Task C — def run_pipeline(data, *steps): loop applying each step. Ch 4.1, 8.2.")
explain("  Task D — def make_sorter(key, reverse): return lambda lst: sorted(...). Ch 8.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    apply_filter_fn = ns.get("apply_filter")
    build_config_fn = ns.get("build_config")
    run_pipeline_fn = ns.get("run_pipeline")
    make_sorter_fn  = ns.get("make_sorter")

    # Task A
    is_up_fn     = lambda d: d["status"] == "up"
    is_iosxe_fn  = lambda d: d["platform"] == "IOS-XE"
    has_vlans_fn = lambda d: len(d["vlans"]) > 2

    af1 = apply_filter_fn(INVENTORY, is_up_fn)                           if apply_filter_fn else None
    af2 = apply_filter_fn(INVENTORY, is_up_fn, is_iosxe_fn)             if apply_filter_fn else None
    af3 = apply_filter_fn(INVENTORY, is_up_fn, is_iosxe_fn, has_vlans_fn) if apply_filter_fn else None
    af_result = (af1, af2, af3)

    exp_af1 = [d["hostname"] for d in INVENTORY if d["status"] == "up"]
    exp_af2 = [d["hostname"] for d in INVENTORY if d["status"] == "up" and d["platform"] == "IOS-XE"]
    exp_af3 = [d["hostname"] for d in INVENTORY if d["status"] == "up" and d["platform"] == "IOS-XE" and len(d["vlans"]) > 2]
    exp_af  = (exp_af1, exp_af2, exp_af3)

    # Task B
    bc1 = build_config_fn("nyc-rtr-01", ntp="10.0.0.100", ip_domain_name="corp.net") if build_config_fn else None
    bc2 = build_config_fn("lon-sw-01",  dns="8.8.8.8") if build_config_fn else None
    bc_result = (bc1, bc2)

    def _build_config(hostname, **settings):
        lines = [f"hostname {hostname}"]
        for k, v in settings.items():
            lines.append(f"{k.replace('_', ' ')} {v}")
        return "\n".join(lines)

    exp_bc1 = _build_config("nyc-rtr-01", ntp="10.0.0.100", ip_domain_name="corp.net")
    exp_bc2 = _build_config("lon-sw-01",  dns="8.8.8.8")
    exp_bc  = (exp_bc1, exp_bc2)

    # Task C
    def step_filter_up(inv):   return [d for d in inv if d["status"] == "up"]
    def step_enrich(inv):      return [{**d, "vlan_count": len(d["vlans"])} for d in inv]
    def step_hostnames(inv):   return [d["hostname"] for d in inv]

    rp_result = run_pipeline_fn(INVENTORY, step_filter_up, step_enrich, step_hostnames) if run_pipeline_fn else None

    data = INVENTORY
    data = step_filter_up(data)
    data = step_enrich(data)
    exp_rp = step_hostnames(data)

    # Task D
    enriched_inv = [{**d, "vlan_count": len(d["vlans"])} for d in INVENTORY]

    sorted_names = make_sorter_fn("hostname")(INVENTORY) if make_sorter_fn else None
    sorted_vlans = make_sorter_fn("vlan_count", reverse=True)(enriched_inv) if make_sorter_fn else None
    ms_result = (
        [d["hostname"] for d in sorted_names] if sorted_names else None,
        [(d["hostname"], d["vlan_count"]) for d in sorted_vlans] if sorted_vlans else None,
    )

    exp_sn = sorted(INVENTORY, key=lambda d: d["hostname"])
    exp_sv = sorted(enriched_inv, key=lambda d: d["vlan_count"], reverse=True)
    exp_ms = (
        [d["hostname"] for d in exp_sn],
        [(d["hostname"], d["vlan_count"]) for d in exp_sv],
    )

    grade(3, [
        (
            "Task A", "apply_filter — *filter_fns all must pass",
            af_result, exp_af,
            "See Chapter 4.1 — *filter_fns is a tuple of functions. Use all(fn(d) for fn in filter_fns).",
            "def apply_filter(inventory, *filter_fns):\n    return [d['hostname'] for d in inventory if all(fn(d) for fn in filter_fns)]",
            "(apply_filter results)",
        ),
        (
            "Task B", "build_config — **settings with underscore-to-space key conversion",
            bc_result, exp_bc,
            "See Chapter 4.2 — iterate settings.items(), format key with k.replace('_',' ').",
            "def build_config(hostname, **settings):\n    lines = [f'hostname {hostname}']\n    for k, v in settings.items():\n        lines.append(f'{k.replace(\"_\",\" \")} {v}')\n    return '\\n'.join(lines)",
            "(build_config results)",
        ),
        (
            "Task C", "run_pipeline — *steps applied in sequence",
            rp_result, exp_rp,
            "See Chapter 8.2 and 4.1 — result = data; for step in steps: result = step(result); return result.",
            "def run_pipeline(data, *steps):\n    result = data\n    for step in steps:\n        result = step(result)\n    return result",
            "run_pipeline result",
        ),
        (
            "Task D", "make_sorter — returns a sort function for given key_field",
            ms_result, exp_ms,
            "See Chapter 8.1 — def make_sorter(key_field, reverse=False): return lambda lst: sorted(lst, key=lambda d: d[key_field], reverse=reverse).",
            "def make_sorter(key_field, reverse=False):\n    return lambda lst: sorted(lst, key=lambda d: d[key_field], reverse=reverse)",
            "(sorted_names, sorted_vlans)",
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