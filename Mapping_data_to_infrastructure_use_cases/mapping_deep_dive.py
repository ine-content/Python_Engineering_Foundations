# mapping_deep_dive.py
# Mapping Data to Infrastructure Use Cases — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

import json
import yaml
import os
import shutil
import tempfile

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

# ── Working directory ─────────────────────────────────────────────────────────
DEMO_DIR = tempfile.mkdtemp(prefix="mapping_demo_")

def demo(filename):
    return os.path.join(DEMO_DIR, filename)

# ─────────────────────────────────────────────────────────────────────────────
# SHARED DATA — used across all chapters
# ─────────────────────────────────────────────────────────────────────────────
INVENTORY = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "NYC", "role": "core",
        "ip": "10.0.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65001, "neighbors": ["10.0.0.2"]},
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
        "site": "LON", "role": "distribution",
        "ip": "10.1.0.1", "vlans": [10, 20],
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
        "site": "SIN", "role": "firewall",
        "ip": "10.2.0.1", "vlans": [30, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
        "site": "AMS", "role": "core",
        "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65002, "neighbors": ["10.0.0.1", "10.3.0.2"]},
    },
    {
        "hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
        "site": "TOK", "role": "access",
        "ip": "10.4.0.1", "vlans": [20, 30],
        "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "SYD", "role": "core",
        "ip": "10.5.0.1", "vlans": [10, 40, 50],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65003, "neighbors": ["10.5.0.2"]},
    },
    {
        "hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
        "site": "DUB", "role": "firewall",
        "ip": "10.6.0.1", "vlans": [10, 20, 30],
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "bgp": None,
    },
    {
        "hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
        "site": "MUM", "role": "core",
        "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
        "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"},
        "bgp": {"as_number": 65004, "neighbors": ["10.7.0.2"]},
    },
]

