# functions_challenges.py
# Python Functions — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: functions_solution.py
# 3. Run functions_grading.py to check your answers

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

# ═════════════════════════════════════════════════════════════════════════════
# INTRO
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         FUNCTIONS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use INVENTORY, GLOBAL_NTP, and RESERVED_VLANS.")
explain("You will write FUNCTIONS — the grader calls them with test data.")
explain("Read each task, write your solution in functions_solution.py,")
explain("then run functions_grading.py to check it.")
blank()
explain("The data is already pasted at the top of")
explain("functions_solution.py — just write your functions below it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Classify a device by hostname", "Easy")
explain("Goal:  Write a function called 'classify_device(hostname)'")
explain("       that takes a hostname string and returns a device type.")
blank()
explain("Rules:")
explain("  • 'rtr' in hostname → return 'router'")
explain("  • 'sw'  in hostname → return 'switch'")
explain("  • 'fw'  in hostname → return 'firewall'")
explain("  • anything else     → return 'unknown'")
blank()
explain("Function signature:  classify_device(hostname)")
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

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Get hostnames of UP devices", "Easy")
explain("Goal:  Write a function called 'get_up_devices(inventory)'")
explain("       that returns a list of hostnames whose status is 'up'.")
blank()
explain("Function signature:  get_up_devices(inventory)")
blank()
header(">>> print(get_up_devices(INVENTORY))")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Count devices by platform", "Easy")
explain("Goal:  Write a function called 'count_by_platform(inventory)'")
explain("       that returns a dict mapping each platform to how")
explain("       many devices use it.")
blank()
explain("Function signature:  count_by_platform(inventory)")
blank()
header(">>> print(count_by_platform(INVENTORY))")
header("{'IOS-XE': 4, 'NX-OS': 2, 'ASA': 2}")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Enrich a device dict", "Easy")
explain("Goal:  Write a function called 'enrich_device(device)'")
explain("       that takes a single device dict and returns a NEW dict")
explain("       with all original fields PLUS three computed fields.")
blank()
explain("Rules:")
explain("  • Keep all existing fields using {**device, ...}")
explain("  • Add 'vlan_count'  → len(d['vlans'])")
explain("  • Add 'iface_count' → len(d['interfaces'])")
explain("  • Add 'device_type' → result of classify_device(hostname)")
blank()
explain("Function signature:  enrich_device(device)")
blank()
header(">>> print(enrich_device(INVENTORY[0]))")
header("{'hostname': 'nyc-rtr-01', ..., 'vlan_count': 3, 'iface_count': 3, 'device_type': 'router'}")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Filter devices by platform with optional status", "Medium")
explain("Goal:  Write a function called 'get_devices_by_platform'")
explain("       with an optional status filter.")
blank()
explain("Function signature:")
header("  def get_devices_by_platform(inventory, platform, status=None):")
blank()
explain("Rules:")
explain("  • Always filter by platform.")
explain("  • If status is provided, also filter by status.")
explain("  • If status is None (default), return all for that platform.")
explain("  • Returns a list of hostnames.")
blank()
header(">>> print(get_devices_by_platform(INVENTORY, 'IOS-XE'))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(get_devices_by_platform(INVENTORY, 'NX-OS', status='down'))")
header("['lon-sw-01', 'tok-sw-01']")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "Validate a device with guard clauses", "Medium")
explain("Goal:  Write a function called 'validate_device'")
explain("       using guard clauses (early return).")
blank()
explain("Function signature:")
header("  def validate_device(device, global_ntp=GLOBAL_NTP):")
blank()
explain("Rules (check in order, return on first failure):")
explain("  1. status != 'up'                → (False, 'device is down')")
explain("  2. platform not in supported     → (False, 'unsupported platform')")
explain("     supported: IOS-XE, NX-OS, ASA, IOS-XR")
explain("  3. no vlans configured           → (False, 'no vlans')")
explain("  4. ntp differs from global_ntp  → (False, 'custom ntp')")
explain("  all pass                         → (True,  'valid')")
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

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Partition devices by status", "Medium")
explain("Goal:  Write a function called 'partition_by_status(inventory)'")
explain("       that returns TWO lists as a tuple: (up_hostnames, down_hostnames).")
blank()
explain("Function signature:  partition_by_status(inventory)")
blank()
header(">>> up, down = partition_by_status(INVENTORY)")
header(">>> print(up)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(down)")
header("['lon-sw-01', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Generate NTP config with *args and keyword-only arg", "Medium")
explain("Goal:  Write a function called 'generate_ntp_config'")
explain("       that accepts multiple NTP servers and a keyword-only")
explain("       argument to control preferencing.")
blank()
explain("Function signature:")
header("  def generate_ntp_config(hostname, *ntp_servers, prefer_first=True):")
blank()
explain("Rules:")
explain("  • Each NTP server gets a line: 'ntp server <ip>'")
explain("  • If prefer_first=True, add ' prefer' to the FIRST server only.")
blank()
header(">>> print(generate_ntp_config('nyc-rtr-01', '10.0.0.100', '10.0.0.101'))")
header("ntp server 10.0.0.100 prefer")
header("ntp server 10.0.0.101")
blank()
header(">>> print(generate_ntp_config('lon-sw-01', '10.0.0.100', prefer_first=False))")
header("ntp server 10.0.0.100")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Apply multiple filter functions with *args", "Hard")
explain("Goal:  Write a function called 'apply_filter'")
explain("       that accepts any number of filter functions and")
explain("       returns only devices that pass ALL of them.")
blank()
explain("Function signature:")
header("  def apply_filter(inventory, *filter_fns):")
blank()
explain("Rules:")
explain("  • A device is included only if it passes EVERY filter function.")
explain("  • Returns a list of hostnames.")
blank()
header(">>> is_up    = lambda d: d['status'] == 'up'")
header(">>> is_iosxe = lambda d: d['platform'] == 'IOS-XE'")
header(">>> has_vlans = lambda d: len(d['vlans']) > 2")
blank()
header(">>> print(apply_filter(INVENTORY, is_up, is_iosxe))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()
header(">>> print(apply_filter(INVENTORY, is_up, is_iosxe, has_vlans))")
header("['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Build config from **kwargs", "Hard")
explain("Goal:  Write a function called 'build_config'")
explain("       that generates a multi-line config string from")
explain("       keyword arguments.")
blank()
explain("Function signature:")
header("  def build_config(hostname, **settings):")
blank()
explain("Rules:")
explain("  • First line is always 'hostname <hostname>'.")
explain("  • Each keyword argument adds a line: '<key> <value>'")
explain("  • Convert underscores in keys to spaces.")
explain("    e.g. ip_domain_name='corp.net' → 'ip domain-name corp.net'")
blank()
header(">>> print(build_config('nyc-rtr-01', ntp='10.0.0.100', ip_domain_name='corp.net'))")
header("hostname nyc-rtr-01")
header("ntp 10.0.0.100")
header("ip domain-name corp.net")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Run a multi-step pipeline", "Hard")
explain("Goal:  Write a function called 'run_pipeline'")
explain("       that applies a sequence of step functions in order,")
explain("       passing the output of each step as input to the next.")
blank()
explain("Function signature:")
header("  def run_pipeline(data, *steps):")
blank()
explain("Rules:")
explain("  • Apply each step function in sequence.")
explain("  • Each step receives the output of the previous step.")
explain("  • Return the final result.")
blank()
header(">>> def step_filter_up(inv):")
header("...     return [d for d in inv if d['status'] == 'up']")
blank()
header(">>> def step_hostnames(inv):")
header("...     return [d['hostname'] for d in inv]")
blank()
header(">>> result = run_pipeline(INVENTORY, step_filter_up, step_hostnames)")
header(">>> print(result)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Return a sort function (factory function)", "Hard")
explain("Goal:  Write a function called 'make_sorter'")
explain("       that RETURNS a new function which sorts a list of dicts.")
blank()
explain("Function signature:")
header("  def make_sorter(key_field, reverse=False):")
blank()
explain("Rules:")
explain("  • make_sorter returns a function — not a sorted list.")
explain("  • The returned function accepts a list of dicts and")
explain("    returns them sorted by key_field in the given direction.")
blank()
header(">>> sort_by_hostname = make_sorter('hostname')")
header(">>> sorted_list = sort_by_hostname(INVENTORY)")
header(">>> print([d['hostname'] for d in sorted_list])")
header("['ams-rtr-02', 'dub-fw-01', 'lon-sw-01', 'mum-rtr-01',")
header(" 'nyc-rtr-01', 'sin-fw-01', 'syd-rtr-01', 'tok-sw-01']")
blank()
header(">>> sort_by_vlans = make_sorter('vlan_count', reverse=True)")
header(">>> enriched = [{**d, 'vlan_count': len(d['vlans'])} for d in INVENTORY]")
header(">>> sorted_vlans = sort_by_vlans(enriched)")
header(">>> print([(d['hostname'], d['vlan_count']) for d in sorted_vlans])")
header("[('ams-rtr-02',4),('mum-rtr-01',4),('nyc-rtr-01',3),('sin-fw-01',3),")
header(" ('syd-rtr-01',3),('dub-fw-01',3),('lon-sw-01',2),('tok-sw-01',2)]")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: functions_solution.py")
explain("The data is already at the top — write your functions below it.")
blank()
explain("Tips by task:")
explain("  Task  1 — if 'rtr' in hostname: return 'router' elif ...")
explain("  Task  2 — return [d['hostname'] for d in inventory if d['status'] == 'up']")
explain("  Task  3 — counts[p] = counts.get(p, 0) + 1 pattern")
explain("  Task  4 — return {**device, 'vlan_count': len(device['vlans']), ...}")
explain("  Task  5 — def func(inventory, platform, status=None): filter on both")
explain("  Task  6 — early return for each failed check, return (True, 'valid') at end")
explain("  Task  7 — return up_list, down_list  (Python returns a tuple)")
explain("  Task  8 — *ntp_servers collects all IPs, prefer_first keyword-only arg")
explain("  Task  9 — all(fn(d) for fn in filter_fns)")
explain("  Task 10 — iterate settings.items(), k.replace('_', ' ')")
explain("  Task 11 — result = data; for step in steps: result = step(result)")
explain("  Task 12 — return lambda lst: sorted(lst, key=lambda d: d[key_field], ...)")

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
print(f"{BOLD}{CYAN}    functions_solution.py{RESET}")
print()
print(f"{BOLD}  When you are ready to check your answers, run:{RESET}")
print()
print(f"{BOLD}{CYAN}    python3 functions_grading.py{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()