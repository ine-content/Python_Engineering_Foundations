# yaml_deep_dive.py
# YAML Parsing — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

import yaml
import json
import os
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

def yaml_block(text):
    """Print a YAML snippet in cyan with no >>> prefix."""
    for line in text.splitlines():
        print(f"    {CYAN}{line}{RESET}")

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
DEMO_DIR = tempfile.mkdtemp(prefix="yaml_demo_")

def demo(filename):
    return os.path.join(DEMO_DIR, filename)

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         YAML PARSING — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is YAML and Why IaC Uses It
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is YAML and Why IaC Uses It")

section("1.1 — Definition")

explain("YAML — YAML Ain't Markup Language.")
explain("A human-readable data serialization format.")
explain("Designed for config files that humans write and edit.")
blank()
explain("In Cisco IaC, YAML is the dominant human-facing format:")
blank()
explain("  Ansible     — playbooks, inventory, host_vars, group_vars")
explain("  Nornir      — hosts.yaml, groups.yaml, defaults.yaml")
explain("  NetBox      — device export/import YAML")
explain("  Custom IaC  — intent files, site configs, VLAN definitions")
blank()
explain("Rule of thumb in IaC:")
explain("  Humans write YAML. Machines produce/consume JSON.")
blank()

pause()

section("1.2 — YAML vs JSON — Same Data, Different Look")

explain("JSON version of a device config:")
blank()
yaml_block('''{
  "hostname": "nyc-rtr-01",
  "platform": "IOS-XE",
  "vlans": [10, 20, 30]
}''')
blank()

explain("Exact same data as YAML:")
blank()
yaml_block('''hostname: nyc-rtr-01
platform: IOS-XE
vlans:
  - 10
  - 20
  - 30''')
blank()
explain("No quotes. No braces. No brackets. Pure indentation.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — YAML Syntax Fundamentals
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "YAML Syntax Fundamentals")

section("2.1 — Scalars — Strings, Numbers, Booleans, Null")

explain("A scalar is a single value — no nesting.")
blank()
yaml_block('''# Strings — quotes optional unless special characters
hostname: nyc-rtr-01
description: "Core router - primary"
notes: \'backup every 24h\'

# Numbers
port:       22
latency:    1.5

# Booleans — true/false (also yes/no, on/off — be careful!)
enabled:    true
monitored:  false

# Null
last_backup: null
vendor:      ~     # ~ is also null in YAML''')
blank()

pause()

section("2.2 — Mappings — Key-Value Pairs")

explain("A mapping is a set of key: value pairs.")
explain("Equivalent to a Python dict or JSON object.")
blank()
yaml_block('''device:
  hostname: nyc-rtr-01
  platform: IOS-XE
  ip: 10.0.0.1
  config:
    ntp: 10.0.0.100
    dns: 8.8.8.8''')
blank()
explain("Indentation defines nesting — 2 spaces is standard.")
explain("DO NOT use tabs — tabs are illegal in YAML.")

pause()

section("2.3 — Sequences — Lists")

explain("A sequence is a list of items, each prefixed with '-'.")
blank()
yaml_block('''# List of strings
ntp_servers:
  - 10.0.0.100
  - 10.0.0.101
  - 10.0.0.102

# List of dicts (devices)
devices:
  - hostname: nyc-rtr-01
    platform: IOS-XE
    status:   up
  - hostname: lon-sw-01
    platform: NX-OS
    status:   down

# Inline list (flow style) — same as above
vlans: [10, 20, 30]''')
blank()

pause()

section("2.4 — Comments and Multiline Strings")

explain("YAML supports comments with # — JSON does not.")
blank()
yaml_block('''# Site: New York
# Owner: Network Ops Team

hostname: nyc-rtr-01   # primary router

# Literal block — preserves newlines (|)
config: |
  hostname nyc-rtr-01
  ntp server 10.0.0.100
  ip domain-name corp.net

# Folded block — newlines become spaces (>)
description: >
  This is the primary
  router for the NYC site.
  Managed by NetOps.''')
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — PyYAML Basics
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "PyYAML Basics")