GLOBAL_NTP    = "10.0.0.100"
RESERVED_VLANS = {1, 1002, 1003, 1004, 1005}

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         MAPPING DATA TO INFRASTRUCTURE USE CASES{RESET}")
print(f"{BOLD}         Zero to Expert — Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is Data Mapping in IaC
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is Data Mapping in IaC")

section("1.1 — The Core Mental Model")

explain("Data mapping is the process of taking data in one shape")
explain("and transforming it into the shape a target system needs.")
blank()
explain("In Cisco IaC the pipeline always looks like this:")
blank()
explain("  SOURCE DATA")
explain("    ↓  (load from YAML/JSON/CSV)")
explain("  PYTHON OBJECTS  (dicts, lists)")
explain("    ↓  (validate, enrich, filter)")
explain("  MAPPED OUTPUT")
explain("    ↓  (Ansible vars / config text / API payload)")
explain("  TARGET SYSTEM")
explain("    (device / Ansible / Nornir / RESTCONF API)")
blank()

pause()

explain("Every chapter in this tutorial is one concrete mapping:")
blank()
explain("  Ch 2  — inventory dict      → Ansible hosts.yaml")
explain("  Ch 3  — device dict         → Cisco config text")
explain("  Ch 4  — VLAN intent         → switchport config lines")
explain("  Ch 5  — role/platform       → platform-specific policy")
explain("  Ch 6  — flat dict           → RESTCONF API payload")
explain("  Ch 7  — inventory checks    → compliance report")
explain("  Ch 8  — before/after state  → deployment change plan")
explain("  Ch 9  — site topology       → BGP peer config")
explain("  Ch 10 — full pipeline       → everything combined")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Mapping Inventory to Ansible Variables
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Mapping Inventory to Ansible Variables")

section("2.1 — What Ansible Expects")

explain("Ansible reads inventory from a hosts.yaml file.")
explain("The structure must match exactly what Ansible expects:")
blank()
yaml_block("""all:
  hosts:
    nyc-rtr-01:
      ansible_host: 10.0.0.1
      ansible_network_os: ios
      ansible_user: admin
    lon-sw-01:
      ansible_host: 10.1.0.1
      ansible_network_os: nxos
      ansible_user: admin""")
blank()

pause()

section("2.2 — Building the Mapping Function")

cmd("PLATFORM_OS = {")
cmd("    'IOS-XE': 'ios',")
cmd("    'NX-OS':  'nxos',")
cmd("    'ASA':    'asa',")
cmd("    'IOS-XR': 'iosxr',")
cmd("}")
blank()

PLATFORM_OS = {"IOS-XE": "ios", "NX-OS": "nxos", "ASA": "asa", "IOS-XR": "iosxr"}

cmd("def build_ansible_inventory(inventory, user='admin'):")
cmd("    hosts = {}")
cmd("    for d in inventory:")
cmd("        hosts[d['hostname']] = {")
cmd("            'ansible_host':       d['ip'],")
cmd("            'ansible_network_os': PLATFORM_OS.get(d['platform'], 'unknown'),")
cmd("            'ansible_user':       user,")
cmd("        }")
cmd("    return {'all': {'hosts': hosts}}")
blank()

def build_ansible_inventory(inventory, user="admin"):
    hosts = {}
    for d in inventory:
        hosts[d["hostname"]] = {
            "ansible_host":       d["ip"],
            "ansible_network_os": PLATFORM_OS.get(d["platform"], "unknown"),
            "ansible_user":       user,
        }
    return {"all": {"hosts": hosts}}

pause()

cmd("ansible_inv = build_ansible_inventory(INVENTORY)")
ansible_inv = build_ansible_inventory(INVENTORY)
cmd("print(yaml.dump(ansible_inv, default_flow_style=False)[:200])")
blank()
for line in yaml.dump(ansible_inv, default_flow_style=False).splitlines()[:14]:
    out(line)
out("  ...")
blank()

pause()

section("2.3 — Writing the hosts.yaml File")

hosts_path = demo("hosts.yaml")
cmd("with open('hosts.yaml', 'w') as f:")
cmd("    yaml.dump(ansible_inv, f, default_flow_style=False)")
with open(hosts_path, "w") as f:
    yaml.dump(ansible_inv, f, default_flow_style=False)
out("Written: hosts.yaml")
blank()

explain("Now Ansible can use this directly:")
explain("  ansible-playbook -i hosts.yaml site.yaml")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Mapping Inventory to Cisco Config Text
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Mapping Inventory to Cisco Config Text")

section("3.1 — Config Generation Pattern")

explain("Take a device dict and produce config text lines.")
explain("One function per config block — NTP, DNS, VLANs, etc.")
blank()

cmd("def gen_base_config(device):")
cmd("    return (")
cmd("        f\"hostname {device['hostname']}\\n\"")
cmd("        f\"ip domain-name corp.net\\n\"")
cmd("        f\"ntp server {device['config']['ntp']}\\n\"")
cmd("        f\"ip name-server {device['config']['dns']}\\n\"")
cmd("    )")
blank()

def gen_base_config(device):
    return (
        f"hostname {device['hostname']}\n"
        f"ip domain-name corp.net\n"
        f"ntp server {device['config']['ntp']}\n"
        f"ip name-server {device['config']['dns']}\n"
    )

device = INVENTORY[0]
cmd("print(gen_base_config(INVENTORY[0]))")
blank()
for line in gen_base_config(device).splitlines():
    out(line)
blank()

pause()

section("3.2 — Platform-Specific VLAN Config")

explain("Different platforms use different VLAN syntax.")
explain("Map platform → config template:")
blank()

cmd("def gen_vlan_config(device):")
cmd("    lines = []")
cmd("    if device['platform'] in ('IOS-XE', 'IOS-XR'):")
cmd("        for vlan in device['vlans']:")
cmd("            lines.append(f'vlan {vlan}')")
cmd("            lines.append(f' name VLAN_{vlan}')")
cmd("    elif device['platform'] == 'NX-OS':")
cmd("        for vlan in device['vlans']:")
cmd("            lines.append(f'vlan {vlan}')")
cmd("            lines.append(f'  name VLAN_{vlan}')")
cmd("    elif device['platform'] == 'ASA':")
cmd("        for vlan in device['vlans']:")
cmd("            lines.append(f'interface vlan{vlan}')")
cmd("    return '\\n'.join(lines)")
blank()

def gen_vlan_config(device):
    lines = []
    if device["platform"] in ("IOS-XE", "IOS-XR"):
        for vlan in device["vlans"]:
            lines.append(f"vlan {vlan}")
            lines.append(f" name VLAN_{vlan}")
    elif device["platform"] == "NX-OS":
        for vlan in device["vlans"]:
            lines.append(f"vlan {vlan}")
            lines.append(f"  name VLAN_{vlan}")
    elif device["platform"] == "ASA":
        for vlan in device["vlans"]:
            lines.append(f"interface vlan{vlan}")
    return "\n".join(lines)

pause()

for d in INVENTORY[:3]:
    cmd(f"print(gen_vlan_config(INVENTORY[{INVENTORY.index(d)}]))  # {d['hostname']}")
    blank()
    for line in gen_vlan_config(d).splitlines():
        out(line)
    blank()

pause()

section("3.3 — Write One Config File Per Device")

explain("Combine all config blocks and write to files:")
blank()

configs_dir = demo("configs")
os.makedirs(configs_dir, exist_ok=True)

cmd("def gen_full_config(device):")
cmd("    parts = [")
cmd("        '! Generated by IaC pipeline',")
cmd("        gen_base_config(device),")
cmd("        gen_vlan_config(device),")
cmd("    ]")
cmd("    return '\\n'.join(parts)")
blank()

def gen_full_config(device):
    parts = [
        "! Generated by IaC pipeline",
        gen_base_config(device),
        gen_vlan_config(device),
    ]
    return "\n".join(parts)

cmd("os.makedirs('configs', exist_ok=True)")
cmd("for d in INVENTORY:")
cmd("    path = f\"configs/{d['hostname']}.cfg\"")
cmd("    with open(path, 'w') as f:")
cmd("        f.write(gen_full_config(d))")
cmd("    print(f'Wrote {path}')")
blank()

for d in INVENTORY:
    path = os.path.join(configs_dir, f"{d['hostname']}.cfg")
    with open(path, "w") as f:
        f.write(gen_full_config(d))
    out(f"Wrote configs/{d['hostname']}.cfg")
blank()

pause()

explain("Show sample output for nyc-rtr-01:")
blank()
with open(os.path.join(configs_dir, "nyc-rtr-01.cfg")) as f:
    for line in f.read().splitlines():
        out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Mapping VLAN Intent to Switchport Config
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Mapping VLAN Intent to Switchport Config")

section("4.1 — VLAN Intent Data")

explain("In IaC, you define your VLAN intent as data first.")
explain("Then generate the config from that data.")
blank()

vlan_intent = {
    10: {"name": "MGMT",   "description": "Management VLAN",   "svi_ip": "10.10.0.1/24"},
    20: {"name": "USERS",  "description": "User workstations",  "svi_ip": "10.20.0.1/24"},
    30: {"name": "VOICE",  "description": "VoIP phones",        "svi_ip": "10.30.0.1/24"},
    40: {"name": "SERVERS","description": "Data centre servers", "svi_ip": "10.40.0.1/24"},
    50: {"name": "DMZ",    "description": "Demilitarized zone",  "svi_ip": "10.50.0.1/24"},
}

cmd("vlan_intent = {")
cmd("    10: {'name':'MGMT',   'description':'Management VLAN',   'svi_ip':'10.10.0.1/24'},")
cmd("    20: {'name':'USERS',  'description':'User workstations',  'svi_ip':'10.20.0.1/24'},")
cmd("    30: {'name':'VOICE',  'description':'VoIP phones',        'svi_ip':'10.30.0.1/24'},")
cmd("    40: {'name':'SERVERS','description':'Data centre servers', 'svi_ip':'10.40.0.1/24'},")
cmd("    50: {'name':'DMZ',    'description':'Demilitarized zone',  'svi_ip':'10.50.0.1/24'},")
cmd("}")
blank()

pause()

section("4.2 — Generating VLAN and SVI Config from Intent")

cmd("def gen_vlan_intent_config(device_vlans, vlan_intent):")
cmd("    lines = []")
cmd("    for vlan_id in device_vlans:")
cmd("        if vlan_id not in vlan_intent:")
cmd("            continue")
cmd("        info = vlan_intent[vlan_id]")
cmd("        lines.append(f'vlan {vlan_id}')")
cmd("        lines.append(f' name {info[\"name\"]}')")
cmd("        lines.append(f'!')")
cmd("        ip, mask = info['svi_ip'].split('/')")
cmd("        prefix   = int(mask)")
cmd("        # Convert prefix to dotted mask")
cmd("        bits     = (0xFFFFFFFF >> (32 - prefix)) << (32 - prefix)")
cmd("        dotted   = '.'.join(str((bits >> (8*i)) & 0xFF)")
cmd("                            for i in reversed(range(4)))")
cmd("        lines.append(f'interface Vlan{vlan_id}')")
cmd("        lines.append(f' description {info[\"description\"]}')")
cmd("        lines.append(f' ip address {ip} {dotted}')")
cmd("        lines.append(f' no shutdown')")
cmd("        lines.append(f'!')")
cmd("    return '\\n'.join(lines)")
blank()

def gen_vlan_intent_config(device_vlans, vlan_intent):
    lines = []
    for vlan_id in device_vlans:
        if vlan_id not in vlan_intent:
            continue
        info = vlan_intent[vlan_id]
        lines.append(f"vlan {vlan_id}")
        lines.append(f" name {info['name']}")
        lines.append("!")
        ip, mask = info["svi_ip"].split("/")
        prefix   = int(mask)
        bits     = (0xFFFFFFFF >> (32 - prefix)) << (32 - prefix)
        dotted   = ".".join(str((bits >> (8 * i)) & 0xFF)
                             for i in reversed(range(4)))
        lines.append(f"interface Vlan{vlan_id}")
        lines.append(f" description {info['description']}")
        lines.append(f" ip address {ip} {dotted}")
        lines.append(" no shutdown")
        lines.append("!")
    return "\n".join(lines)

pause()

device = INVENTORY[0]
cmd("device = INVENTORY[0]  # nyc-rtr-01 — vlans [10, 20, 30]")
cmd("print(gen_vlan_intent_config(device['vlans'], vlan_intent))")
blank()
for line in gen_vlan_intent_config(device["vlans"], vlan_intent).splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Mapping Device Roles to Config Policies
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Mapping Device Roles to Config Policies")

section("5.1 — Role-Based Policy Mapping")

explain("Different device roles need different config policies.")
explain("Map role → policy function, then apply per device.")
blank()

cmd("POLICY_MAP = {")
cmd("    'core':         gen_core_policy,")
cmd("    'distribution': gen_distribution_policy,")
cmd("    'access':       gen_access_policy,")
cmd("    'firewall':     gen_firewall_policy,")
cmd("}")
blank()

explain("Define one function per role:")
blank()

cmd("def gen_core_policy(device):")
cmd("    return [")
cmd("        'spanning-tree mode rapid-pvst',")
cmd("        'spanning-tree portfast bpduguard default',")
cmd("        f'router bgp {device[\"bgp\"][\"as_number\"]}' if device.get('bgp') else '',")
cmd("        ' bgp log-neighbor-changes',")
cmd("        ' no bgp default ipv4-unicast',")
cmd("    ]")
blank()

def gen_core_policy(device):
    lines = [
        "spanning-tree mode rapid-pvst",
        "spanning-tree portfast bpduguard default",
    ]
    if device.get("bgp"):
        lines.append(f"router bgp {device['bgp']['as_number']}")
        lines.append(" bgp log-neighbor-changes")
        lines.append(" no bgp default ipv4-unicast")
    return lines

def gen_distribution_policy(device):
    return [
        "spanning-tree mode rapid-pvst",
        "ip dhcp snooping",
        "ip arp inspection",
        f"! Distribution device — {len(device['vlans'])} VLANs",
    ]

def gen_access_policy(device):
    return [
        "spanning-tree portfast default",
        "spanning-tree bpduguard default",
        "ip dhcp snooping",
        "! Access layer — user-facing ports",
    ]

def gen_firewall_policy(device):
    return [
        "no ip routing",
        "service password-encryption",
        "no cdp run",
        "! Firewall — routing disabled, hardened",
    ]

cmd("def gen_distribution_policy(device): ...")
cmd("def gen_access_policy(device): ...")
cmd("def gen_firewall_policy(device): ...")
blank()

pause()

POLICY_MAP = {
    "core":         gen_core_policy,
    "distribution": gen_distribution_policy,
    "access":       gen_access_policy,
    "firewall":     gen_firewall_policy,
}

cmd("POLICY_MAP = {")
cmd("    'core':         gen_core_policy,")
cmd("    'distribution': gen_distribution_policy,")
cmd("    'access':       gen_access_policy,")
cmd("    'firewall':     gen_firewall_policy,")
cmd("}")
blank()
cmd("for d in INVENTORY:")
cmd("    policy_fn = POLICY_MAP.get(d['role'])")
cmd("    if policy_fn:")
cmd("        lines = policy_fn(d)")
cmd("        print(f\"\\n! {d['hostname']} ({d['role']})\")")
cmd("        for line in lines: print(f'  {line}')")
blank()
for d in INVENTORY:
    policy_fn = POLICY_MAP.get(d["role"])
    if policy_fn:
        lines = policy_fn(d)
        out(f"! {d['hostname']} ({d['role']})")
        for line in [l for l in lines if l]:
            out(f"  {line}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Mapping Flat Data to RESTCONF API Payloads
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Mapping Flat Data to RESTCONF API Payloads")

section("6.1 — What RESTCONF Expects")

explain("RESTCONF PUT requests require a specific JSON structure")
explain("defined by the YANG model. Your flat device dict must")
explain("be reshaped to match that structure exactly.")
blank()
explain("A RESTCONF NTP config payload looks like this:")
blank()
yaml_block("""{
  "Cisco-IOS-XE-native:ntp": {
    "server": {
      "server-list": [
        {"ip-address": "10.0.0.100"},
        {"ip-address": "10.0.0.101"}
      ]
    }
  }
}""")
blank()

pause()

section("6.2 — Building the Payload Mapping Function")

cmd("def build_ntp_payload(device, extra_servers=None):")
cmd("    servers = [device['config']['ntp']]")
cmd("    if extra_servers:")
cmd("        servers.extend(extra_servers)")
cmd("    return {")
cmd("        'Cisco-IOS-XE-native:ntp': {")
cmd("            'server': {")
cmd("                'server-list': [")
cmd("                    {'ip-address': s} for s in servers")
cmd("                ]")
cmd("            }")
cmd("        }")
cmd("    }")
blank()

def build_ntp_payload(device, extra_servers=None):
    servers = [device["config"]["ntp"]]
    if extra_servers:
        servers.extend(extra_servers)
    return {
        "Cisco-IOS-XE-native:ntp": {
            "server": {
                "server-list": [
                    {"ip-address": s} for s in servers
                ]
            }
        }
    }

device = INVENTORY[0]
cmd("payload = build_ntp_payload(INVENTORY[0], extra_servers=['10.0.0.101'])")
payload = build_ntp_payload(device, extra_servers=["10.0.0.101"])
cmd("print(json.dumps(payload, indent=2))")
blank()
for line in json.dumps(payload, indent=2).splitlines():
    out(line)
blank()

pause()

section("6.3 — Mapping VLAN Data to RESTCONF VLAN Payload")

cmd("def build_vlan_payload(device):")
cmd("    return {")
cmd("        'Cisco-IOS-XE-vlan:vlan-list': [")
cmd("            {")
cmd("                'id':   str(v),")
cmd("                'name': f'VLAN_{v}',")
cmd("            }")
cmd("            for v in device['vlans']")
cmd("            if v not in RESERVED_VLANS")
cmd("        ]")
cmd("    }")
blank()

def build_vlan_payload(device):
    return {
        "Cisco-IOS-XE-vlan:vlan-list": [
            {"id": str(v), "name": f"VLAN_{v}"}
            for v in device["vlans"]
            if v not in RESERVED_VLANS
        ]
    }

device = INVENTORY[3]  # ams-rtr-02 — 4 vlans
cmd("payload = build_vlan_payload(INVENTORY[3])  # ams-rtr-02")
payload = build_vlan_payload(device)
cmd("print(json.dumps(payload, indent=2))")
blank()
for line in json.dumps(payload, indent=2).splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Mapping Audit Results to a Compliance Report
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Mapping Audit Results to a Compliance Report")

section("7.1 — Defining Compliance Checks")

explain("A compliance check is a function that takes a device")
explain("and returns (passed: bool, message: str).")
blank()

cmd("COMPLIANCE_CHECKS = {")
cmd("    'status_up':    lambda d: (d['status']=='up',   'device must be up'),")
cmd("    'standard_ntp': lambda d: (d['config']['ntp']==GLOBAL_NTP,")
cmd("                               f'ntp must be {GLOBAL_NTP}'),")
cmd("    'has_vlans':    lambda d: (bool(d['vlans']),    'must have vlans'),")
cmd("    'no_reserved':  lambda d: (")
cmd("                        not any(v in RESERVED_VLANS for v in d['vlans']),")
cmd("                        'no reserved VLANs allowed'),")
cmd("}")
blank()

COMPLIANCE_CHECKS = {
    "status_up":    lambda d: (d["status"] == "up",
                               "device must be up"),
    "standard_ntp": lambda d: (d["config"]["ntp"] == GLOBAL_NTP,
                               f"ntp must be {GLOBAL_NTP}"),
    "has_vlans":    lambda d: (bool(d["vlans"]),
                               "must have vlans"),
    "no_reserved":  lambda d: (not any(v in RESERVED_VLANS for v in d["vlans"]),
                               "no reserved VLANs allowed"),
}

pause()

section("7.2 — Running Checks and Building the Report")

cmd("def run_compliance(inventory, checks):")
cmd("    report = []")
cmd("    for d in inventory:")
cmd("        results = {}")
cmd("        for check_name, check_fn in checks.items():")
cmd("            passed, message = check_fn(d)")
cmd("            results[check_name] = {")
cmd("                'passed':  passed,")
cmd("                'message': message if not passed else 'OK',")
cmd("            }")
cmd("        overall = all(r['passed'] for r in results.values())")
cmd("        report.append({")
cmd("            'hostname': d['hostname'],")
cmd("            'overall':  'PASS' if overall else 'FAIL',")
cmd("            'checks':   results,")
cmd("        })")
cmd("    return report")
blank()

def run_compliance(inventory, checks):
    report = []
    for d in inventory:
        results = {}
        for check_name, check_fn in checks.items():
            passed, message = check_fn(d)
            results[check_name] = {
                "passed":  passed,
                "message": message if not passed else "OK",
            }
        overall = all(r["passed"] for r in results.values())
        report.append({
            "hostname": d["hostname"],
            "overall":  "PASS" if overall else "FAIL",
            "checks":   results,
        })
    return report

pause()

cmd("report = run_compliance(INVENTORY, COMPLIANCE_CHECKS)")
report = run_compliance(INVENTORY, COMPLIANCE_CHECKS)
cmd("for r in report:")
cmd("    fails = [k for k,v in r['checks'].items() if not v['passed']]")
cmd("    print(f\"{r['overall']} {r['hostname']}: {fails or 'all checks passed'}\")")
blank()
for r in report:
    fails = [k for k, v in r["checks"].items() if not v["passed"]]
    color = GREEN if r["overall"] == "PASS" else RED
    out(f"{r['overall']} {r['hostname']}: {fails or 'all checks passed'}")
blank()

pause()

section("7.3 — Writing the Report to JSON")

report_path = demo("compliance_report.json")
cmd("with open('compliance_report.json', 'w') as f:")
cmd("    json.dump(report, f, indent=2)")
with open(report_path, "w") as f:
    json.dump(report, f, indent=2)
out("Written: compliance_report.json")
blank()

explain("Now any tool, dashboard, or CI/CD pipeline can consume it.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Mapping Before/After State to a Deployment Plan
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Mapping Before/After State to a Deployment Plan")

section("8.1 — The Concept")

explain("Before you push a change you have:")
explain("  BEFORE — current state of the device config")
explain("  AFTER  — desired state (from your intent/inventory)")
blank()
explain("The change plan is the diff: what needs to be added,")
explain("removed, or modified to go from before to after.")
blank()

pause()

section("8.2 — Building a Change Diff")

before_state = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20],       "ntp": "10.0.0.100"},
    {"hostname": "lon-sw-01",  "vlans": [10, 20, 99],    "ntp": "10.9.9.9"},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50],    "ntp": "10.0.0.100"},
]

