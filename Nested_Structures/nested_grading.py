# nested_grading.py
# Python Nested Structures — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in nested_solution.py
# 2. Run this script: python3 nested_grading.py
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
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "nested_solution.py"
    if not os.path.exists(filename):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
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
print(f"{BOLD}         NESTED STRUCTURES — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your nested_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    exp_hostnames = [
        d["hostname"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
    ]

    # Task 2
    exp_site_count = {
        site: len(cfg["devices"])
        for site, cfg in NETWORK.items()
    }

    # Task 3
    exp_iface_names = [
        iface["name"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
        for iface in d["interfaces"]
    ]

    # Task 4
    exp_h2site = {
        d["hostname"]: site
        for site, cfg in NETWORK.items()
        for d in cfg["devices"]
    }

    # Task 5
    exp_down = [
        (site, d["hostname"], iface["name"])
        for site, cfg in NETWORK.items()
        for d in cfg["devices"]
        for iface in d["interfaces"]
        if iface["state"] == "down"
    ]

    # Task 6
    exp_vlan_usage = {}
    for cfg in NETWORK.values():
        for d in cfg["devices"]:
            for iface in d["interfaces"]:
                exp_vlan_usage.setdefault(iface["vlan"], set()).add(d["hostname"])
    exp_vlan_usage = {k: sorted(v) for k, v in exp_vlan_usage.items()}

    # Task 7
    exp_iface_count = {
        d["hostname"]: len(d["interfaces"])
        for cfg in NETWORK.values()
        for d in cfg["devices"]
    }

    # Task 8
    exp_site_vlans = {
        site: sorted(set(
            iface["vlan"]
            for d in cfg["devices"]
            for iface in d["interfaces"]
        ))
        for site, cfg in NETWORK.items()
    }

    # Task 9
    exp_all_up = [
        d["hostname"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
        if all(i["state"] == "up" for i in d["interfaces"])
    ]

    # Task 10
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

    # Task 11
    exp_site_summary = {
        site: {
            "device_count":     len(cfg["devices"]),
            "total_interfaces": sum(len(d["interfaces"]) for d in cfg["devices"]),
            "up_count":         sum(1 for d in cfg["devices"] for i in d["interfaces"] if i["state"] == "up"),
            "down_count":       sum(1 for d in cfg["devices"] for i in d["interfaces"] if i["state"] == "down"),
        }
        for site, cfg in NETWORK.items()
    }

    # Task 12
    all_vlans = sorted(set(
        i["vlan"]
        for cfg in NETWORK.values()
        for d in cfg["devices"]
        for i in d["interfaces"]
    ))
    exp_vlan_report = [
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
    ]

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_hostnames = [
        ("Nested list comprehension",
         ["all_hostnames = [d['hostname']",
          "    for cfg in NETWORK.values()",
          "    for d in cfg['devices']]"]),
        ("Nested for loop",
         ["all_hostnames = []",
          "for cfg in NETWORK.values():",
          "    for d in cfg['devices']:",
          "        all_hostnames.append(d['hostname'])"]),
    ]

    ways_site_count = [
        ("Dict comprehension",
         ["site_device_count = {site: len(cfg['devices'])",
          "    for site, cfg in NETWORK.items()}"]),
        ("For loop",
         ["site_device_count = {}",
          "for site, cfg in NETWORK.items():",
          "    site_device_count[site] = len(cfg['devices'])"]),
    ]

    ways_iface_names = [
        ("Nested list comprehension",
         ["all_interface_names = [iface['name']",
          "    for cfg in NETWORK.values()",
          "    for d in cfg['devices']",
          "    for iface in d['interfaces']]"]),
        ("Nested for loop",
         ["all_interface_names = []",
          "for cfg in NETWORK.values():",
          "    for d in cfg['devices']:",
          "        for iface in d['interfaces']:",
          "            all_interface_names.append(iface['name'])"]),
    ]

    ways_h2site = [
        ("Nested dict comprehension",
         ["hostname_to_site = {d['hostname']: site",
          "    for site, cfg in NETWORK.items()",
          "    for d in cfg['devices']}"]),
        ("Nested for loop",
         ["hostname_to_site = {}",
          "for site, cfg in NETWORK.items():",
          "    for d in cfg['devices']:",
          "        hostname_to_site[d['hostname']] = site"]),
    ]

    ways_down = [
        ("Nested list comprehension with filter",
         ["down_interfaces = [(site, d['hostname'], iface['name'])",
          "    for site, cfg in NETWORK.items()",
          "    for d in cfg['devices']",
          "    for iface in d['interfaces']",
          "    if iface['state'] == 'down']"]),
        ("Nested for loop with if",
         ["down_interfaces = []",
          "for site, cfg in NETWORK.items():",
          "    for d in cfg['devices']:",
          "        for iface in d['interfaces']:",
          "            if iface['state'] == 'down':",
          "                down_interfaces.append((site, d['hostname'], iface['name']))"]),
    ]

    ways_vlan_usage = [
        (".setdefault() with set() then sort",
         ["vlan_usage = {}",
          "for cfg in NETWORK.values():",
          "    for d in cfg['devices']:",
          "        for iface in d['interfaces']:",
          "            vlan_usage.setdefault(iface['vlan'], set()).add(d['hostname'])",
          "vlan_usage = {k: sorted(v) for k, v in vlan_usage.items()}"]),
    ]

    ways_iface_count = [
        ("Nested dict comprehension",
         ["device_interface_count = {d['hostname']: len(d['interfaces'])",
          "    for cfg in NETWORK.values()",
          "    for d in cfg['devices']}"]),
        ("Nested for loop",
         ["device_interface_count = {}",
          "for cfg in NETWORK.values():",
          "    for d in cfg['devices']:",
          "        device_interface_count[d['hostname']] = len(d['interfaces'])"]),
    ]

    ways_site_vlans = [
        ("Dict comprehension with set()",
         ["site_vlan_summary = {",
          "    site: sorted(set(",
          "        iface['vlan']",
          "        for d in cfg['devices']",
          "        for iface in d['interfaces']",
          "    ))",
          "    for site, cfg in NETWORK.items()",
          "}"]),
        ("For loop with set()",
         ["site_vlan_summary = {}",
          "for site, cfg in NETWORK.items():",
          "    vlans = set()",
          "    for d in cfg['devices']:",
          "        for iface in d['interfaces']:",
          "            vlans.add(iface['vlan'])",
          "    site_vlan_summary[site] = sorted(vlans)"]),
    ]

    ways_all_up = [
        ("Nested comprehension with all()",
         ["devices_all_up = [d['hostname']",
          "    for cfg in NETWORK.values()",
          "    for d in cfg['devices']",
          "    if all(i['state'] == 'up' for i in d['interfaces'])]"]),
        ("For loop with all()",
         ["devices_all_up = []",
          "for cfg in NETWORK.values():",
          "    for d in cfg['devices']:",
          "        if all(i['state'] == 'up' for i in d['interfaces']):",
          "            devices_all_up.append(d['hostname'])"]),
    ]

    ways_rebuilt = [
        (".setdefault() + .append()",
         ["rebuilt = {}",
          "for r in RECORDS:",
          "    h = r['hostname']",
          "    rebuilt.setdefault(h, {",
          "        'platform': r['platform'],",
          "        'site': r['site'],",
          "        'interfaces': [],",
          "    })",
          "    rebuilt[h]['interfaces'].append({",
          "        'name': r['iface'], 'vlan': r['vlan'], 'state': r['state'],",
          "    })"]),
    ]

    ways_site_summary = [
        ("Dict comprehension with sum()",
         ["site_summary = {",
          "    site: {",
          "        'device_count':     len(cfg['devices']),",
          "        'total_interfaces': sum(len(d['interfaces']) for d in cfg['devices']),",
          "        'up_count':         sum(1 for d in cfg['devices'] for i in d['interfaces'] if i['state'] == 'up'),",
          "        'down_count':       sum(1 for d in cfg['devices'] for i in d['interfaces'] if i['state'] == 'down'),",
          "    }",
          "    for site, cfg in NETWORK.items()",
          "}"]),
        ("For loop",
         ["site_summary = {}",
          "for site, cfg in NETWORK.items():",
          "    ifaces = [i for d in cfg['devices'] for i in d['interfaces']]",
          "    site_summary[site] = {",
          "        'device_count':     len(cfg['devices']),",
          "        'total_interfaces': len(ifaces),",
          "        'up_count':         sum(1 for i in ifaces if i['state'] == 'up'),",
          "        'down_count':       sum(1 for i in ifaces if i['state'] == 'down'),",
          "    }"]),
    ]

    ways_vlan_report = [
        ("Collect unique VLANs then build one dict per VLAN",
         ["all_vlans = sorted(set(",
          "    i['vlan']",
          "    for cfg in NETWORK.values()",
          "    for d in cfg['devices']",
          "    for i in d['interfaces']",
          "))",
          "vlan_report = [",
          "    {",
          "        'vlan': v,",
          "        'sites': sorted(set(site for site, cfg in NETWORK.items()",
          "                        for d in cfg['devices']",
          "                        for i in d['interfaces'] if i['vlan'] == v)),",
          "        'device_count': len(set(d['hostname'] for cfg in NETWORK.values()",
          "                            for d in cfg['devices']",
          "                            if any(i['vlan'] == v for i in d['interfaces']))),",
          "        'interface_count': sum(1 for cfg in NETWORK.values()",
          "                           for d in cfg['devices']",
          "                           for i in d['interfaces'] if i['vlan'] == v),",
          "    }",
          "    for v in all_vlans",
          "]"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task  1", "all_hostnames — 5 hostnames in order",
         ns.get("all_hostnames"), exp_hostnames,
         "Two nested loops: for cfg in NETWORK.values() → for d in cfg['devices'].",
         ways_hostnames, "all_hostnames"),
        ("Task  2", "site_device_count — site → number of devices",
         ns.get("site_device_count"), exp_site_count,
         "Dict comprehension: {site: len(cfg['devices']) for site, cfg in NETWORK.items()}.",
         ways_site_count, "site_device_count"),
        ("Task  3", "all_interface_names — every interface name, 3 levels deep",
         ns.get("all_interface_names"), exp_iface_names,
         "Three nested loops: sites → devices → interfaces.",
         ways_iface_names, "all_interface_names"),
        ("Task  4", "hostname_to_site — hostname → site name",
         ns.get("hostname_to_site"), exp_h2site,
         "Nested dict comprehension: {d['hostname']: site for site, cfg in NETWORK.items() for d in cfg['devices']}.",
         ways_h2site, "hostname_to_site"),
        ("Task  5", "down_interfaces — (site, hostname, iface) tuples where state='down'",
         ns.get("down_interfaces"), exp_down,
         "3-level comprehension with 'if iface[\"state\"] == \"down\"'.",
         ways_down, "down_interfaces"),
        ("Task  6", "vlan_usage — vlan → sorted list of hostnames",
         ns.get("vlan_usage"), exp_vlan_usage,
         "setdefault(vlan, set()).add(hostname), then sort each value.",
         ways_vlan_usage, "vlan_usage"),
        ("Task  7", "device_interface_count — hostname → number of interfaces",
         ns.get("device_interface_count"), exp_iface_count,
         "{d['hostname']: len(d['interfaces']) for all devices}.",
         ways_iface_count, "device_interface_count"),
        ("Task  8", "site_vlan_summary — site → sorted unique VLANs",
         ns.get("site_vlan_summary"), exp_site_vlans,
         "Use set() to deduplicate VLANs per site, then sorted().",
         ways_site_vlans, "site_vlan_summary"),
        ("Task  9", "devices_all_up — hostnames where all interfaces are 'up'",
         ns.get("devices_all_up"), exp_all_up,
         "Use all(i['state'] == 'up' for i in d['interfaces']).",
         ways_all_up, "devices_all_up"),
        ("Task 10", "rebuilt — hostname → {platform, site, interfaces} from RECORDS",
         ns.get("rebuilt"), exp_rebuilt,
         "setdefault(hostname, {platform, site, interfaces:[]}) then append each interface.",
         ways_rebuilt, "rebuilt"),
        ("Task 11", "site_summary — site → {device_count, total_interfaces, up_count, down_count}",
         ns.get("site_summary"), exp_site_summary,
         "Build one dict per site with four sum() expressions.",
         ways_site_summary, "site_summary"),
        ("Task 12", "vlan_report — sorted list of dicts with vlan stats",
         ns.get("vlan_report"), exp_vlan_report,
         "Collect unique VLANs first, then build one dict per VLAN.",
         ways_vlan_report, "vlan_report"),
    ])

pause()