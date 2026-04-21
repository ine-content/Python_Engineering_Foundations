# file_io_deep_dive.py
# File I/O in Python — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

import os
import csv
import json
import shutil
import tempfile

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"    # >>> commands
GREEN  = "\033[92m"    # output values
YELLOW = "\033[93m"    # highlights
WHITE  = "\033[97m"    # explanations
RED    = "\033[91m"    # warnings / errors
BOLD   = "\033[1m"
DIM    = "\033[2m"

def pause():
    input(f"\n{DIM}  [ Press ENTER to continue ]{RESET} ")
    print()

def cmd(command):
    print(f"    {CYAN}>>> {command}{RESET}")

def out(value):
    print(f"    {GREEN}{value}{RESET}")

def warn(value):
    print(f"    {RED}{value}{RESET}")

def explain(text):
    print(f"  {WHITE}{text}{RESET}")

def blank():
    print()

def section(title):
    print(f"{BOLD}{'─' * 62}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'─' * 62}{RESET}")
    blank()

def chapter(num, title):
    bar = "█" * 62
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    print()
    print(f"{BOLD}   CHAPTER {num}{RESET}")
    print(f"{BOLD}   {title}{RESET}")
    print()
    print(f"{BOLD}{bar}{RESET}")
    print(f"{BOLD}{bar}{RESET}")
    blank()

# ── Working directory for demo files ─────────────────────────────────────────
DEMO_DIR = tempfile.mkdtemp(prefix="iac_demo_")

def demo_path(filename):
    return os.path.join(DEMO_DIR, filename)

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         FILE I/O — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is File I/O and Why It Matters in IaC
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is File I/O and Why It Matters in IaC")

section("1.1 — Definition")

explain("File I/O — Input/Output — is reading data from files")
explain("and writing data to files on disk.")
blank()
explain("In Cisco IaC, files are everywhere:")
blank()
explain("  READ  — device inventory CSV, JSON config, hostname list")
explain("  WRITE — generated configs per device, audit reports,")
explain("          compliance logs, enriched inventory JSON")
blank()
explain("Without file I/O, your IaC scripts can only work with")
explain("data that is hardcoded. With file I/O, they work with")
explain("real, external, dynamic data sources.")
blank()

pause()

explain("Typical IaC file workflow:")
blank()
explain("  1. Read inventory.csv  → list of device dicts")
explain("  2. Validate each device")
explain("  3. Generate config per device")
explain("  4. Write configs/nyc-rtr-01.cfg, configs/lon-sw-01.cfg ...")
explain("  5. Write audit_report.txt with results")
blank()

pause()

section("1.2 — Text vs Binary Files")

explain("TEXT files — human-readable characters.")
explain("  .txt .cfg .csv .json .yaml .log")
explain("  Open with mode 'r', 'w', 'a'")
blank()
explain("BINARY files — raw bytes, not human-readable.")
explain("  .png .zip .db .xlsx")
explain("  Open with mode 'rb', 'wb'")
blank()
explain("In Cisco IaC we almost always work with text files.")
explain("Configs, inventories, logs — all plain text.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — open() and the with Statement
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "open() and the with Statement")

section("2.1 — File Modes")

explain("The mode tells Python HOW to open the file:")
blank()
explain("  'r'  — read    (default) — file must exist")
explain("  'w'  — write   — creates file, OVERWRITES if exists")
explain("  'a'  — append  — creates file, adds to end if exists")
explain("  'x'  — create  — creates file, FAILS if exists")
blank()
explain("  'r+' — read and write")
explain("  'rb' — read binary")
blank()

pause()

section("2.2 — The with Statement")

explain("Always use 'with' to open files.")
explain("It automatically closes the file when the block ends,")
explain("even if an error occurs inside the block.")
blank()

cmd("# The with statement — recommended")
cmd("with open('devices.txt', 'w') as f:")
cmd("    f.write('nyc-rtr-01\\n')")
blank()
explain("'f' is the file object. It is closed automatically")
explain("when the with block exits — no need to call f.close().")
blank()

pause()

cmd("# Without with — risky")
cmd("f = open('devices.txt', 'w')")
cmd("f.write('nyc-rtr-01\\n')")
cmd("f.close()   # must call manually — easy to forget")
blank()
warn("If an error happens before f.close(), the file stays open.")
warn("This can corrupt the file or leak a file handle.")
blank()

pause()