after_state = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30],   "ntp": "10.0.0.100"},
    {"hostname": "lon-sw-01",  "vlans": [10, 20],        "ntp": "10.0.0.100"},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50],    "ntp": "10.0.0.100"},
]

cmd("before_state = [  # current device state ]")
cmd("after_state  = [  # desired device state ]")
blank()

cmd("def build_change_plan(before, after):")
cmd("    before_map = {d['hostname']: d for d in before}")
cmd("    after_map  = {d['hostname']: d for d in after}")
cmd("    plan = []")
cmd("    for hostname, desired in after_map.items():")
cmd("        current = before_map.get(hostname, {})")
cmd("        changes = {}")
cmd("        # VLAN diff")
cmd("        add_vlans = set(desired['vlans']) - set(current.get('vlans', []))")
cmd("        rem_vlans = set(current.get('vlans',[])) - set(desired['vlans'])")
cmd("        if add_vlans: changes['vlans_add'] = sorted(add_vlans)")
cmd("        if rem_vlans: changes['vlans_remove'] = sorted(rem_vlans)")
cmd("        # NTP diff")
cmd("        if desired['ntp'] != current.get('ntp'):")
cmd("            changes['ntp'] = {'old': current.get('ntp'), 'new': desired['ntp']}")
cmd("        if changes:")
cmd("            plan.append({'hostname': hostname, 'changes': changes})")
cmd("    return plan")
blank()