section("3.1 — yaml.safe_load() — Parse a YAML String")

explain("safe_load() parses a YAML string into a Python object.")
explain("ALWAYS use safe_load, never yaml.load() — it's unsafe")
explain("with untrusted input (can execute arbitrary code).")
blank()

yaml_str = """\
hostname: nyc-rtr-01
platform: IOS-XE
status:   up
vlans:
  - 10
  - 20
  - 30
config:
  ntp: 10.0.0.100
  dns: 8.8.8.8
"""
cmd('yaml_str = """')
cmd('hostname: nyc-rtr-01')
cmd('platform: IOS-XE')
cmd('status:   up')
cmd('vlans:')
cmd('  - 10')
cmd('  - 20')
cmd('  - 30')
cmd('config:')
cmd('  ntp: 10.0.0.100')
cmd('  dns: 8.8.8.8')
cmd('"""')
blank()

cmd("device = yaml.safe_load(yaml_str)")
device = yaml.safe_load(yaml_str)
cmd("print(device)")
out(device)
cmd("print(type(device))")
out(type(device))
blank()

pause()

cmd("print(device['hostname'])")
out(device["hostname"])
cmd("print(device['vlans'])")
out(device["vlans"])
cmd("print(device['config']['ntp'])")
out(device["config"]["ntp"])
blank()

pause()

section("3.2 — Loading YAML from a File")

explain("Use open() + yaml.safe_load() together.")
blank()

inventory_yaml = """\
devices:
  - hostname: nyc-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.0.0.1
    vlans:    [10, 20, 30]
  - hostname: lon-sw-01
    platform: NX-OS
    status:   down
    ip:       10.1.0.1
    vlans:    [10, 20]
  - hostname: sin-fw-01
    platform: ASA
    status:   up
    ip:       10.2.0.1
    vlans:    [30, 40, 50]
"""

inv_path = demo("inventory.yaml")
with open(inv_path, "w") as f:
    f.write(inventory_yaml)

cmd("with open('inventory.yaml') as f:")
cmd("    data = yaml.safe_load(f)")
with open(inv_path) as f:
    data = yaml.safe_load(f)

cmd("print(type(data))")
out(type(data))
cmd("print(len(data['devices']))")
out(len(data["devices"]))
cmd("for d in data['devices']:")
cmd("    print(d['hostname'], d['platform'], d['status'])")
blank()
for d in data["devices"]:
    out(f"{d['hostname']} {d['platform']} {d['status']}")
blank()

pause()

section("3.3 — yaml.dump() — Serialize to YAML")

explain("yaml.dump() converts a Python object to YAML string.")
blank()

devices_py = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE",
     "status": "up", "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",
     "status": "down", "vlans": [10, 20]},
]
cmd("devices = [  # list of device dicts ]")
blank()
cmd("yaml_out = yaml.dump(devices, default_flow_style=False)")
yaml_out = yaml.dump(devices_py, default_flow_style=False)
cmd("print(yaml_out)")
blank()
for line in yaml_out.splitlines():
    out(line)
blank()

pause()

explain("default_flow_style=False — block style (human-readable).")
explain("default_flow_style=True  — inline/flow style (compact).")
blank()
cmd("print(yaml.dump(devices[0], default_flow_style=True))")
out(yaml.dump(devices_py[0], default_flow_style=True).strip())
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Python ↔ YAML Type Mapping
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Python ↔ YAML Type Mapping")

section("4.1 — The Full Mapping")

explain("YAML → Python:")
blank()
explain("  mapping    →  dict")
explain("  sequence   →  list")
explain("  string     →  str")
explain("  integer    →  int")
explain("  float      →  float")
explain("  true/false →  True/False")
explain("  null / ~   →  None")
explain("  2024-01-15 →  datetime.date  (automatic!)")
blank()

pause()

