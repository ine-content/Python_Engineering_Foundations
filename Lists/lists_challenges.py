# lists_challenges.py
# Python Lists — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in a file called: solution.py
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

import os
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
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30],      "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10, 20],           "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30, 40, 50],       "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10, 20, 30, 40],  "ip": "10.3.0.1"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [20, 30],           "ip": "10.4.0.1"},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10, 40, 50],       "ip": "10.5.0.1"},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down", "vlans": [10, 20, 30],       "ip": "10.6.0.1"},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [20, 30, 40, 50],  "ip": "10.7.0.1"},
]

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    """Load and execute the student's solution file."""
    import sys
    filename = f"lists_solution_ch{challenge_num}.py"

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
        fail(f"Your script raised an error:")
        print()
        traceback.print_exc()
        blank()
        return None


def check(task_label, label, actual, expected, hint_text, solution_code, var_name):
    """Run one assertion. Return True if passed."""
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
        if isinstance(expected, list) and len(expected) > 4:
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
    """
    checks — list of (label, actual, expected, hint_text, solution_code, var_name)
    Returns True if all passed.
    """
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
print()
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON LISTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses the same device INVENTORY list.")
explain("Read the challenge, write your solution in the")
explain("correct file, then run this script to check it.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → lists_solution_ch1.py")
explain("  Challenge 2 (Medium) → lists_solution_ch2.py")
explain("  Challenge 3 (Hard)   → lists_solution_ch3.py")
blank()
explain("IMPORTANT: Copy the INVENTORY list shown on the")
explain("next screen into the TOP of each solution file.")
explain("Your solution will not work without it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW INVENTORY
# ═════════════════════════════════════════════════════════════════════════════
section("The INVENTORY You Will Work With")

explain("Copy this entire block into the TOP of each solution file.")
explain("It is printed with NO indentation so you can copy it directly.")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
explain("Your solution file should start like this:")
blank()
copyable("# lists_solution_ch1.py")
copyable("")
copyable("INVENTORY = [")
copyable("    {'hostname': 'nyc-rtr-01', ...},")
copyable("    ...")
copyable("]")
copyable("")
copyable("# your code below")
copyable("all_hostnames = [...]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Device Report", "Easy")

explain("Using the INVENTORY list, produce the following:")
blank()

section("Task A")
explain("Create a list called 'all_hostnames' containing")
explain("the hostname of every device in INVENTORY.")
explain("Order must match the original INVENTORY order.")
blank()
header(">>> print(all_hostnames)")
header("['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02', 'tok-sw-01', 'syd-rtr-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

section("Task B")
explain("Create a list called 'up_hostnames' containing")
explain("the hostname of every device whose status is 'up'.")
explain("Order must match the original INVENTORY order.")
blank()
header(">>> print(up_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task C")
explain("Create a variable called 'down_count' containing")
explain("the number of devices whose status is 'down'.")
blank()
header(">>> print(down_count)")
header("3")
blank()

pause()

section("Task D")
explain("Create a list called 'platforms' containing the")
explain("platform of every device — UPPERCASE — in INVENTORY order.")
blank()
header(">>> print(platforms)")
header("['IOS-XE', 'NX-OS', 'ASA', 'IOS-XE', 'NX-OS', 'IOS-XE', 'ASA', 'IOS-XE']")
blank()

pause()

explain("Write your solution in: lists_solution_ch1.py")
explain("Remember to paste INVENTORY at the top of your file.")
explain("Use list comprehensions where possible.")
blank()
explain("Example structure:")
blank()
header("# lists_solution_ch1.py")
header("")
header("all_hostnames = [...]")
header("up_hostnames  = [...]")
header("down_count    = ...")
header("platforms     = [...]")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    expected_all  = [d["hostname"] for d in INVENTORY]
    expected_up   = [d["hostname"] for d in INVENTORY if d["status"] == "up"]
    expected_down = sum(1 for d in INVENTORY if d["status"] == "down")
    expected_plat = [d["platform"].upper() for d in INVENTORY]

    grade(1, [
        (
            "Task A",
            "all_hostnames — all 8 hostnames in order",
            ns.get("all_hostnames"),
            expected_all,
            "See Chapter 8 — list comprehensions.",
            "all_hostnames = [d['hostname'] for d in INVENTORY]",
            "all_hostnames",
        ),
        (
            "Task B",
            "up_hostnames — only devices with status 'up'",
            ns.get("up_hostnames"),
            expected_up,
            "See Chapter 8.2 — filtering with an if clause.",
            "up_hostnames = [d['hostname'] for d in INVENTORY if d['status'] == 'up']",
            "up_hostnames",
        ),
        (
            "Task C",
            "down_count — number of devices that are down",
            ns.get("down_count"),
            expected_down,
            "See Chapter 9 — sum() with a generator expression.",
            "down_count = sum(1 for d in INVENTORY if d['status'] == 'down')",
            "down_count",
        ),
        (
            "Task D",
            "platforms — platform of every device, uppercase",
            ns.get("platforms"),
            expected_plat,
            "See Chapter 8.1 — call .upper() inside the comprehension.",
            "platforms = [d['platform'].upper() for d in INVENTORY]",
            "platforms",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "VLAN Analysis", "Medium")

explain("Using the INVENTORY list, produce the following.")
explain("Each device has a 'vlans' key containing a list of VLAN IDs.")
blank()

pause()

section("Task A")
explain("Create a list called 'all_vlans' containing every VLAN ID")
explain("from every device — flattened into a single list.")
explain("Order: outer loop follows INVENTORY order,")
explain("inner loop follows each device's vlan list order.")
blank()
header(">>> print(all_vlans)")
header("[10, 20, 30, 10, 20, 30, 40, 50, 10, 20, 30, 40, 20, 30, 10, 40, 50, 10, 20, 30, 20, 30, 40, 50]")
blank()

pause()

section("Task B")
explain("Create a list called 'unique_vlans' containing every")
explain("unique VLAN ID across all devices, sorted ascending.")
blank()
header(">>> print(unique_vlans)")
header("[10, 20, 30, 40, 50]")
blank()

pause()

section("Task C")
explain("Create a list called 'vlan_30_devices' containing the")
explain("hostname of every device that has VLAN 30 in its vlan list.")
blank()
header(">>> print(vlan_30_devices)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

section("Task D")
explain("Create a list called 'vlan_summary' — a list of dicts.")
explain("Each dict has 'hostname' and 'vlan_count' keys.")
explain("Only include devices that have MORE THAN 2 VLANs.")
explain("Sort by vlan_count descending.")
blank()
header(">>> print(vlan_summary)")
header("[{'hostname': 'mum-rtr-01', 'vlan_count': 4}, {'hostname': 'ams-rtr-02', 'vlan_count': 4},")
header(" {'hostname': 'sin-fw-01', 'vlan_count': 3},  {'hostname': 'nyc-rtr-01', 'vlan_count': 3},")
header(" {'hostname': 'syd-rtr-01', 'vlan_count': 3}, {'hostname': 'dub-fw-01', 'vlan_count': 3}]")
blank()

pause()

explain("Write your solution in: lists_solution_ch2.py")
explain("Remember to paste INVENTORY at the top of your file.")
blank()
explain("Tips:")
explain("  Task A — nested list comprehension (Chapter 8.5)")
explain("  Task B — sorted(set(...))")
explain("  Task C — 'if 30 in d[\"vlans\"]' in comprehension")
explain("  Task D — build dicts in comprehension, then sort")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    expected_all_vlans    = [v for d in INVENTORY for v in d["vlans"]]
    expected_unique       = sorted(set(expected_all_vlans))
    expected_vlan30       = [d["hostname"] for d in INVENTORY if 30 in d["vlans"]]
    expected_summary_raw  = [{"hostname": d["hostname"], "vlan_count": len(d["vlans"])}
                              for d in INVENTORY if len(d["vlans"]) > 2]
    expected_summary      = sorted(expected_summary_raw,
                                   key=lambda x: x["vlan_count"], reverse=True)

    grade(2, [
        (
            "Task A",
            "all_vlans — every vlan from every device, flattened",
            ns.get("all_vlans"),
            expected_all_vlans,
            "See Chapter 8.5 — nested list comprehension.",
            "all_vlans = [v for d in INVENTORY for v in d['vlans']]",
            "all_vlans",
        ),
        (
            "Task B",
            "unique_vlans — unique vlans sorted ascending",
            ns.get("unique_vlans"),
            expected_unique,
            "See Chapter 6 and 9 — wrap in set() to deduplicate, then sorted().",
            "unique_vlans = sorted(set(all_vlans))",
            "unique_vlans",
        ),
        (
            "Task C",
            "vlan_30_devices — hostnames of devices with vlan 30",
            ns.get("vlan_30_devices"),
            expected_vlan30,
            "See Chapter 4.1 — use the 'in' operator to check membership.",
            "vlan_30_devices = [d['hostname'] for d in INVENTORY if 30 in d['vlans']]",
            "vlan_30_devices",
        ),
        (
            "Task D",
            "vlan_summary — dicts with hostname+vlan_count, >2 vlans, sorted desc",
            ns.get("vlan_summary"),
            expected_summary,
            "See Chapter 6.2 — build dicts in comprehension, filter >2, sort with key=lambda.",
            "vlan_summary = sorted([{'hostname': d['hostname'], 'vlan_count': len(d['vlans'])} for d in INVENTORY if len(d['vlans']) > 2], key=lambda x: x['vlan_count'], reverse=True)",
            "vlan_summary",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Config Generator", "Hard")

explain("Using the INVENTORY list, produce the following.")
explain("This challenge combines everything — iteration,")
explain("filtering, transformation, comprehensions, and sorting.")
blank()

pause()

section("Task A")
explain("Create a list called 'config_blocks' — one config")
explain("string per device that is 'up' AND platform 'IOS-XE'.")
explain("Each string must follow this exact format:")
blank()
header("  'hostname <hostname>\\n ntp server 10.0.0.100\\n ip domain-name corp.net'")
blank()
explain("Only include devices that are up AND IOS-XE.")
explain("Order must match INVENTORY order.")
blank()
header(">>> for block in config_blocks: print(block)")
header("hostname nyc-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname ams-rtr-02")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname syd-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
header("hostname mum-rtr-01")
header(" ntp server 10.0.0.100")
header(" ip domain-name corp.net")
blank()

pause()

section("Task B")
explain("Create a list called 'ip_hostname_pairs' — a list of")
explain("strings in the format 'ip --> hostname', for ALL devices,")
explain("sorted alphabetically by hostname.")
blank()
header(">>> print(ip_hostname_pairs)")
header("['10.3.0.1 --> ams-rtr-02', '10.6.0.1 --> dub-fw-01', '10.1.0.1 --> lon-sw-01',")
header(" '10.7.0.1 --> mum-rtr-01', '10.0.0.1 --> nyc-rtr-01', '10.2.0.1 --> sin-fw-01',")
header(" '10.5.0.1 --> syd-rtr-01', '10.4.0.1 --> tok-sw-01']")
blank()

pause()

section("Task C")
explain("Create a list called 'numbered_inventory' — a list of")
explain("strings that number each device. Include ALL devices.")
explain("Number starts at 1. Format: 'N. hostname (platform) — status'")
blank()
header(">>> print(numbered_inventory)")
header("['1. nyc-rtr-01 (IOS-XE) — up',   '2. lon-sw-01 (NX-OS) — down',")
header(" '3. sin-fw-01 (ASA) — up',    '4. ams-rtr-02 (IOS-XE) — up',")
header(" '5. tok-sw-01 (NX-OS) — down', '6. syd-rtr-01 (IOS-XE) — up',")
header(" '7. dub-fw-01 (ASA) — down',  '8. mum-rtr-01 (IOS-XE) — up']")
blank()

pause()

section("Task D")
explain("Create a list called 'platform_groups' — a list of dicts,")
explain("one per unique platform, sorted alphabetically by platform.")
explain("Each dict has:")
explain("  'platform' — the platform name")
explain("  'count'    — how many devices have that platform")
explain("  'up_count' — how many of those devices are 'up'")
blank()
header(">>> print(platform_groups)")
header("[{'platform': 'ASA',    'count': 2, 'up_count': 1},")
header(" {'platform': 'IOS-XE', 'count': 4, 'up_count': 4},")
header(" {'platform': 'NX-OS',  'count': 2, 'up_count': 0}]")
blank()

pause()

explain("Write your solution in: lists_solution_ch3.py")
explain("Remember to paste INVENTORY at the top of your file.")
blank()
explain("Tips:")
explain("  Task A — f-string with \\n, double filter in comprehension")
explain("  Task B — f-string, sorted() with key=lambda")
explain("  Task C — enumerate(INVENTORY, start=1)")
explain("  Task D — find unique platforms first with set(),")
explain("           then build one dict per platform using")
explain("           a comprehension over sorted platforms")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    expected_configs = [
        f"hostname {d['hostname']}\n ntp server 10.0.0.100\n ip domain-name corp.net"
        for d in INVENTORY
        if d["status"] == "up" and d["platform"] == "IOS-XE"
    ]

    expected_pairs = sorted(
        [f"{d['ip']} --> {d['hostname']}" for d in INVENTORY],
        key=lambda s: s.split(" --> ")[1]
    )

    expected_numbered = [
        f"{i}. {d['hostname']} ({d['platform']}) — {d['status']}"
        for i, d in enumerate(INVENTORY, start=1)
    ]

    platforms_unique = sorted(set(d["platform"] for d in INVENTORY))
    expected_groups  = [
        {
            "platform": p,
            "count":    sum(1 for d in INVENTORY if d["platform"] == p),
            "up_count": sum(1 for d in INVENTORY if d["platform"] == p and d["status"] == "up"),
        }
        for p in platforms_unique
    ]

    grade(3, [
        (
            "Task A",
            "config_blocks — 4 IOS-XE + up devices, correct format",
            ns.get("config_blocks"),
            expected_configs,
            "See Chapter 8.3 — double filter with 'and', use f-string with \\n.",
            "config_blocks = [f\"hostname {d['hostname']}\\n ntp server 10.0.0.100\\n ip domain-name corp.net\" for d in INVENTORY if d['status'] == 'up' and d['platform'] == 'IOS-XE']",
            "config_blocks",
        ),
        (
            "Task B",
            "ip_hostname_pairs — all 8 devices, sorted by hostname",
            ns.get("ip_hostname_pairs"),
            expected_pairs,
            "See Chapter 6 — build f-string then sorted() with key=lambda.",
            "ip_hostname_pairs = sorted([f\"{d['ip']} --> {d['hostname']}\" for d in INVENTORY], key=lambda s: s.split(' --> ')[1])",
            "ip_hostname_pairs",
        ),
        (
            "Task C",
            "numbered_inventory — all 8, numbered from 1, correct format",
            ns.get("numbered_inventory"),
            expected_numbered,
            "See Chapter 3.2 — use enumerate(INVENTORY, start=1).",
            "numbered_inventory = [f\"{i}. {d['hostname']} ({d['platform']}) — {d['status']}\" for i, d in enumerate(INVENTORY, start=1)]",
            "numbered_inventory",
        ),
        (
            "Task D",
            "platform_groups — 3 platforms, count + up_count, sorted",
            ns.get("platform_groups"),
            expected_groups,
            "See Chapter 8 and 9 — get unique platforms with set(), sort, build one dict per platform.",
            "platforms_unique = sorted(set(d['platform'] for d in INVENTORY))\nplatform_groups = [{'platform': p, 'count': sum(1 for d in INVENTORY if d['platform'] == p), 'up_count': sum(1 for d in INVENTORY if d['platform'] == p and d['status'] == 'up')} for p in platforms_unique]",
            "platform_groups",
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