def build_change_plan(before, after):
    before_map = {d["hostname"]: d for d in before}
    after_map  = {d["hostname"]: d for d in after}
    plan = []
    for hostname, desired in after_map.items():
        current = before_map.get(hostname, {})
        changes = {}
        add_vlans = set(desired["vlans"]) - set(current.get("vlans", []))
        rem_vlans = set(current.get("vlans", [])) - set(desired["vlans"])
        if add_vlans: changes["vlans_add"]    = sorted(add_vlans)
        if rem_vlans: changes["vlans_remove"] = sorted(rem_vlans)
        if desired["ntp"] != current.get("ntp"):
            changes["ntp"] = {"old": current.get("ntp"), "new": desired["ntp"]}
        if changes:
            plan.append({"hostname": hostname, "changes": changes})
    return plan

pause()

cmd("plan = build_change_plan(before_state, after_state)")
plan = build_change_plan(before_state, after_state)
cmd("print(json.dumps(plan, indent=2))")
blank()
for line in json.dumps(plan, indent=2).splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Mapping Site Topology to BGP Peer Config
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Mapping Site Topology to BGP Peer Config")

section("9.1 — BGP Data in the Inventory")

explain("Core routers in INVENTORY have a 'bgp' key.")
explain("We extract those and generate neighbor statements.")
blank()

