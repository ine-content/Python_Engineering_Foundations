# conditionals_grading.py
# Python Conditionals — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in conditionals_solution.py
# 2. Run this script: python3 conditionals_grading.py
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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "conditionals_solution.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
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
    if isinstance(expected, list) and len(expected) > 4:
        for item in expected:
            print(f"    {GREEN}{item}{RESET}")
    elif isinstance(expected, dict) and len(expected) > 4:
        for k, v in expected.items():
            print(f"    {GREEN}{k!r}: {v!r}{RESET}")
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
print(f"{BOLD}         CONDITIONALS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your conditionals_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    def _label(d):
        h = d["hostname"]
        if "rtr" in h:   return f"Router: {h}"
        elif "sw" in h:  return f"Switch: {h}"
        elif "fw" in h:  return f"Firewall: {h}"
        else:            return f"Unknown: {h}"
    exp_labels = [_label(d) for d in INVENTORY]

    # Task 2
    def _pclass(d):
        if d["platform"] in ("IOS-XE", "NX-OS"): return "switching-routing"
        elif d["platform"] == "ASA":              return "security"
        else:                                     return "other"
    exp_pclass = [_pclass(d) for d in INVENTORY]

    # Task 3
    def _vstatus(d):
        n = len(d["vlans"])
        if n == 0:    return "no-vlans"
        elif n == 1:  return "single-vlan"
        elif n <= 3:  return "few-vlans"
        else:         return "many-vlans"
    exp_vstatus = [_vstatus(d) for d in INVENTORY]

    # Task 4
    exp_ntp = ["standard" if d["config"]["ntp"] == GLOBAL_NTP else "custom" for d in INVENTORY]

    # Task 5
    exp_push = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "up"
        and d["platform"] in ("IOS-XE", "NX-OS")
        and d["vlans"]
    ]

    # Task 6
    exp_review = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "down"
        or not d["vlans"]
        or d["config"]["ntp"] != GLOBAL_NTP
    ]

    # Task 7
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

    # Task 8
    def _summary(d):
        if d["status"] == "down" and not d["vlans"]: return "critical: offline, no vlans"
        elif d["status"] == "down":                  return "warning: offline"
        elif d["platform"] == "ASA" and d["status"] == "up": return "ok: firewall active"
        elif d["status"] == "up" and d["vlans"]:     return "ok: ready"
        else:                                        return "unknown"
    exp_summary = [_summary(d) for d in INVENTORY]

    # Task 9
    SUPPORTED = ("IOS-XE", "NX-OS", "ASA", "IOS-XR")
    def _validate(d):
        if d["status"] != "up":                          return "fail: device is down"
        if d["platform"] not in SUPPORTED:               return "fail: unsupported platform"
        if not d["vlans"]:                               return "fail: no vlans"
        if any(v in RESERVED_VLANS for v in d["vlans"]): return "fail: reserved vlan found"
        if d["config"]["ntp"] != GLOBAL_NTP:             return "warn: custom ntp"
        return "valid"
    exp_validation = [_validate(d) for d in INVENTORY]

    # Task 10
    exp_first = None
    for d in INVENTORY:
        if d["platform"] == "IOS-XE" and d["status"] == "up" and len(d["vlans"]) > 3:
            exp_first = d
            break

    # Task 11
    def _module(p):
        match p:
            case "IOS-XE":  return "cisco.ios.ios_config"
            case "NX-OS":   return "cisco.nxos.nxos_config"
            case "ASA":     return "cisco.asa.asa_config"
            case "IOS-XR":  return "cisco.iosxr.iosxr_config"
            case _:         return "manual_intervention_required"
    exp_modules = [_module(d["platform"]) for d in INVENTORY]

    # Task 12
    def _action(d):
        if d["status"] == "down":                                       return "skip"
        if d["platform"] == "ASA" and d["status"] == "up":             return "push-firewall-policy"
        if d["platform"] in ("IOS-XE", "NX-OS") and d["status"] == "up" and d["vlans"]: return "push-switch-config"
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

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_labels = [
        ("For loop with if/elif/else",
         ["device_labels = []",
          "for d in INVENTORY:",
          "    h = d['hostname']",
          "    if 'rtr' in h:   device_labels.append(f'Router: {h}')",
          "    elif 'sw' in h:  device_labels.append(f'Switch: {h}')",
          "    elif 'fw' in h:  device_labels.append(f'Firewall: {h}')",
          "    else:            device_labels.append(f'Unknown: {h}')"]),
        ("List comprehension with helper function",
         ["def classify(d):",
          "    h = d['hostname']",
          "    if 'rtr' in h:   return f'Router: {h}'",
          "    elif 'sw' in h:  return f'Switch: {h}'",
          "    elif 'fw' in h:  return f'Firewall: {h}'",
          "    else:            return f'Unknown: {h}'",
          "device_labels = [classify(d) for d in INVENTORY]"]),
    ]

    ways_pclass = [
        ("Ternary in list comprehension",
         ["platform_class = [",
          "    'switching-routing' if d['platform'] in ('IOS-XE', 'NX-OS')",
          "    else 'security' if d['platform'] == 'ASA'",
          "    else 'other'",
          "    for d in INVENTORY",
          "]"]),
        ("For loop with if/elif/else",
         ["platform_class = []",
          "for d in INVENTORY:",
          "    if d['platform'] in ('IOS-XE', 'NX-OS'):",
          "        platform_class.append('switching-routing')",
          "    elif d['platform'] == 'ASA':",
          "        platform_class.append('security')",
          "    else:",
          "        platform_class.append('other')"]),
    ]

    ways_vstatus = [
        ("For loop with if/elif/elif/else",
         ["vlan_status = []",
          "for d in INVENTORY:",
          "    n = len(d['vlans'])",
          "    if n == 0:    vlan_status.append('no-vlans')",
          "    elif n == 1:  vlan_status.append('single-vlan')",
          "    elif n <= 3:  vlan_status.append('few-vlans')",
          "    else:         vlan_status.append('many-vlans')"]),
        ("Helper function + comprehension",
         ["def vlan_label(d):",
          "    n = len(d['vlans'])",
          "    if n == 0:    return 'no-vlans'",
          "    elif n == 1:  return 'single-vlan'",
          "    elif n <= 3:  return 'few-vlans'",
          "    else:         return 'many-vlans'",
          "vlan_status = [vlan_label(d) for d in INVENTORY]"]),
    ]

    ways_ntp = [
        ("Ternary comprehension",
         ["ntp_check = ['standard' if d['config']['ntp'] == GLOBAL_NTP else 'custom'",
          "             for d in INVENTORY]"]),
        ("For loop",
         ["ntp_check = []",
          "for d in INVENTORY:",
          "    if d['config']['ntp'] == GLOBAL_NTP:",
          "        ntp_check.append('standard')",
          "    else:",
          "        ntp_check.append('custom')"]),
    ]

    ways_push = [
        ("List comprehension with 'and'",
         ["push_ready = [",
          "    d['hostname'] for d in INVENTORY",
          "    if d['status'] == 'up'",
          "    and d['platform'] in ('IOS-XE', 'NX-OS')",
          "    and d['vlans']",
          "]"]),
        ("For loop",
         ["push_ready = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS') and d['vlans']:",
          "        push_ready.append(d['hostname'])"]),
    ]

    ways_review = [
        ("List comprehension with 'or'",
         ["needs_review = [",
          "    d['hostname'] for d in INVENTORY",
          "    if d['status'] == 'down'",
          "    or not d['vlans']",
          "    or d['config']['ntp'] != GLOBAL_NTP",
          "]"]),
        ("For loop",
         ["needs_review = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'down' or not d['vlans'] or d['config']['ntp'] != GLOBAL_NTP:",
          "        needs_review.append(d['hostname'])"]),
    ]

    ways_warnings = [
        ("List comprehension with any()",
         ["test_devices = [",
          "    {'hostname': 'nyc-rtr-01', 'vlans': [1, 10, 20]},",
          "    {'hostname': 'lon-sw-01',  'vlans': [10, 20]},",
          "    {'hostname': 'sin-fw-01',  'vlans': [1002, 30]},",
          "]",
          "vlan_warnings = [",
          "    f\"{d['hostname']}: reserved vlans {[v for v in d['vlans'] if v in RESERVED_VLANS]}\"",
          "    for d in test_devices",
          "    if any(v in RESERVED_VLANS for v in d['vlans'])",
          "]"]),
    ]

    ways_summary = [
        ("Helper function + comprehension",
         ["def summarise(d):",
          "    if d['status'] == 'down' and not d['vlans']: return 'critical: offline, no vlans'",
          "    elif d['status'] == 'down':                  return 'warning: offline'",
          "    elif d['platform'] == 'ASA' and d['status'] == 'up': return 'ok: firewall active'",
          "    elif d['status'] == 'up' and d['vlans']:    return 'ok: ready'",
          "    else:                                        return 'unknown'",
          "config_summary = [summarise(d) for d in INVENTORY]"]),
        ("For loop with if/elif chain",
         ["config_summary = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'down' and not d['vlans']:",
          "        config_summary.append('critical: offline, no vlans')",
          "    elif d['status'] == 'down':",
          "        config_summary.append('warning: offline')",
          "    elif d['platform'] == 'ASA' and d['status'] == 'up':",
          "        config_summary.append('ok: firewall active')",
          "    elif d['status'] == 'up' and d['vlans']:",
          "        config_summary.append('ok: ready')",
          "    else:",
          "        config_summary.append('unknown')"]),
    ]

    ways_validate = [
        ("Guard clauses with early return",
         ["def validate_device(d):",
          "    if d['status'] != 'up':                           return 'fail: device is down'",
          "    if d['platform'] not in ('IOS-XE','NX-OS','ASA','IOS-XR'): return 'fail: unsupported platform'",
          "    if not d['vlans']:                                return 'fail: no vlans'",
          "    if any(v in RESERVED_VLANS for v in d['vlans']): return 'fail: reserved vlan found'",
          "    if d['config']['ntp'] != GLOBAL_NTP:             return 'warn: custom ntp'",
          "    return 'valid'",
          "validation_results = [validate_device(d) for d in INVENTORY]"]),
    ]

    ways_first = [
        ("For loop with break",
         ["first_match = None",
          "for d in INVENTORY:",
          "    if d['platform'] == 'IOS-XE' and d['status'] == 'up' and len(d['vlans']) > 3:",
          "        first_match = d",
          "        break"]),
        ("next() with generator",
         ["first_match = next(",
          "    (d for d in INVENTORY",
          "     if d['platform'] == 'IOS-XE' and d['status'] == 'up' and len(d['vlans']) > 3),",
          "    None",
          ")"]),
    ]

    ways_modules = [
        ("match/case inside function",
         ["def get_module(p):",
          "    match p:",
          "        case 'IOS-XE':  return 'cisco.ios.ios_config'",
          "        case 'NX-OS':   return 'cisco.nxos.nxos_config'",
          "        case 'ASA':     return 'cisco.asa.asa_config'",
          "        case 'IOS-XR':  return 'cisco.iosxr.iosxr_config'",
          "        case _:         return 'manual_intervention_required'",
          "module_map = [get_module(d['platform']) for d in INVENTORY]"]),
        ("dict lookup",
         ["MODULE_MAP = {",
          "    'IOS-XE': 'cisco.ios.ios_config',",
          "    'NX-OS':  'cisco.nxos.nxos_config',",
          "    'ASA':    'cisco.asa.asa_config',",
          "    'IOS-XR': 'cisco.iosxr.iosxr_config',",
          "}",
          "module_map = [MODULE_MAP.get(d['platform'], 'manual_intervention_required') for d in INVENTORY]"]),
    ]

    ways_plan = [
        ("Helper functions + comprehension",
         ["def get_action(d):",
          "    if d['status'] == 'down':                                        return 'skip'",
          "    if d['platform'] == 'ASA' and d['status'] == 'up':              return 'push-firewall-policy'",
          "    if d['platform'] in ('IOS-XE','NX-OS') and d['status'] == 'up' and d['vlans']: return 'push-switch-config'",
          "    return 'manual-review'",
          "",
          "deployment_plan = [",
          "    {",
          "        'hostname': d['hostname'],",
          "        'action':   get_action(d),",
          "        'priority': 'high' if len(d['vlans']) > 3 else 'normal',",
          "        'module':   get_module(d['platform']),",
          "    }",
          "    for d in INVENTORY",
          "]"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task  1", "device_labels — Router/Switch/Firewall/Unknown prefix",
         ns.get("device_labels"), exp_labels,
         "Use 'in' to check hostname: 'rtr' in d['hostname'].",
         ways_labels, "device_labels"),
        ("Task  2", "platform_class — switching-routing / security / other",
         ns.get("platform_class"), exp_pclass,
         "Use 'in' with a tuple: d['platform'] in ('IOS-XE', 'NX-OS').",
         ways_pclass, "platform_class"),
        ("Task  3", "vlan_status — no-vlans/single-vlan/few-vlans/many-vlans",
         ns.get("vlan_status"), exp_vstatus,
         "Use if/elif/elif/else on len(d['vlans']).",
         ways_vstatus, "vlan_status"),
        ("Task  4", "ntp_check — standard / custom",
         ns.get("ntp_check"), exp_ntp,
         "Ternary: 'standard' if d['config']['ntp'] == GLOBAL_NTP else 'custom'.",
         ways_ntp, "ntp_check"),
        ("Task  5", "push_ready — up + IOS-XE/NX-OS + has vlans",
         ns.get("push_ready"), exp_push,
         "Combine with 'and': status=='up' and platform in (...) and d['vlans'].",
         ways_push, "push_ready"),
        ("Task  6", "needs_review — down OR no vlans OR custom NTP",
         ns.get("needs_review"), exp_review,
         "Combine with 'or': status=='down' or not d['vlans'] or ntp!=GLOBAL_NTP.",
         ways_review, "needs_review"),
        ("Task  7", "vlan_warnings — devices with reserved VLANs",
         ns.get("vlan_warnings"), exp_warnings,
         "Use any(v in RESERVED_VLANS for v in d['vlans']) on test_devices.",
         ways_warnings, "vlan_warnings"),
        ("Task  8", "config_summary — ordered if/elif rules per device",
         ns.get("config_summary"), exp_summary,
         "Order matters — check 'down AND no vlans' before just 'down'.",
         ways_summary, "config_summary"),
        ("Task  9", "validation_results — guard clause validation per device",
         ns.get("validation_results"), exp_validation,
         "def validate_device(d): with early return for each failed check.",
         ways_validate, "validation_results"),
        ("Task 10", "first_match — first IOS-XE up device with >3 vlans",
         ns.get("first_match"), exp_first,
         "For loop with if condition + break. Initialise first_match = None before loop.",
         ways_first, "first_match"),
        ("Task 11", "module_map — Ansible module name per platform",
         ns.get("module_map"), exp_modules,
         "match d['platform']: case 'IOS-XE': ... case _: ...",
         ways_modules, "module_map"),
        ("Task 12", "deployment_plan — list of dicts with action, priority, module",
         ns.get("deployment_plan"), exp_plan,
         "Combine action if/elif, ternary priority, match/case module.",
         ways_plan, "deployment_plan"),
    ])

pause()