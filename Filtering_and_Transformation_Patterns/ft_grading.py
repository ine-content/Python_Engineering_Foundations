# ft_grading.py
# Filtering and Transformation Patterns — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in ft_solution.py
# 2. Run this script: python3 ft_grading.py
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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution():
    filename = "ft_solution.py"
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
print(f"{BOLD}         FILTERING & TRANSFORMATION — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your ft_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Expected values ────────────────────────────────────────────────────────

    # Task 1
    exp_up_ips = [d["ip"] for d in INVENTORY if d["status"] == "up"]

    # Task 2
    exp_enriched = [
        {
            "hostname":   d["hostname"],
            "platform":   d["platform"],
            "vlan_count": len(d["vlans"]),
            "status":     d["status"],
        }
        for d in INVENTORY
    ]

    # Task 3
    exp_h2ntp = {d["hostname"]: d["config"]["ntp"] for d in INVENTORY}

    # Task 4
    exp_custom_ntp = [
        d["hostname"] for d in INVENTORY
        if d["config"]["ntp"] != GLOBAL_NTP
    ]

    # Task 5
    exp_push = [
        d["hostname"] for d in INVENTORY
        if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS")
    ]
    exp_skip = [
        d["hostname"] for d in INVENTORY
        if not (d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS"))
    ]

    # Task 6
    platforms_u = sorted(set(d["platform"] for d in INVENTORY))
    exp_pg = {
        p: sorted(d["hostname"] for d in INVENTORY if d["platform"] == p)
        for p in platforms_u
    }

    # Task 7
    exp_ps = {}
    for p in platforms_u:
        devices_p = [d for d in INVENTORY if d["platform"] == p]
        exp_ps[p] = {
            "total":     len(devices_p),
            "up_count":  sum(1 for d in devices_p if d["status"] == "up"),
            "avg_vlans": sum(len(d["vlans"]) for d in devices_p) / len(devices_p),
        }

    # Task 8
    all_vlans = sorted(set(v for d in INVENTORY for v in d["vlans"]))
    exp_vu = [
        {
            "vlan":         v,
            "device_count": sum(1 for d in INVENTORY if v in d["vlans"]),
            "hostnames":    sorted(d["hostname"] for d in INVENTORY if v in d["vlans"]),
        }
        for v in all_vlans
    ]

    # Task 9
    step1 = [d for d in INVENTORY if d["status"] == "up"]
    step2 = [{**d, "vlans": [v for v in d["vlans"] if v not in RESERVED_VLANS]} for d in step1]
    step3 = [d for d in step2 if d["vlans"]]
    exp_pipeline = [
        {"hostname": d["hostname"], "platform": d["platform"], "clean_vlans": d["vlans"]}
        for d in step3
    ]

    # Task 10
    exp_report = [
        {
            "hostname":        d["hostname"],
            "status":          d["status"],
            "up_interfaces":   [i["name"] for i in d["interfaces"] if i["state"] == "up"],
            "down_interfaces": [i["name"] for i in d["interfaces"] if i["state"] == "down"],
            "all_up":          all(i["state"] == "up" for i in d["interfaces"]),
        }
        for d in INVENTORY
    ]

    # Task 11
    exp_flat = [
        {
            "hostname": d["hostname"],
            "iface":    i["name"],
            "vlan":     i["vlan"],
            "platform": d["platform"],
        }
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "up"
    ]

    # Task 12
    up_ifaces = [
        (d["platform"], i["vlan"])
        for d in INVENTORY
        for i in d["interfaces"]
        if i["state"] == "up"
    ]
    unique_vlans_d = sorted(set(vlan for _, vlan in up_ifaces))
    exp_vpm = {
        v: sorted(set(p for p, vlan in up_ifaces if vlan == v))
        for v in unique_vlans_d
    }

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_up_ips = [
        ("List comprehension",
         ["up_ips = [d['ip'] for d in INVENTORY if d['status'] == 'up']"]),
        ("For loop",
         ["up_ips = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up':",
          "        up_ips.append(d['ip'])"]),
    ]

    ways_enriched = [
        ("List comprehension",
         ["enriched = [",
          "    {",
          "        'hostname':   d['hostname'],",
          "        'platform':   d['platform'],",
          "        'vlan_count': len(d['vlans']),",
          "        'status':     d['status'],",
          "    }",
          "    for d in INVENTORY",
          "]"]),
        ("For loop",
         ["enriched = []",
          "for d in INVENTORY:",
          "    enriched.append({",
          "        'hostname':   d['hostname'],",
          "        'platform':   d['platform'],",
          "        'vlan_count': len(d['vlans']),",
          "        'status':     d['status'],",
          "    })"]),
    ]

    ways_h2ntp = [
        ("Dict comprehension",
         ["hostname_to_ntp = {d['hostname']: d['config']['ntp'] for d in INVENTORY}"]),
        ("For loop",
         ["hostname_to_ntp = {}",
          "for d in INVENTORY:",
          "    hostname_to_ntp[d['hostname']] = d['config']['ntp']"]),
    ]

    ways_custom_ntp = [
        ("List comprehension",
         ["custom_ntp_hosts = [d['hostname'] for d in INVENTORY",
          "                    if d['config']['ntp'] != GLOBAL_NTP]"]),
        ("For loop",
         ["custom_ntp_hosts = []",
          "for d in INVENTORY:",
          "    if d['config']['ntp'] != GLOBAL_NTP:",
          "        custom_ntp_hosts.append(d['hostname'])"]),
    ]

    ways_partition = [
        ("Two comprehensions",
         ["push_ready  = [d['hostname'] for d in INVENTORY",
          "               if d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS')]",
          "skip_devices = [d['hostname'] for d in INVENTORY",
          "                if not (d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS'))]"]),
        ("For loop with if/else",
         ["push_ready   = []",
          "skip_devices = []",
          "for d in INVENTORY:",
          "    if d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS'):",
          "        push_ready.append(d['hostname'])",
          "    else:",
          "        skip_devices.append(d['hostname'])"]),
    ]

    ways_pg = [
        ("Dict comprehension over sorted platforms",
         ["platforms = sorted(set(d['platform'] for d in INVENTORY))",
          "platform_groups = {",
          "    p: sorted(d['hostname'] for d in INVENTORY if d['platform'] == p)",
          "    for p in platforms",
          "}"]),
        (".setdefault() + .sort()",
         ["platform_groups = {}",
          "for d in INVENTORY:",
          "    platform_groups.setdefault(d['platform'], []).append(d['hostname'])",
          "for k in platform_groups:",
          "    platform_groups[k].sort()"]),
    ]

    ways_ps = [
        ("Dict comprehension per platform",
         ["platforms = sorted(set(d['platform'] for d in INVENTORY))",
          "platform_stats = {",
          "    p: {",
          "        'total':     sum(1 for d in INVENTORY if d['platform'] == p),",
          "        'up_count':  sum(1 for d in INVENTORY if d['platform'] == p and d['status'] == 'up'),",
          "        'avg_vlans': sum(len(d['vlans']) for d in INVENTORY if d['platform'] == p)",
          "                     / sum(1 for d in INVENTORY if d['platform'] == p),",
          "    }",
          "    for p in platforms",
          "}"]),
    ]

    ways_vu = [
        ("Collect unique vlans then build one dict per vlan",
         ["all_vlans = sorted(set(v for d in INVENTORY for v in d['vlans']))",
          "vlan_usage = [",
          "    {",
          "        'vlan':         v,",
          "        'device_count': sum(1 for d in INVENTORY if v in d['vlans']),",
          "        'hostnames':    sorted(d['hostname'] for d in INVENTORY if v in d['vlans']),",
          "    }",
          "    for v in all_vlans",
          "]"]),
    ]

    ways_pipeline = [
        ("4 separate steps",
         ["step1 = [d for d in INVENTORY if d['status'] == 'up']",
          "step2 = [{**d, 'vlans': [v for v in d['vlans'] if v not in RESERVED_VLANS]}",
          "         for d in step1]",
          "step3 = [d for d in step2 if d['vlans']]",
          "pipeline_result = [",
          "    {'hostname': d['hostname'], 'platform': d['platform'], 'clean_vlans': d['vlans']}",
          "    for d in step3",
          "]"]),
    ]

    ways_report = [
        ("List comprehension with inner comprehensions",
         ["device_report = [",
          "    {",
          "        'hostname':        d['hostname'],",
          "        'status':          d['status'],",
          "        'up_interfaces':   [i['name'] for i in d['interfaces'] if i['state'] == 'up'],",
          "        'down_interfaces': [i['name'] for i in d['interfaces'] if i['state'] == 'down'],",
          "        'all_up':          all(i['state'] == 'up' for i in d['interfaces']),",
          "    }",
          "    for d in INVENTORY",
          "]"]),
    ]

    ways_flat = [
        ("Nested comprehension with filter",
         ["interface_flat = [",
          "    {",
          "        'hostname': d['hostname'],",
          "        'iface':    i['name'],",
          "        'vlan':     i['vlan'],",
          "        'platform': d['platform'],",
          "    }",
          "    for d in INVENTORY",
          "    for i in d['interfaces']",
          "    if i['state'] == 'up'",
          "]"]),
        ("Nested for loop",
         ["interface_flat = []",
          "for d in INVENTORY:",
          "    for i in d['interfaces']:",
          "        if i['state'] == 'up':",
          "            interface_flat.append({",
          "                'hostname': d['hostname'],",
          "                'iface': i['name'],",
          "                'vlan': i['vlan'],",
          "                'platform': d['platform'],",
          "            })"]),
    ]

    ways_vpm = [
        ("Collect (platform, vlan) pairs then group by vlan",
         ["up_ifaces = [",
          "    (d['platform'], i['vlan'])",
          "    for d in INVENTORY",
          "    for i in d['interfaces']",
          "    if i['state'] == 'up'",
          "]",
          "vlans = sorted(set(v for _, v in up_ifaces))",
          "vlan_platform_map = {",
          "    v: sorted(set(p for p, vlan in up_ifaces if vlan == v))",
          "    for v in vlans",
          "}"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task  1", "up_ips — IPs of all 'up' devices",
         ns.get("up_ips"), exp_up_ips,
         "[d['ip'] for d in INVENTORY if d['status'] == 'up'].",
         ways_up_ips, "up_ips"),
        ("Task  2", "enriched — all 8 devices with hostname/platform/vlan_count/status",
         ns.get("enriched"), exp_enriched,
         "Build a dict per device with exactly 4 keys including vlan_count: len(d['vlans']).",
         ways_enriched, "enriched"),
        ("Task  3", "hostname_to_ntp — hostname → ntp server",
         ns.get("hostname_to_ntp"), exp_h2ntp,
         "{d['hostname']: d['config']['ntp'] for d in INVENTORY}.",
         ways_h2ntp, "hostname_to_ntp"),
        ("Task  4", "custom_ntp_hosts — hostnames with non-standard NTP",
         ns.get("custom_ntp_hosts"), exp_custom_ntp,
         "Filter where d['config']['ntp'] != GLOBAL_NTP.",
         ways_custom_ntp, "custom_ntp_hosts"),
        ("Task  5", "push_ready and skip_devices — correct partition",
         (ns.get("push_ready"), ns.get("skip_devices")),
         (exp_push, exp_skip),
         "Two comprehensions: one with 'up and IOS-XE/NX-OS', one negated.",
         ways_partition, "(push_ready, skip_devices)"),
        ("Task  6", "platform_groups — platform → sorted list of hostnames",
         ns.get("platform_groups"), exp_pg,
         "Get unique platforms, then {p: sorted([...]) for p in platforms}.",
         ways_pg, "platform_groups"),
        ("Task  7", "platform_stats — platform → {total, up_count, avg_vlans}",
         ns.get("platform_stats"), exp_ps,
         "Filter per platform, compute total/up_count/avg_vlans.",
         ways_ps, "platform_stats"),
        ("Task  8", "vlan_usage — sorted list of {vlan, device_count, hostnames}",
         ns.get("vlan_usage"), exp_vu,
         "Collect unique vlans with set(), sort, build one dict per vlan.",
         ways_vu, "vlan_usage"),
        ("Task  9", "pipeline_result — 4-step filtered and transformed list",
         ns.get("pipeline_result"), exp_pipeline,
         "4 steps: filter up, remove reserved vlans, filter non-empty, reshape.",
         ways_pipeline, "pipeline_result"),
        ("Task 10", "device_report — all 8 devices with interface breakdown and all_up flag",
         ns.get("device_report"), exp_report,
         "Build up_interfaces and down_interfaces with inner comprehensions, use all().",
         ways_report, "device_report"),
        ("Task 11", "interface_flat — flattened up-only interfaces across all devices",
         ns.get("interface_flat"), exp_flat,
         "Nested comprehension: for d in INVENTORY for i in d['interfaces'] if i['state']=='up'.",
         ways_flat, "interface_flat"),
        ("Task 12", "vlan_platform_map — vlan → sorted unique platforms on UP interfaces only",
         ns.get("vlan_platform_map"), exp_vpm,
         "Collect (platform, vlan) pairs from UP interfaces only, then group by vlan.",
         ways_vpm, "vlan_platform_map"),
    ], ns=ns)

pause()