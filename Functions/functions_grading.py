# functions_grading.py
# Python Functions — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in functions_solution.py
# 2. Run this script: python3 functions_grading.py
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
    filename = "functions_solution.py"
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
print(f"{BOLD}         FUNCTIONS — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your functions_solution.py ...")
blank()

ns = run_solution()
if ns:

    # ── Pull functions from student namespace ──────────────────────────────────
    classify_fn    = ns.get("classify_device")
    get_up_fn      = ns.get("get_up_devices")
    count_fn       = ns.get("count_by_platform")
    enrich_fn      = ns.get("enrich_device")
    by_plat_fn     = ns.get("get_devices_by_platform")
    validate_fn    = ns.get("validate_device")
    partition_fn   = ns.get("partition_by_status")
    ntp_cfg_fn     = ns.get("generate_ntp_config")
    apply_filter_fn = ns.get("apply_filter")
    build_cfg_fn   = ns.get("build_config")
    pipeline_fn    = ns.get("run_pipeline")
    sorter_fn      = ns.get("make_sorter")

    # ── Expected values (reference implementations) ────────────────────────────

    # Task 1
    def _classify(hostname):
        if "rtr" in hostname:   return "router"
        elif "sw" in hostname:  return "switch"
        elif "fw" in hostname:  return "firewall"
        else:                   return "unknown"

    classify_results = [classify_fn(h) for h in ["nyc-rtr-01","lon-sw-01","sin-fw-01","ams-rtr-02","abc-xyz-01"]] if classify_fn else None
    exp_classify = [_classify(h) for h in ["nyc-rtr-01","lon-sw-01","sin-fw-01","ams-rtr-02","abc-xyz-01"]]

    # Task 2
    get_up_results = get_up_fn(INVENTORY) if get_up_fn else None
    exp_up = [d["hostname"] for d in INVENTORY if d["status"] == "up"]

    # Task 3
    count_results = count_fn(INVENTORY) if count_fn else None
    exp_counts = {}
    for d in INVENTORY:
        exp_counts[d["platform"]] = exp_counts.get(d["platform"], 0) + 1

    # Task 4
    def _enrich(device):
        h = device["hostname"]
        return {**device, "vlan_count": len(device["vlans"]),
                "iface_count": len(device["interfaces"]),
                "device_type": _classify(h)}

    enrich_results = enrich_fn(INVENTORY[0]) if enrich_fn else None
    exp_enrich = _enrich(INVENTORY[0])

    # Task 5
    byp_all  = by_plat_fn(INVENTORY, "IOS-XE") if by_plat_fn else None
    byp_up   = by_plat_fn(INVENTORY, "IOS-XE", status="up") if by_plat_fn else None
    byp_down = by_plat_fn(INVENTORY, "NX-OS", status="down") if by_plat_fn else None
    byp_result = (byp_all, byp_up, byp_down)
    exp_byp = (
        [d["hostname"] for d in INVENTORY if d["platform"] == "IOS-XE"],
        [d["hostname"] for d in INVENTORY if d["platform"] == "IOS-XE" and d["status"] == "up"],
        [d["hostname"] for d in INVENTORY if d["platform"] == "NX-OS" and d["status"] == "down"],
    )

    # Task 6
    def _validate(device, global_ntp=GLOBAL_NTP):
        if device["status"] != "up":                                         return (False, "device is down")
        if device["platform"] not in ("IOS-XE","NX-OS","ASA","IOS-XR"):     return (False, "unsupported platform")
        if not device.get("vlans"):                                          return (False, "no vlans")
        if device.get("config", {}).get("ntp") != global_ntp:               return (False, "custom ntp")
        return (True, "valid")

    val_results = [validate_fn(d) for d in INVENTORY] if validate_fn else None
    exp_val = [_validate(d) for d in INVENTORY]

    # Task 7
    part_result = partition_fn(INVENTORY) if partition_fn else None
    exp_part = (
        [d["hostname"] for d in INVENTORY if d["status"] == "up"],
        [d["hostname"] for d in INVENTORY if d["status"] == "down"],
    )

    # Task 8
    ntp_r1 = ntp_cfg_fn("nyc-rtr-01", "10.0.0.100", "10.0.0.101") if ntp_cfg_fn else None
    ntp_r2 = ntp_cfg_fn("lon-sw-01",  "10.0.0.100", prefer_first=False) if ntp_cfg_fn else None
    ntp_result = (ntp_r1, ntp_r2)
    exp_ntp = (
        "ntp server 10.0.0.100 prefer\nntp server 10.0.0.101",
        "ntp server 10.0.0.100",
    )

    # Task 9
    is_up_fn_l    = lambda d: d["status"] == "up"
    is_iosxe_fn_l = lambda d: d["platform"] == "IOS-XE"
    has_vlans_fn_l = lambda d: len(d["vlans"]) > 2

    af1 = apply_filter_fn(INVENTORY, is_up_fn_l, is_iosxe_fn_l) if apply_filter_fn else None
    af2 = apply_filter_fn(INVENTORY, is_up_fn_l, is_iosxe_fn_l, has_vlans_fn_l) if apply_filter_fn else None
    af_result = (af1, af2)
    exp_af = (
        [d["hostname"] for d in INVENTORY if d["status"] == "up" and d["platform"] == "IOS-XE"],
        [d["hostname"] for d in INVENTORY if d["status"] == "up" and d["platform"] == "IOS-XE" and len(d["vlans"]) > 2],
    )

    # Task 10
    bc1 = build_cfg_fn("nyc-rtr-01", ntp="10.0.0.100", ip_domain_name="corp.net") if build_cfg_fn else None
    bc2 = build_cfg_fn("lon-sw-01",  dns="8.8.8.8") if build_cfg_fn else None
    bc_result = (bc1, bc2)

    def _build_cfg(hostname, **settings):
        lines = [f"hostname {hostname}"]
        for k, v in settings.items():
            lines.append(f"{k.replace('_', ' ')} {v}")
        return "\n".join(lines)

    exp_bc = (
        _build_cfg("nyc-rtr-01", ntp="10.0.0.100", ip_domain_name="corp.net"),
        _build_cfg("lon-sw-01",  dns="8.8.8.8"),
    )

    # Task 11
    def step_filter_up(inv):  return [d for d in inv if d["status"] == "up"]
    def step_hostnames(inv):  return [d["hostname"] for d in inv]

    rp_result = pipeline_fn(INVENTORY, step_filter_up, step_hostnames) if pipeline_fn else None
    exp_rp = step_hostnames(step_filter_up(INVENTORY))

    # Task 12
    enriched_inv = [{**d, "vlan_count": len(d["vlans"])} for d in INVENTORY]
    sorted_names = sorter_fn("hostname")(INVENTORY) if sorter_fn else None
    sorted_vlans = sorter_fn("vlan_count", reverse=True)(enriched_inv) if sorter_fn else None
    ms_result = (
        [d["hostname"] for d in sorted_names] if sorted_names else None,
        [(d["hostname"], d["vlan_count"]) for d in sorted_vlans] if sorted_vlans else None,
    )
    exp_sn = sorted(INVENTORY, key=lambda d: d["hostname"])
    exp_sv = sorted(enriched_inv, key=lambda d: d["vlan_count"], reverse=True)
    exp_ms = (
        [d["hostname"] for d in exp_sn],
        [(d["hostname"], d["vlan_count"]) for d in exp_sv],
    )

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_classify = [
        ("if/elif/else",
         ["def classify_device(hostname):",
          "    if 'rtr' in hostname:   return 'router'",
          "    elif 'sw' in hostname:  return 'switch'",
          "    elif 'fw' in hostname:  return 'firewall'",
          "    return 'unknown'"]),
    ]

    ways_get_up = [
        ("List comprehension",
         ["def get_up_devices(inventory):",
          "    return [d['hostname'] for d in inventory if d['status'] == 'up']"]),
        ("For loop",
         ["def get_up_devices(inventory):",
          "    result = []",
          "    for d in inventory:",
          "        if d['status'] == 'up':",
          "            result.append(d['hostname'])",
          "    return result"]),
    ]

    ways_count = [
        ("For loop with .get()",
         ["def count_by_platform(inventory):",
          "    counts = {}",
          "    for d in inventory:",
          "        p = d['platform']",
          "        counts[p] = counts.get(p, 0) + 1",
          "    return counts"]),
    ]

    ways_enrich = [
        ("{**device, ...} spread",
         ["def enrich_device(device):",
          "    return {",
          "        **device,",
          "        'vlan_count':  len(device['vlans']),",
          "        'iface_count': len(device['interfaces']),",
          "        'device_type': classify_device(device['hostname']),",
          "    }"]),
    ]

    ways_byplat = [
        ("Default parameter with optional filter",
         ["def get_devices_by_platform(inventory, platform, status=None):",
          "    return [",
          "        d['hostname'] for d in inventory",
          "        if d['platform'] == platform",
          "        and (status is None or d['status'] == status)",
          "    ]"]),
    ]

    ways_validate = [
        ("Guard clauses with early return",
         ["def validate_device(device, global_ntp=GLOBAL_NTP):",
          "    if device['status'] != 'up':                           return (False, 'device is down')",
          "    if device['platform'] not in ('IOS-XE','NX-OS','ASA','IOS-XR'): return (False, 'unsupported platform')",
          "    if not device.get('vlans'):                            return (False, 'no vlans')",
          "    if device.get('config',{}).get('ntp') != global_ntp:  return (False, 'custom ntp')",
          "    return (True, 'valid')"]),
    ]

    ways_partition = [
        ("Two comprehensions returned as tuple",
         ["def partition_by_status(inventory):",
          "    up   = [d['hostname'] for d in inventory if d['status'] == 'up']",
          "    down = [d['hostname'] for d in inventory if d['status'] == 'down']",
          "    return up, down"]),
    ]

    ways_ntp_cfg = [
        ("*args with enumerate and prefer_first",
         ["def generate_ntp_config(hostname, *ntp_servers, prefer_first=True):",
          "    lines = []",
          "    for i, server in enumerate(ntp_servers):",
          "        line = f'ntp server {server}'",
          "        if prefer_first and i == 0:",
          "            line += ' prefer'",
          "        lines.append(line)",
          "    return '\\n'.join(lines)"]),
    ]

    ways_apply_filter = [
        ("*filter_fns with all()",
         ["def apply_filter(inventory, *filter_fns):",
          "    return [",
          "        d['hostname'] for d in inventory",
          "        if all(fn(d) for fn in filter_fns)",
          "    ]"]),
    ]

    ways_build_cfg = [
        ("**kwargs with key.replace()",
         ["def build_config(hostname, **settings):",
          "    lines = [f'hostname {hostname}']",
          "    for k, v in settings.items():",
          "        lines.append(f'{k.replace(\"_\", \" \")} {v}')",
          "    return '\\n'.join(lines)"]),
    ]

    ways_pipeline = [
        ("Loop applying each step",
         ["def run_pipeline(data, *steps):",
          "    result = data",
          "    for step in steps:",
          "        result = step(result)",
          "    return result"]),
        ("functools.reduce",
         ["from functools import reduce",
          "def run_pipeline(data, *steps):",
          "    return reduce(lambda acc, step: step(acc), steps, data)"]),
    ]

    ways_sorter = [
        ("Factory function returning a lambda",
         ["def make_sorter(key_field, reverse=False):",
          "    return lambda lst: sorted(lst, key=lambda d: d[key_field], reverse=reverse)"]),
        ("Factory function returning a named function",
         ["def make_sorter(key_field, reverse=False):",
          "    def sorter(lst):",
          "        return sorted(lst, key=lambda d: d[key_field], reverse=reverse)",
          "    return sorter"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task  1", "classify_device — router/switch/firewall/unknown",
         classify_results, exp_classify,
         "if 'rtr' in hostname: return 'router' elif 'sw' ... elif 'fw' ...",
         ways_classify, "classify_device results"),
        ("Task  2", "get_up_devices — list of hostnames with status 'up'",
         get_up_results, exp_up,
         "return [d['hostname'] for d in inventory if d['status'] == 'up']",
         ways_get_up, "get_up_devices(INVENTORY)"),
        ("Task  3", "count_by_platform — platform → count dict",
         count_results, exp_counts,
         "counts[p] = counts.get(p, 0) + 1 inside a for loop.",
         ways_count, "count_by_platform(INVENTORY)"),
        ("Task  4", "enrich_device — original dict + vlan_count, iface_count, device_type",
         enrich_results, exp_enrich,
         "return {**device, 'vlan_count': len(device['vlans']), ...}",
         ways_enrich, "enrich_device(INVENTORY[0])"),
        ("Task  5", "get_devices_by_platform — with optional status filter",
         byp_result, exp_byp,
         "def func(inventory, platform, status=None): filter on platform and optionally status.",
         ways_byplat, "(all_iosxe, up_iosxe, down_nxos)"),
        ("Task  6", "validate_device — guard clauses returning (bool, msg)",
         val_results, exp_val,
         "Early return for each failed check: (False, 'reason'). Return (True, 'valid') at end.",
         ways_validate, "[validate_device(d) for d in INVENTORY]"),
        ("Task  7", "partition_by_status — returns (up_list, down_list) tuple",
         part_result, exp_part,
         "return up, down — Python packs two values into a tuple automatically.",
         ways_partition, "partition_by_status(INVENTORY)"),
        ("Task  8", "generate_ntp_config — *args servers, prefer_first keyword-only",
         ntp_result, exp_ntp,
         "*ntp_servers collects all IPs. prefer_first=True adds ' prefer' to the first server.",
         ways_ntp_cfg, "(ntp_result1, ntp_result2)"),
        ("Task  9", "apply_filter — *filter_fns all must pass",
         af_result, exp_af,
         "all(fn(d) for fn in filter_fns) checks every filter function against the device.",
         ways_apply_filter, "(apply_filter results)"),
        ("Task 10", "build_config — **settings with underscore-to-space key conversion",
         bc_result, exp_bc,
         "Iterate settings.items(), format key with k.replace('_', ' ').",
         ways_build_cfg, "(build_config results)"),
        ("Task 11", "run_pipeline — *steps applied in sequence",
         rp_result, exp_rp,
         "result = data; for step in steps: result = step(result); return result.",
         ways_pipeline, "run_pipeline result"),
        ("Task 12", "make_sorter — returns a sort function for given key_field",
         ms_result, exp_ms,
         "return lambda lst: sorted(lst, key=lambda d: d[key_field], reverse=reverse).",
         ways_sorter, "(sorted_names, sorted_vlans)"),
    ], ns=ns)

pause()