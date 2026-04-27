# conditionals_challenges.py
# Python Conditionals — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: conditionals_solution.py
# 3. Run conditionals_grading.py to check your answers

import os

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
GLOBAL_NTP     = "10.0.0.100"
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         CONDITIONALS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use INVENTORY, GLOBAL_NTP, and RESERVED_VLANS.")
explain("Read each task, write your solution in conditionals_solution.py,")
explain("then run conditionals_grading.py to check it.")
blank()
explain("The data is already pasted at the top of")
explain("conditionals_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Label devices by hostname type", "Easy")
explain("Goal:  Build a list called 'device_labels' — one string")
explain("       per device that classifies it by hostname.")
blank()
explain("Rules:")
explain("  • hostname contains 'rtr' → 'Router: <hostname>'")
explain("  • hostname contains 'sw'  → 'Switch: <hostname>'")
explain("  • hostname contains 'fw'  → 'Firewall: <hostname>'")
explain("  • anything else           → 'Unknown: <hostname>'")
blank()
explain("Variable name:  device_labels")
blank()
header(">>> print(device_labels)")
header("['Router: nyc-rtr-01', 'Switch: lon-sw-01', 'Firewall: sin-fw-01',")
header(" 'Router: ams-rtr-02', 'Switch: tok-sw-01', 'Router: syd-rtr-01',")
header(" 'Firewall: dub-fw-01', 'Router: mum-rtr-01']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Classify platforms", "Easy")
explain("Goal:  Build a list called 'platform_class' — one string")
explain("       per device classifying its platform.")
blank()
explain("Rules:")
explain("  • platform is 'IOS-XE' or 'NX-OS' → 'switching-routing'")
explain("  • platform is 'ASA'                → 'security'")
explain("  • anything else                    → 'other'")
blank()
explain("Variable name:  platform_class")
blank()
header(">>> print(platform_class)")
header("['switching-routing', 'switching-routing', 'security',")
header(" 'switching-routing', 'switching-routing', 'switching-routing',")
header(" 'security', 'switching-routing']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Describe VLAN count", "Easy")
explain("Goal:  Build a list called 'vlan_status' — one string")
explain("       per device describing its VLAN count.")
blank()
explain("Rules:")
explain("  • 0 VLANs        → 'no-vlans'")
explain("  • exactly 1 VLAN → 'single-vlan'")
explain("  • 2 or 3 VLANs   → 'few-vlans'")
explain("  • 4 or more VLANs → 'many-vlans'")
blank()
explain("Variable name:  vlan_status")
blank()
header(">>> print(vlan_status)")
header("['few-vlans', 'few-vlans', 'few-vlans', 'many-vlans',")
header(" 'few-vlans', 'few-vlans', 'few-vlans', 'many-vlans']")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Check NTP against global standard", "Easy")
explain("Goal:  Build a list called 'ntp_check' — one string")
explain("       per device indicating whether its NTP matches GLOBAL_NTP.")
blank()
explain("Rules:")
explain("  • device NTP == GLOBAL_NTP → 'standard'")
explain("  • device NTP != GLOBAL_NTP → 'custom'")
blank()
explain("Variable name:  ntp_check")
blank()
header(">>> print(ntp_check)")
header("['standard', 'custom', 'standard', 'standard',")
header(" 'custom', 'standard', 'standard', 'custom']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Find push-ready devices", "Medium")
explain("Goal:  Build a list called 'push_ready' containing the")
explain("       hostname of every device that meets ALL of these:")
blank()
explain("Rules:")
explain("  • status is 'up'")
explain("  • platform is 'IOS-XE' or 'NX-OS'")
explain("  • has at least one VLAN configured")
blank()
explain("Variable name:  push_ready")
blank()
header(">>> print(push_ready)")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Find devices that need review", "Medium")
explain("Goal:  Build a list called 'needs_review' containing the")
explain("       hostname of every device that meets ANY of these:")
blank()
explain("Rules:")
explain("  • status is 'down'")
explain("  • has no VLANs configured")
explain("  • NTP differs from GLOBAL_NTP")
blank()
explain("Variable name:  needs_review")
blank()
header(">>> print(needs_review)")
header("['lon-sw-01', 'tok-sw-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Detect reserved VLANs", "Medium")
explain("Goal:  Build a list called 'vlan_warnings' — one string")
explain("       per device that has ANY reserved VLAN in its vlan list.")
blank()
explain("Rules:")
explain("  • RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}")
explain("  • Format: '<hostname>: reserved vlans <list>'")
explain("  • Use this test_devices list in your solution file:")
blank()
header("test_devices = [")
header("    {'hostname': 'nyc-rtr-01', 'vlans': [1, 10, 20]},")
header("    {'hostname': 'lon-sw-01',  'vlans': [10, 20]},")
header("    {'hostname': 'sin-fw-01',  'vlans': [1002, 30]},")
header("]")
blank()
explain("Variable name:  vlan_warnings")
blank()
header(">>> print(vlan_warnings)")
header("['nyc-rtr-01: reserved vlans [1]',")
header(" 'sin-fw-01: reserved vlans [1002]']")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Summarise device readiness", "Medium")
explain("Goal:  Build a list called 'config_summary' — one string")
explain("       per device. Use these rules in order (first match wins):")
blank()
explain("Rules:")
explain("  • status 'down' AND no vlans        → 'critical: offline, no vlans'")
explain("  • status 'down'                      → 'warning: offline'")
explain("  • platform 'ASA' AND status 'up'    → 'ok: firewall active'")
explain("  • status 'up' AND has vlans          → 'ok: ready'")
explain("  • anything else                      → 'unknown'")
blank()
explain("Variable name:  config_summary")
blank()
header(">>> print(config_summary)")
header("['ok: ready', 'warning: offline', 'ok: firewall active',")
header(" 'ok: ready', 'warning: offline', 'ok: ready',")
header(" 'warning: offline', 'ok: ready']")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Validate devices with guard clauses", "Hard")
explain("Goal:  Write a function called 'validate_device(device)'")
explain("       using GUARD CLAUSES (early return pattern).")
explain("       Return the FIRST failure message that applies,")
explain("       or 'valid' if all checks pass.")
blank()
explain("Rules (in order):")
explain("  1. status is not 'up'               → 'fail: device is down'")
explain("  2. platform not in supported list    → 'fail: unsupported platform'")
explain("     supported: IOS-XE, NX-OS, ASA, IOS-XR")
explain("  3. no vlans configured               → 'fail: no vlans'")
explain("  4. any vlan in RESERVED_VLANS        → 'fail: reserved vlan found'")
explain("  5. NTP differs from GLOBAL_NTP       → 'warn: custom ntp'")
explain("  all pass                             → 'valid'")
blank()
explain("Then create a list called 'validation_results' by calling")
explain("validate_device(d) for each device in INVENTORY.")
blank()
explain("Variable name:  validation_results")
blank()
header(">>> print(validation_results)")
header("['valid', 'fail: device is down', 'valid',")
header(" 'valid', 'fail: device is down', 'valid',")
header(" 'fail: device is down', 'warn: custom ntp']")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Find first matching device with break", "Hard")
explain("Goal:  Use a for loop with break to find the FIRST device")
explain("       in INVENTORY that meets ALL of these conditions.")
blank()
explain("Rules:")
explain("  • platform is 'IOS-XE'")
explain("  • status is 'up'")
explain("  • has more than 3 VLANs")
blank()
explain("Rules:")
explain("  • Store the result in 'first_match'.")
explain("  • If nothing matches, first_match should be None.")
blank()
explain("Variable name:  first_match")
blank()
header(">>> print(first_match)")
header("{'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'status': 'up',")
header(" 'ip': '10.3.0.1', 'vlans': [10, 20, 30, 40],")
header(" 'config': {'ntp': '10.0.0.100', 'dns': '8.8.8.8'}}")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Map platforms to Ansible modules with match/case", "Hard")
explain("Goal:  Build a list called 'module_map' containing the")
explain("       Ansible module name for each device using match/case.")
blank()
explain("Rules:")
explain("  • 'IOS-XE'  → 'cisco.ios.ios_config'")
explain("  • 'NX-OS'   → 'cisco.nxos.nxos_config'")
explain("  • 'ASA'     → 'cisco.asa.asa_config'")
explain("  • 'IOS-XR'  → 'cisco.iosxr.iosxr_config'")
explain("  • anything  → 'manual_intervention_required'")
blank()
explain("Variable name:  module_map")
blank()
header(">>> print(module_map)")
header("['cisco.ios.ios_config', 'cisco.nxos.nxos_config', 'cisco.asa.asa_config',")
header(" 'cisco.ios.ios_config', 'cisco.nxos.nxos_config', 'cisco.ios.ios_config',")
header(" 'cisco.asa.asa_config', 'cisco.ios.ios_config']")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Build a deployment plan", "Hard")
explain("Goal:  Build a list called 'deployment_plan' — one dict")
explain("       per device built using conditional logic.")
blank()
explain("Rules:")
explain("  Each dict must have exactly four keys:")
explain("    'hostname' — the hostname")
explain("    'action'   — determined by these rules (first match wins):")
explain("         status 'down'                   → 'skip'")
explain("         platform 'ASA' and status 'up'  → 'push-firewall-policy'")
explain("         IOS-XE/NX-OS, up, vlans present → 'push-switch-config'")
explain("         anything else                   → 'manual-review'")
explain("    'priority' — 'high' if more than 3 vlans, else 'normal'")
explain("    'module'   — same logic as Task 11")
blank()
explain("Variable name:  deployment_plan")
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

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: conditionals_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task  1 — if/elif/elif/else on hostname: 'rtr' in hostname")
explain("  Task  2 — d['platform'] in ('IOS-XE', 'NX-OS')")
explain("  Task  3 — if/elif/elif/else on len(d['vlans'])")
explain("  Task  4 — ternary: 'standard' if d['config']['ntp'] == GLOBAL_NTP else 'custom'")
explain("  Task  5 — combine with 'and': status=='up' and platform in (...) and d['vlans']")
explain("  Task  6 — combine with 'or': status=='down' or not d['vlans'] or ntp!=GLOBAL_NTP")
explain("  Task  7 — any(v in RESERVED_VLANS for v in d['vlans'])")
explain("  Task  8 — order matters — check 'down AND no vlans' before just 'down'")
explain("  Task  9 — def validate_device(d): with early return for each failed check")
explain("  Task 10 — for loop with if + break, initialise first_match = None before loop")
explain("  Task 11 — match d['platform']: case 'IOS-XE': ... case _: ...")
explain("  Task 12 — combine action if/elif, ternary priority, match/case module")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# DONE
# ═════════════════════════════════════════════════════════════════════════════
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}  All tasks read. Now write your solution in:{RESET}")
print()
print(f"{BOLD}{CYAN}    conditionals_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 conditionals_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()