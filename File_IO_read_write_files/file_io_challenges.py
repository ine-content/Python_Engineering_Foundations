# file_io_challenges.py
# Python File I/O — Student Challenges
# Cisco IaC Perspective
#
# HOW IT WORKS:
# 1. Read the challenge carefully
# 2. Write your solution in the correct file
# 3. Run this script again — it will evaluate your solution
# 4. Fix any hints and re-run until you get Good Job!

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

def copyable(text):
    print(f"{CYAN}{text}{RESET}")

def header(text):
    print(f"    {CYAN}{text}{RESET}")

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
# SHARED TEST DATA
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
# GRADER
# ─────────────────────────────────────────────────────────────────────────────
def run_solution(challenge_num, work_dir):
    """
    Run the student's solution file inside work_dir.
    Injects INVENTORY, GLOBAL_NTP, and WORK_DIR into the namespace.
    """
    filename = f"file_io_solution_ch{challenge_num}.py"
    if not os.path.exists(filename):
        blank()
        print(f"    {RED}✘  File '{filename}' not found.{RESET}")
        blank()
        explain(f"  Create a file called '{filename}' in the same folder")
        explain(f"  as this script, write your solution, then run this")
        explain(f"  script again.")
        blank()
        explain(f"  Do not move on to the next challenge until this")
        explain(f"  one is complete.")
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
        with open(filename) as f:
            code = f.read()
        import textwrap
        code = textwrap.dedent(code)
        # Run from inside WORK_DIR so relative paths work
        old_cwd = os.getcwd()
        os.chdir(work_dir)
        try:
            exec(compile(code, filename, "exec"), namespace)
        finally:
            os.chdir(old_cwd)
        return namespace
    except Exception:
        blank()
        print(f"    {RED}✘  Your script raised an error:{RESET}")
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
        print(f"    {YELLOW}💡 Hint: {hint_text}{RESET}")
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