type_yaml = """\
hostname:   nyc-rtr-01
port:       22
latency:    1.5
active:     true
backup:     null
checked:    2024-01-15
vlans:      [10, 20, 30]
config:
  ntp:      10.0.0.100
"""
cmd("type_yaml = '''")
for line in type_yaml.strip().splitlines():
    cmd(line)
cmd("'''")
blank()

cmd("parsed = yaml.safe_load(type_yaml)")
parsed = yaml.safe_load(type_yaml)
cmd("for key, val in parsed.items():")
cmd("    print(f'{key}: {type(val).__name__} = {val!r}')")
blank()
for key, val in parsed.items():
    out(f"{key}: {type(val).__name__} = {val!r}")
blank()

pause()

explain("Notice: '2024-01-15' automatically becomes datetime.date!")
explain("This is unique to YAML — JSON never does this.")
explain("If you want it as a string, quote it: '\"2024-01-15\"'")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Loading Device Inventory from YAML
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Loading Device Inventory from YAML")

section("5.1 — A Realistic inventory.yaml")

explain("A real Cisco IaC inventory YAML file:")
blank()
yaml_block("""---
# Cisco IaC — Device Inventory
# Managed by: Network Automation Team

global:
  ntp_servers:
    - 10.0.0.100
    - 10.0.0.101
  dns: 8.8.8.8
  domain: corp.net

devices:
  - hostname: nyc-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.0.0.1
    site:     NYC
    vlans:    [10, 20, 30]
    config:
      ntp: 10.0.0.100
      dns: 8.8.8.8

  - hostname: lon-sw-01
    platform: NX-OS
    status:   down
    ip:       10.1.0.1
    site:     LON
    vlans:    [10, 20]
    config:
      ntp: 10.1.0.100
      dns: 8.8.8.8""")
blank()

pause()

full_inventory_yaml = """\
---
global:
  ntp_servers:
    - 10.0.0.100
    - 10.0.0.101
  dns: 8.8.8.8
  domain: corp.net

devices:
  - hostname: nyc-rtr-01
    platform: IOS-XE
    status:   up
    ip:       10.0.0.1
    site:     NYC
    vlans:    [10, 20, 30]
    config:
      ntp: 10.0.0.100
      dns: 8.8.8.8

  - hostname: lon-sw-01
    platform: NX-OS
    status:   down
    ip:       10.1.0.1
    site:     LON
    vlans:    [10, 20]
    config:
      ntp: 10.1.0.100
      dns: 8.8.8.8

  - hostname: sin-fw-01
    platform: ASA
    status:   up
    ip:       10.2.0.1
    site:     SIN
    vlans:    [30, 40, 50]
    config:
      ntp: 10.0.0.100
      dns: 8.8.8.8
"""
full_inv_path = demo("full_inventory.yaml")
with open(full_inv_path, "w") as f:
    f.write(full_inventory_yaml)

cmd("with open('inventory.yaml') as f:")
cmd("    inv = yaml.safe_load(f)")
with open(full_inv_path) as f:
    inv = yaml.safe_load(f)

blank()
cmd("# Access global settings")
cmd("print(inv['global']['ntp_servers'])")
out(inv["global"]["ntp_servers"])
cmd("print(inv['global']['domain'])")
out(inv["global"]["domain"])
blank()

pause()

