# conditionals_challenges.py
# Python Conditionals — Student Challenges
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
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"conditionals_solution_ch{challenge_num}.py"
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
print(f"{BOLD}         CONDITIONALS — STUDENT CHALLENGES{RESET}")
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
explain("  Challenge 1 (Easy)   → conditionals_solution_ch1.py")
explain("  Challenge 2 (Medium) → conditionals_solution_ch2.py")
explain("  Challenge 3 (Hard)   → conditionals_solution_ch3.py")
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
challenge_header(1, "Basic Conditionals", "Easy")

explain("Use if/elif/else, comparison operators, and 'in'")
explain("to classify and label devices from INVENTORY.")
blank()

pause()

section("Task A")
explain("Create a list called 'device_labels' — one string")
explain("per device. Each string must classify the device")
explain("by its hostname using these rules:")
blank()
explain("  hostname contains 'rtr' → 'Router: <hostname>'")
explain("  hostname contains 'sw'  → 'Switch: <hostname>'")
explain("  hostname contains 'fw'  → 'Firewall: <hostname>'")
explain("  anything else           → 'Unknown: <hostname>'")
blank()
header(">>> print(device_labels)")
header("['Router: nyc-rtr-01', 'Switch: lon-sw-01', 'Firewall: sin-fw-01',")
header(" 'Router: ams-rtr-02', 'Switch: tok-sw-01', 'Router: syd-rtr-01',")
header(" 'Firewall: dub-fw-01', 'Router: mum-rtr-01']")
blank()

pause()

section("Task B")
explain("Create a list called 'platform_class' — one string")
explain("per device using these rules:")
blank()
explain("  platform is 'IOS-XE' or 'NX-OS' → 'switching-routing'")
explain("  platform is 'ASA'                → 'security'")
explain("  anything else                    → 'other'")
blank()
header(">>> print(platform_class)")
header("['switching-routing', 'switching-routing', 'security',")
header(" 'switching-routing', 'switching-routing', 'switching-routing',")
header(" 'security', 'switching-routing']")
blank()

pause()

section("Task C")
explain("Create a list called 'vlan_status' — one string")
explain("per device describing its VLAN situation:")
blank()
explain("  device has no VLANs              → 'no-vlans'")
explain("  device has exactly 1 VLAN        → 'single-vlan'")
explain("  device has 2 or 3 VLANs          → 'few-vlans'")
explain("  device has 4 or more VLANs       → 'many-vlans'")
blank()
header(">>> print(vlan_status)")
header("['few-vlans', 'few-vlans', 'few-vlans', 'many-vlans',")
header(" 'few-vlans', 'few-vlans', 'few-vlans', 'many-vlans']")
blank()

pause()

section("Task D")
explain("Create a list called 'ntp_check' — one string per device:")
blank()
explain("  device NTP matches GLOBAL_NTP → 'standard'")
explain("  device NTP differs            → 'custom'")
blank()
header(">>> print(ntp_check)")
header("['standard', 'custom', 'standard', 'standard',")
header(" 'custom', 'standard', 'standard', 'custom']")
blank()

pause()

