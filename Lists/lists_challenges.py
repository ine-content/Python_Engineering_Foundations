# lists_challenges_merged.py
# Python Lists — Student Challenge (Merged)
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read each task carefully
# 2. Write your solution in a file called: lists_solution.py
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
    print(f"{CYAN}{text}{RESET}")

def fail(text):
    print(f"    {RED}✘  {text}{RESET}")

def hint(text):
    print(f"    {YELLOW}💡 Hint: {text}{RESET}")

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
def run_solution():
    import sys
    filename = "lists_solution.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
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
        fail("Your script raised an error:")
        print()
        traceback.print_exc()
        blank()
        return None


def check(task_label, label, actual, expected, hint_text, solution_ways, var_name):
    if actual == expected:
        print(f"    {GREEN}✔  {task_label}: {label}{RESET}")
        return True
    else:
        print(f"    {RED}✘  {task_label}: {label}{RESET}")
        blank()
        hint(hint_text)
        blank()
        print(f"    {YELLOW}Ways to write the solution:{RESET}")
        for way_label, way_code in solution_ways:
            print(f"    {YELLOW}  ▸ {way_label}{RESET}")
            for line in way_code:
                print(f"    {CYAN}    {line}{RESET}")
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


def grade(checks):
    blank()
    section("Grading your solution...")
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        if check(task_label, label, actual, expected, hint_text, solution_ways, var_name):
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
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON LISTS — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("12 tasks — Easy, Medium, and Hard — all in one challenge.")
explain("All tasks use the same device INVENTORY list.")
explain("Read each task, write your solution in the file below,")
explain("then run this script to check it.")
blank()
explain("File to create:  lists_solution.py")
blank()
explain("IMPORTANT: Copy the INVENTORY list shown on the next")
explain("screen into the TOP of your solution file.")
explain("Your solution will not work without it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW INVENTORY
# ═════════════════════════════════════════════════════════════════════════════
section("The INVENTORY You Will Work With")
explain("Copy this entire block into the TOP of your solution file.")
explain("It is printed with NO indentation so you can copy it directly.")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
explain("Your solution file should start like this:")
blank()
copyable("# lists_solution.py")
copyable("")
copyable("INVENTORY = [")
copyable("    {'hostname': 'nyc-rtr-01', ...},")
copyable("    ...")
copyable("]")
copyable("")
copyable("# your answers below — one variable per task")
copyable("all_hostnames = [...]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# TASKS
# ═════════════════════════════════════════════════════════════════════════════

# ── Task 1 ────────────────────────────────────────────────────────────────────
task_section(1, "Extract all hostnames", "Easy")
explain("Goal:  Build a list of the hostname of every device.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  all_hostnames")
blank()
header(">>> print(all_hostnames)")
header("['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02',")
header(" 'tok-sw-01', 'syd-rtr-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 2 ────────────────────────────────────────────────────────────────────
task_section(2, "Filter devices that are UP", "Easy")
explain("Goal:  Build a list of hostnames for devices whose")
explain("       status is 'up' only.")
blank()
explain("Rules:")
explain("  • Skip any device whose status is 'down'.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  up_hostnames")
blank()
header(">>> print(up_hostnames)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'syd-rtr-01', 'mum-rtr-01']")
blank()

pause()

# ── Task 3 ────────────────────────────────────────────────────────────────────
task_section(3, "Count devices that are DOWN", "Easy")
explain("Goal:  Count how many devices have status 'down'.")
blank()
explain("Rules:")
explain("  • Store the result as a single integer (not a list).")
blank()
explain("Variable name:  down_count")
blank()
header(">>> print(down_count)")
header("3")
blank()

pause()

# ── Task 4 ────────────────────────────────────────────────────────────────────
task_section(4, "Extract platforms in UPPERCASE", "Easy")
explain("Goal:  Build a list of the platform of every device,")
explain("       converted to UPPERCASE.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Keep the same order as INVENTORY.")
explain("  • Each platform string must be fully uppercase.")
blank()
explain("Variable name:  platforms")
blank()
header(">>> print(platforms)")
header("['IOS-XE', 'NX-OS', 'ASA', 'IOS-XE', 'NX-OS', 'IOS-XE', 'ASA', 'IOS-XE']")
blank()

pause()

# ── Task 5 ────────────────────────────────────────────────────────────────────
task_section(5, "Flatten all VLANs into one list", "Medium")
explain("Goal:  Build a single flat list containing every VLAN ID")
explain("       from every device.")
blank()
explain("Rules:")
explain("  • Each device has a 'vlans' key with a list of VLAN IDs.")
explain("  • Outer loop must follow INVENTORY order.")
explain("  • Inner loop must follow each device's vlan list order.")
explain("  • Do NOT remove duplicates — keep every occurrence.")
blank()
explain("Variable name:  all_vlans")
blank()
header(">>> print(all_vlans)")
header("[10, 20, 30, 10, 20, 30, 40, 50, 10, 20, 30, 40, 20, 30,")
header(" 10, 40, 50, 10, 20, 30, 20, 30, 40, 50]")
blank()

pause()

# ── Task 6 ────────────────────────────────────────────────────────────────────
task_section(6, "List unique VLANs in ascending order", "Medium")
explain("Goal:  Build a sorted list of unique VLAN IDs that")
explain("       appear across the entire inventory.")
blank()
explain("Rules:")
explain("  • Each VLAN ID must appear exactly once.")
explain("  • Sort ascending (lowest number first).")
explain("  • You may use all_vlans from Task 5 as a starting point.")
blank()
explain("Variable name:  unique_vlans")
blank()
header(">>> print(unique_vlans)")
header("[10, 20, 30, 40, 50]")
blank()

pause()

# ── Task 7 ────────────────────────────────────────────────────────────────────
task_section(7, "Find devices carrying VLAN 30", "Medium")
explain("Goal:  Build a list of hostnames for every device")
explain("       that has VLAN 30 in its vlan list.")
blank()
explain("Rules:")
explain("  • Check each device's 'vlans' list for the value 30.")
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  vlan_30_devices")
blank()
header(">>> print(vlan_30_devices)")
header("['nyc-rtr-01', 'sin-fw-01', 'ams-rtr-02', 'tok-sw-01', 'dub-fw-01']")
blank()

pause()

# ── Task 8 ────────────────────────────────────────────────────────────────────
task_section(8, "Summarise devices with more than 2 VLANs", "Medium")
explain("Goal:  Build a list of dicts — one dict per device that")
explain("       has MORE THAN 2 VLANs — sorted by vlan_count")
explain("       descending (highest count first).")
blank()
explain("Rules:")
explain("  • Only include devices where len(vlans) > 2.")
explain("  • Each dict must have exactly two keys:")
explain("      'hostname'   — the device hostname")
explain("      'vlan_count' — the number of VLANs on that device")
explain("  • Sort by vlan_count descending.")
blank()
explain("Variable name:  vlan_summary")
blank()
header(">>> print(vlan_summary)")
header("[{'hostname': 'mum-rtr-01', 'vlan_count': 4},")
header(" {'hostname': 'ams-rtr-02', 'vlan_count': 4},")
header(" {'hostname': 'sin-fw-01',  'vlan_count': 3},")
header(" {'hostname': 'nyc-rtr-01', 'vlan_count': 3},")
header(" {'hostname': 'syd-rtr-01', 'vlan_count': 3},")
header(" {'hostname': 'dub-fw-01',  'vlan_count': 3}]")
blank()

pause()

# ── Task 9 ────────────────────────────────────────────────────────────────────
task_section(9, "Generate IOS-XE config blocks", "Hard")
explain("Goal:  Build a list of multi-line config strings — one")
explain("       string per device that is BOTH 'up' AND 'IOS-XE'.")
blank()
explain("Rules:")
explain("  • Skip any device that is 'down' or not 'IOS-XE'.")
explain(r"  • Each config string must use \n to separate these three lines:")
blank()
header("  'hostname <hostname>\\n ntp server 10.0.0.100\\n ip domain-name corp.net'")
blank()
explain("  • Keep the same order as INVENTORY.")
blank()
explain("Variable name:  config_blocks")
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

# ── Task 10 ───────────────────────────────────────────────────────────────────
task_section(10, "Build IP to hostname pairs sorted by hostname", "Hard")
explain("Goal:  Build a list of strings in the format")
explain("       'ip --> hostname' for ALL 8 devices,")
explain("       sorted alphabetically by hostname.")
blank()
explain("Rules:")
explain("  • Include every device regardless of status or platform.")
explain("  • Format each string exactly as:  'x.x.x.x --> hostname'")
explain("  • Sort the final list by the hostname part (A to Z).")
blank()
explain("Variable name:  ip_hostname_pairs")
blank()
header(">>> print(ip_hostname_pairs)")
header("['10.3.0.1 --> ams-rtr-02', '10.6.0.1 --> dub-fw-01',")
header(" '10.1.0.1 --> lon-sw-01',  '10.7.0.1 --> mum-rtr-01',")
header(" '10.0.0.1 --> nyc-rtr-01', '10.2.0.1 --> sin-fw-01',")
header(" '10.5.0.1 --> syd-rtr-01', '10.4.0.1 --> tok-sw-01']")
blank()

pause()

# ── Task 11 ───────────────────────────────────────────────────────────────────
task_section(11, "Number every device in the inventory", "Hard")
explain("Goal:  Build a list of strings that label each device")
explain("       with a sequential number.")
blank()
explain("Rules:")
explain("  • Include all 8 devices.")
explain("  • Numbering starts at 1 and follows INVENTORY order.")
explain("  • Format each string exactly as:")
explain("      'N. hostname (platform) \u2014 status'")
explain("    where N is the device's position number.")
blank()
explain("Variable name:  numbered_inventory")
blank()
header(">>> print(numbered_inventory)")
header("['1. nyc-rtr-01 (IOS-XE) \u2014 up',")
header(" '2. lon-sw-01 (NX-OS) \u2014 down',")
header(" '3. sin-fw-01 (ASA) \u2014 up',")
header(" '4. ams-rtr-02 (IOS-XE) \u2014 up',")
header(" '5. tok-sw-01 (NX-OS) \u2014 down',")
header(" '6. syd-rtr-01 (IOS-XE) \u2014 up',")
header(" '7. dub-fw-01 (ASA) \u2014 down',")
header(" '8. mum-rtr-01 (IOS-XE) \u2014 up']")
blank()

pause()

# ── Task 12 ───────────────────────────────────────────────────────────────────
task_section(12, "Group devices by platform", "Hard")
explain("Goal:  Build a list of dicts — one dict per unique platform")
explain("       — summarising the total device count and how many")
explain("       of those devices are currently 'up'.")
blank()
explain("Rules:")
explain("  • One dict per unique platform (3 platforms total).")
explain("  • Sort the list alphabetically by platform name.")
explain("  • Each dict must have exactly three keys:")
explain("      'platform' — the platform name (e.g. 'IOS-XE')")
explain("      'count'    — total devices with that platform")
explain("      'up_count' — devices with that platform AND status 'up'")
blank()
explain("Variable name:  platform_groups")
blank()
header(">>> print(platform_groups)")
header("[{'platform': 'ASA',    'count': 2, 'up_count': 1},")
header(" {'platform': 'IOS-XE', 'count': 4, 'up_count': 4},")
header(" {'platform': 'NX-OS',  'count': 2, 'up_count': 0}]")
blank()

pause()

# ── Tips ──────────────────────────────────────────────────────────────────────
explain("Write your solution in: lists_solution.py")
explain("Remember to paste INVENTORY at the top of your file.")
blank()
explain("Tips by task:")
explain("  Task  1 — list comprehension: [d['hostname'] for d in INVENTORY]")
explain("  Task  2 — add an if clause:   [... if d['status'] == 'up']")
explain("  Task  3 — sum() with a generator expression")
explain("  Task  4 — call .upper() inside the comprehension")
explain("  Task  5 — nested comprehension: [v for d in INVENTORY for v in d['vlans']]")
explain("  Task  6 — sorted(set(all_vlans))")
explain("  Task  7 — use 'in' operator: if 30 in d['vlans']")
explain("  Task  8 — build dicts in comprehension, filter > 2, sort with key=lambda")
explain("  Task  9 — double filter: if d['status'] == 'up' and d['platform'] == 'IOS-XE'")
explain("  Task 10 — sorted(..., key=lambda s: s.split(' --> ')[1])")
explain("  Task 11 — enumerate(INVENTORY, start=1)")
explain("  Task 12 — get unique platforms with set(), sort, build one dict per platform")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# GRADE
# ═════════════════════════════════════════════════════════════════════════════
ns = run_solution()
if ns:

    expected_all_hostnames = [d["hostname"] for d in INVENTORY]
    expected_up_hostnames  = [d["hostname"] for d in INVENTORY if d["status"] == "up"]
    expected_down_count    = sum(1 for d in INVENTORY if d["status"] == "down")
    expected_platforms     = [d["platform"].upper() for d in INVENTORY]

    expected_all_vlans   = [v for d in INVENTORY for v in d["vlans"]]
    expected_unique      = sorted(set(expected_all_vlans))
    expected_vlan30      = [d["hostname"] for d in INVENTORY if 30 in d["vlans"]]
    expected_summary_raw = [{"hostname": d["hostname"], "vlan_count": len(d["vlans"])}
                             for d in INVENTORY if len(d["vlans"]) > 2]
    expected_summary     = sorted(expected_summary_raw, key=lambda x: x["vlan_count"], reverse=True)

    expected_configs = [
        f"hostname {d['hostname']}\n ntp server 10.0.0.100\n ip domain-name corp.net"
        for d in INVENTORY if d["status"] == "up" and d["platform"] == "IOS-XE"
    ]
    expected_pairs = sorted(
        [f"{d['ip']} --> {d['hostname']}" for d in INVENTORY],
        key=lambda s: s.split(" --> ")[1]
    )
    expected_numbered = [
        f"{i}. {d['hostname']} ({d['platform']}) \u2014 {d['status']}"
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

    ways_all_hostnames = [
        ("List comprehension",
         ["all_hostnames = [d['hostname'] for d in INVENTORY]"]),
        ("For loop",
         ["all_hostnames = []",
          "for d in INVENTORY:",
          "    all_hostnames.append(d['hostname'])"]),
        ("map()",
         ["all_hostnames = list(map(lambda d: d['hostname'], INVENTORY))"]),
    ]
    ways_up_hostnames = [
        ("List comprehension with filter",
         ["up_hostnames = [d['hostname'] for d in INVENTORY if d['status'] == 'up']"]),
        ("For loop with if",
         ["up_hostnames = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up':",
          "        up_hostnames.append(d['hostname'])"]),
        ("filter() + map()",
         ["up_hostnames = list(map(lambda d: d['hostname'],",
          "    filter(lambda d: d['status'] == 'up', INVENTORY)))"]),
    ]
    ways_down_count = [
        ("sum() with generator",
         ["down_count = sum(1 for d in INVENTORY if d['status'] == 'down')"]),
        ("len() with comprehension",
         ["down_count = len([d for d in INVENTORY if d['status'] == 'down'])"]),
        ("For loop counter",
         ["down_count = 0",
          "for d in INVENTORY:",
          "    if d['status'] == 'down':",
          "        down_count += 1"]),
    ]
    ways_platforms = [
        ("List comprehension with .upper()",
         ["platforms = [d['platform'].upper() for d in INVENTORY]"]),
        ("For loop",
         ["platforms = []",
          "for d in INVENTORY:",
          "    platforms.append(d['platform'].upper())"]),
        ("map()",
         ["platforms = list(map(lambda d: d['platform'].upper(), INVENTORY))"]),
    ]
    ways_all_vlans = [
        ("Nested list comprehension",
         ["all_vlans = [v for d in INVENTORY for v in d['vlans']]"]),
        ("For loop (nested)",
         ["all_vlans = []",
          "for d in INVENTORY:",
          "    for v in d['vlans']:",
          "        all_vlans.append(v)"]),
        ("sum() to flatten",
         ["all_vlans = sum([d['vlans'] for d in INVENTORY], [])"]),
    ]
    ways_unique_vlans = [
        ("sorted(set(...))",
         ["unique_vlans = sorted(set(all_vlans))"]),
        ("Manual dedup with for loop",
         ["seen = []",
          "for v in all_vlans:",
          "    if v not in seen:",
          "        seen.append(v)",
          "unique_vlans = sorted(seen)"]),
        ("dict.fromkeys() to deduplicate",
         ["unique_vlans = sorted(dict.fromkeys(all_vlans))"]),
    ]
    ways_vlan30 = [
        ("List comprehension with 'in'",
         ["vlan_30_devices = [d['hostname'] for d in INVENTORY if 30 in d['vlans']]"]),
        ("For loop",
         ["vlan_30_devices = []",
          "for d in INVENTORY:",
          "    if 30 in d['vlans']:",
          "        vlan_30_devices.append(d['hostname'])"]),
        ("filter()",
         ["vlan_30_devices = [d['hostname'] for d in",
          "    filter(lambda d: 30 in d['vlans'], INVENTORY)]"]),
    ]
    ways_vlan_summary = [
        ("Comprehension + sorted()",
         ["vlan_summary = sorted(",
          "    [{'hostname': d['hostname'], 'vlan_count': len(d['vlans'])}",
          "     for d in INVENTORY if len(d['vlans']) > 2],",
          "    key=lambda x: x['vlan_count'], reverse=True",
          ")"]),
        ("For loop then sort",
         ["vlan_summary = []",
          "for d in INVENTORY:",
          "    if len(d['vlans']) > 2:",
          "        vlan_summary.append({'hostname': d['hostname'], 'vlan_count': len(d['vlans'])})",
          "vlan_summary.sort(key=lambda x: x['vlan_count'], reverse=True)"]),
    ]
    ways_configs = [
        ("List comprehension with f-string and double filter",
         ["config_blocks = [",
          "    f\"hostname {d['hostname']}\\n ntp server 10.0.0.100\\n ip domain-name corp.net\"",
          "    for d in INVENTORY",
          "    if d['status'] == 'up' and d['platform'] == 'IOS-XE'",
          "]"]),
        ("For loop with if",
         ["config_blocks = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up' and d['platform'] == 'IOS-XE':",
          "        block = f\"hostname {d['hostname']}\\n ntp server 10.0.0.100\\n ip domain-name corp.net\"",
          "        config_blocks.append(block)"]),
        ("For loop with '\\n'.join()",
         ["config_blocks = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up' and d['platform'] == 'IOS-XE':",
          "        lines = [f\"hostname {d['hostname']}\",",
          "                 \" ntp server 10.0.0.100\",",
          "                 \" ip domain-name corp.net\"]",
          "        config_blocks.append('\\n'.join(lines))"]),
    ]
    ways_pairs = [
        ("Comprehension + sorted() with lambda",
         ["ip_hostname_pairs = sorted(",
          "    [f\"{d['ip']} --> {d['hostname']}\" for d in INVENTORY],",
          "    key=lambda s: s.split(' --> ')[1]",
          ")"]),
        ("For loop then sort",
         ["ip_hostname_pairs = []",
          "for d in INVENTORY:",
          "    ip_hostname_pairs.append(f\"{d['ip']} --> {d['hostname']}\")",
          "ip_hostname_pairs.sort(key=lambda s: s.split(' --> ')[1])"]),
        ("Sort INVENTORY first, then build strings",
         ["ip_hostname_pairs = [",
          "    f\"{d['ip']} --> {d['hostname']}\"",
          "    for d in sorted(INVENTORY, key=lambda d: d['hostname'])",
          "]"]),
    ]
    ways_numbered = [
        ("Comprehension with enumerate()",
         ["numbered_inventory = [",
          "    f\"{i}. {d['hostname']} ({d['platform']}) \u2014 {d['status']}\"",
          "    for i, d in enumerate(INVENTORY, start=1)",
          "]"]),
        ("For loop with manual counter",
         ["numbered_inventory = []",
          "i = 1",
          "for d in INVENTORY:",
          "    numbered_inventory.append(f\"{i}. {d['hostname']} ({d['platform']}) \u2014 {d['status']}\")",
          "    i += 1"]),
        ("range() + index",
         ["numbered_inventory = [",
          "    f\"{i+1}. {INVENTORY[i]['hostname']} ({INVENTORY[i]['platform']}) \u2014 {INVENTORY[i]['status']}\"",
          "    for i in range(len(INVENTORY))",
          "]"]),
    ]
    ways_groups = [
        ("set() + sorted() + comprehension",
         ["platforms_unique = sorted(set(d['platform'] for d in INVENTORY))",
          "platform_groups = [",
          "    {",
          "        'platform': p,",
          "        'count':    sum(1 for d in INVENTORY if d['platform'] == p),",
          "        'up_count': sum(1 for d in INVENTORY if d['platform'] == p and d['status'] == 'up'),",
          "    }",
          "    for p in platforms_unique",
          "]"]),
        ("For loop building a dict of dicts, then convert",
         ["groups = {}",
          "for d in INVENTORY:",
          "    p = d['platform']",
          "    if p not in groups:",
          "        groups[p] = {'platform': p, 'count': 0, 'up_count': 0}",
          "    groups[p]['count'] += 1",
          "    if d['status'] == 'up':",
          "        groups[p]['up_count'] += 1",
          "platform_groups = sorted(groups.values(), key=lambda x: x['platform'])"]),
    ]

    grade([
        ("Task  1", "all_hostnames — all 8 hostnames in INVENTORY order",
         ns.get("all_hostnames"), expected_all_hostnames,
         "See Chapter 8 — list comprehensions.",
         ways_all_hostnames, "all_hostnames"),
        ("Task  2", "up_hostnames — hostnames where status == 'up'",
         ns.get("up_hostnames"), expected_up_hostnames,
         "See Chapter 8.2 — add an if clause to your comprehension.",
         ways_up_hostnames, "up_hostnames"),
        ("Task  3", "down_count — integer count of devices with status 'down'",
         ns.get("down_count"), expected_down_count,
         "See Chapter 9 — sum() with a generator expression.",
         ways_down_count, "down_count"),
        ("Task  4", "platforms — platform of every device, uppercase",
         ns.get("platforms"), expected_platforms,
         "See Chapter 8.1 — call .upper() inside the comprehension.",
         ways_platforms, "platforms"),
        ("Task  5", "all_vlans — every VLAN from every device, flattened",
         ns.get("all_vlans"), expected_all_vlans,
         "See Chapter 8.5 — nested list comprehension: [v for d in INVENTORY for v in d['vlans']]",
         ways_all_vlans, "all_vlans"),
        ("Task  6", "unique_vlans — deduplicated VLANs sorted ascending",
         ns.get("unique_vlans"), expected_unique,
         "See Chapters 6 & 9 — wrap all_vlans in set() to deduplicate, then sorted().",
         ways_unique_vlans, "unique_vlans"),
        ("Task  7", "vlan_30_devices — hostnames of devices that carry VLAN 30",
         ns.get("vlan_30_devices"), expected_vlan30,
         "See Chapter 4.1 — use the 'in' operator: if 30 in d['vlans']",
         ways_vlan30, "vlan_30_devices"),
        ("Task  8", "vlan_summary — {hostname, vlan_count} for devices with >2 VLANs, sorted desc",
         ns.get("vlan_summary"), expected_summary,
         "See Chapter 6.2 — build dicts in comprehension, filter len > 2, sort with key=lambda.",
         ways_vlan_summary, "vlan_summary"),
        ("Task  9", "config_blocks — config strings for IOS-XE + up devices",
         ns.get("config_blocks"), expected_configs,
         "See Chapter 8.3 — double filter with 'and'; use \\n inside f-string.",
         ways_configs, "config_blocks"),
        ("Task 10", "ip_hostname_pairs — 'ip --> hostname' strings sorted by hostname",
         ns.get("ip_hostname_pairs"), expected_pairs,
         "See Chapter 6 — build the f-strings first, then sorted() with key=lambda.",
         ways_pairs, "ip_hostname_pairs"),
        ("Task 11", "numbered_inventory — '1. hostname (platform) \u2014 status' for all 8",
         ns.get("numbered_inventory"), expected_numbered,
         "See Chapter 3.2 — use enumerate(INVENTORY, start=1).",
         ways_numbered, "numbered_inventory"),
        ("Task 12", "platform_groups — [{platform, count, up_count}] sorted by platform",
         ns.get("platform_groups"), expected_groups,
         "See Chapters 8 & 9 — collect unique platforms with set(), sort, build one dict per platform.",
         ways_groups, "platform_groups"),
    ])

pause()

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}   All tasks complete.{RESET}")
print(f"{BOLD}   You are ready for the next topic.{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()