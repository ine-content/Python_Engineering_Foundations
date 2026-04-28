# capstone_grading.py
# Python IaC Capstone Lab — Grader
# Cisco IaC Perspective

import os
import sys
import json
import yaml
import shutil
import tempfile
import traceback

RESET  = "\033[0m"; CYAN = "\033[96m"; GREEN = "\033[92m"
YELLOW = "\033[93m"; WHITE = "\033[97m"; RED = "\033[91m"
BOLD   = "\033[1m";  DIM  = "\033[2m"

def pause():
    input(f"\n{DIM}  [ Press ENTER to continue ]{RESET} ")
    print()

def fail(text):    print(f"    {RED}✘  {text}{RESET}")
def hint(text):    print(f"    {YELLOW}💡 Hint: {text}{RESET}")
def explain(text): print(f"  {WHITE}{text}{RESET}")
def blank():       print()

def section(title):
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
GLOBAL_NTP      = "10.0.0.100"
RESERVED_VLANS  = {1, 1002, 1003, 1004, 1005}
PLATFORM_OS     = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa", "IOS-XR": "iosxr"}

VLAN_INTENT = {
    10: {"name": "MGMT",    "svi_ip": "10.10.0.1/24"},
    20: {"name": "USERS",   "svi_ip": "10.20.0.1/24"},
    30: {"name": "VOICE",   "svi_ip": "10.30.0.1/24"},
    40: {"name": "SERVERS", "svi_ip": "10.40.0.1/24"},
    50: {"name": "DMZ",     "svi_ip": "10.50.0.1/24"},
}

INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "NYC", "role": "core", "ip": "10.0.0.1",
        "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65001, "neighbors": ["10.3.0.1"]},
    },
    {
        "hostname": "lon-sw-01", "platform": "NX-OS", "status": "down",
        "site": "LON", "role": "distribution", "ip": "10.1.0.1",
        "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "sin-fw-01", "platform": "ASA", "status": "up",
        "site": "SIN", "role": "firewall", "ip": "10.2.0.1",
        "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "site": "AMS", "role": "core", "ip": "10.3.0.1",
        "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65002, "neighbors": ["10.0.0.1"]},
    },
    {
        "hostname": "tok-sw-01", "platform": "NX-OS", "status": "down",
        "site": "TOK", "role": "access", "ip": "10.4.0.1",
        "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "SYD", "role": "core", "ip": "10.5.0.1",
        "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65003, "neighbors": ["10.7.0.1"]},
    },
    {
        "hostname": "dub-fw-01", "platform": "ASA", "status": "down",
        "site": "DUB", "role": "firewall", "ip": "10.6.0.1",
        "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "MUM", "role": "core", "ip": "10.7.0.1",
        "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65004, "neighbors": ["10.5.0.1"]},
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# RUN SOLUTION
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(work_dir):
    filename = "capstone_solution.py"
    solution_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    if not os.path.exists(solution_path):
        blank(); fail(f"File '{filename}' not found."); blank()
        explain(f"  Create '{filename}' in the same folder and try again.")
        blank(); sys.exit()

    namespace = {
        "INVENTORY":      INVENTORY,
        "GLOBAL_NTP":     GLOBAL_NTP,
        "RESERVED_VLANS": RESERVED_VLANS,
        "PLATFORM_OS":    PLATFORM_OS,
        "VLAN_INTENT":    VLAN_INTENT,
        "json":           json,
        "yaml":           yaml,
        "os":             os,
    }
    try:
        with open(solution_path) as f:
            code = f.read()
        import textwrap
        old_cwd = os.getcwd()
        os.chdir(work_dir)
        try:
            exec(compile(textwrap.dedent(code), filename, "exec"), namespace)
        finally:
            os.chdir(old_cwd)
        return namespace
    except Exception:
        blank(); fail("Your script raised an error:"); print()
        traceback.print_exc(); blank(); return None


# ─────────────────────────────────────────────────────────────────────────────
# SHOW TASK REVIEW
# ─────────────────────────────────────────────────────────────────────────────
def show_task_review(label, passed, actual, expected, hint_text, solution_ways, var_name):
    status = f"{GREEN}✔  PASSED{RESET}" if passed else f"{RED}✘  FAILED{RESET}"
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {label}{RESET}")
    print(f"  {status}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

    if not passed:
        hint(hint_text); blank()
        print(f"    {YELLOW}What your code produced:{RESET}")
        print(f"    {CYAN}>>> print({var_name}){RESET}")
        # truncate large outputs
        actual_str = str(actual)
        if len(actual_str) > 300:
            actual_str = actual_str[:300] + " ..."
        print(f"    {RED}{actual_str}{RESET}"); blank()

    print(f"    {YELLOW}Solution approach:{RESET}")
    for way_label, way_code in solution_ways:
        print(f"    {YELLOW}  ▸ {way_label}{RESET}")
        for line in way_code:
            print(f"    {CYAN}    {line}{RESET}")
        blank()

    print(f"    {YELLOW}Correct answer:{RESET}")
    expected_str = str(expected)
    if len(expected_str) > 300:
        expected_str = expected_str[:300] + " ..."
    print(f"    {GREEN}    {expected_str}{RESET}")
    blank()


# ─────────────────────────────────────────────────────────────────────────────
# GRADE
# ─────────────────────────────────────────────────────────────────────────────
def grade(checks, ns=None):
    total   = len(checks)
    results = []
    passed  = 0

    for label, actual, expected, hint_text, solution_ways, var_name in checks:
        if expected is None and ns is not None:
            ok = var_name.strip("()") in ns and actual == expected
        else:
            ok = (actual == expected)
        if ok:
            passed += 1
        results.append((label, ok, actual, expected, hint_text, solution_ways, var_name))

    blank()
    bar = "█" * 62
    pct = passed / total
    score_color = GREEN if pct >= 0.8 else YELLOW if pct >= 0.6 else RED
    print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}"); print()
    print(f"{BOLD}  YOUR SCORE:  {score_color}{passed} / {total}{RESET}"); print()
    for label, ok, *_ in results:
        mark = f"{GREEN}✔{RESET}" if ok else f"{RED}✘{RESET}"
        print(f"    {mark}  {label}")
    print(); print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}")

    blank()
    explain("Press ENTER to review each check.")
    for label, ok, actual, expected, hint_text, solution_ways, var_name in results:
        pause()
        show_task_review(label, ok, actual, expected, hint_text, solution_ways, var_name)

    blank(); print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}"); print()
    if pct >= 0.8:
        print(f"{BOLD}{GREEN}  ✔  EXCELLENT! You scored {passed}/{total}.{RESET}"); print()
        print(f"{BOLD}{GREEN}  Capstone complete. You are ready for production IaC.{RESET}")
    elif pct >= 0.6:
        print(f"{BOLD}{YELLOW}  You scored {passed}/{total}.{RESET}"); print()
        print(f"{BOLD}{YELLOW}  Good effort — review the hints and aim for 80%+.{RESET}")
    else:
        print(f"{BOLD}{RED}  You scored {passed}/{total}.{RESET}"); print()
        print(f"{BOLD}{YELLOW}  Review the topic files and try again.{RESET}")
    print(); print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}")


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}"); print()
print(f"{BOLD}         CAPSTONE LAB — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}"); print()
print(f"{BOLD}{bar}{RESET}"); print(f"{BOLD}{bar}{RESET}"); blank()
explain("Grading your capstone_solution.py ..."); blank()

work_dir = tempfile.mkdtemp(prefix="capstone_")
ns = run_solution(work_dir)