section("2.3 — Writing a Simple File")

explain("Create a device hostname list and write it to a file:")
blank()

hostnames = [
    "nyc-rtr-01", "lon-sw-01", "sin-fw-01",
    "ams-rtr-02", "tok-sw-01", "syd-rtr-01",
]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01',")
cmd("             'ams-rtr-02', 'tok-sw-01', 'syd-rtr-01']")
blank()

path = demo_path("devices.txt")
cmd(f"with open('devices.txt', 'w') as f:")
cmd("    for h in hostnames:")
cmd("        f.write(h + '\\n')")
with open(path, "w") as f:
    for h in hostnames:
        f.write(h + "\n")
blank()

cmd("# Verify — check file contents")
cmd("with open('devices.txt', 'r') as f:")
cmd("    print(f.read())")
blank()
with open(path, "r") as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Reading Files
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Reading Files")

section("3.1 — .read() — Entire File as One String")

explain(".read() returns the entire file content as one string.")
explain("Use for small files where you want everything at once.")
blank()

cmd("with open('devices.txt', 'r') as f:")
cmd("    content = f.read()")
cmd("print(type(content))")
cmd("print(repr(content[:40]))")
with open(path, "r") as f:
    content = f.read()
out(type(content))
out(repr(content[:40]))
blank()

pause()

section("3.2 — .readlines() — All Lines as a List")

explain(".readlines() returns a list of lines — each with \\n.")
explain("Use when you need to index specific lines.")
blank()

cmd("with open('devices.txt', 'r') as f:")
cmd("    lines = f.readlines()")
cmd("print(lines)")
with open(path, "r") as f:
    lines = f.readlines()
out(lines)
blank()

pause()

explain("Strip the \\n from each line:")
blank()
cmd("lines = [line.strip() for line in lines]")
lines = [line.strip() for line in lines]
cmd("print(lines)")
out(lines)
blank()

pause()

section("3.3 — Iterate Line by Line — Most Common Pattern")

explain("Iterate the file object directly — memory efficient.")
explain("Python reads one line at a time. Best for large files.")
blank()

cmd("with open('devices.txt', 'r') as f:")
cmd("    for line in f:")
cmd("        hostname = line.strip()")
cmd("        if hostname:   # skip blank lines")
cmd("            print(f'  Connecting to {hostname}...')")
blank()
with open(path, "r") as f:
    for line in f:
        hostname = line.strip()
        if hostname:
            out(f"  Connecting to {hostname}...")
blank()

pause()

section("3.4 — Parsing a Structured Text File")

explain("Real IaC files often have fields separated by spaces")
explain("or pipes. Parse them into dicts as you read.")
blank()

# Write a structured device file first
device_list_path = demo_path("device_list.txt")
device_list_content = """\
# Cisco IaC Device List
# hostname        platform   ip
nyc-rtr-01        IOS-XE     10.0.0.1
lon-sw-01         NX-OS      10.1.0.1
sin-fw-01         ASA        10.2.0.1
ams-rtr-02        IOS-XE     10.3.0.1
"""
with open(device_list_path, "w") as f:
    f.write(device_list_content)

cmd("# device_list.txt contains:")
cmd("# hostname        platform   ip")
cmd("# nyc-rtr-01      IOS-XE     10.0.0.1")
cmd("# lon-sw-01       NX-OS      10.1.0.1")
cmd("# ...")
blank()

cmd("devices = []")
cmd("with open('device_list.txt', 'r') as f:")
cmd("    for line in f:")
cmd("        line = line.strip()")
cmd("        if not line or line.startswith('#'):")
cmd("            continue   # skip blank lines and comments")
cmd("        parts = line.split()")
cmd("        devices.append({")
cmd("            'hostname': parts[0],")
cmd("            'platform': parts[1],")
cmd("            'ip':       parts[2],")
cmd("        })")
blank()