cmd("# Process devices")
cmd("for d in inv['devices']:")
cmd("    ntp_ok = d['config']['ntp'] == inv['global']['ntp_servers'][0]")
cmd("    print(f\"{d['hostname']}: ntp={'OK' if ntp_ok else 'CUSTOM'}\")")
blank()
global_ntp = inv["global"]["ntp_servers"][0]
for d in inv["devices"]:
    ntp_ok = d["config"]["ntp"] == global_ntp
    out(f"{d['hostname']}: ntp={'OK' if ntp_ok else 'CUSTOM'}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Loading Ansible-Style host_vars
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Loading Ansible-Style host_vars")

section("6.1 — Ansible host_vars Structure")

explain("In Ansible, each device gets its own YAML file in")
explain("the host_vars/ directory. One file = one device.")
blank()
yaml_block("""host_vars/
  nyc-rtr-01.yaml
  lon-sw-01.yaml
  sin-fw-01.yaml""")
blank()

explain("Each file contains only that device's variables:")
blank()
yaml_block("""# host_vars/nyc-rtr-01.yaml
---
ansible_host: 10.0.0.1
ansible_network_os: ios
ansible_user: admin

ntp_servers:
  - 10.0.0.100
  - 10.0.0.101

vlans:
  - id: 10
    name: MGMT
  - id: 20
    name: USERS
  - id: 30
    name: VOICE

bgp:
  as_number: 65001
  neighbors:
    - ip: 10.0.0.2
      remote_as: 65002
    - ip: 10.0.0.3
      remote_as: 65003""")
blank()

pause()

section("6.2 — Loading All host_vars Files")

explain("Read all YAML files in a directory:")
blank()

# Create demo host_vars
host_vars_dir = demo("host_vars")
os.makedirs(host_vars_dir, exist_ok=True)

host_var_files = {
    "nyc-rtr-01.yaml": """\
ansible_host: 10.0.0.1
ansible_network_os: ios
ntp_servers: [10.0.0.100, 10.0.0.101]
vlans: [{id: 10, name: MGMT}, {id: 20, name: USERS}]
bgp:
  as_number: 65001
  neighbors: [{ip: 10.0.0.2, remote_as: 65002}]
""",
    "lon-sw-01.yaml": """\
ansible_host: 10.1.0.1
ansible_network_os: nxos
ntp_servers: [10.1.0.100]
vlans: [{id: 10, name: MGMT}, {id: 20, name: USERS}]
""",
    "sin-fw-01.yaml": """\
ansible_host: 10.2.0.1
ansible_network_os: asa
ntp_servers: [10.0.0.100]
vlans: [{id: 30, name: DMZ}, {id: 40, name: OUTSIDE}]
""",
}

for fname, content in host_var_files.items():
    with open(os.path.join(host_vars_dir, fname), "w") as f:
        f.write(content)

cmd("host_vars = {}")
host_vars = {}
cmd("for filename in sorted(os.listdir('host_vars')):")
cmd("    if not filename.endswith('.yaml'): continue")
cmd("    hostname = filename.replace('.yaml', '')")
cmd("    with open(f'host_vars/{filename}') as f:")
cmd("        host_vars[hostname] = yaml.safe_load(f)")
for filename in sorted(os.listdir(host_vars_dir)):
    if not filename.endswith(".yaml"):
        continue
    hostname = filename.replace(".yaml", "")
    with open(os.path.join(host_vars_dir, filename)) as f:
        host_vars[hostname] = yaml.safe_load(f)

cmd("for hostname, data in host_vars.items():")
cmd("    print(f\"{hostname}: {data['ansible_network_os']} {data['ansible_host']}\")")
blank()
for hostname, data in host_vars.items():
    out(f"{hostname}: {data['ansible_network_os']} {data['ansible_host']}")
blank()

pause()

cmd("# Access BGP config for nyc-rtr-01")
cmd("bgp = host_vars['nyc-rtr-01'].get('bgp', {})")
bgp = host_vars["nyc-rtr-01"].get("bgp", {})
cmd("print(bgp['as_number'])")
out(bgp["as_number"])
cmd("print(bgp['neighbors'])")
out(bgp["neighbors"])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Writing YAML Output
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Writing YAML Output")

section("7.1 — yaml.dump() Options")

explain("Control the output format with these parameters:")
blank()

device = {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "vlans": [10, 20, 30],
    "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'vlans': [10,20,30], 'config': {'ntp':'10.0.0.100','dns':'8.8.8.8'}}")
blank()

explain("default_flow_style=False — block (human-readable):")
blank()
cmd("print(yaml.dump(device, default_flow_style=False))")
blank()
for line in yaml.dump(device, default_flow_style=False).splitlines():
    out(line)
blank()

pause()

explain("sort_keys=False — preserve insertion order:")
blank()
cmd("print(yaml.dump(device, default_flow_style=False, sort_keys=False))")
blank()
for line in yaml.dump(device, default_flow_style=False, sort_keys=False).splitlines():
    out(line)
blank()

pause()

explain("allow_unicode=True — keep special chars readable:")
blank()
data_unicode = {"site": "São Paulo", "status": "✔ active"}
cmd("data = {'site': 'São Paulo', 'status': '✔ active'}")
cmd("print(yaml.dump(data, allow_unicode=True))")
out(yaml.dump(data_unicode, allow_unicode=True).strip())
cmd("print(yaml.dump(data, allow_unicode=False))  # escapes unicode")
out(yaml.dump(data_unicode, allow_unicode=False).strip())
blank()

pause()

section("7.2 — Writing YAML to a File")

explain("Write enriched inventory back to YAML:")
blank()

inventory_py = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
     "vlans": [10, 20]},
]
for d in inventory_py:
    d["vlan_count"] = len(d["vlans"])

