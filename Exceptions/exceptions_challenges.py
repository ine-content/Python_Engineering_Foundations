# exceptions_challenges.py
# Python Exceptions — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: exceptions_solution.py
# 3. Run exceptions_grading.py to check your answers

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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         EXCEPTIONS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("8 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("You will write functions that raise, catch, and handle")
explain("exceptions in real IaC scenarios.")
explain("Read each task, write your solution in exceptions_solution.py,")
explain("then run exceptions_grading.py to check it.")
blank()
explain("The data is already pasted at the top of")
explain("exceptions_solution.py — just write your answers below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Catch a KeyError when accessing device fields", "Easy")
explain("Goal:  Write a function called 'safe_get(device, key)'")
explain("       that returns the value of device[key].")
explain("       If the key does not exist, catch the KeyError and")
explain("       return None instead of crashing.")
blank()
explain("Function signature:  safe_get(device, key)")
blank()
header(">>> print(safe_get(INVENTORY[0], 'hostname'))")
header("'nyc-rtr-01'")
blank()
header(">>> print(safe_get(INVENTORY[0], 'missing_key'))")
header("None")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Catch a TypeError when processing bad input", "Easy")
explain("Goal:  Write a function called 'count_vlans(device)'")
explain("       that returns len(device['vlans']).")
explain("       If device is not a dict OR vlans is not a list,")
explain("       catch TypeError and return -1.")
blank()
explain("Function signature:  count_vlans(device)")
blank()
header(">>> print(count_vlans(INVENTORY[0]))")
header("3")
blank()
header(">>> print(count_vlans('not-a-dict'))")
header("-1")
blank()
header(">>> print(count_vlans({'vlans': 'bad-value'}))")
header("-1")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Use try/except/else/finally", "Easy")
explain("Goal:  Write a function called 'parse_ip_octet(ip_string)'")
explain("       that extracts the last octet from an IP string")
explain("       (e.g. '10.0.0.1' → 1) and returns it as an integer.")
blank()
explain("Rules:")
explain("  • Use try/except/else/finally.")
explain("  • If the conversion fails (ValueError or IndexError),")
explain("    return -1 in the except block.")
explain("  • In the else block, return the parsed integer.")
explain("  • The finally block must print: 'parse_ip_octet done'")
blank()
explain("Function signature:  parse_ip_octet(ip_string)")
blank()
header(">>> result = parse_ip_octet('10.0.0.1')")
header("parse_ip_octet done")
header(">>> print(result)")
header("1")
blank()
header(">>> result = parse_ip_octet('bad-ip')")
header("parse_ip_octet done")
header(">>> print(result)")
header("-1")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Raise a ValueError for invalid device status", "Easy")
explain("Goal:  Write a function called 'validate_status(device)'")
explain("       that raises a ValueError if the device's status is")
explain("       not 'up' or 'down'.")
explain("       If the status is valid, return True.")
blank()
explain("Rules:")
explain("  • Allowed values: 'up' and 'down' only.")
explain("  • Error message must be:")
explain("      'Invalid status: <value>'")
blank()
explain("Function signature:  validate_status(device)")
blank()
header(">>> print(validate_status(INVENTORY[0]))")
header("True")
blank()
header(">>> validate_status({'hostname': 'test', 'status': 'unknown'})")
header("ValueError: Invalid status: unknown")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Define and raise a custom exception", "Medium")
explain("Goal:  Define a custom exception class called")
explain("       'DeviceOfflineError' that inherits from Exception.")
explain("       Then write a function 'connect(device)' that raises")
explain("       DeviceOfflineError if the device status is 'down',")
explain("       or returns 'connected: <hostname>' if status is 'up'.")
blank()
explain("Function signature:  connect(device)")
blank()
header(">>> print(connect(INVENTORY[0]))")
header("'connected: nyc-rtr-01'")
blank()
header(">>> connect(INVENTORY[1])")
header("DeviceOfflineError: lon-sw-01 is offline")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Catch multiple exception types", "Medium")
explain("Goal:  Write a function called 'safe_connect(device)'")
explain("       that calls connect(device) and handles errors.")
blank()
explain("Rules:")
explain("  • If DeviceOfflineError is raised → return 'offline: <hostname>'")
explain("  • If any other Exception is raised → return 'error: <msg>'")
explain("  • If no exception → return the result of connect(device)")
blank()
explain("Function signature:  safe_connect(device)")
blank()
header(">>> print(safe_connect(INVENTORY[0]))")
header("'connected: nyc-rtr-01'")
blank()
header(">>> print(safe_connect(INVENTORY[1]))")
header("'offline: lon-sw-01'")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Process a batch with exception handling and summary", "Medium")
explain("Goal:  Write a function called 'batch_connect(inventory)'")
explain("       that calls safe_connect() on every device and")
explain("       returns a summary dict.")
blank()
explain("Rules:")
explain("  • The summary dict must have exactly three keys:")
explain("      'connected' — list of hostnames that connected")
explain("      'offline'   — list of hostnames that are offline")
explain("      'errors'    — list of hostnames that had other errors")
blank()
explain("Function signature:  batch_connect(inventory)")
blank()
header(">>> result = batch_connect(INVENTORY)")
header(">>> print(result['connected'])")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(result['offline'])")
header("['lon-sw-01', 'tok-sw-01', 'dub-fw-01']")
blank()
header(">>> print(result['errors'])")
header("[]")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Build a safe JSON parser with chained exceptions", "Hard")
explain("Goal:  Write a function called 'safe_parse_config(raw)'")
explain("       that parses a JSON string into a device config dict.")
blank()
explain("Rules:")
explain("  • Import json inside the function (or at top of file).")
explain("  • If raw is not a string → raise TypeError:")
explain("      'Expected str, got <type>'")
explain("  • If raw is not valid JSON → catch json.JSONDecodeError")
explain("    and raise ValueError:")
explain("      'Invalid JSON: <original error message>'")
explain("  • If parsed result is not a dict → raise ValueError:")
explain("      'Expected dict, got <type>'")
explain("  • If all checks pass → return the parsed dict.")
blank()
explain("Function signature:  safe_parse_config(raw)")
blank()
header(">>> print(safe_parse_config('{\"ntp\": \"10.0.0.100\"}'))")
header("{'ntp': '10.0.0.100'}")
blank()
header(">>> safe_parse_config(123)")
header("TypeError: Expected str, got <class 'int'>")
blank()
header(">>> safe_parse_config('bad json')")
header("ValueError: Invalid JSON: ...")
blank()
header(">>> safe_parse_config('[1, 2, 3]')")
header("ValueError: Expected dict, got <class 'list'>")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: exceptions_solution.py")
explain("The data is already at the top — write your answers below it.")
blank()
explain("Tips by task:")
explain("  Task 1 — try: return device[key]  except KeyError: return None")
explain("  Task 2 — try: return len(device['vlans'])  except TypeError: return -1")
explain("  Task 3 — try/except/else/finally — return in else, print in finally")
explain("  Task 4 — if status not in ('up','down'): raise ValueError(f'...')")
explain("  Task 5 — class DeviceOfflineError(Exception): pass")
explain("           def connect(d): if d['status']=='down': raise DeviceOfflineError(...)")
explain("  Task 6 — except DeviceOfflineError: ... except Exception as e: ...")
explain("  Task 7 — call safe_connect(), check the returned string prefix")
explain("  Task 8 — isinstance(raw, str), json.loads, isinstance(result, dict)")
explain("           raise ValueError(...) from e  for chained exceptions")

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
print(f"{BOLD}{CYAN}    exceptions_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 exceptions_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()