devices = []
with open(device_list_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        devices.append({
            "hostname": parts[0],
            "platform": parts[1],
            "ip":       parts[2],
        })

cmd("for d in devices: print(d)")
blank()
for d in devices:
    out(d)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Writing Files
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Writing Files")

section("4.1 — .write() — Write a String")

explain(".write() writes exactly what you give it.")
explain("It does NOT add a newline — you must add \\n yourself.")
blank()

report_path = demo_path("audit_report.txt")
cmd("with open('audit_report.txt', 'w') as f:")
cmd("    f.write('=== Cisco IaC Audit Report ===\\n')")
cmd("    f.write(f'Devices scanned: {len(devices)}\\n')")
cmd("    for d in devices:")
cmd("        f.write(f\"  {d['hostname']}: {d['platform']} {d['ip']}\\n\")")
blank()

with open(report_path, "w") as f:
    f.write("=== Cisco IaC Audit Report ===\n")
    f.write(f"Devices scanned: {len(devices)}\n")
    for d in devices:
        f.write(f"  {d['hostname']}: {d['platform']} {d['ip']}\n")

cmd("with open('audit_report.txt') as f:")
cmd("    print(f.read())")
blank()
with open(report_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

section("4.2 — Append Mode — Add Without Overwriting")

explain("Mode 'a' opens the file and adds to the END.")
explain("Use for log files where you want to keep old entries.")
blank()

log_path = demo_path("deploy_log.txt")
cmd("# First write")
cmd("with open('deploy_log.txt', 'w') as f:")
cmd("    f.write('2024-01-01 nyc-rtr-01 config pushed\\n')")
with open(log_path, "w") as f:
    f.write("2024-01-01 nyc-rtr-01 config pushed\n")
blank()

cmd("# Append a new entry — does not overwrite")
cmd("with open('deploy_log.txt', 'a') as f:")
cmd("    f.write('2024-01-02 lon-sw-01 config pushed\\n')")
with open(log_path, "a") as f:
    f.write("2024-01-02 lon-sw-01 config pushed\n")
blank()

cmd("with open('deploy_log.txt') as f:")
cmd("    print(f.read())")
blank()
with open(log_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

section("4.3 — writelines() — Write a List of Strings")

explain(".writelines() writes each string in a list.")
explain("Does NOT add newlines — include them in each string.")
blank()

cmd("ntp_servers = ['10.0.0.100', '10.0.0.101', '10.0.0.102']")
ntp_servers = ["10.0.0.100", "10.0.0.101", "10.0.0.102"]
ntp_path = demo_path("ntp_servers.txt")
cmd("lines = [f'ntp server {s}\\n' for s in ntp_servers]")
lines = [f"ntp server {s}\n" for s in ntp_servers]
cmd("with open('ntp_servers.txt', 'w') as f:")
cmd("    f.writelines(lines)")
with open(ntp_path, "w") as f:
    f.writelines(lines)
blank()

cmd("with open('ntp_servers.txt') as f:")
cmd("    print(f.read())")
blank()
with open(ntp_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Working with Paths
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Working with Paths")

section("5.1 — os.path — Classic Path Operations")

explain("os.path works on all operating systems.")
blank()

cmd("import os")
blank()
cmd("path = 'configs/nyc-rtr-01.cfg'")
path_str = "configs/nyc-rtr-01.cfg"
blank()
cmd("print(os.path.basename(path))")
out(os.path.basename(path_str))
cmd("print(os.path.dirname(path))")
out(os.path.dirname(path_str))
cmd("print(os.path.splitext(path))")
out(os.path.splitext(path_str))
blank()

pause()

cmd("print(os.path.join('configs', 'nyc-rtr-01.cfg'))")
out(os.path.join("configs", "nyc-rtr-01.cfg"))
cmd("print(os.path.exists('devices.txt'))")
out(os.path.exists(path))
cmd("print(os.path.exists('nonexistent.txt'))")
out(os.path.exists("nonexistent.txt"))
blank()

pause()

section("5.2 — pathlib.Path — Modern Path Operations")

explain("pathlib.Path (Python 3.4+) is object-oriented.")
explain("Cleaner syntax, works on all platforms.")
blank()

from pathlib import Path
cmd("from pathlib import Path")
blank()

cmd("p = Path('configs/nyc-rtr-01.cfg')")
p = Path("configs/nyc-rtr-01.cfg")
cmd("print(p.name)")
out(p.name)
cmd("print(p.stem)")
out(p.stem)
cmd("print(p.suffix)")
out(p.suffix)
cmd("print(p.parent)")
out(p.parent)
blank()

pause()

cmd("# Build paths with / operator")
cmd("base = Path('configs')")
base = Path("configs")
cmd("device_path = base / 'nyc-rtr-01.cfg'")
device_path = base / "nyc-rtr-01.cfg"
cmd("print(device_path)")
out(device_path)
blank()

pause()

section("5.3 — Creating Directories and Listing Files")

explain("Create a directory if it does not exist:")
blank()

configs_dir = demo_path("configs")
cmd("os.makedirs('configs', exist_ok=True)")
os.makedirs(configs_dir, exist_ok=True)
cmd("# exist_ok=True — no error if it already exists")
blank()

explain("Write one config file per device:")
blank()
inventory_for_files = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "ip": "10.2.0.1"},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'ip': '10.1.0.1'},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'ip': '10.2.0.1'},")
cmd("]")
blank()
cmd("for device in inventory:")
cmd("    filepath = os.path.join('configs', f\"{device['hostname']}.cfg\")")
cmd("    with open(filepath, 'w') as f:")
cmd("        f.write(f\"hostname {device['hostname']}\\n\")")
cmd("        f.write(f\"! platform: {device['platform']}\\n\")")
cmd("        f.write(f\"! ip: {device['ip']}\\n\")")
blank()

for device in inventory_for_files:
    filepath = os.path.join(configs_dir, f"{device['hostname']}.cfg")
    with open(filepath, "w") as f:
        f.write(f"hostname {device['hostname']}\n")
        f.write(f"! platform: {device['platform']}\n")
        f.write(f"! ip: {device['ip']}\n")

explain("List all .cfg files in the configs directory:")
blank()
cmd("cfg_files = [f for f in os.listdir('configs') if f.endswith('.cfg')]")
cfg_files = [f for f in os.listdir(configs_dir) if f.endswith(".cfg")]
cmd("for f in sorted(cfg_files): print(f)")
blank()
for f in sorted(cfg_files):
    out(f)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Generating and Writing Config Files
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Generating and Writing Config Files")

section("6.1 — One Config File Per Device")

explain("The core IaC file pattern — generate a config block")
explain("for each device and write each to its own file.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE",
     "ip": "10.0.0.1", "vlans": [10, 20, 30],
     "ntp": "10.0.0.100", "dns": "8.8.8.8"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",
     "ip": "10.1.0.1", "vlans": [10, 20],
     "ntp": "10.1.0.100", "dns": "8.8.8.8"},
    {"hostname": "sin-fw-01",  "platform": "ASA",
     "ip": "10.2.0.1", "vlans": [30, 40],
     "ntp": "10.0.0.100", "dns": "8.8.8.8"},
]
cmd("inventory = [  # 3 devices with ntp/dns/vlans ]")
blank()