out_path = demo("output_inventory.yaml")
cmd("for d in inventory: d['vlan_count'] = len(d['vlans'])")
blank()
cmd("with open('output_inventory.yaml', 'w') as f:")
cmd("    yaml.dump(inventory, f, default_flow_style=False, sort_keys=False)")
with open(out_path, "w") as f:
    yaml.dump(inventory_py, f, default_flow_style=False, sort_keys=False)
blank()

cmd("with open('output_inventory.yaml') as f:")
cmd("    print(f.read())")
blank()
with open(out_path) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Multi-Document YAML
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Multi-Document YAML")

section("8.1 — The --- Separator")

explain("A single YAML file can hold multiple documents.")
explain("Separate them with --- (three dashes).")
explain("Common in Kubernetes, Ansible, and IaC config files.")
blank()
yaml_block("""---
hostname: nyc-rtr-01
platform: IOS-XE
---
hostname: lon-sw-01
platform: NX-OS
---
hostname: sin-fw-01
platform: ASA""")
blank()

pause()

section("8.2 — yaml.safe_load_all() — Read All Documents")

multi_yaml = """\
---
hostname: nyc-rtr-01
platform: IOS-XE
status:   up
vlans:    [10, 20, 30]
---
hostname: lon-sw-01
platform: NX-OS
status:   down
vlans:    [10, 20]
---
hostname: sin-fw-01
platform: ASA
status:   up
vlans:    [30, 40, 50]
"""
multi_path = demo("multi_devices.yaml")
with open(multi_path, "w") as f:
    f.write(multi_yaml)

cmd("with open('multi_devices.yaml') as f:")
cmd("    devices = list(yaml.safe_load_all(f))")
with open(multi_path) as f:
    devices_multi = list(yaml.safe_load_all(f))

cmd("print(f'{len(devices)} documents loaded')")
out(f"{len(devices_multi)} documents loaded")
cmd("for d in devices:")
cmd("    print(d['hostname'], d['platform'])")
blank()
for d in devices_multi:
    out(f"{d['hostname']} {d['platform']}")
blank()

pause()

explain("Practical use — one YAML file per deployment batch:")
blank()
yaml_block("""---
# Batch 1: Core routers
hostname: nyc-rtr-01
role: core
---
# Batch 2: Distribution switches
hostname: nyc-sw-01
role: distribution""")
blank()

explain("yaml.safe_load_all() returns a generator —")
explain("wrap in list() to get all docs at once, or")
explain("iterate directly to process one at a time.")

pause()

section("8.3 — yaml.dump_all() — Write Multiple Documents")

explain("Write multiple Python objects as multi-document YAML:")
blank()