def grade(challenge_num, checks_list):
    blank()
    section("Grading your solution...")
    passed = 0
    for args in checks_list:
        if check(*args):
            passed += 1
    blank()
    total = len(checks_list)
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
print(f"{BOLD}         FILE I/O — STUDENT CHALLENGES{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
explain("You have two challenges — Easy and Medium.")
explain("Each one involves reading and writing real files.")
blank()
explain("Files to create:")
explain("  Challenge 1 (Easy)   → file_io_solution_ch1.py")
explain("  Challenge 2 (Medium) → file_io_solution_ch2.py")
blank()
explain("HOW GRADING WORKS FOR FILE I/O:")
explain("  Your script runs in a temporary working directory.")
explain("  Use relative paths — just 'devices.txt', not full path.")
explain("  The grader reads the files your script creates and")
explain("  checks their contents.")
blank()
explain("INVENTORY, GLOBAL_NTP, os, csv, json are all available")
explain("in your solution file — no need to import or define them.")
explain("(But you CAN import them again — no harm done.)")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SHOW INVENTORY
# ═════════════════════════════════════════════════════════════════════════════
section("The INVENTORY You Will Work With")

explain("This is available in your solution file as INVENTORY.")
blank()
copyable("INVENTORY = [")
for d in INVENTORY:
    copyable(f"    {d},")
copyable("]")
blank()
copyable("GLOBAL_NTP = '10.0.0.100'")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 1 — EASY
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(1, "Plain Text File Read and Write", "Easy")

explain("Read and write plain text files using INVENTORY.")
explain("Use relative paths — the grader runs your script")
explain("from a temporary working directory.")
blank()

pause()

section("Task A")
explain("Write the hostname of every device in INVENTORY")
explain("to a file called 'hostnames.txt', one per line.")
blank()
header("Expected contents of hostnames.txt:")
header("nyc-rtr-01")
header("lon-sw-01")
header("sin-fw-01")
header("ams-rtr-02")
header("tok-sw-01")
header("syd-rtr-01")
header("dub-fw-01")
header("mum-rtr-01")
blank()

pause()

section("Task B")
explain("Read back 'hostnames.txt' and produce a list called")
explain("'read_hostnames' containing each hostname as a string.")
explain("No trailing newlines — strip each line.")
blank()
header(">>> print(read_hostnames)")
header("['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02',")
header(" 'tok-sw-01',  'syd-rtr-01', 'dub-fw-01', 'mum-rtr-01']")
blank()

pause()

section("Task C")
explain("Parse a device list file. The grader will create a file")
explain("called 'device_list.txt' in your working directory with")
explain("this content:")
blank()
header("# hostname        platform   ip")
header("nyc-rtr-01        IOS-XE     10.0.0.1")
header("lon-sw-01         NX-OS      10.1.0.1")
header("sin-fw-01         ASA        10.2.0.1")
blank()
explain("Read this file and produce a list called 'parsed_devices'")
explain("— one dict per device line (skip comment/blank lines).")
explain("Each dict: {'hostname': ..., 'platform': ..., 'ip': ...}")
blank()
header(">>> print(parsed_devices)")
header("[{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'},")
header(" {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'ip': '10.1.0.1'},")
header(" {'hostname': 'sin-fw-01',  'platform': 'ASA',    'ip': '10.2.0.1'}]")
blank()

pause()

section("Task D")
explain("Create a folder called 'configs' and write one config")
explain("file per device in INVENTORY.")
explain("Filename: configs/<hostname>.cfg")
explain("Content (3 lines per file):")
blank()
header("hostname <hostname>")
header("ntp server <ntp from config>")
header("ip name-server <dns from config>")
blank()
explain("After writing, store the SORTED list of .cfg filenames")
explain("(not full paths — just the filename) in 'cfg_files'.")
blank()
header(">>> print(cfg_files)")
header("['ams-rtr-02.cfg', 'dub-fw-01.cfg', 'lon-sw-01.cfg',")
header(" 'mum-rtr-01.cfg', 'nyc-rtr-01.cfg', 'sin-fw-01.cfg',")
header(" 'syd-rtr-01.cfg', 'tok-sw-01.cfg']")
blank()

pause()

explain("Write your solution in: file_io_solution_ch1.py")
blank()
explain("Tips:")
explain("  Task A — open('hostnames.txt','w') then f.write(h+'\\n') for each. Ch 4.1.")
explain("  Task B — open read, line.strip() for line in f, filter blanks. Ch 3.3.")
explain("  Task C — file 'device_list.txt' is pre-created. Skip # and blank lines.")
explain("           parts=line.split() gives [hostname, platform, ip]. Ch 3.4.")
explain("  Task D — os.makedirs('configs', exist_ok=True), write 3 lines per device.")
explain("           sorted(os.listdir('configs')) for file list. Ch 5.3.")

pause()

# ── Grade Challenge 1 ─────────────────────────────────────────────────────────
work_dir_1 = tempfile.mkdtemp(prefix="ch1_")

# Pre-create device_list.txt for Task C
with open(os.path.join(work_dir_1, "device_list.txt"), "w") as f:
    f.write("# hostname        platform   ip\n")
    f.write("nyc-rtr-01        IOS-XE     10.0.0.1\n")
    f.write("lon-sw-01         NX-OS      10.1.0.1\n")
    f.write("sin-fw-01         ASA        10.2.0.1\n")

ns = run_solution(1, work_dir_1)
if ns:
    # Task A — check file contents
    txt_path = os.path.join(work_dir_1, "hostnames.txt")
    file_lines = []
    if os.path.exists(txt_path):
        with open(txt_path) as f:
            file_lines = [l.strip() for l in f if l.strip()]

    exp_lines = [d["hostname"] for d in INVENTORY]

    # Task B — check read_hostnames variable
    read_hostnames = ns.get("read_hostnames")

    # Task C — check parsed_devices
    parsed_devices = ns.get("parsed_devices")
    exp_parsed = [
        {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"},
        {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1"},
        {"hostname": "sin-fw-01",  "platform": "ASA",    "ip": "10.2.0.1"},
    ]

    # Task D — check cfg_files list and actual file contents
    cfg_files = ns.get("cfg_files")
    exp_cfg_files = sorted(f"{d['hostname']}.cfg" for d in INVENTORY)

    # Also verify content of one cfg file
    sample_cfg_path = os.path.join(work_dir_1, "configs", "nyc-rtr-01.cfg")
    sample_cfg = ""
    if os.path.exists(sample_cfg_path):
        with open(sample_cfg_path) as f:
            sample_cfg = f.read().strip()
    exp_sample_cfg = "hostname nyc-rtr-01\nntp server 10.0.0.100\nip name-server 8.8.8.8"

    grade(1, [
        (
            "Task A", "hostnames.txt — 8 hostnames written, one per line",
            file_lines, exp_lines,
            "See Chapter 4.1 — open('hostnames.txt','w') then f.write(d['hostname']+'\\n') for each device.",
            "with open('hostnames.txt', 'w') as f:\n    for d in INVENTORY:\n        f.write(d['hostname'] + '\\n')",
            "contents of hostnames.txt",
        ),
        (
            "Task B", "read_hostnames — list of 8 stripped hostnames",
            read_hostnames, exp_lines,
            "See Chapter 3.3 — iterate file, strip() each line, skip blanks.",
            "with open('hostnames.txt') as f:\n    read_hostnames = [line.strip() for line in f if line.strip()]",
            "read_hostnames",
        ),
        (
            "Task C", "parsed_devices — 3 dicts from device_list.txt",
            parsed_devices, exp_parsed,
            "See Chapter 3.4 — skip lines starting with # or blank. parts=line.split() gives 3 fields.",
            "parsed_devices = []\nwith open('device_list.txt') as f:\n    for line in f:\n        line = line.strip()\n        if not line or line.startswith('#'): continue\n        p = line.split()\n        parsed_devices.append({'hostname':p[0],'platform':p[1],'ip':p[2]})",
            "parsed_devices",
        ),
        (
            "Task D", "cfg_files — sorted list of .cfg filenames + correct file content",
            (cfg_files, sample_cfg), (exp_cfg_files, exp_sample_cfg),
            "See Chapter 5.3 and 6.1 — makedirs('configs'), write 3 lines per device, sorted(os.listdir('configs')).",
            "os.makedirs('configs', exist_ok=True)\nfor d in INVENTORY:\n    with open(f\"configs/{d['hostname']}.cfg\",'w') as f:\n        f.write(f\"hostname {d['hostname']}\\n\")\n        f.write(f\"ntp server {d['config']['ntp']}\\n\")\n        f.write(f\"ip name-server {d['config']['dns']}\\n\")\ncfg_files = sorted(os.listdir('configs'))",
            "(cfg_files, nyc-rtr-01.cfg contents)",
        ),
    ])

shutil.rmtree(work_dir_1, ignore_errors=True)
pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHALLENGE 2 — MEDIUM
# ═════════════════════════════════════════════════════════════════════════════
challenge_header(2, "CSV and JSON Round-Trips", "Medium")

explain("Read and write CSV and JSON files using INVENTORY.")
explain("Your script runs in a temporary working directory —")
explain("use relative paths throughout.")
blank()

pause()

section("Task A")
explain("Write INVENTORY to a CSV file called 'inventory.csv'.")
explain("Include these columns in this order:")
explain("  hostname, platform, status, ip")
explain("Use csv.DictWriter with a header row.")
blank()
header("Expected contents of inventory.csv:")
header("hostname,platform,status,ip")
header("nyc-rtr-01,IOS-XE,up,10.0.0.1")
header("lon-sw-01,NX-OS,down,10.1.0.1")
header("sin-fw-01,ASA,up,10.2.0.1")
header("... (8 rows total)")
blank()

pause()

section("Task B")
explain("Read 'inventory.csv' back using csv.DictReader.")
explain("Produce a list called 'csv_devices' — one dict per row.")
explain("Filter to include ONLY devices whose status is 'up'.")
blank()
header(">>> print(csv_devices)")
header("[{'hostname':'nyc-rtr-01','platform':'IOS-XE','status':'up','ip':'10.0.0.1'},")
header(" {'hostname':'sin-fw-01', 'platform':'ASA',   'status':'up','ip':'10.2.0.1'},")
header(" {'hostname':'ams-rtr-02','platform':'IOS-XE','status':'up','ip':'10.3.0.1'},")
header(" {'hostname':'syd-rtr-01','platform':'IOS-XE','status':'up','ip':'10.5.0.1'},")
header(" {'hostname':'mum-rtr-01','platform':'IOS-XE','status':'up','ip':'10.7.0.1'}]")
blank()

pause()

section("Task C")
explain("Write INVENTORY to a JSON file called 'inventory.json'")
explain("using json.dump() with indent=2.")
explain("Then read it back using json.load() and produce a")
explain("variable called 'json_inventory' containing the data.")
blank()
header(">>> print(type(json_inventory))")
header("<class 'list'>")
blank()
header(">>> print(len(json_inventory))")
header("8")
blank()
header(">>> print(json_inventory[0]['hostname'])")
header("'nyc-rtr-01'")
blank()
header(">>> print(json_inventory[0]['vlans'])")
header("[10, 20, 30]")
blank()

pause()

section("Task D")
explain("Load 'inventory.json', enrich each device by adding")
explain("a 'vlan_count' field (length of the vlans list),")
explain("then write the enriched data back to 'inventory.json'.")
blank()
explain("Then read it back and produce a variable called")
explain("'vlan_counts' — a dict mapping hostname → vlan_count.")
blank()
header(">>> print(vlan_counts)")
header("{'nyc-rtr-01': 3, 'lon-sw-01': 2, 'sin-fw-01': 3,")
header(" 'ams-rtr-02': 4, 'tok-sw-01': 2, 'syd-rtr-01': 3,")
header(" 'dub-fw-01': 3,  'mum-rtr-01': 4}")
blank()

pause()

explain("Write your solution in: file_io_solution_ch2.py")
blank()
explain("Tips:")
explain("  Task A — csv.DictWriter with fieldnames=['hostname','platform','status','ip'].")
explain("           writeheader() then writerows(INVENTORY). newline='' in open(). Ch 7.2.")
explain("  Task B — csv.DictReader, filter rows where row['status']=='up'. Ch 7.3.")
explain("  Task C — json.dump(INVENTORY, f, indent=2), then json.load(f). Ch 8.2/8.3.")
explain("  Task D — load JSON, add vlan_count, write back, reload, build dict. Ch 8.4.")

pause()

# ── Grade Challenge 2 ─────────────────────────────────────────────────────────
work_dir_2 = tempfile.mkdtemp(prefix="ch2_")

ns = run_solution(2, work_dir_2)
if ns:
    fields = ["hostname", "platform", "status", "ip"]

    # Task A — check CSV file contents
    csv_path = os.path.join(work_dir_2, "inventory.csv")
    csv_rows = []
    if os.path.exists(csv_path):
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            csv_rows = [dict(row) for row in reader]

    exp_csv_rows = [{f: d[f] for f in fields} for d in INVENTORY]

    # Task B — check csv_devices (up only)
    csv_devices = ns.get("csv_devices")
    exp_csv_up = [{f: d[f] for f in fields} for d in INVENTORY if d["status"] == "up"]

    # Task C — check json_inventory
    json_inv = ns.get("json_inventory")
    exp_json_inv = INVENTORY  # full list

    # Task D — check vlan_counts
    vlan_counts = ns.get("vlan_counts")
    exp_vc = {d["hostname"]: len(d["vlans"]) for d in INVENTORY}

    # Also verify JSON file has vlan_count
    json_path = os.path.join(work_dir_2, "inventory.json")
    json_has_vc = False
    if os.path.exists(json_path):
        with open(json_path) as f:
            jdata = json.load(f)
        json_has_vc = all("vlan_count" in d for d in jdata)

    grade(2, [
        (
            "Task A", "inventory.csv — 8 rows with hostname/platform/status/ip",
            csv_rows, exp_csv_rows,
            "See Chapter 7.2 — DictWriter(f, fieldnames=[...]), writeheader(), writerows(INVENTORY). Use newline=''.",
            "with open('inventory.csv','w',newline='') as f:\n    w=csv.DictWriter(f,fieldnames=['hostname','platform','status','ip'],extrasaction='ignore')\n    w.writeheader()\n    w.writerows(INVENTORY)",
            "inventory.csv contents",
        ),
        (
            "Task B", "csv_devices — 5 up-only device dicts from CSV",
            csv_devices, exp_csv_up,
            "See Chapter 7.3 — DictReader, filter rows where row['status']=='up'.",
            "with open('inventory.csv',newline='') as f:\n    csv_devices=[dict(r) for r in csv.DictReader(f) if r['status']=='up']",
            "csv_devices",
        ),
        (
            "Task C", "json_inventory — full 8-device list loaded from JSON file",
            json_inv, exp_json_inv,
            "See Chapter 8.2/8.3 — json.dump(INVENTORY, f, indent=2) then json.load(f).",
            "with open('inventory.json','w') as f:\n    json.dump(INVENTORY,f,indent=2)\nwith open('inventory.json') as f:\n    json_inventory=json.load(f)",
            "json_inventory",
        ),
        (
            "Task D", "vlan_counts — hostname → vlan_count dict (enriched JSON written back)",
            vlan_counts, exp_vc,
            "See Chapter 8.4 — load, add vlan_count, write back, reload, build dict.",
            "with open('inventory.json') as f: data=json.load(f)\nfor d in data: d['vlan_count']=len(d['vlans'])\nwith open('inventory.json','w') as f: json.dump(data,f,indent=2)\nwith open('inventory.json') as f: data=json.load(f)\nvlan_counts={d['hostname']:d['vlan_count'] for d in data}",
            "vlan_counts",
        ),
    ])

shutil.rmtree(work_dir_2, ignore_errors=True)
pause()

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}   Both challenges complete.{RESET}")
print(f"{BOLD}   You are ready for the next topic.{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()