cmd("def generate_config(device):")
cmd("    lines = [")
cmd("        f\"hostname {device['hostname']}\",")
cmd("        f\"! Platform: {device['platform']}\",")
cmd("        f\"ip address {device['ip']}\",")
cmd("        f\"ntp server {device['ntp']}\",")
cmd("        f\"ip name-server {device['dns']}\",")
cmd("    ]")
cmd("    for vlan in device['vlans']:")
cmd("        lines.append(f'vlan {vlan}')")
cmd("    return '\\n'.join(lines)")
blank()

def generate_config(device):
    lines = [
        f"hostname {device['hostname']}",
        f"! Platform: {device['platform']}",
        f"ip address {device['ip']}",
        f"ntp server {device['ntp']}",
        f"ip name-server {device['dns']}",
    ]
    for vlan in device["vlans"]:
        lines.append(f"vlan {vlan}")
    return "\n".join(lines)

pause()

gen_configs_dir = demo_path("generated_configs")
os.makedirs(gen_configs_dir, exist_ok=True)
cmd("os.makedirs('generated_configs', exist_ok=True)")
cmd("for device in inventory:")
cmd("    config = generate_config(device)")
cmd("    filepath = os.path.join('generated_configs', f\"{device['hostname']}.cfg\")")
cmd("    with open(filepath, 'w') as f:")
cmd("        f.write(config)")
cmd("    print(f\"Wrote {filepath}\")")
blank()

for device in inventory:
    config = generate_config(device)
    filepath = os.path.join(gen_configs_dir, f"{device['hostname']}.cfg")
    with open(filepath, "w") as f:
        f.write(config)
    out(f"Wrote {device['hostname']}.cfg")
blank()

pause()

