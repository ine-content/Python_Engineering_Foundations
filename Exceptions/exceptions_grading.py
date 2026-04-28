# exceptions_grading.py
# Python Exceptions — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in exceptions_solution.py
# 2. Run this script: python3 exceptions_grading.py
# 3. Fix any hints and re-run until you get Good Job!

import os
import sys
import json
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
INVENTORY = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.0.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.1.0.1", "vlans": [10, 20],
     "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"}},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
     "ip": "10.2.0.1", "vlans": [30, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
     "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.4.0.1", "vlans": [20, 30],
     "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"}},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.5.0.1", "vlans": [10, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
     "ip": "10.6.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
     "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"}},
]

GLOBAL_NTP = "10.0.0.100"

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "exceptions_solution.py"
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
        "INVENTORY":  INVENTORY,
        "GLOBAL_NTP": GLOBAL_NTP,
        "json":       json,
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


def grade(checks, ns=None):
    total = len(checks)

    results = []
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        if expected is None and ns is not None:
            student_defined = var_name.strip("()") in ns
            ok = student_defined and (actual == expected)
        else:
            ok = (actual == expected)
        if ok:
            passed += 1
        results.append((task_label, label, ok, actual, expected, hint_text, solution_ways, var_name))

    blank()
    bar = "█" * 62
    score_color = GREEN if passed >= 6 else YELLOW if passed >= 4 else RED
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
    if passed >= 6:
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
    return passed >= 6


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         EXCEPTIONS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your exceptions_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Pull functions from student namespace ──────────────────────────────────
    safe_get_fn         = ns.get("safe_get")
    count_vlans_fn      = ns.get("count_vlans")
    parse_ip_fn         = ns.get("parse_ip_octet")
    validate_status_fn  = ns.get("validate_status")
    connect_fn          = ns.get("connect")
    safe_connect_fn     = ns.get("safe_connect")
    batch_connect_fn    = ns.get("batch_connect")
    safe_parse_fn       = ns.get("safe_parse_config")
    DeviceOfflineError  = ns.get("DeviceOfflineError")

    # ── Task 1: safe_get ───────────────────────────────────────────────────────
    t1_results = None
    if safe_get_fn:
        try:
            t1_results = (
                safe_get_fn(INVENTORY[0], "hostname"),
                safe_get_fn(INVENTORY[0], "missing_key"),
                safe_get_fn(INVENTORY[3], "ip"),
            )
        except Exception as e:
            t1_results = f"raised: {e}"
    exp_t1 = ("nyc-rtr-01", None, "10.3.0.1")

    # ── Task 2: count_vlans ────────────────────────────────────────────────────
    t2_results = None
    if count_vlans_fn:
        try:
            t2_results = (
                count_vlans_fn(INVENTORY[0]),
                count_vlans_fn("not-a-dict"),
                count_vlans_fn({"vlans": "bad-value"}),
            )
        except Exception as e:
            t2_results = f"raised: {e}"
    exp_t2 = (3, -1, -1)

    # ── Task 3: parse_ip_octet ─────────────────────────────────────────────────
    t3_results = None
    if parse_ip_fn:
        import io, contextlib
        try:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                r1 = parse_ip_fn("10.0.0.1")
                r2 = parse_ip_fn("bad-ip")
                r3 = parse_ip_fn("10.3.0.255")
            printed = buf.getvalue()
            t3_results = (r1, r2, r3, printed.count("parse_ip_octet done"))
        except Exception as e:
            t3_results = f"raised: {e}"
    exp_t3 = (1, -1, 255, 3)  # 3 calls → 3 "done" prints

    # ── Task 4: validate_status ────────────────────────────────────────────────
    t4_results = None
    if validate_status_fn:
        try:
            r1 = validate_status_fn(INVENTORY[0])   # up → True
            r2 = validate_status_fn(INVENTORY[1])   # down → True
            try:
                validate_status_fn({"hostname": "x", "status": "unknown"})
                r3 = "no-error"
            except ValueError as e:
                r3 = str(e)
            except Exception as e:
                r3 = f"wrong-exception: {e}"
            t4_results = (r1, r2, r3)
        except Exception as e:
            t4_results = f"raised: {e}"
    exp_t4 = (True, True, "Invalid status: unknown")

    # ── Task 5: connect / DeviceOfflineError ───────────────────────────────────
    t5_results = None
    if connect_fn and DeviceOfflineError:
        try:
            r1 = connect_fn(INVENTORY[0])   # up → connected
            try:
                connect_fn(INVENTORY[1])    # down → DeviceOfflineError
                r2 = "no-error"
            except Exception as e:
                r2 = (type(e).__name__, str(e))
            t5_results = (r1, r2)
        except Exception as e:
            t5_results = f"raised: {e}"
    exp_t5 = ("connected: nyc-rtr-01", ("DeviceOfflineError", "lon-sw-01 is offline"))

    # ── Task 6: safe_connect ───────────────────────────────────────────────────
    t6_results = None
    if safe_connect_fn:
        try:
            t6_results = (
                safe_connect_fn(INVENTORY[0]),   # up
                safe_connect_fn(INVENTORY[1]),   # down
                safe_connect_fn(INVENTORY[2]),   # up
            )
        except Exception as e:
            t6_results = f"raised: {e}"
    exp_t6 = ("connected: nyc-rtr-01", "offline: lon-sw-01", "connected: sin-fw-01")

    # ── Task 7: batch_connect ──────────────────────────────────────────────────
    t7_results = None
    if batch_connect_fn:
        try:
            t7_results = batch_connect_fn(INVENTORY)
        except Exception as e:
            t7_results = f"raised: {e}"
    exp_t7 = {
        "connected": ["nyc-rtr-01", "sin-fw-01", "ams-rtr-02", "syd-rtr-01", "mum-rtr-01"],
        "offline":   ["lon-sw-01", "tok-sw-01", "dub-fw-01"],
        "errors":    [],
    }

    # ── Task 8: safe_parse_config ──────────────────────────────────────────────
    t8_results = None
    if safe_parse_fn:
        try:
            r1 = safe_parse_fn('{"ntp": "10.0.0.100"}')
            try:
                safe_parse_fn(123)
                r2 = "no-error"
            except TypeError as e:
                r2 = str(e)
            except Exception as e:
                r2 = f"wrong: {e}"
            try:
                safe_parse_fn("bad json {{")
                r3 = "no-error"
            except ValueError as e:
                r3 = "ValueError"
            except Exception as e:
                r3 = f"wrong: {e}"
            try:
                safe_parse_fn("[1, 2, 3]")
                r4 = "no-error"
            except ValueError as e:
                r4 = str(e)
            except Exception as e:
                r4 = f"wrong: {e}"
            t8_results = (r1, r2, r3, r4)
        except Exception as e:
            t8_results = f"raised: {e}"
    exp_t8 = (
        {"ntp": "10.0.0.100"},
        f"Expected str, got {type(123)}",
        "ValueError",
        f"Expected dict, got {type([])}",
    )

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_safe_get = [
        ("try/except KeyError",
         ["def safe_get(device, key):",
          "    try:",
          "        return device[key]",
          "    except KeyError:",
          "        return None"]),
        ("dict.get()",
         ["def safe_get(device, key):",
          "    return device.get(key, None)"]),
    ]

    ways_count_vlans = [
        ("try/except TypeError",
         ["def count_vlans(device):",
          "    try:",
          "        return len(device['vlans'])",
          "    except TypeError:",
          "        return -1"]),
    ]

    ways_parse_ip = [
        ("try/except/else/finally",
         ["def parse_ip_octet(ip_string):",
          "    try:",
          "        result = int(ip_string.split('.')[-1])",
          "    except (ValueError, IndexError):",
          "        return -1",
          "    else:",
          "        return result",
          "    finally:",
          "        print('parse_ip_octet done')"]),
    ]

    ways_validate = [
        ("raise ValueError with message",
         ["def validate_status(device):",
          "    status = device['status']",
          "    if status not in ('up', 'down'):",
          "        raise ValueError(f'Invalid status: {status}')",
          "    return True"]),
    ]

    ways_connect = [
        ("Custom exception class + raise",
         ["class DeviceOfflineError(Exception):",
          "    pass",
          "",
          "def connect(device):",
          "    if device['status'] == 'down':",
          "        raise DeviceOfflineError(f\"{device['hostname']} is offline\")",
          "    return f\"connected: {device['hostname']}\""]),
    ]

    ways_safe_connect = [
        ("except DeviceOfflineError / except Exception",
         ["def safe_connect(device):",
          "    try:",
          "        return connect(device)",
          "    except DeviceOfflineError:",
          "        return f\"offline: {device['hostname']}\"",
          "    except Exception as e:",
          "        return f\"error: {e}\""]),
    ]

    ways_batch = [
        ("Loop over inventory calling safe_connect",
         ["def batch_connect(inventory):",
          "    result = {'connected': [], 'offline': [], 'errors': []}",
          "    for d in inventory:",
          "        outcome = safe_connect(d)",
          "        if outcome.startswith('connected'):",
          "            result['connected'].append(d['hostname'])",
          "        elif outcome.startswith('offline'):",
          "            result['offline'].append(d['hostname'])",
          "        else:",
          "            result['errors'].append(d['hostname'])",
          "    return result"]),
    ]

    ways_safe_parse = [
        ("isinstance checks + chained ValueError",
         ["def safe_parse_config(raw):",
          "    import json",
          "    if not isinstance(raw, str):",
          "        raise TypeError(f'Expected str, got {type(raw)}')",
          "    try:",
          "        result = json.loads(raw)",
          "    except json.JSONDecodeError as e:",
          "        raise ValueError(f'Invalid JSON: {e}') from e",
          "    if not isinstance(result, dict):",
          "        raise ValueError(f'Expected dict, got {type(result)}')",
          "    return result"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task 1", "safe_get — returns value or None on KeyError",
         t1_results, exp_t1,
         "try: return device[key]  except KeyError: return None",
         ways_safe_get, "safe_get results"),
        ("Task 2", "count_vlans — returns len or -1 on TypeError",
         t2_results, exp_t2,
         "try: return len(device['vlans'])  except TypeError: return -1",
         ways_count_vlans, "count_vlans results"),
        ("Task 3", "parse_ip_octet — try/except/else/finally with print",
         t3_results, exp_t3,
         "Use try/except/else/finally. Return in else. Print in finally.",
         ways_parse_ip, "parse_ip_octet results"),
        ("Task 4", "validate_status — raises ValueError for invalid status",
         t4_results, exp_t4,
         "if status not in ('up', 'down'): raise ValueError(f'Invalid status: {status}')",
         ways_validate, "validate_status results"),
        ("Task 5", "DeviceOfflineError + connect — raises on down devices",
         t5_results, exp_t5,
         "class DeviceOfflineError(Exception): pass. Raise it when status=='down'.",
         ways_connect, "connect results"),
        ("Task 6", "safe_connect — handles DeviceOfflineError and Exception",
         t6_results, exp_t6,
         "except DeviceOfflineError: return 'offline: ...'  except Exception: return 'error: ...'",
         ways_safe_connect, "safe_connect results"),
        ("Task 7", "batch_connect — summary dict with connected/offline/errors",
         t7_results, exp_t7,
         "Call safe_connect() per device, check string prefix to sort into buckets.",
         ways_batch, "batch_connect(INVENTORY)"),
        ("Task 8", "safe_parse_config — TypeError, ValueError, chained exceptions",
         t8_results, exp_t8,
         "isinstance(raw, str) → TypeError. json.JSONDecodeError → raise ValueError from e.",
         ways_safe_parse, "safe_parse_config results"),
    ], ns=ns)

pause()