cmd("bgp_devices = [d for d in INVENTORY if d.get('bgp')]")
bgp_devices = [d for d in INVENTORY if d.get("bgp")]
cmd("for d in bgp_devices:")
cmd("    print(f\"{d['hostname']}: AS{d['bgp']['as_number']} neighbors={d['bgp']['neighbors']}\")")
blank()
for d in bgp_devices:
    out(f"{d['hostname']}: AS{d['bgp']['as_number']} neighbors={d['bgp']['neighbors']}")
blank()

pause()

section("9.2 — Generating BGP Neighbor Statements")

cmd("def gen_bgp_config(device, inventory):")
cmd("    if not device.get('bgp'):")
cmd("        return ''")
cmd("    # Build a map of ip → device for neighbor lookup")
cmd("    ip_map = {d['ip']: d for d in inventory}")
cmd("    lines  = [")
cmd("        f\"router bgp {device['bgp']['as_number']}\",")
cmd("        ' bgp log-neighbor-changes',")
cmd("    ]")
cmd("    for neighbor_ip in device['bgp']['neighbors']:")
cmd("        neighbor = ip_map.get(neighbor_ip, {})")
cmd("        remote_as = neighbor.get('bgp', {}).get('as_number', 'UNKNOWN')")
cmd("        lines.append(f' neighbor {neighbor_ip} remote-as {remote_as}')")
cmd("        lines.append(f' neighbor {neighbor_ip} description {neighbor.get(\"hostname\",\"unknown\")}')")
cmd("    return '\\n'.join(lines)")
blank()

