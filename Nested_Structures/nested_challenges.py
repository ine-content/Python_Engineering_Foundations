# nested_challenges.py
# Python Nested Structures — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

import os
import sys
import copy
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
NETWORK = {
    "NYC": {
        "region": "us-east",
        "devices": [
            {
                "hostname": "nyc-rtr-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "up"},
                    {"name": "Gi0/2", "vlan": 30, "state": "down"},
                ],
            },
            {
                "hostname": "nyc-sw-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 40, "state": "up"},
                ],
            },
        ],
    },
    "LON": {
        "region": "eu-west",
        "devices": [
            {
                "hostname": "lon-sw-01",
                "platform": "NX-OS",
                "status":   "down",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "down"},
                ],
            },
            {
                "hostname": "lon-fw-01",
                "platform": "ASA",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 30, "state": "up"},
                    {"name": "Gi0/1", "vlan": 50, "state": "up"},
                ],
            },
        ],
    },
    "SIN": {
        "region": "ap-southeast",
        "devices": [
            {
                "hostname": "sin-rtr-01",
                "platform": "IOS-XE",
                "status":   "up",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "up"},
                    {"name": "Gi0/2", "vlan": 50, "state": "up"},
                ],
            },
        ],
    },
}

RECORDS = [
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 20, "state": "up"},
    {"site": "NYC", "hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/2", "vlan": 30, "state": "down"},
    {"site": "NYC", "hostname": "nyc-sw-01",  "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "NYC", "hostname": "nyc-sw-01",  "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 40, "state": "up"},
    {"site": "LON", "hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "LON", "hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/1", "vlan": 20, "state": "down"},
    {"site": "LON", "hostname": "lon-fw-01",  "platform": "ASA",    "iface": "Gi0/0", "vlan": 30, "state": "up"},
    {"site": "LON", "hostname": "lon-fw-01",  "platform": "ASA",    "iface": "Gi0/1", "vlan": 50, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 20, "state": "up"},
    {"site": "SIN", "hostname": "sin-rtr-01", "platform": "IOS-XE", "iface": "Gi0/2", "vlan": 50, "state": "up"},
]

