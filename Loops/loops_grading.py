# loops_grading.py
# Python Loops — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in loops_solution.py
# 2. Run this script: python3 loops_grading.py
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
INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
            {"name": "Gi0/2", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
        ],
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
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
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "down"},
            {"name": "Gi0/1", "vlan": 30, "state": "down"},
        ],
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "up"},
            {"name": "Gi0/2", "vlan": 50, "state": "down"},
        ],
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
        ],
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "interfaces": [
            {"name": "Gi0/0", "vlan": 20, "state": "up"},
            {"name": "Gi0/1", "vlan": 30, "state": "up"},
            {"name": "Gi0/2", "vlan": 40, "state": "up"},
            {"name": "Gi0/3", "vlan": 50, "state": "up"},
        ],
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "loops_solution.py"
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
        # If the expected answer is None, only mark as correct when the
        # student has explicitly defined the variable in their solution.
        # This prevents an unattempted task from passing by accident.
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
print(f"{BOLD}         LOOPS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your loops_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    exp_counts = {}
    for d in INVENTORY:
        exp_counts[d["platform"]] = exp_counts.get(d["platform"], 0) + 1

    # Task 2
    exp_numbered = [
        f"{i}. {d['hostname']} ({d['platform']})"
        for i, d in enumerate(INVENTORY, start=1)
    ]

    # Task 3
    seen_v = set()
    for d in INVENTORY:
        for v in d["vlans"]:
            seen_v.add(v)
    exp_vlans = sorted(seen_v)

    # Task 4
    regions = ["us-east","eu-west","ap-se","eu-central",
               "ap-ne","au-east","eu-west","ap-south"]
    exp_regions = [f"{d['hostname']} \u2192 {r}" for d, r in zip(INVENTORY, regions)]

    # Task 5
    exp_down = [
        f"{d['hostname']} | {i['name']} | {i['vlan']}"
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "down"
    ]

    # Task 6
    exp_first_nxos = None
    for d in INVENTORY:
        if d["platform"] == "NX-OS" and d["status"] == "up":
            exp_first_nxos = d["hostname"]
            break

    # Task 7
    exp_iface_summary = []
    for d in INVENTORY:
        for i in d["interfaces"]:
            if i["state"] != "up":
                continue
            if i["vlan"] <= 20:
                continue
            exp_iface_summary.append({
                "hostname": d["hostname"],
                "iface":    i["name"],
                "vlan":     i["vlan"],
            })

    # Task 8
    exp_max_host  = ""
    exp_max_count = 0
    for d in INVENTORY:
        if len(d["interfaces"]) > exp_max_count:
            exp_max_count = len(d["interfaces"])
            exp_max_host  = d["hostname"]

    # Task 9
    hostnames = [d["hostname"] for d in INVENTORY]
    exp_batches = [hostnames[i:i+3] for i in range(0, len(hostnames), 3)]

    # Task 10
    vlan_feed = [10, 30, 10, 20, 50, 30, 40, 20, 10, 50]
    seen_u = set()
    exp_unique = []
    for v in vlan_feed:
        if v not in seen_u:
            exp_unique.append(v)
            seen_u.add(v)

    # Task 11
    queue_orig = ["lon-sw-01", "nyc-rtr-01", "sin-fw-01", "nyc-sw-01"]
    exp_failed  = []
    exp_success = []
    q = queue_orig.copy()
    while q:
        device = q.pop(0)
        if device.startswith("nyc"):
            exp_success.append(device)
        else:
            exp_failed.append(device)

    # Task 12
    sorted_vlans = [10, 20, 30, 40, 50, 100, 200]
    exp_gaps = [
        {
            "from_vlan": sorted_vlans[i],
            "to_vlan":   sorted_vlans[i+1],
            "gap":       sorted_vlans[i+1] - sorted_vlans[i],
        }
        for i in range(len(sorted_vlans) - 1)
    ]

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_counts = [
        ("For loop with .get()",
         ["platform_counts = {}",
          "for d in INVENTORY:",
          "    p = d['platform']",
          "    platform_counts[p] = platform_counts.get(p, 0) + 1"]),
        ("For loop with .setdefault()",
         ["platform_counts = {}",
          "for d in INVENTORY:",
          "    platform_counts.setdefault(d['platform'], 0)",
          "    platform_counts[d['platform']] += 1"]),
    ]

    ways_numbered = [
        ("enumerate() in list comprehension",
         ["numbered = [f'{i}. {d[\"hostname\"]} ({d[\"platform\"]})'",
          "           for i, d in enumerate(INVENTORY, start=1)]"]),
        ("For loop with enumerate()",
         ["numbered = []",
          "for i, d in enumerate(INVENTORY, start=1):",
          "    numbered.append(f'{i}. {d[\"hostname\"]} ({d[\"platform\"]})')"]),
    ]

    ways_vlans = [
        ("set() then sorted()",
         ["seen = set()",
          "for d in INVENTORY:",
          "    for v in d['vlans']:",
          "        seen.add(v)",
          "all_vlans = sorted(seen)"]),
        ("set comprehension",
         ["all_vlans = sorted({v for d in INVENTORY for v in d['vlans']})"]),
    ]

    ways_regions = [
        ("zip() in list comprehension",
         ["regions = ['us-east','eu-west','ap-se','eu-central',",
          "           'ap-ne','au-east','eu-west','ap-south']",
          "device_regions = [f\"{d['hostname']} \u2192 {r}\" for d, r in zip(INVENTORY, regions)]"]),
        ("For loop with zip()",
         ["device_regions = []",
          "for d, r in zip(INVENTORY, regions):",
          "    device_regions.append(f\"{d['hostname']} \u2192 {r}\")"]),
    ]

    ways_down = [
        ("Nested list comprehension",
         ["down_report = [",
          "    f\"{d['hostname']} | {i['name']} | {i['vlan']}\"",
          "    for d in INVENTORY",
          "    for i in d['interfaces']",
          "    if i['state'] == 'down'",
          "]"]),
        ("Nested for loop",
         ["down_report = []",
          "for d in INVENTORY:",
          "    for i in d['interfaces']:",
          "        if i['state'] == 'down':",
          "            down_report.append(f\"{d['hostname']} | {i['name']} | {i['vlan']}\")"]),
    ]

    ways_first_nxos = [
        ("For loop with break",
         ["first_nxos_up = None",
          "for d in INVENTORY:",
          "    if d['platform'] == 'NX-OS' and d['status'] == 'up':",
          "        first_nxos_up = d['hostname']",
          "        break"]),
        ("next() with generator",
         ["first_nxos_up = next(",
          "    (d['hostname'] for d in INVENTORY",
          "     if d['platform'] == 'NX-OS' and d['status'] == 'up'),",
          "    None",
          ")"]),
    ]

    ways_iface_summary = [
        ("Nested loops with continue",
         ["interface_summary = []",
          "for d in INVENTORY:",
          "    for i in d['interfaces']:",
          "        if i['state'] != 'up': continue",
          "        if i['vlan'] <= 20: continue",
          "        interface_summary.append({",
          "            'hostname': d['hostname'],",
          "            'iface': i['name'],",
          "            'vlan': i['vlan'],",
          "        })"]),
        ("Nested comprehension with filter",
         ["interface_summary = [",
          "    {'hostname': d['hostname'], 'iface': i['name'], 'vlan': i['vlan']}",
          "    for d in INVENTORY",
          "    for i in d['interfaces']",
          "    if i['state'] == 'up' and i['vlan'] > 20",
          "]"]),
    ]

    ways_max = [
        ("For loop with running max",
         ["most_interfaces_host  = ''",
          "most_interfaces_count = 0",
          "for d in INVENTORY:",
          "    if len(d['interfaces']) > most_interfaces_count:",
          "        most_interfaces_count = len(d['interfaces'])",
          "        most_interfaces_host  = d['hostname']"]),
        ("max() with key",
         ["best = max(INVENTORY, key=lambda d: len(d['interfaces']))",
          "most_interfaces_host  = best['hostname']",
          "most_interfaces_count = len(best['interfaces'])"]),
    ]

    ways_batches = [
        ("range() with step + slice",
         ["hostnames = [d['hostname'] for d in INVENTORY]",
          "batches = [hostnames[i:i+3] for i in range(0, len(hostnames), 3)]"]),
        ("For loop with range()",
         ["hostnames = [d['hostname'] for d in INVENTORY]",
          "batches = []",
          "for i in range(0, len(hostnames), 3):",
          "    batches.append(hostnames[i:i+3])"]),
    ]

    ways_unique = [
        ("For loop with seen set",
         ["vlan_feed = [10, 30, 10, 20, 50, 30, 40, 20, 10, 50]",
          "seen = set()",
          "unique_vlans_ordered = []",
          "for v in vlan_feed:",
          "    if v not in seen:",
          "        unique_vlans_ordered.append(v)",
          "        seen.add(v)"]),
        ("dict.fromkeys() — preserves order in Python 3.7+",
         ["unique_vlans_ordered = list(dict.fromkeys(vlan_feed))"]),
    ]

    ways_while = [
        ("while loop with pop(0)",
         ["queue = ['lon-sw-01', 'nyc-rtr-01', 'sin-fw-01', 'nyc-sw-01']",
          "failed_devices  = []",
          "success_devices = []",
          "while queue:",
          "    device = queue.pop(0)",
          "    if device.startswith('nyc'):",
          "        success_devices.append(device)",
          "    else:",
          "        failed_devices.append(device)"]),
    ]

    ways_gaps = [
        ("range() sliding window",
         ["sorted_vlans = [10, 20, 30, 40, 50, 100, 200]",
          "vlan_gaps = [",
          "    {",
          "        'from_vlan': sorted_vlans[i],",
          "        'to_vlan':   sorted_vlans[i+1],",
          "        'gap':       sorted_vlans[i+1] - sorted_vlans[i],",
          "    }",
          "    for i in range(len(sorted_vlans) - 1)",
          "]"]),
        ("zip() with offset slice",
         ["vlan_gaps = [",
          "    {'from_vlan': a, 'to_vlan': b, 'gap': b - a}",
          "    for a, b in zip(sorted_vlans, sorted_vlans[1:])",
          "]"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task  1", "platform_counts — platform → count",
         ns.get("platform_counts"), exp_counts,
         "counts[p] = counts.get(p, 0) + 1 inside a for loop.",
         ways_counts, "platform_counts"),
        ("Task  2", "numbered — 'N. hostname (platform)' from 1",
         ns.get("numbered"), exp_numbered,
         "enumerate(INVENTORY, start=1) gives (number, device) pairs.",
         ways_numbered, "numbered"),
        ("Task  3", "all_vlans — sorted unique VLANs across all devices",
         ns.get("all_vlans"), exp_vlans,
         "Build a set(), nested loop over d['vlans'], then sorted().",
         ways_vlans, "all_vlans"),
        ("Task  4", "device_regions — 'hostname → region' via zip()",
         ns.get("device_regions"), exp_regions,
         "zip(INVENTORY, regions) gives (device, region) pairs.",
         ways_regions, "device_regions"),
        ("Task  5", "down_report — 'hostname | iface | vlan' for all down interfaces",
         ns.get("down_report"), exp_down,
         "Nested loops: for d in INVENTORY, for i in d['interfaces'], if i['state']=='down'.",
         ways_down, "down_report"),
        ("Task  6", "first_nxos_up — hostname of first NX-OS + up device (or None)",
         ns.get("first_nxos_up"), exp_first_nxos,
         "For loop + if + break. Initialise first_nxos_up = None before the loop.",
         ways_first_nxos, "first_nxos_up"),
        ("Task  7", "interface_summary — dicts for up interfaces with vlan > 20",
         ns.get("interface_summary"), exp_iface_summary,
         "Nested loops with continue to skip state!='up' or vlan<=20.",
         ways_iface_summary, "interface_summary"),
        ("Task  8", "most_interfaces_host and most_interfaces_count",
         (ns.get("most_interfaces_host"), ns.get("most_interfaces_count")),
         (exp_max_host, exp_max_count),
         "Track max_count and max_host in loop: if len(d['interfaces']) > max_count.",
         ways_max, "(most_interfaces_host, most_interfaces_count)"),
        ("Task  9", "batches — hostnames chunked into groups of 3",
         ns.get("batches"), exp_batches,
         "range(0, len(INVENTORY), 3), slice hostnames[i:i+3].",
         ways_batches, "batches"),
        ("Task 10", "unique_vlans_ordered — deduplicated, order preserved",
         ns.get("unique_vlans_ordered"), exp_unique,
         "seen=set(), for v in vlan_feed: if v not in seen: append(v) and seen.add(v).",
         ways_unique, "unique_vlans_ordered"),
        ("Task 11", "failed_devices and success_devices from while queue loop",
         (ns.get("failed_devices"), ns.get("success_devices")),
         (exp_failed, exp_success),
         "while queue: device=queue.pop(0), if device.startswith('nyc') → success else failed.",
         ways_while, "(failed_devices, success_devices)"),
        ("Task 12", "vlan_gaps — sliding window dicts with from/to/gap",
         ns.get("vlan_gaps"), exp_gaps,
         "range(len(sorted_vlans)-1), access [i] and [i+1] to build each dict.",
         ways_gaps, "vlan_gaps"),
    ], ns=ns)

pause()