explain("Read back and print one config to verify:")
blank()
sample_path = os.path.join(gen_configs_dir, "nyc-rtr-01.cfg")
cmd("with open('generated_configs/nyc-rtr-01.cfg') as f:")
cmd("    print(f.read())")
blank()
with open(sample_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

section("6.2 — Writing an Audit Report")

explain("After processing devices, write a summary report:")
blank()

report2_path = demo_path("deployment_report.txt")
cmd("with open('deployment_report.txt', 'w') as f:")
cmd("    f.write('=== Deployment Report ===\\n\\n')")
cmd("    for device in inventory:")
cmd("        status = 'OK' if device['platform'] in ('IOS-XE','NX-OS') else 'REVIEW'")
cmd("        f.write(f\"[{status}] {device['hostname']} ({device['platform']})\\n\")")
blank()

with open(report2_path, "w") as f:
    f.write("=== Deployment Report ===\n\n")
    for device in inventory:
        status = "OK" if device["platform"] in ("IOS-XE", "NX-OS") else "REVIEW"
        f.write(f"[{status}] {device['hostname']} ({device['platform']})\n")

cmd("with open('deployment_report.txt') as f:")
cmd("    print(f.read())")
blank()
with open(report2_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — CSV Files
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "CSV Files")

section("7.1 — Why CSV in IaC")

explain("CSV (Comma Separated Values) is the universal format")
explain("for device inventories in Cisco IaC.")
blank()
explain("Network engineers maintain device lists in Excel.")
explain("Export as CSV → your Python script reads it.")
explain("Your script processes and writes a new CSV back.")
blank()

pause()

section("7.2 — csv.DictWriter — Write CSV with Headers")

explain("DictWriter writes dicts as rows — header comes first.")
blank()

inventory_csv = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "ip": "10.3.0.1"},
]
csv_path = demo_path("inventory.csv")
cmd("import csv")
cmd("inventory = [  # 4 device dicts ]")
blank()

cmd("with open('inventory.csv', 'w', newline='') as f:")
cmd("    fields = ['hostname', 'platform', 'status', 'ip']")
cmd("    writer = csv.DictWriter(f, fieldnames=fields)")
cmd("    writer.writeheader()")
cmd("    writer.writerows(inventory)")
blank()

with open(csv_path, "w", newline="") as f:
    fields = ["hostname", "platform", "status", "ip"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(inventory_csv)

explain("Let's see what the CSV looks like:")
blank()
with open(csv_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

section("7.3 — csv.DictReader — Read CSV into List of Dicts")

explain("DictReader reads each row as a dict using the header.")
explain("This is the most common CSV read pattern in IaC.")
blank()

cmd("devices = []")
cmd("with open('inventory.csv', 'r', newline='') as f:")
cmd("    reader = csv.DictReader(f)")
cmd("    for row in reader:")
cmd("        devices.append(dict(row))")
blank()

devices_from_csv = []
with open(csv_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        devices_from_csv.append(dict(row))

cmd("for d in devices: print(d)")
blank()
for d in devices_from_csv:
    out(d)
blank()

pause()

explain("Filter and write a subset back to a new CSV:")
blank()
up_csv_path = demo_path("inventory_up.csv")
cmd("up_devices = [d for d in devices if d['status'] == 'up']")
up_devices = [d for d in devices_from_csv if d["status"] == "up"]
blank()
cmd("with open('inventory_up.csv', 'w', newline='') as f:")
cmd("    writer = csv.DictWriter(f, fieldnames=fields)")
cmd("    writer.writeheader()")
cmd("    writer.writerows(up_devices)")
blank()
with open(up_csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(up_devices)

cmd("with open('inventory_up.csv') as f:")
cmd("    print(f.read())")
blank()
with open(up_csv_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — JSON Files (File Layer Only)
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "JSON Files")

section("8.1 — Why JSON in IaC")

explain("JSON is the standard format for machine-readable")
explain("device inventories and config data in IaC.")
blank()
explain("Ansible, Nornir, and Netmiko all work with JSON.")
explain("Your Python script reads inventory.json, processes")
explain("each device, and writes the enriched result back.")
blank()
explain("This chapter covers JSON as FILE I/O only.")
explain("Deep JSON parsing and serialization is its own topic.")
blank()

pause()

section("8.2 — json.dump() — Write Python Object to JSON File")

explain("json.dump() serialises a Python object and writes")
explain("it directly to a file.")
blank()

inventory_json = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "vlans": [10, 20, 30], "config": {"ntp": "10.0.0.100"}},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
     "vlans": [10, 20],     "config": {"ntp": "10.1.0.100"}},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
     "vlans": [30, 40, 50], "config": {"ntp": "10.0.0.100"}},
]
json_path = demo_path("inventory.json")