# ─────────────────────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num):
    filename = f"nested_solution_ch{challenge_num}.py"
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

    namespace = {"NETWORK": NETWORK, "RECORDS": RECORDS}
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
    if actual == expected:
        print(f"    {GREEN}✔  {task_label}: {label}{RESET}")
        return True
    else:
        print(f"    {RED}✘  {task_label}: {label}{RESET}")
        blank()
        hint(hint_text)
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
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         NESTED STRUCTURES — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have three challenges — Easy, Medium, Hard.")
explain("Each one uses NETWORK and RECORDS shown below.")
explain("Read the challenge, write your solution in the")
explain("correct file, then run this script to check it.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → nested_solution_ch1.py")
explain("  Challenge 2 (Medium) → nested_solution_ch2.py")
explain("  Challenge 3 (Hard)   → nested_solution_ch3.py")
blank()
explain("IMPORTANT: Copy NETWORK and RECORDS shown on the")
explain("next screen into the TOP of each solution file.")
explain("They are printed with NO indentation — copy directly.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW DATA
# ═════════════════════════════════════════════════════════════════════════════
section("The Data You Will Work With")

explain("NETWORK — three-level nested structure:")
explain("  site → devices (list) → interfaces (list)")
blank()
copyable("NETWORK = {")
for site, site_cfg in NETWORK.items():
    copyable(f"    '{site}': {{")
    copyable(f"        'region': '{site_cfg['region']}',")
    copyable(f"        'devices': [")
    for device in site_cfg["devices"]:
        copyable(f"            {{")
        copyable(f"                'hostname': '{device['hostname']}',")
        copyable(f"                'platform': '{device['platform']}',")
        copyable(f"                'status':   '{device['status']}',")
        copyable(f"                'interfaces': [")
        for iface in device["interfaces"]:
            copyable(f"                    {{'name': '{iface['name']}', 'vlan': {iface['vlan']}, 'state': '{iface['state']}'}},")
        copyable(f"                ],")
        copyable(f"            }},")
    copyable(f"        ],")
    copyable(f"    }},")
copyable("}")
blank()

pause()

explain("RECORDS — same data as a flat list of dicts:")
blank()
copyable("RECORDS = [")
for r in RECORDS:
    copyable(f"    {r},")
copyable("]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Basic Navigation", "Easy")

explain("Using NETWORK, produce the following.")
explain("Structure reminder: NETWORK[site]['devices'] is a list of dicts.")
explain("Each device has 'hostname', 'platform', 'status', 'interfaces'.")
blank()

pause()

section("Task A")
explain("Create a list called 'all_hostnames' containing every")
explain("hostname across all sites, in NETWORK iteration order.")
blank()
header(">>> print(all_hostnames)")
header("['nyc-rtr-01', 'nyc-sw-01', 'lon-sw-01', 'lon-fw-01', 'sin-rtr-01']")
blank()

pause()

section("Task B")
explain("Create a dict called 'site_device_count' mapping")
explain("each site name to the number of devices it has.")
blank()
header(">>> print(site_device_count)")
header("{'NYC': 2, 'LON': 2, 'SIN': 1}")
blank()

pause()

section("Task C")
explain("Create a list called 'all_interface_names' containing")
explain("every interface name across all devices and all sites.")
explain("Order: outer site loop, then device loop, then interface loop.")
blank()
header(">>> print(all_interface_names)")
header("['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/0', 'Gi0/1',")
header(" 'Gi0/0', 'Gi0/1', 'Gi0/0', 'Gi0/1',")
header(" 'Gi0/0', 'Gi0/1', 'Gi0/2']")
blank()

pause()

section("Task D")
explain("Create a dict called 'hostname_to_site' mapping")
explain("each hostname to the site it belongs to.")
blank()
header(">>> print(hostname_to_site)")
header("{'nyc-rtr-01': 'NYC', 'nyc-sw-01': 'NYC',")
header(" 'lon-sw-01':  'LON', 'lon-fw-01': 'LON',")
header(" 'sin-rtr-01': 'SIN'}")
blank()

pause()

explain("Write your solution in: nested_solution_ch1.py")
explain("Remember to paste NETWORK and RECORDS at the top.")
blank()
explain("Tips:")
explain("  Task A — two nested loops: site → devices. See Ch 6.3.")
explain("  Task B — {site: len(cfg['devices']) for site, cfg in NETWORK.items()}.")
explain("  Task C — three nested loops: site → devices → interfaces.")
explain("  Task D — {d['hostname']: site for site, cfg ...")
explain("            for d in cfg['devices']}. See Ch 6.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
ns = run_solution(1)
if ns:
    exp_hostnames = [
        d["hostname"]
        for site_cfg in NETWORK.values()
        for d in site_cfg["devices"]
    ]

    exp_site_count = {
        site: len(cfg["devices"])
        for site, cfg in NETWORK.items()
    }

    exp_iface_names = [
        iface["name"]
        for site_cfg in NETWORK.values()
        for device in site_cfg["devices"]
        for iface in device["interfaces"]
    ]

    exp_h2site = {
        d["hostname"]: site
        for site, cfg in NETWORK.items()
        for d in cfg["devices"]
    }

    grade(1, [
        (
            "Task A",
            "all_hostnames — 5 hostnames in order",
            ns.get("all_hostnames"),
            exp_hostnames,
            "See Chapter 6.3 — two nested loops over sites then devices.",
            "[d['hostname'] for site_cfg in NETWORK.values() for d in site_cfg['devices']]",
            "all_hostnames",
        ),
        (
            "Task B",
            "site_device_count — site → number of devices",
            ns.get("site_device_count"),
            exp_site_count,
            "See Chapter 6.3 — dict comprehension over NETWORK.items().",
            "{site: len(cfg['devices']) for site, cfg in NETWORK.items()}",
            "site_device_count",
        ),
        (
            "Task C",
            "all_interface_names — every interface name, 3 levels deep",
            ns.get("all_interface_names"),
            exp_iface_names,
            "See Chapter 6.3 — three nested loops: sites → devices → interfaces.",
            "[i['name'] for site_cfg in NETWORK.values() for d in site_cfg['devices'] for i in d['interfaces']]",
            "all_interface_names",
        ),
        (
            "Task D",
            "hostname_to_site — hostname → site name",
            ns.get("hostname_to_site"),
            exp_h2site,
            "See Chapter 6 — {d['hostname']: site for site, cfg in NETWORK.items() for d in cfg['devices']}.",
            "{d['hostname']: site for site, cfg in NETWORK.items() for d in cfg['devices']}",
            "hostname_to_site",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "Querying and Grouping", "Medium")

explain("Using NETWORK, produce the following.")
explain("These tasks require filtering and grouping across")
explain("multiple levels of the nested structure.")
blank()

pause()

section("Task A")
explain("Create a list called 'down_interfaces' containing")
explain("a tuple of (site, hostname, interface_name) for every")
explain("interface whose state is 'down'. Order matches")
explain("iteration order of NETWORK.")
blank()
header(">>> print(down_interfaces)")
header("[('NYC', 'nyc-rtr-01', 'Gi0/2'),")
header(" ('LON', 'lon-sw-01',  'Gi0/1')]")
blank()

pause()

section("Task B")
explain("Create a dict called 'vlan_usage' mapping each")
explain("VLAN number to a SORTED list of hostnames that")
explain("have that VLAN on at least one interface.")
blank()
header(">>> print(vlan_usage)")
header("{10: ['lon-sw-01', 'nyc-rtr-01', 'nyc-sw-01', 'sin-rtr-01'],")
header(" 20: ['lon-sw-01', 'nyc-rtr-01', 'sin-rtr-01'],")
header(" 30: ['lon-fw-01', 'nyc-rtr-01'],")
header(" 40: ['nyc-sw-01'],")
header(" 50: ['lon-fw-01', 'sin-rtr-01']}")
blank()

pause()

section("Task C")
explain("Create a dict called 'device_interface_count'")
explain("mapping each hostname to the number of interfaces it has.")
blank()
header(">>> print(device_interface_count)")
header("{'nyc-rtr-01': 3, 'nyc-sw-01': 2,")
header(" 'lon-sw-01':  2, 'lon-fw-01': 2,")
header(" 'sin-rtr-01': 3}")
blank()

pause()

section("Task D")
explain("Create a dict called 'site_vlan_summary' mapping")
explain("each site to a sorted list of unique VLANs used")
explain("across all its devices and interfaces.")
blank()
header(">>> print(site_vlan_summary)")
header("{'NYC': [10, 20, 30, 40],")
header(" 'LON': [10, 20, 30, 50],")
header(" 'SIN': [10, 20, 50]}")
blank()

pause()

explain("Write your solution in: nested_solution_ch2.py")
explain("Remember to paste NETWORK and RECORDS at the top.")
blank()
explain("Tips:")
explain("  Task A — 3-level comprehension with if iface['state']=='down'.")
explain("  Task B — setdefault(vlan, set()) then .add(hostname), then sort.")
explain("  Task C — {d['hostname']: len(d['interfaces']) ...}.")
explain("  Task D — {site: sorted(set(i['vlan'] for d ... for i ...)) ...}.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
ns = run_solution(2)
if ns:
    # Task A
    exp_down = [
        (site, d["hostname"], iface["name"])
        for site, cfg in NETWORK.items()
        for d in cfg["devices"]
        for iface in d["interfaces"]
        if iface["state"] == "down"
    ]

    # Task B
    exp_vlan_usage = {}
    for site_cfg in NETWORK.values():
        for d in site_cfg["devices"]:
            for iface in d["interfaces"]:
                vlan = iface["vlan"]
                exp_vlan_usage.setdefault(vlan, set())
                exp_vlan_usage[vlan].add(d["hostname"])
    exp_vlan_usage = {k: sorted(v) for k, v in exp_vlan_usage.items()}

    # Task C
    exp_iface_count = {
        d["hostname"]: len(d["interfaces"])
        for site_cfg in NETWORK.values()
        for d in site_cfg["devices"]
    }

    # Task D
    exp_site_vlans = {
        site: sorted(set(
            iface["vlan"]
            for d in cfg["devices"]
            for iface in d["interfaces"]
        ))
        for site, cfg in NETWORK.items()
    }

    grade(2, [
        (
            "Task A",
            "down_interfaces — (site, hostname, iface) tuples where state='down'",
            ns.get("down_interfaces"),
            exp_down,
            "See Chapter 7.2 — 3-level comprehension with 'if iface[\"state\"] == \"down\"'.",
            "[(site, d['hostname'], i['name']) for site, cfg in NETWORK.items() for d in cfg['devices'] for i in d['interfaces'] if i['state'] == 'down']",
            "down_interfaces",
        ),
        (
            "Task B",
            "vlan_usage — vlan → sorted list of hostnames using it",
            ns.get("vlan_usage"),
            exp_vlan_usage,
            "See Chapter 5.2 — setdefault(vlan, set()).add(hostname), then sort each value.",
            "vlan_usage = {}\nfor cfg in NETWORK.values():\n  for d in cfg['devices']:\n    for i in d['interfaces']:\n      vlan_usage.setdefault(i['vlan'], set()).add(d['hostname'])\nvlan_usage = {k: sorted(v) for k, v in vlan_usage.items()}",
            "vlan_usage",
        ),
        (
            "Task C",
            "device_interface_count — hostname → number of interfaces",
            ns.get("device_interface_count"),
            exp_iface_count,
            "See Chapter 7.2 — {d['hostname']: len(d['interfaces']) for all devices}.",
            "{d['hostname']: len(d['interfaces']) for cfg in NETWORK.values() for d in cfg['devices']}",
            "device_interface_count",
        ),
        (
            "Task D",
            "site_vlan_summary — site → sorted unique VLANs across all devices",
            ns.get("site_vlan_summary"),
            exp_site_vlans,
            "See Chapter 5.2 — use set() to deduplicate, then sorted().",
            "{site: sorted(set(i['vlan'] for d in cfg['devices'] for i in d['interfaces'])) for site, cfg in NETWORK.items()}",
            "site_vlan_summary",
        ),
    ])

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 3 — HARD
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(3, "Advanced Patterns", "Hard")

explain("Using NETWORK and RECORDS, produce the following.")
explain("This challenge combines querying, reshaping,")
explain("aggregating, and building complex nested results.")
blank()

pause()

section("Task A")
explain("Create a list called 'devices_all_up' containing")
explain("the hostname of every device where ALL interfaces")
explain("have state 'up'. Order matches NETWORK iteration order.")
blank()
header(">>> print(devices_all_up)")
header("['nyc-sw-01', 'lon-fw-01', 'sin-rtr-01']")
blank()

pause()

section("Task B")
explain("Using RECORDS (the flat list), rebuild the nested")
explain("structure as a dict called 'rebuilt'.")
explain("Structure: hostname → {platform, site, interfaces: [...]}")
explain("Each interface: {name, vlan, state}")
explain("Order of interfaces matches order in RECORDS.")
blank()
header(">>> print(rebuilt['nyc-rtr-01'])")
header("{'platform': 'IOS-XE', 'site': 'NYC',")
header(" 'interfaces': [{'name': 'Gi0/0', 'vlan': 10, 'state': 'up'},")
header("                {'name': 'Gi0/1', 'vlan': 20, 'state': 'up'},")
header("                {'name': 'Gi0/2', 'vlan': 30, 'state': 'down'}]}")
blank()
header(">>> print(rebuilt['sin-rtr-01'])")
header("{'platform': 'IOS-XE', 'site': 'SIN',")
header(" 'interfaces': [{'name': 'Gi0/0', 'vlan': 10, 'state': 'up'},")
header("                {'name': 'Gi0/1', 'vlan': 20, 'state': 'up'},")
header("                {'name': 'Gi0/2', 'vlan': 50, 'state': 'up'}]}")
blank()

pause()

section("Task C")
explain("Create a dict called 'site_summary' mapping each")
explain("site to a summary dict with four keys:")
explain("  'device_count'     → total devices in that site")
explain("  'total_interfaces' → total interfaces across all devices")
explain("  'up_count'         → number of interfaces with state 'up'")
explain("  'down_count'       → number of interfaces with state 'down'")
blank()
header(">>> print(site_summary['NYC'])")
header("{'device_count': 2, 'total_interfaces': 5, 'up_count': 4, 'down_count': 1}")
blank()
header(">>> print(site_summary['LON'])")
header("{'device_count': 2, 'total_interfaces': 4, 'up_count': 3, 'down_count': 1}")
blank()
header(">>> print(site_summary['SIN'])")
header("{'device_count': 1, 'total_interfaces': 3, 'up_count': 3, 'down_count': 0}")
blank()

pause()

section("Task D")
explain("Create a list called 'vlan_report' — one dict per")
explain("unique VLAN across all sites and devices.")
explain("Each dict has:")
explain("  'vlan'            → the VLAN number")
explain("  'sites'           → sorted list of sites where it appears")
explain("  'device_count'    → number of devices that have it")
explain("  'interface_count' → number of interfaces using it")
explain("Sort the list by vlan number ascending.")
blank()
header(">>> for r in vlan_report: print(r)")
header("{'vlan': 10, 'sites': ['LON','NYC','SIN'], 'device_count': 4, 'interface_count': 4}")
header("{'vlan': 20, 'sites': ['LON','NYC','SIN'], 'device_count': 3, 'interface_count': 3}")
header("{'vlan': 30, 'sites': ['LON','NYC'],       'device_count': 2, 'interface_count': 2}")
header("{'vlan': 40, 'sites': ['NYC'],             'device_count': 1, 'interface_count': 1}")
header("{'vlan': 50, 'sites': ['LON','SIN'],       'device_count': 2, 'interface_count': 2}")
blank()

pause()

explain("Write your solution in: nested_solution_ch3.py")
explain("Remember to paste NETWORK and RECORDS at the top.")
blank()
explain("Tips:")
explain("  Task A — all(i['state']=='up' for i in d['interfaces']).")
explain("  Task B — setdefault(hostname, {platform, site, interfaces:[]})")
explain("           then .append() each interface. Use RECORDS.")
explain("  Task C — {site: {'device_count': ..., 'total_interfaces': ...,")
explain("            'up_count': ..., 'down_count': ...} for site, cfg ...}.")
explain("  Task D — collect unique VLANs first, then build one dict")
explain("           per VLAN by scanning all interfaces.")

pause()

# ── Grade Challenge 3 ─────────────────────────────────────────────────────────
ns = run_solution(3)
if ns:
    # Task A
    exp_all_up = [
        d["hostname"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
        if all(i["state"] == "up" for i in d["interfaces"])
    ]

    # Task B
    exp_rebuilt = {}
    for r in RECORDS:
        h = r["hostname"]
        exp_rebuilt.setdefault(h, {
            "platform":   r["platform"],
            "site":       r["site"],
            "interfaces": [],
        })
        exp_rebuilt[h]["interfaces"].append({
            "name":  r["iface"],
            "vlan":  r["vlan"],
            "state": r["state"],
        })

    # Task C
    exp_site_summary = {
        site: {
            "device_count":     len(cfg["devices"]),
            "total_interfaces": sum(len(d["interfaces"]) for d in cfg["devices"]),
            "up_count":         sum(1 for d in cfg["devices"] for i in d["interfaces"] if i["state"] == "up"),
            "down_count":       sum(1 for d in cfg["devices"] for i in d["interfaces"] if i["state"] == "down"),
        }
        for site, cfg in NETWORK.items()
    }

    # Task D
    all_vlans = sorted(set(
        i["vlan"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
        for i in d["interfaces"]
    ))
    exp_vlan_report = sorted([
        {
            "vlan":            v,
            "sites":           sorted(set(
                                site
                                for site, cfg in NETWORK.items()
                                for d in cfg["devices"]
                                for i in d["interfaces"]
                                if i["vlan"] == v
                               )),
            "device_count":    len(set(
                                d["hostname"]
                                for cfg in NETWORK.values()
                                for d in cfg["devices"]
                                if any(i["vlan"] == v for i in d["interfaces"])
                               )),
            "interface_count": sum(
                                1
                                for cfg in NETWORK.values()
                                for d in cfg["devices"]
                                for i in d["interfaces"]
                                if i["vlan"] == v
                               ),
        }
        for v in all_vlans
    ], key=lambda x: x["vlan"])

    grade(3, [
        (
            "Task A",
            "devices_all_up — hostnames where all interfaces are 'up'",
            ns.get("devices_all_up"),
            exp_all_up,
            "See Chapter 7.2 — use all(i['state']=='up' for i in d['interfaces']).",
            "[d['hostname'] for cfg in NETWORK.values() for d in cfg['devices'] if all(i['state']=='up' for i in d['interfaces'])]",
            "devices_all_up",
        ),
        (
            "Task B",
            "rebuilt — hostname → {platform, site, interfaces} from RECORDS",
            ns.get("rebuilt"),
            exp_rebuilt,
            "See Chapter 8.1 — setdefault(hostname, {platform, site, interfaces:[]}) then append each interface.",
            "rebuilt = {}\nfor r in RECORDS:\n  rebuilt.setdefault(r['hostname'], {'platform': r['platform'], 'site': r['site'], 'interfaces': []})\n  rebuilt[r['hostname']]['interfaces'].append({'name': r['iface'], 'vlan': r['vlan'], 'state': r['state']})",
            "rebuilt",
        ),
        (
            "Task C",
            "site_summary — site → {device_count, total_interfaces, up_count, down_count}",
            ns.get("site_summary"),
            exp_site_summary,
            "See Chapter 7.2 — build one dict per site with four sum() expressions.",
            "{site: {'device_count': len(cfg['devices']), 'total_interfaces': sum(len(d['interfaces']) for d in cfg['devices']), 'up_count': sum(1 for d in cfg['devices'] for i in d['interfaces'] if i['state']=='up'), 'down_count': sum(1 for d in cfg['devices'] for i in d['interfaces'] if i['state']=='down')} for site, cfg in NETWORK.items()}",
            "site_summary",
        ),
        (
            "Task D",
            "vlan_report — sorted list of dicts with vlan stats",
            ns.get("vlan_report"),
            exp_vlan_report,
            "See Chapter 7 — collect unique VLANs first, then build one dict per VLAN.",
            "Get unique vlans with set(), then for each vlan build {vlan, sites: sorted(set(...)), device_count: len(set(...)), interface_count: sum(...)}, sort by vlan.",
            "vlan_report",
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