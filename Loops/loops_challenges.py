# loops_challenges.py
# Python Loops — Student Challenges
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
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
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
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "down"},
            {"name": "Gi0/1", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
            {"name": "Gi0/2", "vlan": 50, "state": "down"},
        ],
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "up"},
            {"name": "Gi0/1", "vlan": 30, "state": "up"},
            {"name": "Gi0/2", "vlan": 40, "state": "up"},
            {"name": "Gi0/3", "vlan": 50, "state": "up"},
        ],
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"loops_solution_ch{challenge_num}.py"
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

    namespace = {"INVENTORY": INVENTORY}
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


def grade(challenge_num, checks):
    blank()
    section("Grading your solution...")
    passed = 0
    for args in checks:
        if check(*args):
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
print(f"{BOLD}         LOOPS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses the same INVENTORY list.")
explain("Read the challenge, write your solution in the")
explain("correct file, then run this script to check it.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → loops_solution_ch1.py")
explain("  Challenge 2 (Medium) → loops_solution_ch2.py")
explain("  Challenge 3 (Hard)   → loops_solution_ch3.py")
blank()
explain("IMPORTANT: Copy INVENTORY shown on the next screen")
explain("into the TOP of each solution file.")
explain("It is printed with NO indentation — copy directly.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("Each device has: hostname, platform, status, ip,")
explain("vlans (list), and interfaces (list of dicts).")
blank()
explain("Copy this entire block into the TOP of each solution file.")
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
challenge_header(1, "Basic Loops and Accumulators", "Easy")

explain("Use for loops and accumulator patterns to")
explain("process INVENTORY and produce the following.")
blank()

pause()

section("Task A")
explain("Using a for loop and a counter, create a variable")
explain("called 'platform_counts' — a dict mapping each")
explain("platform to how many times it appears in INVENTORY.")
blank()
header(">>> print(platform_counts)")
header("{'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
blank()

pause()

section("Task B")
explain("Using enumerate(), create a list called 'numbered'")
explain("— one string per device, numbered starting at 1.")
explain("Format: 'N. hostname (platform)'")
blank()
header(">>> print(numbered)")
header("['1. nyc-rtr-01 (IOS-XE)', '2. lon-sw-01 (NX-OS)',")
header(" '3. sin-fw-01 (ASA)',     '4. ams-rtr-02 (IOS-XE)',")
header(" '5. tok-sw-01 (NX-OS)',   '6. syd-rtr-01 (IOS-XE)',")
header(" '7. dub-fw-01 (ASA)',     '8. mum-rtr-01 (IOS-XE)']")
blank()

pause()

section("Task C")
explain("Using a for loop over INVENTORY, collect all unique")
explain("VLAN IDs across all devices into a sorted list")
explain("called 'all_vlans'. Each device has a 'vlans' key.")
blank()
header(">>> print(all_vlans)")
header("[10, 20, 30, 40, 50]")
blank()

pause()

section("Task D")
explain("Using zip(), pair up INVENTORY with this list of")
explain("regions to produce a list called 'device_regions'")
explain("— one string per pair.")
explain("Format: 'hostname → region'")
blank()
header("regions = ['us-east','eu-west','ap-se','eu-central',")
header("           'ap-ne','au-east','eu-west','ap-south']")
blank()
header(">>> print(device_regions)")
header("['nyc-rtr-01 → us-east', 'lon-sw-01 → eu-west',")
header(" 'sin-fw-01 → ap-se',    'ams-rtr-02 → eu-central',")
header(" 'tok-sw-01 → ap-ne',    'syd-rtr-01 → au-east',")
header(" 'dub-fw-01 → eu-west',  'mum-rtr-01 → ap-south']")
blank()

pause()

explain("Write your solution in: loops_solution_ch1.py")
explain("Remember to paste INVENTORY at the top.")
blank()
explain("Tips:")
explain("  Task A — counts[p] = counts.get(p, 0) + 1. See Ch 7.4.")
explain("  Task B — enumerate(INVENTORY, start=1). See Ch 4.1.")
explain("  Task C — build a set() then sorted(). See Ch 7.3.")
explain("  Task D — zip(INVENTORY, regions). See Ch 4.2.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    exp_counts = {}
    for d in INVENTORY:
        exp_counts[d["platform"]] = exp_counts.get(d["platform"], 0) + 1

    exp_numbered = [
        f"{i}. {d['hostname']} ({d['platform']})"
        for i, d in enumerate(INVENTORY, start=1)
    ]

    seen = set()
    for d in INVENTORY:
        for v in d["vlans"]:
            seen.add(v)
    exp_vlans = sorted(seen)

    regions = ["us-east","eu-west","ap-se","eu-central",
               "ap-ne","au-east","eu-west","ap-south"]
    exp_regions = [
        f"{d['hostname']} → {r}"
        for d, r in zip(INVENTORY, regions)
    ]

    grade(1, [
        (
            "Task A", "platform_counts — platform → count",
            ns.get("platform_counts"), exp_counts,
            "See Chapter 7.4 — counts[p] = counts.get(p, 0) + 1.",
            "platform_counts = {}\nfor d in INVENTORY:\n    p = d['platform']\n    platform_counts[p] = platform_counts.get(p, 0) + 1",
            "platform_counts",
        ),
        (
            "Task B", "numbered — 'N. hostname (platform)' strings from 1",
            ns.get("numbered"), exp_numbered,
            "See Chapter 4.1 — enumerate(INVENTORY, start=1).",
            "numbered = [f'{i}. {d[\"hostname\"]} ({d[\"platform\"]})' for i, d in enumerate(INVENTORY, start=1)]",
            "numbered",
        ),
        (
            "Task C", "all_vlans — sorted unique VLANs across all devices",
            ns.get("all_vlans"), exp_vlans,
            "See Chapter 7.3 — build a set(), nested loop over d['vlans'], then sorted().",
            "seen = set()\nfor d in INVENTORY:\n    for v in d['vlans']:\n        seen.add(v)\nall_vlans = sorted(seen)",
            "all_vlans",
        ),
        (
            "Task D", "device_regions — 'hostname → region' strings via zip()",
            ns.get("device_regions"), exp_regions,
            "See Chapter 4.2 — zip(INVENTORY, regions) gives (device, region) pairs.",
            "regions = ['us-east','eu-west','ap-se','eu-central','ap-ne','au-east','eu-west','ap-south']\ndevice_regions = [f\"{d['hostname']} → {r}\" for d, r in zip(INVENTORY, regions)]",
            "device_regions",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Nested Loops and Loop Control", "Medium")

explain("Use nested loops, break, continue, and for...else")
explain("to process INVENTORY at the interface level.")
blank()

pause()

section("Task A")
explain("Using nested loops, create a list called 'down_report'")
explain("— one string per interface that is 'down' across ALL")
explain("devices. Format: 'hostname | iface_name | vlan'")
explain("Order: outer loop follows INVENTORY, inner follows interfaces.")
blank()
header(">>> print(down_report)")
header("['nyc-rtr-01 | Gi0/2 | 30',")
header(" 'lon-sw-01  | Gi0/1 | 20',")
header(" 'tok-sw-01  | Gi0/0 | 20',")
header(" 'tok-sw-01  | Gi0/1 | 30',")
header(" 'syd-rtr-01 | Gi0/2 | 50',")
header(" 'dub-fw-01  | Gi0/1 | 20']")
blank()

pause()

section("Task B")
explain("Using a for loop with break and for...else,")
explain("find the FIRST device in INVENTORY whose platform")
explain("is 'NX-OS' and status is 'up'.")
blank()
explain("Store the hostname in 'first_nxos_up'.")
explain("If no such device exists store None.")
blank()
header(">>> print(first_nxos_up)")
header("None")
blank()
explain("(All NX-OS devices in INVENTORY are down —")
explain(" so the answer is None.)")
blank()

pause()

section("Task C")
explain("Using a for loop with continue, create a list called")
explain("'interface_summary' — one dict per interface that is")
explain("'up' AND whose vlan is greater than 20.")
explain("Each dict: {'hostname': ..., 'iface': ..., 'vlan': ...}")
explain("Skip all other interfaces using continue.")
blank()
header(">>> print(interface_summary)")
header("[{'hostname': 'nyc-rtr-01', 'iface': 'Gi0/2', 'vlan': 30},")
header(" {'hostname': 'sin-fw-01',  'iface': 'Gi0/0', 'vlan': 30},")
header(" {'hostname': 'sin-fw-01',  'iface': 'Gi0/1', 'vlan': 40},")
header(" {'hostname': 'ams-rtr-02', 'iface': 'Gi0/2', 'vlan': 30},")
header(" {'hostname': 'ams-rtr-02', 'iface': 'Gi0/3', 'vlan': 40},")
header(" {'hostname': 'syd-rtr-01', 'iface': 'Gi0/1', 'vlan': 40},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/1', 'vlan': 30},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/2', 'vlan': 40},")
header(" {'hostname': 'mum-rtr-01', 'iface': 'Gi0/3', 'vlan': 50}]")
blank()

pause()

section("Task D")
explain("Using a for loop and a running max tracker,")
explain("find the device with the MOST interfaces.")
explain("Store the hostname in 'most_interfaces_host' and")
explain("the count in 'most_interfaces_count'.")
blank()
header(">>> print(most_interfaces_host)")
header("'ams-rtr-02'")
blank()
header(">>> print(most_interfaces_count)")
header("4")
blank()

pause()

explain("Write your solution in: loops_solution_ch2.py")
explain("Remember to paste INVENTORY at the top.")
blank()
explain("Tips:")
explain("  Task A — nested for: for d in INVENTORY, for iface in d['interfaces'].")
explain("  Task B — for loop + if + break + else. See Ch 6.2.")
explain("  Task C — nested loops, continue if state!='up' or vlan<=20. See Ch 6.1.")
explain("  Task D — track max_val and max_host in loop. See Ch 7.5.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    exp_down = [
        f"{d['hostname']} | {i['name']} | {i['vlan']}"
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "down"
    ]

    exp_first_nxos = None
    for d in INVENTORY:
        if d["platform"] == "NX-OS" and d["status"] == "up":
            exp_first_nxos = d["hostname"]
            break

    exp_iface_summary = []
    for d in INVENTORY:
        for i in d["interfaces"]:
            if i["state"] != "up":
                continue
            if i["vlan"] <= 20:
                continue
            exp_iface_summary.append({
                "hostname": d["hostname"],
                "iface":    i["name"],
                "vlan":     i["vlan"],
            })

    exp_max_host  = ""
    exp_max_count = 0
    for d in INVENTORY:
        if len(d["interfaces"]) > exp_max_count:
            exp_max_count = len(d["interfaces"])
            exp_max_host  = d["hostname"]

    grade(2, [
        (
            "Task A", "down_report — 'hostname | iface | vlan' for all down interfaces",
            ns.get("down_report"), exp_down,
            "See Chapter 5.2 — nested loops: for d in INVENTORY, for i in d['interfaces'], if i['state']=='down'.",
            "down_report = [f\"{d['hostname']} | {i['name']} | {i['vlan']}\" for d in INVENTORY for i in d['interfaces'] if i['state']=='down']",
            "down_report",
        ),
        (
            "Task B", "first_nxos_up — hostname of first NX-OS + up device (or None)",
            ns.get("first_nxos_up"), exp_first_nxos,
            "See Chapter 6.2 — for loop + if + break. Use for...else to set None if not found.",
            "first_nxos_up = None\nfor d in INVENTORY:\n    if d['platform']=='NX-OS' and d['status']=='up':\n        first_nxos_up = d['hostname']\n        break",
            "first_nxos_up",
        ),
        (
            "Task C", "interface_summary — dicts for up interfaces with vlan > 20",
            ns.get("interface_summary"), exp_iface_summary,
            "See Chapter 6.1 — nested loops with continue to skip state!='up' or vlan<=20.",
            "interface_summary = []\nfor d in INVENTORY:\n    for i in d['interfaces']:\n        if i['state'] != 'up': continue\n        if i['vlan'] <= 20: continue\n        interface_summary.append({'hostname': d['hostname'], 'iface': i['name'], 'vlan': i['vlan']})",
            "interface_summary",
        ),
        (
            "Task D", "most_interfaces_host and most_interfaces_count",
            (ns.get("most_interfaces_host"), ns.get("most_interfaces_count")),
            (exp_max_host, exp_max_count),
            "See Chapter 7.5 — track max_count and max_host in a loop with if len(d['interfaces']) > max_count.",
            "max_host = ''\nmax_count = 0\nfor d in INVENTORY:\n    if len(d['interfaces']) > max_count:\n        max_count = len(d['interfaces'])\n        max_host = d['hostname']\nmost_interfaces_host = max_host\nmost_interfaces_count = max_count",
            "(most_interfaces_host, most_interfaces_count)",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Advanced Loop Patterns", "Hard")

explain("Combine chunking, deduplication, while loops,")
explain("and sliding window to solve real IaC problems.")
blank()

pause()

section("Task A")
explain("Chunk INVENTORY into batches of 3 using a for loop")
explain("with range(). Create a list called 'batches' where")
explain("each item is a list of hostnames in that batch.")
blank()
header(">>> print(batches)")
header("[['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01'],")
header(" ['ams-rtr-02', 'tok-sw-01', 'syd-rtr-01'],")
header(" ['dub-fw-01',  'mum-rtr-01']]")
blank()

pause()

section("Task B")
explain("The following list has duplicate entries.")
explain("Using a for loop with a 'seen' set, deduplicate")
explain("it while PRESERVING the original order.")
explain("Store the result in 'unique_vlans_ordered'.")
blank()
header("vlan_feed = [10, 30, 10, 20, 50, 30, 40, 20, 10, 50]")
blank()
header(">>> print(unique_vlans_ordered)")
header("[10, 30, 20, 50, 40]")
blank()

pause()

section("Task C")
explain("Using a while loop, simulate a retry mechanism.")
explain("You have a queue of devices to connect to.")
explain("Each attempt pops the first device off the queue.")
explain("If the device name starts with 'nyc' — connection succeeds.")
explain("Otherwise — it fails and is added to 'failed_devices'.")
explain("Stop when the queue is empty.")
blank()
explain("Use this queue:")
blank()
header("queue = ['lon-sw-01', 'nyc-rtr-01', 'sin-fw-01', 'nyc-sw-01']")
blank()
explain("Create 'failed_devices' — list of devices that failed.")
explain("Create 'success_devices' — list of devices that succeeded.")
blank()
header(">>> print(failed_devices)")
header("['lon-sw-01', 'sin-fw-01']")
blank()
header(">>> print(success_devices)")
header("['nyc-rtr-01', 'nyc-sw-01']")
blank()

pause()

section("Task D")
explain("Using a sliding window (consecutive pairs), create")
explain("a list called 'vlan_gaps' — one dict per adjacent")
explain("pair of VLANs in this sorted list:")
blank()
header("sorted_vlans = [10, 20, 30, 40, 50, 100, 200]")
blank()
explain("Each dict has:")
explain("  'from_vlan' → first VLAN in the pair")
explain("  'to_vlan'   → second VLAN in the pair")
explain("  'gap'       → difference between them")
blank()
header(">>> for g in vlan_gaps: print(g)")
header("{'from_vlan': 10,  'to_vlan': 20,  'gap': 10}")
header("{'from_vlan': 20,  'to_vlan': 30,  'gap': 10}")
header("{'from_vlan': 30,  'to_vlan': 40,  'gap': 10}")
header("{'from_vlan': 40,  'to_vlan': 50,  'gap': 10}")
header("{'from_vlan': 50,  'to_vlan': 100, 'gap': 50}")
header("{'from_vlan': 100, 'to_vlan': 200, 'gap': 100}")
blank()

pause()

explain("Write your solution in: loops_solution_ch3.py")
explain("Remember to paste INVENTORY at the top.")
blank()
explain("Tips:")
explain("  Task A — range(0, len(INVENTORY), 3), slice hostnames. See Ch 9.1.")
explain("  Task B — seen=set(), if v not in seen: unique.append(v); seen.add(v). See Ch 9.4.")
explain("  Task C — while queue: device = queue.pop(0), then if/else. See Ch 3.3.")
explain("  Task D — range(len(sorted_vlans)-1), access [i] and [i+1]. See Ch 9.2.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    chunk_size = 3
    hostnames = [d["hostname"] for d in INVENTORY]
    exp_batches = [
        hostnames[i:i+chunk_size]
        for i in range(0, len(hostnames), chunk_size)
    ]

    vlan_feed = [10, 30, 10, 20, 50, 30, 40, 20, 10, 50]
    seen_v = set()
    exp_unique = []
    for v in vlan_feed:
        if v not in seen_v:
            exp_unique.append(v)
            seen_v.add(v)

    queue = ["lon-sw-01", "nyc-rtr-01", "sin-fw-01", "nyc-sw-01"]
    exp_failed  = []
    exp_success = []
    q_copy = queue.copy()
    while q_copy:
        device = q_copy.pop(0)
        if device.startswith("nyc"):
            exp_success.append(device)
        else:
            exp_failed.append(device)

    sorted_vlans = [10, 20, 30, 40, 50, 100, 200]
    exp_gaps = [
        {
            "from_vlan": sorted_vlans[i],
            "to_vlan":   sorted_vlans[i+1],
            "gap":       sorted_vlans[i+1] - sorted_vlans[i],
        }
        for i in range(len(sorted_vlans) - 1)
    ]

    grade(3, [
        (
            "Task A", "batches — INVENTORY hostnames chunked into groups of 3",
            ns.get("batches"), exp_batches,
            "See Chapter 9.1 — range(0, len(INVENTORY), 3), slice with [i:i+3].",
            "hostnames = [d['hostname'] for d in INVENTORY]\nbatches = [hostnames[i:i+3] for i in range(0, len(hostnames), 3)]",
            "batches",
        ),
        (
            "Task B", "unique_vlans_ordered — deduplicated, order preserved",
            ns.get("unique_vlans_ordered"), exp_unique,
            "See Chapter 9.4 — seen=set(), for v in vlan_feed: if v not in seen: append+add.",
            "seen = set()\nunique_vlans_ordered = []\nfor v in [10,30,10,20,50,30,40,20,10,50]:\n    if v not in seen:\n        unique_vlans_ordered.append(v)\n        seen.add(v)",
            "unique_vlans_ordered",
        ),
        (
            "Task C", "failed_devices and success_devices from while queue loop",
            (ns.get("failed_devices"), ns.get("success_devices")),
            (exp_failed, exp_success),
            "See Chapter 3.3 — while queue: device=queue.pop(0), if device.startswith('nyc') → success else failed.",
            "queue=['lon-sw-01','nyc-rtr-01','sin-fw-01','nyc-sw-01']\nfailed_devices=[]\nsuccess_devices=[]\nwhile queue:\n    d=queue.pop(0)\n    if d.startswith('nyc'): success_devices.append(d)\n    else: failed_devices.append(d)",
            "(failed_devices, success_devices)",
        ),
        (
            "Task D", "vlan_gaps — sliding window dicts with from/to/gap",
            ns.get("vlan_gaps"), exp_gaps,
            "See Chapter 9.2 — range(len(sorted_vlans)-1), access [i] and [i+1].",
            "sorted_vlans=[10,20,30,40,50,100,200]\nvlan_gaps=[{'from_vlan':sorted_vlans[i],'to_vlan':sorted_vlans[i+1],'gap':sorted_vlans[i+1]-sorted_vlans[i]} for i in range(len(sorted_vlans)-1)]",
            "vlan_gaps",
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