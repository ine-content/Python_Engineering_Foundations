# file_io_grading.py
# Python File I/O — Grader
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Write your solution in file_io_solution.py
# 2. Run this script: python3 file_io_grading.py
# 3. Fix any hints and re-run until you get Good Job!

import os
import sys
import csv
import json
import shutil
import tempfile
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

# ─────────────────────────────────────────────────────────────────────────────
# GRADER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(work_dir):
    filename = "file_io_solution.py"
    solution_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    if not os.path.exists(solution_path):
        blank()
        fail(f"File '{filename}' not found.")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        sys.exit()

    namespace = {
        "INVENTORY":  INVENTORY,
        "GLOBAL_NTP": GLOBAL_NTP,
        "WORK_DIR":   work_dir,
        "os":         os,
        "csv":        csv,
        "json":       json,
    }
    try:
        with open(solution_path) as f:
            code = f.read()
        import textwrap
        code = textwrap.dedent(code)
        old_cwd = os.getcwd()
        os.chdir(work_dir)
        try:
            exec(compile(code, filename, "exec"), namespace)
        finally:
            os.chdir(old_cwd)
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
    score_color = GREEN if passed >= 6 else YELLOW if passed >= 4 else RED
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
    if passed >= 6:
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
    return passed >= 6


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
print()
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         FILE I/O — GRADER{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("Grading your file_io_solution.py ...")
blank()

# ── Create temporary working directory ────────────────────────────────────────
work_dir = tempfile.mkdtemp(prefix="file_io_")

# Pre-create device_list.txt for Task 3
with open(os.path.join(work_dir, "device_list.txt"), "w") as f:
    f.write("# hostname        platform   ip\n")
    f.write("nyc-rtr-01        IOS-XE     10.0.0.1\n")
    f.write("lon-sw-01         NX-OS      10.1.0.1\n")
    f.write("sin-fw-01         ASA        10.2.0.1\n")

ns = run_solution(work_dir)
if ns:

    fields = ["hostname", "platform", "status", "ip"]

    # ── Task 1: check hostnames.txt file contents ──────────────────────────────
    txt_path = os.path.join(work_dir, "hostnames.txt")
    file_lines = []
    if os.path.exists(txt_path):
        with open(txt_path) as f:
            file_lines = [l.strip() for l in f if l.strip()]
    exp_lines = [d["hostname"] for d in INVENTORY]

    # ── Task 2: check read_hostnames variable ──────────────────────────────────
    read_hostnames = ns.get("read_hostnames")

    # ── Task 3: check parsed_devices variable ──────────────────────────────────
    parsed_devices = ns.get("parsed_devices")
    exp_parsed = [
        {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"},
        {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1"},
        {"hostname": "sin-fw-01",  "platform": "ASA",    "ip": "10.2.0.1"},
    ]

    # ── Task 4: check cfg_files list + sample file content ────────────────────
    cfg_files = ns.get("cfg_files")
    exp_cfg_files = sorted(f"{d['hostname']}.cfg" for d in INVENTORY)

    sample_cfg_path = os.path.join(work_dir, "configs", "nyc-rtr-01.cfg")
    sample_cfg = ""
    if os.path.exists(sample_cfg_path):
        with open(sample_cfg_path) as f:
            sample_cfg = f.read().strip()
    exp_sample_cfg = "hostname nyc-rtr-01\nntp server 10.0.0.100\nip name-server 8.8.8.8"

    # ── Task 5: check CSV file contents ───────────────────────────────────────
    csv_path = os.path.join(work_dir, "inventory.csv")
    csv_rows = []
    if os.path.exists(csv_path):
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            csv_rows = [dict(row) for row in reader]
    exp_csv_rows = [{f: d[f] for f in fields} for d in INVENTORY]

    # ── Task 6: check csv_devices (up only) ───────────────────────────────────
    csv_devices = ns.get("csv_devices")
    exp_csv_up = [{f: d[f] for f in fields} for d in INVENTORY if d["status"] == "up"]

    # ── Task 7: check json_inventory variable ─────────────────────────────────
    json_inv = ns.get("json_inventory")
    exp_json_inv = INVENTORY

    # ── Task 8: check vlan_counts variable ────────────────────────────────────
    vlan_counts = ns.get("vlan_counts")
    exp_vc = {d["hostname"]: len(d["vlans"]) for d in INVENTORY}

    # ── Solution ways ──────────────────────────────────────────────────────────

    ways_write_txt = [
        ("open write + loop",
         ["with open('hostnames.txt', 'w') as f:",
          "    for d in INVENTORY:",
          "        f.write(d['hostname'] + '\\n')"]),
        ("open write + join",
         ["with open('hostnames.txt', 'w') as f:",
          "    f.write('\\n'.join(d['hostname'] for d in INVENTORY) + '\\n')"]),
    ]

    ways_read_txt = [
        ("List comprehension with strip()",
         ["with open('hostnames.txt') as f:",
          "    read_hostnames = [line.strip() for line in f if line.strip()]"]),
        ("For loop",
         ["read_hostnames = []",
          "with open('hostnames.txt') as f:",
          "    for line in f:",
          "        line = line.strip()",
          "        if line:",
          "            read_hostnames.append(line)"]),
    ]

    ways_parse = [
        ("For loop skipping # and blank lines",
         ["parsed_devices = []",
          "with open('device_list.txt') as f:",
          "    for line in f:",
          "        line = line.strip()",
          "        if not line or line.startswith('#'):",
          "            continue",
          "        parts = line.split()",
          "        parsed_devices.append({",
          "            'hostname': parts[0],",
          "            'platform': parts[1],",
          "            'ip': parts[2],",
          "        })"]),
    ]

    ways_cfg_files = [
        ("makedirs + write loop + listdir",
         ["os.makedirs('configs', exist_ok=True)",
          "for d in INVENTORY:",
          "    with open(f\"configs/{d['hostname']}.cfg\", 'w') as f:",
          "        f.write(f\"hostname {d['hostname']}\\n\")",
          "        f.write(f\"ntp server {d['config']['ntp']}\\n\")",
          "        f.write(f\"ip name-server {d['config']['dns']}\\n\")",
          "cfg_files = sorted(os.listdir('configs'))"]),
    ]

    ways_csv_write = [
        ("DictWriter with writeheader + writerows",
         ["with open('inventory.csv', 'w', newline='') as f:",
          "    writer = csv.DictWriter(f,",
          "                fieldnames=['hostname', 'platform', 'status', 'ip'],",
          "                extrasaction='ignore')",
          "    writer.writeheader()",
          "    writer.writerows(INVENTORY)"]),
    ]

    ways_csv_read = [
        ("DictReader with filter",
         ["with open('inventory.csv', newline='') as f:",
          "    csv_devices = [dict(row) for row in csv.DictReader(f)",
          "                   if row['status'] == 'up']"]),
    ]

    ways_json = [
        ("json.dump then json.load",
         ["with open('inventory.json', 'w') as f:",
          "    json.dump(INVENTORY, f, indent=2)",
          "with open('inventory.json') as f:",
          "    json_inventory = json.load(f)"]),
    ]

    ways_enrich_json = [
        ("load, enrich, write back, reload, build dict",
         ["with open('inventory.json') as f:",
          "    data = json.load(f)",
          "for d in data:",
          "    d['vlan_count'] = len(d['vlans'])",
          "with open('inventory.json', 'w') as f:",
          "    json.dump(data, f, indent=2)",
          "with open('inventory.json') as f:",
          "    data = json.load(f)",
          "vlan_counts = {d['hostname']: d['vlan_count'] for d in data}"]),
    ]

    # ── Run grade ──────────────────────────────────────────────────────────────
    grade([
        ("Task 1", "hostnames.txt — 8 hostnames written, one per line",
         file_lines, exp_lines,
         "open('hostnames.txt', 'w') then f.write(d['hostname'] + '\\n') for each device.",
         ways_write_txt, "contents of hostnames.txt"),
        ("Task 2", "read_hostnames — list of 8 stripped hostnames",
         read_hostnames, exp_lines,
         "Iterate file lines, strip() each one, skip blanks.",
         ways_read_txt, "read_hostnames"),
        ("Task 3", "parsed_devices — 3 dicts from device_list.txt",
         parsed_devices, exp_parsed,
         "Skip lines starting with '#' or blank. parts = line.split() gives 3 fields.",
         ways_parse, "parsed_devices"),
        ("Task 4", "cfg_files — sorted list of .cfg filenames + correct file content",
         (cfg_files, sample_cfg), (exp_cfg_files, exp_sample_cfg),
         "os.makedirs('configs', exist_ok=True), write 3 lines per device, sorted(os.listdir('configs')).",
         ways_cfg_files, "(cfg_files, nyc-rtr-01.cfg contents)"),
        ("Task 5", "inventory.csv — 8 rows with hostname/platform/status/ip",
         csv_rows, exp_csv_rows,
         "csv.DictWriter with fieldnames=[...], writeheader(), writerows(). Use newline=''.",
         ways_csv_write, "inventory.csv contents"),
        ("Task 6", "csv_devices — 5 up-only device dicts from CSV",
         csv_devices, exp_csv_up,
         "csv.DictReader, filter rows where row['status'] == 'up'.",
         ways_csv_read, "csv_devices"),
        ("Task 7", "json_inventory — full 8-device list loaded from JSON",
         json_inv, exp_json_inv,
         "json.dump(INVENTORY, f, indent=2) then json.load(f).",
         ways_json, "json_inventory"),
        ("Task 8", "vlan_counts — hostname → vlan_count from enriched JSON",
         vlan_counts, exp_vc,
         "Load JSON, add vlan_count to each dict, write back, reload, build hostname→count dict.",
         ways_enrich_json, "vlan_counts"),
    ], ns=ns)

shutil.rmtree(work_dir, ignore_errors=True)
pause()