def gen_bgp_config(device, inventory):
    if not device.get("bgp"):
        return ""
    ip_map = {d["ip"]: d for d in inventory}
    lines  = [
        f"router bgp {device['bgp']['as_number']}",
        " bgp log-neighbor-changes",
    ]
    for neighbor_ip in device["bgp"]["neighbors"]:
        neighbor  = ip_map.get(neighbor_ip, {})
        remote_as = neighbor.get("bgp", {}).get("as_number", "UNKNOWN")
        lines.append(f" neighbor {neighbor_ip} remote-as {remote_as}")
        lines.append(f" neighbor {neighbor_ip} description {neighbor.get('hostname','unknown')}")
    return "\n".join(lines)

pause()

for d in bgp_devices:
    bgp_cfg = gen_bgp_config(d, INVENTORY)
    if bgp_cfg:
        out(f"! {d['hostname']}")
        for line in bgp_cfg.splitlines():
            out(line)
        blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — The Full IaC Pipeline
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "The Full IaC Pipeline")

section("10.1 — Combining All Steps")

explain("A complete IaC pipeline uses every skill you have built:")
blank()
explain("  1. Read inventory from YAML")
explain("  2. Validate each device")
explain("  3. Enrich with computed fields")
explain("  4. Generate config per device")
explain("  5. Write per-device .cfg files")
explain("  6. Run compliance checks")
explain("  7. Write JSON audit report")
blank()