docs = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS"},
]
cmd("docs = [{'hostname': 'nyc-rtr-01', ...}, {'hostname': 'lon-sw-01', ...}]")
cmd("print(yaml.dump_all(docs, default_flow_style=False))")
blank()
for line in yaml.dump_all(docs, default_flow_style=False).splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — YAML vs JSON
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "YAML vs JSON")

section("9.1 — When to Use Each")

explain("Use YAML when:")
explain("  — humans write or edit the file")
explain("  — config files checked into git")
explain("  — Ansible playbooks, Nornir inventory")
explain("  — comments are needed to explain intent")
explain("  — readability is more important than strict parsing")
blank()
explain("Use JSON when:")
explain("  — machines produce or consume the data")
explain("  — REST API payloads and responses")
explain("  — data passed between programs")
explain("  — strict parsing and no ambiguity needed")
blank()

pause()

section("9.2 — Same Data in Both Formats")

explain("The same INVENTORY device in YAML and JSON:")
blank()

explain("YAML (human writes this):")
blank()
yaml_block("""- hostname: nyc-rtr-01
  platform: IOS-XE
  status:   up
  vlans:
    - 10
    - 20
    - 30
  config:
    ntp: 10.0.0.100
    dns: 8.8.8.8""")
blank()

pause()

explain("JSON (machine sends this):")
blank()
yaml_block("""[{"hostname":"nyc-rtr-01","platform":"IOS-XE","status":"up",
  "vlans":[10,20,30],"config":{"ntp":"10.0.0.100","dns":"8.8.8.8"}}]""")
blank()

pause()

section("9.3 — Converting Between YAML and JSON")

explain("Load YAML → Python → dump JSON:")
blank()

yaml_device = """\
hostname: nyc-rtr-01
platform: IOS-XE
vlans: [10, 20, 30]
"""
cmd("yaml_str = 'hostname: nyc-rtr-01\\nplatform: IOS-XE\\nvlans: [10,20,30]'")
cmd("python_obj = yaml.safe_load(yaml_str)")
python_obj = yaml.safe_load(yaml_device)
cmd("json_str   = json.dumps(python_obj, indent=2)")
json_str_out = json.dumps(python_obj, indent=2)
cmd("print(json_str)")
blank()
for line in json_str_out.splitlines():
    out(line)
blank()

pause()

explain("Load JSON → Python → dump YAML:")
blank()
json_in = '{"hostname": "nyc-rtr-01", "platform": "IOS-XE", "vlans": [10, 20, 30]}'
cmd("json_str = '{\"hostname\": \"nyc-rtr-01\", ...}'")
cmd("python_obj = json.loads(json_str)")
py_obj2 = json.loads(json_in)
cmd("yaml_out   = yaml.dump(python_obj, default_flow_style=False)")
yaml_out2 = yaml.dump(py_obj2, default_flow_style=False)
cmd("print(yaml_out)")
blank()
for line in yaml_out2.splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — The Norway Problem (yes/no/on/off as Booleans)")

explain("YAML 1.1 treats yes/no/on/off/true/false as booleans.")
explain("This causes nasty bugs with country codes and switch states.")
blank()

yaml_block("""# DANGER — these parse as booleans in YAML 1.1
country: NO     # → False  (Norway bug!)
enabled: yes    # → True
port_state: on  # → True
bgp_active: off # → False""")
blank()

norway_yaml = "country: NO\nenabled: yes\nport_state: on"
cmd("parsed = yaml.safe_load('country: NO\\nenabled: yes\\nport_state: on')")
norway_parsed = yaml.safe_load(norway_yaml)
cmd("print(parsed)")
warn(norway_parsed)
blank()

pause()

explain("Fix — quote values that should be strings:")
blank()
yaml_block("""country: 'NO'     # stays as string 'NO'
enabled: 'yes'    # stays as string 'yes'
port_state: 'on'  # stays as string 'on'""")
blank()