cmd("import json")
cmd("inventory = [  # 3 device dicts ]")
blank()

cmd("with open('inventory.json', 'w') as f:")
cmd("    json.dump(inventory, f, indent=2)")
blank()

with open(json_path, "w") as f:
    json.dump(inventory_json, f, indent=2)

explain("indent=2 makes the JSON human-readable:")
blank()
cmd("with open('inventory.json') as f:")
cmd("    print(f.read())")
blank()
with open(json_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

section("8.3 — json.load() — Read JSON File into Python Object")

explain("json.load() reads a JSON file and returns")
explain("the equivalent Python object — list, dict, etc.")
blank()

cmd("with open('inventory.json') as f:")
cmd("    data = json.load(f)")
blank()

with open(json_path) as f:
    data = json.load(f)

cmd("print(type(data))")
out(type(data))
cmd("print(len(data))")
out(len(data))
cmd("print(data[0]['hostname'])")
out(data[0]["hostname"])
cmd("print(data[0]['vlans'])")
out(data[0]["vlans"])
blank()

pause()

section("8.4 — Read, Enrich, Write Back")

explain("The full IaC JSON file pattern:")
explain("load → process → write back")
blank()

cmd("# 1. Load")
cmd("with open('inventory.json') as f:")
cmd("    inventory = json.load(f)")
blank()

cmd("# 2. Enrich — add vlan_count to each device")
cmd("for device in inventory:")
cmd("    device['vlan_count'] = len(device['vlans'])")
blank()

cmd("# 3. Write back")
cmd("with open('inventory.json', 'w') as f:")
cmd("    json.dump(inventory, f, indent=2)")
blank()

with open(json_path) as f:
    inventory_loaded = json.load(f)
for device in inventory_loaded:
    device["vlan_count"] = len(device["vlans"])
with open(json_path, "w") as f:
    json.dump(inventory_loaded, f, indent=2)

cmd("# Verify")
cmd("with open('inventory.json') as f:")
cmd("    data = json.load(f)")
cmd("print(data[0])")
blank()
with open(json_path) as f:
    verified = json.load(f)
out(verified[0])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Checking and Protecting Files
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Checking and Protecting Files")

section("9.1 — Check Before Writing")

explain("In IaC, never silently overwrite an existing config.")
explain("Always check if the file exists first.")
blank()

hostname = "nyc-rtr-01"
cfg_check_path = demo_path(f"{hostname}.cfg")
cmd(f"hostname = 'nyc-rtr-01'")
cmd("filepath = f'{hostname}.cfg'")
blank()

cmd("if os.path.exists(filepath):")
cmd("    print(f'WARNING: {filepath} already exists — skipping')")
cmd("else:")
cmd("    with open(filepath, 'w') as f:")
cmd("        f.write('hostname nyc-rtr-01\\n')")
cmd("    print(f'Written: {filepath}')")
blank()

if os.path.exists(cfg_check_path):
    out(f"WARNING: {hostname}.cfg already exists — skipping")
else:
    with open(cfg_check_path, "w") as f:
        f.write("hostname nyc-rtr-01\n")
    out(f"Written: {hostname}.cfg")
blank()

cmd("# Run again — file now exists")
if os.path.exists(cfg_check_path):
    out(f"WARNING: {hostname}.cfg already exists — skipping")
else:
    with open(cfg_check_path, "w") as f:
        f.write("hostname nyc-rtr-01\n")
    out(f"Written: {hostname}.cfg")
blank()

pause()

section("9.2 — Mode 'x' — Exclusive Creation")

explain("Mode 'x' creates a new file but raises FileExistsError")
explain("if the file already exists — fail-safe write.")
blank()

safe_path = demo_path("safe_test.cfg")
cmd("try:")
cmd("    with open('safe_test.cfg', 'x') as f:")
cmd("        f.write('hostname safe-device\\n')")
cmd("    print('File created')")
cmd("except FileExistsError:")
cmd("    print('File already exists — not overwritten')")
blank()

try:
    with open(safe_path, "x") as f:
        f.write("hostname safe-device\n")
    out("File created")
except FileExistsError:
    out("File already exists — not overwritten")

try:
    with open(safe_path, "x") as f:
        f.write("hostname safe-device\n")
    out("File created")
except FileExistsError:
    out("File already exists — not overwritten")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — Forgetting newline='') with CSV")