explain("Write your solution in: conditionals_solution_ch1.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — if/elif/elif/else inside a list comprehension or loop.")
explain("  Task B — use 'in' to check multiple platforms: platform in ('IOS-XE','NX-OS').")
explain("  Task C — check len(d['vlans']) with if/elif/elif/else.")
explain("  Task D — compare d['config']['ntp'] with GLOBAL_NTP.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    def _label(d):
        h = d["hostname"]
        if "rtr" in h:   return f"Router: {h}"
        elif "sw" in h:  return f"Switch: {h}"
        elif "fw" in h:  return f"Firewall: {h}"
        else:            return f"Unknown: {h}"

    def _pclass(d):
        if d["platform"] in ("IOS-XE", "NX-OS"): return "switching-routing"
        elif d["platform"] == "ASA":              return "security"
        else:                                     return "other"

    def _vstatus(d):
        n = len(d["vlans"])
        if n == 0:        return "no-vlans"
        elif n == 1:      return "single-vlan"
        elif n <= 3:      return "few-vlans"
        else:             return "many-vlans"

    def _ntp(d):
        return "standard" if d["config"]["ntp"] == GLOBAL_NTP else "custom"

    exp_labels  = [_label(d)   for d in INVENTORY]
    exp_pclass  = [_pclass(d)  for d in INVENTORY]
    exp_vstatus = [_vstatus(d) for d in INVENTORY]
    exp_ntp     = [_ntp(d)     for d in INVENTORY]

    grade(1, [
        (
            "Task A", "device_labels — Router/Switch/Firewall/Unknown prefix",
            ns.get("device_labels"), exp_labels,
            "See Chapter 2.3 — use 'in' to check hostname: 'rtr' in hostname.",
            "device_labels = []\nfor d in INVENTORY:\n    h = d['hostname']\n    if 'rtr' in h: device_labels.append(f'Router: {h}')\n    elif 'sw' in h: device_labels.append(f'Switch: {h}')\n    elif 'fw' in h: device_labels.append(f'Firewall: {h}')\n    else: device_labels.append(f'Unknown: {h}')",
            "device_labels",
        ),
        (
            "Task B", "platform_class — switching-routing / security / other",
            ns.get("platform_class"), exp_pclass,
            "See Chapter 3.3 — use 'in' with a tuple: d['platform'] in ('IOS-XE', 'NX-OS').",
            "platform_class = ['switching-routing' if d['platform'] in ('IOS-XE','NX-OS') else 'security' if d['platform']=='ASA' else 'other' for d in INVENTORY]",
            "platform_class",
        ),
        (
            "Task C", "vlan_status — no-vlans/single-vlan/few-vlans/many-vlans",
            ns.get("vlan_status"), exp_vstatus,
            "See Chapter 1.2 — use if/elif/elif/else on len(d['vlans']).",
            "vlan_status = []\nfor d in INVENTORY:\n    n = len(d['vlans'])\n    if n == 0: vlan_status.append('no-vlans')\n    elif n == 1: vlan_status.append('single-vlan')\n    elif n <= 3: vlan_status.append('few-vlans')\n    else: vlan_status.append('many-vlans')",
            "vlan_status",
        ),
        (
            "Task D", "ntp_check — standard / custom",
            ns.get("ntp_check"), exp_ntp,
            "See Chapter 6.2 — ternary: 'standard' if d['config']['ntp'] == GLOBAL_NTP else 'custom'.",
            "ntp_check = ['standard' if d['config']['ntp'] == GLOBAL_NTP else 'custom' for d in INVENTORY]",
            "ntp_check",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Boolean Logic and Truthy", "Medium")

explain("Use boolean operators, truthy/falsy checks, and")
explain("combined conditions to produce the following.")
blank()

pause()

section("Task A")
explain("Create a list called 'push_ready' containing the")
explain("hostname of every device that meets ALL of these:")
blank()
explain("  status is 'up'")
explain("  platform is 'IOS-XE' or 'NX-OS'")
explain("  has at least one VLAN configured")
blank()
header(">>> print(push_ready)")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

section("Task B")
explain("Create a list called 'needs_review' containing the")
explain("hostname of every device that meets ANY of these:")
blank()
explain("  status is 'down'")
explain("  has no VLANs configured")
explain("  NTP differs from GLOBAL_NTP")
blank()
header(">>> print(needs_review)")
header("['lon-sw-01', 'tok-sw-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

section("Task C")
explain("Create a list called 'vlan_warnings' containing a")
explain("string for each device that has ANY reserved VLAN")
explain("in its vlan list. Format: '<hostname>: reserved vlans <list>'")
explain("RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
blank()
explain("Note: none of the devices in INVENTORY currently")
explain("have reserved VLANs — so test with this data instead:")
blank()
header("test_devices = [")
header("    {'hostname': 'nyc-rtr-01', 'vlans': [1, 10, 20]},")
header("    {'hostname': 'lon-sw-01',  'vlans': [10, 20]},")
header("    {'hostname': 'sin-fw-01',  'vlans': [1002, 30]},")
header("]")
blank()
header(">>> print(vlan_warnings)")
header("['nyc-rtr-01: reserved vlans [1]',")
header(" 'sin-fw-01: reserved vlans [1002]']")
blank()

pause()

section("Task D")
explain("Create a list called 'config_summary' — one string")
explain("per device describing its overall readiness.")
explain("Use these rules in order (first match wins):")
blank()
explain("  status is 'down' AND no vlans         → 'critical: offline, no vlans'")
explain("  status is 'down'                       → 'warning: offline'")
explain("  platform is 'ASA' AND status is 'up'  → 'ok: firewall active'")
explain("  status is 'up' AND has vlans           → 'ok: ready'")
explain("  anything else                          → 'unknown'")
blank()
header(">>> print(config_summary)")
header("['ok: ready', 'warning: offline', 'ok: firewall active',")
header(" 'ok: ready', 'warning: offline', 'ok: ready',")
header(" 'warning: offline', 'ok: ready']")
blank()

pause()

explain("Write your solution in: conditionals_solution_ch2.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — use 'and' to combine all three conditions.")
explain("  Task B — use 'or' across the three conditions. See Ch 3.2.")
explain("  Task C — use a separate test_devices list in your file.")
explain("           any(v in RESERVED_VLANS for v in d['vlans']).")
explain("  Task D — order matters — check 'down AND no vlans' first.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    exp_push = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "up"
        and d["platform"] in ("IOS-XE", "NX-OS")
        and d["vlans"]
    ]

    exp_review = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "down"
        or not d["vlans"]
        or d["config"]["ntp"] != GLOBAL_NTP
    ]

    test_devices = [
        {"hostname": "nyc-rtr-01", "vlans": [1, 10, 20]},
        {"hostname": "lon-sw-01",  "vlans": [10, 20]},
        {"hostname": "sin-fw-01",  "vlans": [1002, 30]},
    ]
    exp_warnings = [
        f"{d['hostname']}: reserved vlans {[v for v in d['vlans'] if v in RESERVED_VLANS]}"
        for d in test_devices
        if any(v in RESERVED_VLANS for v in d["vlans"])
    ]

    def _summary(d):
        if d["status"] == "down" and not d["vlans"]: return "critical: offline, no vlans"
        elif d["status"] == "down":                  return "warning: offline"
        elif d["platform"] == "ASA" and d["status"] == "up": return "ok: firewall active"
        elif d["status"] == "up" and d["vlans"]:     return "ok: ready"
        else:                                        return "unknown"

    exp_summary = [_summary(d) for d in INVENTORY]

    grade(2, [
        (
            "Task A", "push_ready — up + IOS-XE/NX-OS + has vlans",
            ns.get("push_ready"), exp_push,
            "See Chapter 3.1 — combine with 'and': status=='up' and platform in (...) and d['vlans'].",
            "push_ready = [d['hostname'] for d in INVENTORY if d['status']=='up' and d['platform'] in ('IOS-XE','NX-OS') and d['vlans']]",
            "push_ready",
        ),
        (
            "Task B", "needs_review — down OR no vlans OR custom NTP",
            ns.get("needs_review"), exp_review,
            "See Chapter 3.2 — combine with 'or': status=='down' or not d['vlans'] or ntp!=GLOBAL_NTP.",
            "needs_review = [d['hostname'] for d in INVENTORY if d['status']=='down' or not d['vlans'] or d['config']['ntp']!=GLOBAL_NTP]",
            "needs_review",
        ),
        (
            "Task C", "vlan_warnings — devices with reserved VLANs",
            ns.get("vlan_warnings"), exp_warnings,
            "See Chapter 3 — any(v in RESERVED_VLANS for v in d['vlans']). Use the test_devices list.",
            "vlan_warnings = [f\"{d['hostname']}: reserved vlans {[v for v in d['vlans'] if v in RESERVED_VLANS]}\" for d in test_devices if any(v in RESERVED_VLANS for v in d['vlans'])]",
            "vlan_warnings",
        ),
        (
            "Task D", "config_summary — ordered if/elif rules per device",
            ns.get("config_summary"), exp_summary,
            "See Chapter 1.2 — order matters: check 'down AND no vlans' before just 'down'.",
            "def classify(d):\n    if d['status']=='down' and not d['vlans']: return 'critical: offline, no vlans'\n    elif d['status']=='down': return 'warning: offline'\n    elif d['platform']=='ASA' and d['status']=='up': return 'ok: firewall active'\n    elif d['status']=='up' and d['vlans']: return 'ok: ready'\n    else: return 'unknown'\nconfig_summary = [classify(d) for d in INVENTORY]",
            "config_summary",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Complex Logic and Patterns", "Hard")

explain("Combine everything — nested conditions, guard clauses,")
explain("break/continue, match/case, and complex filtering.")
blank()

pause()

section("Task A")
explain("Write a function called 'validate_device(device)'")
explain("that uses GUARD CLAUSES (early return pattern) to")
explain("validate a device. Return the FIRST failure message")
explain("that applies, or 'valid' if all checks pass.")
blank()
explain("Checks in order:")
explain("  1. status is not 'up'                → 'fail: device is down'")
explain("  2. platform not in supported list     → 'fail: unsupported platform'")
explain("     supported: IOS-XE, NX-OS, ASA, IOS-XR")
explain("  3. no vlans configured                → 'fail: no vlans'")
explain("  4. any vlan in RESERVED_VLANS         → 'fail: reserved vlan found'")
explain("  5. NTP differs from GLOBAL_NTP        → 'warn: custom ntp'")
explain("  all pass                              → 'valid'")
blank()
explain("Then create a list called 'validation_results' by")
explain("calling validate_device(d) for each device in INVENTORY.")
blank()
header(">>> print(validation_results)")
header("['valid', 'fail: device is down', 'valid',")
header(" 'valid', 'fail: device is down', 'valid',")
header(" 'fail: device is down', 'warn: custom ntp']")
blank()

pause()

section("Task B")
explain("Use a for loop with break to find the FIRST device")
explain("in INVENTORY that meets ALL of these conditions:")
blank()
explain("  platform is 'IOS-XE'")
explain("  status is 'up'")
explain("  has more than 3 VLANs")
blank()
explain("Store the result in 'first_match'.")
explain("If nothing matches, 'first_match' should be None.")
blank()
header(">>> print(first_match)")
header("{'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'status': 'up',")
header(" 'ip': '10.3.0.1', 'vlans': [10, 20, 30, 40],")
header(" 'config': {'ntp': '10.0.0.100', 'dns': '8.8.8.8'}}")
blank()

pause()

section("Task C")
explain("Use match/case to create a list called 'module_map'")
explain("containing the Ansible module name for each device.")
blank()
explain("Rules:")
explain("  platform 'IOS-XE'         → 'cisco.ios.ios_config'")
explain("  platform 'NX-OS'          → 'cisco.nxos.nxos_config'")
explain("  platform 'ASA'            → 'cisco.asa.asa_config'")
explain("  platform 'IOS-XR'         → 'cisco.iosxr.iosxr_config'")
explain("  anything else             → 'manual_intervention_required'")
blank()
header(">>> print(module_map)")
header("['cisco.ios.ios_config', 'cisco.nxos.nxos_config', 'cisco.asa.asa_config',")
header(" 'cisco.ios.ios_config', 'cisco.nxos.nxos_config', 'cisco.ios.ios_config',")
header(" 'cisco.asa.asa_config', 'cisco.ios.ios_config']")
blank()

pause()

section("Task D")
explain("Create a list called 'deployment_plan' — one dict")
explain("per device, built using conditional logic.")
blank()
explain("Each dict has:")
explain("  'hostname'  → the hostname")
explain("  'action'    → determined by these rules:")
explain("       status 'down'                    → 'skip'")
explain("       platform 'ASA' and status 'up'   → 'push-firewall-policy'")
explain("       platform in IOS-XE/NX-OS,")
explain("         status 'up', vlans present      → 'push-switch-config'")
explain("       anything else                    → 'manual-review'")
explain("  'priority'  → 'high' if more than 3 vlans else 'normal'")
explain("  'module'    → same logic as Task C")
blank()
header(">>> for d in deployment_plan: print(d)")
header("{'hostname': 'nyc-rtr-01', 'action': 'push-switch-config', 'priority': 'normal', 'module': 'cisco.ios.ios_config'}")
header("{'hostname': 'lon-sw-01',  'action': 'skip',               'priority': 'normal', 'module': 'cisco.nxos.nxos_config'}")
header("{'hostname': 'sin-fw-01',  'action': 'push-firewall-policy','priority': 'normal', 'module': 'cisco.asa.asa_config'}")
header("{'hostname': 'ams-rtr-02', 'action': 'push-switch-config', 'priority': 'high',   'module': 'cisco.ios.ios_config'}")
header("{'hostname': 'tok-sw-01',  'action': 'skip',               'priority': 'normal', 'module': 'cisco.nxos.nxos_config'}")
header("{'hostname': 'syd-rtr-01', 'action': 'push-switch-config', 'priority': 'normal', 'module': 'cisco.ios.ios_config'}")
header("{'hostname': 'dub-fw-01',  'action': 'skip',               'priority': 'normal', 'module': 'cisco.asa.asa_config'}")
header("{'hostname': 'mum-rtr-01', 'action': 'push-switch-config', 'priority': 'high',   'module': 'cisco.ios.ios_config'}")
blank()

pause()

explain("Write your solution in: conditionals_solution_ch3.py")
explain("Remember to paste the data block at the top.")
blank()
explain("Tips:")
explain("  Task A — def validate_device(d): with early returns. See Ch 5.3.")
explain("  Task B — for loop with if + break + else. See Ch 7.2.")
explain("  Task C — match d['platform']: case 'IOS-XE': ... See Ch 9.")
explain("  Task D — combine tasks A/B/C logic into one comprehension.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    SUPPORTED = ("IOS-XE", "NX-OS", "ASA", "IOS-XR")

    def _validate(d):
        if d["status"] != "up":
            return "fail: device is down"
        if d["platform"] not in SUPPORTED:
            return "fail: unsupported platform"
        if not d["vlans"]:
            return "fail: no vlans"
        if any(v in RESERVED_VLANS for v in d["vlans"]):
            return "fail: reserved vlan found"
        if d["config"]["ntp"] != GLOBAL_NTP:
            return "warn: custom ntp"
        return "valid"

    exp_validation = [_validate(d) for d in INVENTORY]

    exp_first = None
    for d in INVENTORY:
        if d["platform"] == "IOS-XE" and d["status"] == "up" and len(d["vlans"]) > 3:
            exp_first = d
            break

    def _module(platform):
        match platform:
            case "IOS-XE":  return "cisco.ios.ios_config"
            case "NX-OS":   return "cisco.nxos.nxos_config"
            case "ASA":     return "cisco.asa.asa_config"
            case "IOS-XR":  return "cisco.iosxr.iosxr_config"
            case _:         return "manual_intervention_required"

    exp_modules = [_module(d["platform"]) for d in INVENTORY]

    def _action(d):
        if d["status"] == "down":
            return "skip"
        if d["platform"] == "ASA" and d["status"] == "up":
            return "push-firewall-policy"
        if d["platform"] in ("IOS-XE", "NX-OS") and d["status"] == "up" and d["vlans"]:
            return "push-switch-config"
        return "manual-review"

    exp_plan = [
        {
            "hostname": d["hostname"],
            "action":   _action(d),
            "priority": "high" if len(d["vlans"]) > 3 else "normal",
            "module":   _module(d["platform"]),
        }
        for d in INVENTORY
    ]

    grade(3, [
        (
            "Task A", "validation_results — guard clause validation per device",
            ns.get("validation_results"), exp_validation,
            "See Chapter 5.3 — def validate_device(d): with early return for each failed check.",
            "def validate_device(d):\n    if d['status'] != 'up': return 'fail: device is down'\n    if d['platform'] not in ('IOS-XE','NX-OS','ASA','IOS-XR'): return 'fail: unsupported platform'\n    if not d['vlans']: return 'fail: no vlans'\n    if any(v in RESERVED_VLANS for v in d['vlans']): return 'fail: reserved vlan found'\n    if d['config']['ntp'] != GLOBAL_NTP: return 'warn: custom ntp'\n    return 'valid'\nvalidation_results = [validate_device(d) for d in INVENTORY]",
            "validation_results",
        ),
        (
            "Task B", "first_match — first IOS-XE up device with >3 vlans",
            ns.get("first_match"), exp_first,
            "See Chapter 7.2 — for loop with if condition + break. Store matched device in first_match.",
            "first_match = None\nfor d in INVENTORY:\n    if d['platform']=='IOS-XE' and d['status']=='up' and len(d['vlans'])>3:\n        first_match = d\n        break",
            "first_match",
        ),
        (
            "Task C", "module_map — Ansible module name per platform",
            ns.get("module_map"), exp_modules,
            "See Chapter 9.1 — match d['platform']: case 'IOS-XE': ... case _: ...",
            "def get_module(p):\n    match p:\n        case 'IOS-XE': return 'cisco.ios.ios_config'\n        case 'NX-OS': return 'cisco.nxos.nxos_config'\n        case 'ASA': return 'cisco.asa.asa_config'\n        case 'IOS-XR': return 'cisco.iosxr.iosxr_config'\n        case _: return 'manual_intervention_required'\nmodule_map = [get_module(d['platform']) for d in INVENTORY]",
            "module_map",
        ),
        (
            "Task D", "deployment_plan — list of dicts with action, priority, module",
            ns.get("deployment_plan"), exp_plan,
            "See Chapters 1, 6, 9 — combine action if/elif, ternary priority, match/case module.",
            "deployment_plan = [{'hostname': d['hostname'], 'action': get_action(d), 'priority': 'high' if len(d['vlans'])>3 else 'normal', 'module': get_module(d['platform'])} for d in INVENTORY]",
            "deployment_plan",
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