pause()

section("10.2 — Step 1-2: Load and Validate")

inventory_yaml = yaml.dump(
    [{"hostname": d["hostname"], "platform": d["platform"],
      "status": d["status"], "ip": d["ip"],
      "vlans": d["vlans"], "config": d["config"],
      "bgp": d["bgp"], "site": d["site"], "role": d["role"]}
     for d in INVENTORY],
    default_flow_style=False
)
inv_path = demo("pipeline_inventory.yaml")
with open(inv_path, "w") as f:
    f.write(inventory_yaml)

cmd("# Step 1 — Load YAML")
cmd("with open('inventory.yaml') as f:")
cmd("    inventory = yaml.safe_load(f)")
with open(inv_path) as f:
    pipeline_inv = yaml.safe_load(f)
blank()

cmd("# Step 2 — Validate")
cmd("def is_valid(d):")
cmd("    return (d.get('status') == 'up'")
cmd("            and d.get('platform') in ('IOS-XE','NX-OS','ASA'))")
blank()

def is_valid(d):
    return (d.get("status") == "up"
            and d.get("platform") in ("IOS-XE", "NX-OS", "ASA"))

cmd("valid   = [d for d in inventory if is_valid(d)]")
cmd("skipped = [d['hostname'] for d in inventory if not is_valid(d)]")
valid   = [d for d in pipeline_inv if is_valid(d)]
skipped = [d["hostname"] for d in pipeline_inv if not is_valid(d)]
cmd("print(f'{len(valid)} valid, {len(skipped)} skipped: {skipped}')")
out(f"{len(valid)} valid, {len(skipped)} skipped: {skipped}")
blank()