explain("On Windows, csv.writer adds \\r\\n if you don't")
explain("pass newline='' — causing extra blank lines.")
blank()

cmd("# Wrong — may produce double blank lines on Windows")
cmd("with open('inventory.csv', 'w') as f:  # missing newline=''")
cmd("    writer = csv.writer(f)")
blank()

cmd("# Correct — always use newline='' with csv module")
cmd("with open('inventory.csv', 'w', newline='') as f:")
cmd("    writer = csv.writer(f)")
blank()
explain("Rule: always pass newline='' when opening CSV files.")

pause()

section("10.2 — 'w' Overwrites Silently")

explain("Mode 'w' deletes all existing content without warning.")
explain("In IaC this can destroy a config file you worked hard")
explain("to build. Always think before using 'w'.")
blank()

cmd("# Dangerous — silently overwrites")
cmd("with open('nyc-rtr-01.cfg', 'w') as f:")
cmd("    f.write('wrong config')   # previous config is gone!")
blank()

cmd("# Safer pattern — write to temp, rename when done")
cmd("import tempfile, shutil")
cmd("with tempfile.NamedTemporaryFile('w', delete=False) as tmp:")
cmd("    tmp.write('correct config')")
cmd("    tmp_name = tmp.name")
cmd("shutil.move(tmp_name, 'nyc-rtr-01.cfg')   # atomic replace")
blank()
explain("This way, if writing fails halfway, the original is safe.")

pause()

section("10.3 — Encoding Issues")

explain("Always specify encoding='utf-8' when reading/writing")
explain("files that may contain non-ASCII characters.")
blank()

cmd("# Safe — always explicit about encoding")
cmd("with open('inventory.json', 'r', encoding='utf-8') as f:")
cmd("    data = json.load(f)")
blank()
cmd("with open('report.txt', 'w', encoding='utf-8') as f:")
cmd("    f.write('Device: ams-rtr-02 — status: ✔')")
blank()
explain("utf-8 is the standard for Cisco IaC tooling.")

pause()

section("10.4 — Path Separators — Windows vs Mac/Linux")

explain("Never hardcode / or \\ in paths.")
explain("Use os.path.join() or pathlib.Path / operator.")
blank()

cmd("# Wrong — breaks on Windows")
cmd("path = 'configs/' + hostname + '.cfg'")
blank()

cmd("# Correct — works on all platforms")
cmd("path = os.path.join('configs', hostname + '.cfg')")
out(os.path.join("configs", "nyc-rtr-01.cfg"))
blank()

cmd("# Or with pathlib")
cmd("path = Path('configs') / f'{hostname}.cfg'")
out(Path("configs") / "nyc-rtr-01.cfg")
blank()

pause()

# ── Clean up demo files ───────────────────────────────────────────────────────
shutil.rmtree(DEMO_DIR, ignore_errors=True)

# ═════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
bar = "█" * 62
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}   SUMMARY — ZERO TO EXPERT{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
blank()
print(f"  {BOLD}Ch 1{RESET}   What is File I/O — IaC workflow, text vs binary")
print(f"  {BOLD}Ch 2{RESET}   open() and with — modes r/w/a/x, why with is essential")
print(f"  {BOLD}Ch 3{RESET}   Reading — .read(), .readlines(), line-by-line, parse structured")
print(f"  {BOLD}Ch 4{RESET}   Writing — .write(), append mode, .writelines()")
print(f"  {BOLD}Ch 5{RESET}   Paths — os.path, pathlib, makedirs, list .cfg files")
print(f"  {BOLD}Ch 6{RESET}   Config files — generate + write per device, audit report")
print(f"  {BOLD}Ch 7{RESET}   CSV — DictWriter/DictReader, filter and write subset")
print(f"  {BOLD}Ch 8{RESET}   JSON — json.dump/load, read-enrich-write-back pattern")
print(f"  {BOLD}Ch 9{RESET}   Protecting files — check exists, mode 'x', safe overwrite")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — newline='' CSV, 'w' overwrites, encoding, path sep")
blank()
print(f"  {WHITE}Every example used real Cisco IaC tasks —")
print(f"  reading device inventories, writing configs per device,")
print(f"  CSV/JSON round-trips, audit reports, deployment logs.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()