if ns:

    # ── REFERENCE ANSWERS ─────────────────────────────────────────────────────

    # Part 1
    exp_up_devices     = [d for d in INVENTORY if d["status"] == "up"]
    exp_h2ip           = {d["hostname"]: d["ip"] for d in INVENTORY}
    exp_site_hosts     = {}
    for d in INVENTORY:
        exp_site_hosts.setdefault(d["site"], []).append(d["hostname"])
    for k in exp_site_hosts:
        exp_site_hosts[k].sort()
    exp_all_vlans      = sorted(set(v for d in INVENTORY for v in d["vlans"]))

    # Part 2
    exp_v2h = {}
    for d in INVENTORY:
        for v in d["vlans"]:
            exp_v2h.setdefault(v, set()).add(d["hostname"])
    exp_v2h = {k: sorted(v) for k, v in exp_v2h.items()}

    exp_bgp_devices = sorted(d["hostname"] for d in INVENTORY if d["bgp"] is not None)

    exp_enriched = {
        d["hostname"]: {
            "site":        d["site"],
            "role":        d["role"],
            "platform":    d["platform"],
            "status":      d["status"],
            "vlan_count":  len(d["vlans"]),
            "has_bgp":     d["bgp"] is not None,
        }
        for d in INVENTORY
    }

    # Part 3
    def _classify(h):
        if "rtr" in h: return "router"
        if "sw"  in h: return "switch"
        if "fw"  in h: return "firewall"
        return "unknown"

    def _gen_base(d):
        return (f"hostname {d['hostname']}\n"
                f"ntp server {d['config']['ntp']}\n"
                f"ip name-server {d['config']['dns']}")

    classify_fn = ns.get("classify_device")
    gen_base_fn = ns.get("gen_base_config")
    by_role_fn  = ns.get("get_devices_by_role")

    classify_results = None
    if classify_fn:
        try:
            classify_results = (
                classify_fn("nyc-rtr-01"),
                classify_fn("lon-sw-01"),
                classify_fn("sin-fw-01"),
                classify_fn("abc-xyz-01"),
            )
        except Exception as e:
            classify_results = f"raised: {e}"
    exp_classify = ("router", "switch", "firewall", "unknown")

    gen_base_result = gen_base_fn(INVENTORY[0]) if gen_base_fn else None
    exp_gen_base    = _gen_base(INVENTORY[0])

    by_role_result = None
    if by_role_fn:
        try:
            by_role_result = by_role_fn(INVENTORY, "core")
        except Exception as e:
            by_role_result = f"raised: {e}"
    exp_by_role = sorted(d["hostname"] for d in INVENTORY if d["role"] == "core")

    # Part 4
    exp_plat_counts = {}
    for d in INVENTORY:
        exp_plat_counts[d["platform"]] = exp_plat_counts.get(d["platform"], 0) + 1

    exp_first_large = None
    for d in INVENTORY:
        if d["status"] == "up" and len(d["vlans"]) > 3:
            exp_first_large = d["hostname"]
            break

    def _label(d):
        if d["status"] == "down":                       return f"OFFLINE: {d['hostname']}"
        if d["platform"] == "ASA" and d["status"] == "up": return f"FIREWALL: {d['hostname']}"
        if d["role"] == "core"    and d["status"] == "up": return f"CORE: {d['hostname']}"
        return f"OTHER: {d['hostname']}"
    exp_labels = [_label(d) for d in INVENTORY]

    # Part 5
    DeviceOfflineError = ns.get("DeviceOfflineError")
    safe_connect_fn    = ns.get("safe_connect")
    batch_connect_fn   = ns.get("batch_connect")

    safe_connect_results = None
    if safe_connect_fn and DeviceOfflineError:
        try:
            r1 = safe_connect_fn(INVENTORY[0])
            try:
                safe_connect_fn(INVENTORY[1])
                r2 = "no-error"
            except Exception as e:
                r2 = (type(e).__name__, str(e))
            safe_connect_results = (r1, r2)
        except Exception as e:
            safe_connect_results = f"raised: {e}"
    exp_safe_connect = (
        "connected: nyc-rtr-01",
        ("DeviceOfflineError", "lon-sw-01 is offline"),
    )

    batch_result = batch_connect_fn(INVENTORY) if batch_connect_fn else None
    exp_batch = {
        "connected": ["nyc-rtr-01", "sin-fw-01", "ams-rtr-02", "syd-rtr-01", "mum-rtr-01"],
        "offline":   ["lon-sw-01", "tok-sw-01", "dub-fw-01"],
        "errors":    [],
    }

    # Part 6
    exp_ansible_inv = {
        "all": {
            "hosts": {
                d["hostname"]: {
                    "ansible_host":       d["ip"],
                    "ansible_network_os": PLATFORM_OS[d["platform"]],
                    "ansible_user":       "admin",
                }
                for d in INVENTORY
            }
        }
    }
    exp_ansible_yaml_starts = "all:\n"
    ansible_inv_yaml = ns.get("ansible_inv_yaml", "")
    ansible_yaml_ok  = isinstance(ansible_inv_yaml, str) and ansible_inv_yaml.startswith(exp_ansible_yaml_starts)

    up_devs = [d for d in INVENTORY if d["status"] == "up"]
    exp_ntp_payloads = [
        {
            "hostname": d["hostname"],
            "payload": {
                "Cisco-IOS-XE-native:ntp": {
                    "server": {
                        "server-list": [{"ip-address": d["config"]["ntp"]}]
                    }
                }
            },
        }
        for d in up_devs
    ]

    # Part 7 — file checks
    hosts_path = os.path.join(work_dir, "hosts.yaml")
    hosts_reloaded = None
    if os.path.exists(hosts_path):
        with open(hosts_path) as f:
            hosts_reloaded = yaml.safe_load(f)

    cfg_files = ns.get("cfg_files")
    exp_cfg_files = sorted(f"{d['hostname']}.cfg" for d in INVENTORY)

    nyc_cfg_path = os.path.join(work_dir, "configs", "nyc-rtr-01.cfg")
    nyc_cfg = ""
    if os.path.exists(nyc_cfg_path):
        with open(nyc_cfg_path) as f:
            nyc_cfg = f.read().strip()
    exp_nyc_cfg = _gen_base(INVENTORY[0])

    json_inv = ns.get("json_inventory")

    # Part 8
    def _compliance(d):
        checks = {
            "status_up":    d["status"] == "up",
            "standard_ntp": d["config"]["ntp"] == GLOBAL_NTP,
            "has_vlans":    bool(d["vlans"]),
        }
        return {
            "hostname": d["hostname"],
            "overall":  "PASS" if all(checks.values()) else "FAIL",
            "checks":   checks,
        }
    exp_compliance = [_compliance(d) for d in INVENTORY]

    pipeline_valid = [d for d in INVENTORY
                      if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS")]
    exp_pipeline_report = [
        {
            "hostname":      d["hostname"],
            "status":        d["status"],
            "vlan_count":    len(d["vlans"]),
            "connect_result": f"connected: {d['hostname']}",
            "config_lines":  len(_gen_base(d).splitlines()),
        }
        for d in pipeline_valid
    ]
    exp_pipeline_hostnames = sorted(d["hostname"] for d in pipeline_valid)

    pipe_report_path = os.path.join(work_dir, "pipeline_report.json")
    pipe_report_file = None
    if os.path.exists(pipe_report_path):
        with open(pipe_report_path) as f:
            pipe_report_file = json.load(f)

    # ── SOLUTION WAYS ──────────────────────────────────────────────────────────

    w1a = [("List comprehension",
            ["up_devices = [d for d in INVENTORY if d['status'] == 'up']"])]
    w1b = [("Dict comprehension",
            ["hostname_to_ip = {d['hostname']: d['ip'] for d in INVENTORY}"])]
    w1c = [("setdefault + sort",
            ["site_hostnames = {}",
             "for d in INVENTORY:",
             "    site_hostnames.setdefault(d['site'], []).append(d['hostname'])",
             "for k in site_hostnames: site_hostnames[k].sort()"])]
    w1d = [("sorted set comprehension",
            ["all_vlans = sorted(set(v for d in INVENTORY for v in d['vlans']))"])]
    w2a = [("setdefault + sorted",
            ["vlan_to_hostnames = {}",
             "for d in INVENTORY:",
             "    for v in d['vlans']:",
             "        vlan_to_hostnames.setdefault(v, set()).add(d['hostname'])",
             "vlan_to_hostnames = {k: sorted(v) for k, v in vlan_to_hostnames.items()}"])]
    w2b = [("sorted comprehension",
            ["bgp_devices = sorted(d['hostname'] for d in INVENTORY if d['bgp'] is not None)"])]
    w2c = [("Dict comprehension with projection",
            ["enriched_inventory = {",
             "    d['hostname']: {",
             "        'site': d['site'], 'role': d['role'], 'platform': d['platform'],",
             "        'status': d['status'], 'vlan_count': len(d['vlans']),",
             "        'has_bgp': d['bgp'] is not None,",
             "    }",
             "    for d in INVENTORY",
             "}"])]
    w3a = [("if/elif chain",
            ["def classify_device(hostname):",
             "    if 'rtr' in hostname: return 'router'",
             "    if 'sw'  in hostname: return 'switch'",
             "    if 'fw'  in hostname: return 'firewall'",
             "    return 'unknown'"])]
    w3b = [("f-string join",
            ["def gen_base_config(device):",
             "    return (f'hostname {device[\"hostname\"]}\\n'",
             "            f'ntp server {device[\"config\"][\"ntp\"]}\\n'",
             "            f'ip name-server {device[\"config\"][\"dns\"]}')"])]
    w3c = [("sorted comprehension",
            ["def get_devices_by_role(inventory, role):",
             "    return sorted(d['hostname'] for d in inventory if d['role'] == role)"])]
    w4a = [("For loop with .get()",
            ["platform_counts = {}",
             "for d in INVENTORY:",
             "    p = d['platform']",
             "    platform_counts[p] = platform_counts.get(p, 0) + 1"])]
    w4b = [("For loop with break",
            ["first_large_up_device = None",
             "for d in INVENTORY:",
             "    if d['status'] == 'up' and len(d['vlans']) > 3:",
             "        first_large_up_device = d['hostname']",
             "        break"])]
    w4c = [("if/elif chain per device",
            ["device_labels = []",
             "for d in INVENTORY:",
             "    if d['status'] == 'down':",
             "        device_labels.append(f'OFFLINE: {d[\"hostname\"]}')",
             "    elif d['platform'] == 'ASA' and d['status'] == 'up':",
             "        device_labels.append(f'FIREWALL: {d[\"hostname\"]}')",
             "    elif d['role'] == 'core' and d['status'] == 'up':",
             "        device_labels.append(f'CORE: {d[\"hostname\"]}')",
             "    else:",
             "        device_labels.append(f'OTHER: {d[\"hostname\"]}')",])]
    w5a = [("class inheriting Exception",
            ["class DeviceOfflineError(Exception):",
             "    pass"])]
    w5b = [("raise on down, return on up",
            ["def safe_connect(device):",
             "    if device['status'] == 'down':",
             "        raise DeviceOfflineError(f\"{device['hostname']} is offline\")",
             "    return f\"connected: {device['hostname']}\""])]
    w5c = [("loop with try/except",
            ["def batch_connect(inventory):",
             "    result = {'connected': [], 'offline': [], 'errors': []}",
             "    for d in inventory:",
             "        try:",
             "            safe_connect(d)",
             "            result['connected'].append(d['hostname'])",
             "        except DeviceOfflineError:",
             "            result['offline'].append(d['hostname'])",
             "        except Exception:",
             "            result['errors'].append(d['hostname'])",
             "    return result"])]
    w6a = [("dict comprehension with PLATFORM_OS",
            ["ansible_inv = {'all': {'hosts': {",
             "    d['hostname']: {",
             "        'ansible_host': d['ip'],",
             "        'ansible_network_os': PLATFORM_OS[d['platform']],",
             "        'ansible_user': 'admin',",
             "    }",
             "    for d in INVENTORY",
             "}}}"])]
    w6b = [("yaml.dump",
            ["ansible_inv_yaml = yaml.dump(ansible_inv, default_flow_style=False)"])]
    w6c = [("list comprehension",
            ["ntp_payloads = [",
             "    {'hostname': d['hostname'],",
             "     'payload': {'Cisco-IOS-XE-native:ntp': {",
             "         'server': {'server-list': [{'ip-address': d['config']['ntp']}]}}}}",
             "    for d in INVENTORY if d['status'] == 'up'",
             "]"])]
    w7a = [("yaml.dump to file",
            ["with open('hosts.yaml', 'w') as f:",
             "    yaml.dump(ansible_inv, f, default_flow_style=False)"])]
    w7b = [("makedirs + write per device",
            ["os.makedirs('configs', exist_ok=True)",
             "for d in INVENTORY:",
             "    with open(f\"configs/{d['hostname']}.cfg\", 'w') as f:",
             "        f.write(gen_base_config(d))",
             "cfg_files = sorted(os.listdir('configs'))"])]
    w7c = [("json.dump then json.load",
            ["with open('inventory.json', 'w') as f:",
             "    json.dump(INVENTORY, f, indent=2)",
             "with open('inventory.json') as f:",
             "    json_inventory = json.load(f)"])]
    w8a = [("per-device check dict",
            ["compliance_report = []",
             "for d in INVENTORY:",
             "    checks = {",
             "        'status_up':    d['status'] == 'up',",
             "        'standard_ntp': d['config']['ntp'] == GLOBAL_NTP,",
             "        'has_vlans':    bool(d['vlans']),",
             "    }",
             "    compliance_report.append({",
             "        'hostname': d['hostname'],",
             "        'overall': 'PASS' if all(checks.values()) else 'FAIL',",
             "        'checks': checks,",
             "    })"])]
    w8b = [("filter + connect + config",
            ["pipeline_report = []",
             "valid = [d for d in INVENTORY",
             "         if d['status'] == 'up' and d['platform'] in ('IOS-XE','NX-OS')]",
             "for d in valid:",
             "    pipeline_report.append({",
             "        'hostname':      d['hostname'],",
             "        'status':        d['status'],",
             "        'vlan_count':    len(d['vlans']),",
             "        'connect_result': safe_connect(d),",
             "        'config_lines':  len(gen_base_config(d).splitlines()),",
             "    })",
             "pipeline_hostnames = sorted(d['hostname'] for d in valid)"])]
    w8c = [("json.dump to file",
            ["with open('pipeline_report.json', 'w') as f:",
             "    json.dump(pipeline_report, f, indent=2)"])]

    # ── RUN GRADE ──────────────────────────────────────────────────────────────
    grade([
        # Part 1
        ("1a. up_devices — 5 device dicts with status 'up'",
         ns.get("up_devices"), exp_up_devices,
         "[d for d in INVENTORY if d['status'] == 'up']",
         w1a, "up_devices"),
        ("1b. hostname_to_ip — 8 hostname→ip pairs",
         ns.get("hostname_to_ip"), exp_h2ip,
         "{d['hostname']: d['ip'] for d in INVENTORY}",
         w1b, "hostname_to_ip"),
        ("1c. site_hostnames — site → sorted list of hostnames",
         ns.get("site_hostnames"), exp_site_hosts,
         "setdefault + append + sort per site",
         w1c, "site_hostnames"),
        ("1d. all_vlans — [10, 20, 30, 40, 50]",
         ns.get("all_vlans"), exp_all_vlans,
         "sorted(set(v for d in INVENTORY for v in d['vlans']))",
         w1d, "all_vlans"),
        # Part 2
        ("2a. vlan_to_hostnames — vlan → sorted hostnames",
         ns.get("vlan_to_hostnames"), exp_v2h,
         "setdefault(v, set()).add(hostname), then sorted",
         w2a, "vlan_to_hostnames"),
        ("2b. bgp_devices — sorted hostnames with bgp != None",
         ns.get("bgp_devices"), exp_bgp_devices,
         "sorted(d['hostname'] for d in INVENTORY if d['bgp'] is not None)",
         w2b, "bgp_devices"),
        ("2c. enriched_inventory — hostname → {site,role,platform,status,vlan_count,has_bgp}",
         ns.get("enriched_inventory"), exp_enriched,
         "dict comprehension with 6 keys per device",
         w2c, "enriched_inventory"),
        # Part 3
        ("3a. classify_device — router/switch/firewall/unknown",
         classify_results, exp_classify,
         "if 'rtr' in hostname: return 'router' elif 'sw' ... elif 'fw' ...",
         w3a, "classify_device results"),
        ("3b. gen_base_config — 3-line config string",
         gen_base_result, exp_gen_base,
         "f-string: hostname / ntp server / ip name-server",
         w3b, "gen_base_config(INVENTORY[0])"),
        ("3c. get_devices_by_role — sorted hostnames by role",
         by_role_result, exp_by_role,
         "sorted(d['hostname'] for d in inventory if d['role'] == role)",
         w3c, "get_devices_by_role(INVENTORY,'core')"),
        # Part 4
        ("4a. platform_counts — {'IOS-XE':4,'NX-OS':2,'ASA':2}",
         ns.get("platform_counts"), exp_plat_counts,
         "counts[p] = counts.get(p, 0) + 1 in a for loop",
         w4a, "platform_counts"),
        ("4b. first_large_up_device — 'ams-rtr-02'",
         ns.get("first_large_up_device"), exp_first_large,
         "for loop with if status=='up' and len(vlans)>3: ... break",
         w4b, "first_large_up_device"),
        ("4c. device_labels — OFFLINE/FIREWALL/CORE/OTHER prefix per device",
         ns.get("device_labels"), exp_labels,
         "if/elif chain: down → OFFLINE, ASA up → FIREWALL, core up → CORE",
         w4c, "device_labels"),
        # Part 5
        ("5a+5b. DeviceOfflineError + safe_connect results",
         safe_connect_results, exp_safe_connect,
         "class DeviceOfflineError(Exception): pass. Raise when status=='down'.",
         w5a + w5b, "safe_connect results"),
        ("5c. batch_connect — {connected, offline, errors}",
         batch_result, exp_batch,
         "try: safe_connect(d) → connected. except DeviceOfflineError → offline.",
         w5c, "batch_connect(INVENTORY)"),
        # Part 6
        ("6a. ansible_inv — {'all':{'hosts':{...}}} all 8 devices",
         ns.get("ansible_inv"), exp_ansible_inv,
         "{'all':{'hosts':{d['hostname']:{ansible_host,ansible_network_os,...}}}}",
         w6a, "ansible_inv"),
        ("6b. ansible_inv_yaml — YAML string starting with 'all:\\n'",
         ansible_yaml_ok, True,
         "yaml.dump(ansible_inv, default_flow_style=False)",
         w6b, "ansible_inv_yaml"),
        ("6c. ntp_payloads — 5 RESTCONF dicts for up devices",
         ns.get("ntp_payloads"), exp_ntp_payloads,
         "{'Cisco-IOS-XE-native:ntp':{'server':{'server-list':[{'ip-address':...}]}}}",
         w6c, "ntp_payloads"),
        # Part 7
        ("7a. hosts.yaml — written correctly to disk",
         hosts_reloaded, exp_ansible_inv,
         "with open('hosts.yaml','w') as f: yaml.dump(ansible_inv, f, default_flow_style=False)",
         w7a, "yaml.safe_load('hosts.yaml')"),
        ("7b. cfg_files — 8 sorted .cfg filenames + nyc-rtr-01.cfg content",
         (cfg_files, nyc_cfg), (exp_cfg_files, exp_nyc_cfg),
         "os.makedirs('configs'), write gen_base_config(d) per device",
         w7b, "(cfg_files, nyc-rtr-01.cfg content)"),
        ("7c. json_inventory — equals INVENTORY after round-trip",
         json_inv, INVENTORY,
         "json.dump(INVENTORY, f, indent=2) then json.load(f)",
         w7c, "json_inventory"),
        # Part 8
        ("8a. compliance_report — PASS/FAIL per device, 3 checks",
         ns.get("compliance_report"), exp_compliance,
         "check status_up, standard_ntp, has_vlans per device",
         w8a, "compliance_report"),
        ("8b. pipeline_report — 3 dicts for up IOS-XE/NX-OS devices",
         ns.get("pipeline_report"), exp_pipeline_report,
         "filter up + IOS-XE/NX-OS, safe_connect, gen_base_config",
         w8b, "pipeline_report"),
        ("8b. pipeline_hostnames — ['ams-rtr-02','nyc-rtr-01','syd-rtr-01']",
         ns.get("pipeline_hostnames"), exp_pipeline_hostnames,
         "sorted(d['hostname'] for d in valid)",
         w8b, "pipeline_hostnames"),
        ("8c. pipeline_report.json — written to disk correctly",
         pipe_report_file, exp_pipeline_report,
         "json.dump(pipeline_report, f, indent=2)",
         w8c, "pipeline_report.json"),
    ], ns=ns)

shutil.rmtree(work_dir, ignore_errors=True)
pause()