pause()

section("10.3 — Steps 3-5: Enrich, Generate, Write")

cmd("# Step 3 — Enrich")
cmd("for d in valid:")
cmd("    d['vlan_count'] = len(d['vlans'])")
cmd("    d['device_type'] = ('rtr' in d['hostname'] and 'router'")
cmd("                        or 'sw' in d['hostname'] and 'switch'")
cmd("                        or 'firewall')")
for d in valid:
    d["vlan_count"] = len(d["vlans"])
    d["device_type"] = ("router" if "rtr" in d["hostname"]
                        else "switch" if "sw" in d["hostname"]
                        else "firewall")
blank()

pipeline_configs_dir = demo("pipeline_configs")
os.makedirs(pipeline_configs_dir, exist_ok=True)
cmd("# Steps 4-5 — Generate and write configs")
cmd("os.makedirs('pipeline_configs', exist_ok=True)")
cmd("for d in valid:")
cmd("    config = gen_full_config(d)")
cmd("    with open(f\"pipeline_configs/{d['hostname']}.cfg\", 'w') as f:")
cmd("        f.write(config)")
cmd("print(f'Wrote {len(valid)} config files')")
for d in valid:
    config = gen_full_config(d)
    with open(os.path.join(pipeline_configs_dir, f"{d['hostname']}.cfg"), "w") as f:
        f.write(config)
out(f"Wrote {len(valid)} config files")
blank()

pause()

section("10.4 — Steps 6-7: Audit and Report")

cmd("# Step 6 — Compliance")
cmd("audit = run_compliance(valid, COMPLIANCE_CHECKS)")
audit = run_compliance(valid, COMPLIANCE_CHECKS)
blank()

cmd("# Step 7 — Write JSON report")
audit_path = demo("audit_report.json")
cmd("with open('audit_report.json', 'w') as f:")
cmd("    json.dump(audit, f, indent=2)")
with open(audit_path, "w") as f:
    json.dump(audit, f, indent=2)
out("Written: audit_report.json")
blank()

cmd("# Print summary")
cmd("passed = sum(1 for r in audit if r['overall']=='PASS')")
cmd("failed = sum(1 for r in audit if r['overall']=='FAIL')")
cmd("print(f'Audit: {passed} PASS, {failed} FAIL')")
passed = sum(1 for r in audit if r["overall"] == "PASS")
failed = sum(1 for r in audit if r["overall"] == "FAIL")
out(f"Audit: {passed} PASS, {failed} FAIL")
blank()

pause()

explain("The full pipeline in 30 lines of Python:")
blank()
explain("  1. yaml.safe_load()         — load inventory")
explain("  2. filter with condition    — validate")
explain("  3. list comprehension       — enrich")
explain("  4. gen_full_config()        — generate config text")
explain("  5. open + write             — write .cfg files")
explain("  6. run_compliance()         — audit checks")
explain("  7. json.dump()              — write report")
blank()
explain("Every single technique used here came from the")
explain("previous topics in this course.")

pause()

# ── Clean up ─────────────────────────────────────────────────────────────────
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
print(f"  {BOLD}Ch 1{RESET}   Mental model — source → Python → mapped output → target")
print(f"  {BOLD}Ch 2{RESET}   Ansible inventory — inventory dict → hosts.yaml")
print(f"  {BOLD}Ch 3{RESET}   Config text — device dict → per-device .cfg files")
print(f"  {BOLD}Ch 4{RESET}   VLAN intent — intent dict → switchport + SVI config")
print(f"  {BOLD}Ch 5{RESET}   Role policies — role → policy function → config lines")
print(f"  {BOLD}Ch 6{RESET}   RESTCONF payloads — flat dict → nested API JSON")
print(f"  {BOLD}Ch 7{RESET}   Compliance report — checks → pass/fail → JSON report")
print(f"  {BOLD}Ch 8{RESET}   Change plan — before/after state → diff → ordered changes")
print(f"  {BOLD}Ch 9{RESET}   BGP config — site topology + neighbors → router bgp blocks")
print(f"  {BOLD}Ch 10{RESET}  Full pipeline — YAML load → validate → enrich → configs → audit")
blank()
print(f"  {WHITE}This topic brings together every skill from the course:")
print(f"  data structures, functions, filtering, file I/O,")
print(f"  JSON, YAML — applied to real Cisco IaC tasks.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()