fixed_yaml = "country: 'NO'\nenabled: 'yes'\nport_state: 'on'"
cmd("parsed = yaml.safe_load(\"country: 'NO'\\nenabled: 'yes'\\nport_state: 'on'\")")
fixed_parsed = yaml.safe_load(fixed_yaml)
cmd("print(parsed)")
out(fixed_parsed)
blank()

pause()

section("10.2 — load() Is Unsafe — Always Use safe_load()")

explain("yaml.load() can execute arbitrary Python code.")
explain("An attacker could inject malicious YAML into your inventory.")
explain("ALWAYS use yaml.safe_load() — no exceptions.")
blank()

cmd("# Wrong — NEVER do this with external data")
cmd("data = yaml.load(yaml_str)   # can execute code!")
blank()
cmd("# Correct — always safe_load")
cmd("data = yaml.safe_load(yaml_str)")
blank()
explain("PyYAML will warn you if you use load() without a Loader.")
explain("The warning itself is a sign you are doing it wrong.")

pause()

section("10.3 — Tabs Are Illegal in YAML")

explain("YAML uses spaces ONLY for indentation.")
explain("A tab character in your YAML file causes a parse error.")
blank()

tab_yaml = "hostname: nyc-rtr-01\n\tplatform: IOS-XE"
cmd("bad_yaml = 'hostname: nyc-rtr-01\\n\\tplatform: IOS-XE'  # tab!")
cmd("yaml.safe_load(bad_yaml)")
blank()
try:
    yaml.safe_load(tab_yaml)
except yaml.YAMLError as e:
    warn(f"YAMLError: {str(e)[:80]}")
blank()
explain("Your editor should be set to 'expand tabs to spaces'.")
explain("Most IaC teams use 2-space indentation.")

pause()

section("10.4 — Indentation Errors")

explain("YAML is indentation-sensitive — one wrong space breaks it.")
blank()
yaml_block("""# Wrong — config is at wrong indent level
device:
  hostname: nyc-rtr-01
 config:         # ← should be 2 spaces, not 1
    ntp: 10.0.0.100""")
blank()

bad_indent = "device:\n  hostname: nyc-rtr-01\n config:\n    ntp: 10.0.0.100"
cmd("yaml.safe_load(bad_yaml_indent)")
blank()
try:
    yaml.safe_load(bad_indent)
except yaml.YAMLError as e:
    warn(f"YAMLError: {str(e)[:80]}")
blank()

yaml_block("""# Correct — consistent 2-space indentation
device:
  hostname: nyc-rtr-01
  config:
    ntp: 10.0.0.100""")
blank()
good = yaml.safe_load("device:\n  hostname: nyc-rtr-01\n  config:\n    ntp: 10.0.0.100")
out(good)
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
print(f"  {BOLD}Ch 1{RESET}   What is YAML — IaC role, YAML vs JSON purpose")
print(f"  {BOLD}Ch 2{RESET}   YAML syntax — scalars, mappings, sequences, multiline")
print(f"  {BOLD}Ch 3{RESET}   PyYAML basics — safe_load, load from file, dump")
print(f"  {BOLD}Ch 4{RESET}   Type mapping — date auto-parse, bool/null/int/float")
print(f"  {BOLD}Ch 5{RESET}   Device inventory — realistic inventory.yaml, global + devices")
print(f"  {BOLD}Ch 6{RESET}   Ansible host_vars — per-device YAML files, load directory")
print(f"  {BOLD}Ch 7{RESET}   Writing YAML — dump options, sort_keys, allow_unicode, to file")
print(f"  {BOLD}Ch 8{RESET}   Multi-document — ---, safe_load_all, dump_all")
print(f"  {BOLD}Ch 9{RESET}   YAML vs JSON — when to use each, converting between them")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — Norway problem, safe_load, tabs illegal, indentation")
blank()
print(f"  {WHITE}Every example used real Cisco IaC patterns —")
print(f"  Ansible inventories, host_vars, Nornir-style configs,")
print(f"  multi-document deployment batches, intent files.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()