# lists_grading.py
# Python Lists — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in lists_solution.py
# 2. Run this script: python3 lists_grading.py
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

def header(text):
    print(f"    {CYAN}{text}{RESET}")

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
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
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
    else:
        print(f"    {GREEN}{expected}{RESET}")
    blank()


def grade(checks):
    total = len(checks)

    # ── Run all checks silently ────────────────────────────────────────────────
    results = []
    passed = 0
    for task_label, label, actual, expected, hint_text, solution_ways, var_name in checks:
        ok = (actual == expected)
        if ok:
            passed += 1
        results.append((task_label, label, ok, actual, expected, hint_text, solution_ways, var_name))

    # ── Show score first ───────────────────────────────────────────────────────
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

    # ── Walk through each task review one by one ───────────────────────────────
    blank()
    explain("Press ENTER to review each task — solutions are shown for all tasks.")
    for task_label, label, ok, actual, expected, hint_text, solution_ways, var_name in results:
        pause()
        show_task_review(task_label, label, ok, actual, expected, hint_text, solution_ways, var_name)

    # ── Final message based on score ───────────────────────────────────────────
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
print(f"{BOLD}         PYTHON LISTS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your lists_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────
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

    # ── Solution ways ──────────────────────────────────────────────────────────
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

    # ── Run grade ──────────────────────────────────────────────────────────────
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