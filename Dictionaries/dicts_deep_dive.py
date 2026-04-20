# dicts_deep_dive.py
# Dicts in Python — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

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

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON DICTS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a Dict
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a Dict")

section("1.1 — Definition")

explain("A dict is an ordered, mutable collection of key-value pairs.")
explain("Ordered  — insertion order is preserved (Python 3.7+).")
explain("Mutable  — you can add, remove, or change key-value pairs.")
explain("Key-value — every piece of data has a name (key) and a value.")
blank()
explain("In Cisco IaC, dicts model real things:")
explain("  A device   → hostname, platform, ip, status")
explain("  An interface → name, mode, vlan, state")
explain("  A site     → name, region, devices, vlans")
blank()

pause()

section("1.2 — Creating Dicts")

explain("An empty dict:")
blank()
cmd("device = {}")
device = {}
cmd("print(device)")
out(device)
cmd("print(type(device))")
out(type(device))
blank()

pause()

explain("A dict representing a Cisco device:")
blank()
cmd("device = {")
cmd("    'hostname': 'nyc-rtr-01',")
cmd("    'platform': 'IOS-XE',")
cmd("    'ip':       '10.0.0.1',")
cmd("    'status':   'up',")
cmd("}")
device = {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "ip":       "10.0.0.1",
    "status":   "up",
}
cmd("print(device)")
out(device)
blank()

pause()

explain("Values can be any type — strings, ints, bools, lists, dicts:")
blank()
cmd("interface = {")
cmd("    'name':    'GigabitEthernet0/0',")
cmd("    'vlan':    10,")
cmd("    'enabled': True,")
cmd("    'peers':   ['10.0.0.2', '10.0.0.3'],")
cmd("}")
interface = {
    "name":    "GigabitEthernet0/0",
    "vlan":    10,
    "enabled": True,
    "peers":   ["10.0.0.2", "10.0.0.3"],
}
cmd("print(interface)")
out(interface)
blank()

pause()

explain("Keys must be immutable — strings, ints, tuples work.")
explain("Lists cannot be keys.")
blank()
cmd("d = {}")
d = {}
cmd("d['hostname'] = 'nyc-rtr-01'   # string key — ok")
d["hostname"] = "nyc-rtr-01"
cmd("d[1]         = 'primary'       # int key    — ok")
d[1] = "primary"
cmd("d[('NYC',1)] = 'site-1'        # tuple key  — ok")
d[("NYC", 1)] = "site-1"
cmd("print(d)")
out(d)
blank()

pause()

explain("Dict vs list — when to use which:")
blank()
explain("  Use a LIST when order matters and items are the same kind:")
explain("    ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
explain("  Use a DICT when each item has named fields:")
explain("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()

pause()

explain("Length — how many key-value pairs:")
blank()
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("print(len(device))")
out(len(device))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Accessing Values
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Accessing Values")

section("2.1 — Square Bracket Access")

explain("Access a value by its key using square brackets.")
blank()

device = {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "ip":       "10.0.0.1",
    "status":   "up",
}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'ip': '10.0.0.1', 'status': 'up'}")
blank()
cmd("print(device['hostname'])")
out(device["hostname"])
cmd("print(device['ip'])")
out(device["ip"])
cmd("print(device['status'])")
out(device["status"])
blank()

pause()

explain("Accessing a key that does not exist raises KeyError:")
blank()
cmd("print(device['vendor'])")
blank()
try:
    print(device["vendor"])
except KeyError as e:
    warn(f"KeyError: {e}")
blank()

pause()

section("2.2 — .get() — Safe Access With a Default")

explain(".get(key) returns None if key does not exist — no error.")
explain(".get(key, default) returns default if key does not exist.")
blank()

cmd("print(device.get('hostname'))")
out(device.get("hostname"))
blank()
cmd("print(device.get('vendor'))")
out(device.get("vendor"))
blank()
cmd("print(device.get('vendor', 'Cisco'))")
out(device.get("vendor", "Cisco"))
blank()

pause()

explain("Practical use — safe access in a loop:")
blank()
inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS", "vendor": "Cisco"},
    {"hostname": "sin-fw-01"},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS', 'vendor': 'Cisco'},")
cmd("    {'hostname': 'sin-fw-01'},")
cmd("]")
blank()
cmd("for d in inventory:")
cmd("    platform = d.get('platform', 'UNKNOWN')")
cmd("    print(f\"{d['hostname']}: {platform}\")")
blank()
for d in inventory:
    platform = d.get("platform", "UNKNOWN")
    out(f"{d['hostname']}: {platform}")
blank()

pause()

section("2.3 — Nested Dict Access")

explain("Chain square brackets to access nested dicts.")
blank()

site = {
    "name": "NYC",
    "router": {
        "hostname": "nyc-rtr-01",
        "bgp": {
            "as_number": 65001,
            "neighbors": ["10.0.0.2", "10.0.0.3"],
        },
    },
}
cmd("site = {")
cmd("    'name': 'NYC',")
cmd("    'router': {")
cmd("        'hostname': 'nyc-rtr-01',")
cmd("        'bgp': {")
cmd("            'as_number': 65001,")
cmd("            'neighbors': ['10.0.0.2', '10.0.0.3'],")
cmd("        },")
cmd("    },")
cmd("}")
blank()

pause()

cmd("print(site['name'])")
out(site["name"])
cmd("print(site['router']['hostname'])")
out(site["router"]["hostname"])
cmd("print(site['router']['bgp']['as_number'])")
out(site["router"]["bgp"]["as_number"])
cmd("print(site['router']['bgp']['neighbors'][0])")
out(site["router"]["bgp"]["neighbors"][0])
blank()

pause()

explain("Use .get() for safe nested access:")
blank()
cmd("print(site.get('router', {}).get('bgp', {}).get('as_number', 'N/A'))")
out(site.get("router", {}).get("bgp", {}).get("as_number", "N/A"))
cmd("print(site.get('firewall', {}).get('ip', 'N/A'))")
out(site.get("firewall", {}).get("ip", "N/A"))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Checking Keys
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Checking Keys")

section("3.1 — in and not in")

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
blank()
cmd("print('hostname' in device)")
out("hostname" in device)
cmd("print('vendor' in device)")
out("vendor" in device)
cmd("print('vendor' not in device)")
out("vendor" not in device)
blank()

pause()

explain("Practical use — add a key only if it does not exist:")
blank()
cmd("if 'vendor' not in device:")
cmd("    device['vendor'] = 'Cisco'")
if "vendor" not in device:
    device["vendor"] = "Cisco"
cmd("print(device)")
out(device)
blank()

pause()

section("3.2 — .keys(), .values(), .items()")

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
blank()

cmd("print(device.keys())")
out(device.keys())
cmd("print(device.values())")
out(device.values())
cmd("print(device.items())")
out(device.items())
blank()

pause()

explain("Convert to list to index or slice:")
blank()
cmd("print(list(device.keys()))")
out(list(device.keys()))
cmd("print(list(device.values()))")
out(list(device.values()))
blank()

pause()

explain("Check if a value exists:")
blank()
cmd("print('IOS-XE' in device.values())")
out("IOS-XE" in device.values())
cmd("print('ASA' in device.values())")
out("ASA" in device.values())
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Modifying Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Modifying Dicts")

section("4.1 — Adding and Updating Keys")

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()

explain("Add a new key:")
blank()
cmd("device['ip'] = '10.0.0.1'")
device["ip"] = "10.0.0.1"
cmd("print(device)")
out(device)
blank()

pause()

explain("Update an existing key:")
blank()
cmd("device['hostname'] = 'nyc-rtr-01-core'")
device["hostname"] = "nyc-rtr-01-core"
cmd("print(device)")
out(device)
blank()

pause()

explain("Add multiple keys at once with .update():")
blank()
cmd("device.update({'vendor': 'Cisco', 'status': 'up', 'vlans': [10, 20]})")
device.update({"vendor": "Cisco", "status": "up", "vlans": [10, 20]})
cmd("print(device)")
out(device)
blank()

pause()

section("4.2 — Removing Keys")

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'ip': '10.0.0.1', 'status': 'up'}")
blank()

explain("del — remove a key:")
blank()
cmd("del device['status']")
del device["status"]
cmd("print(device)")
out(device)
blank()

pause()

explain(".pop(key) — remove and return the value:")
blank()
cmd("ip = device.pop('ip')")
ip = device.pop("ip")
cmd("print(ip)")
out(ip)
cmd("print(device)")
out(device)
blank()

pause()

explain(".pop(key, default) — safe pop, no KeyError if missing:")
blank()
cmd("vendor = device.pop('vendor', 'not set')")
vendor = device.pop("vendor", "not set")
cmd("print(vendor)")
out(vendor)
cmd("print(device)")
out(device)
blank()

pause()

section("4.3 — .setdefault() — Add Only If Missing")

explain(".setdefault(key, value) adds the key only if it")
explain("does not already exist. Returns the value either way.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()
cmd("device.setdefault('status', 'up')")
device.setdefault("status", "up")
cmd("print(device)")
out(device)
blank()

pause()

cmd("device.setdefault('status', 'down')   # key exists — not overwritten")
device.setdefault("status", "down")
cmd("print(device['status'])")
out(device["status"])
blank()

pause()

explain("Practical use — build a dict of lists safely:")
blank()
cmd("groups = {}")
groups = {}
cmd("devices = [")
cmd("    ('IOS-XE', 'nyc-rtr-01'),")
cmd("    ('NX-OS',  'lon-sw-01'),")
cmd("    ('IOS-XE', 'ams-rtr-02'),")
cmd("]")
devices_pairs = [
    ("IOS-XE", "nyc-rtr-01"),
    ("NX-OS",  "lon-sw-01"),
    ("IOS-XE", "ams-rtr-02"),
]
cmd("for platform, hostname in devices:")
cmd("    groups.setdefault(platform, [])")
cmd("    groups[platform].append(hostname)")
for platform, hostname in devices_pairs:
    groups.setdefault(platform, [])
    groups[platform].append(hostname)
cmd("print(groups)")
out(groups)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Iterating Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Iterating Dicts")

section("5.1 — Iterating Keys")

explain("A plain for loop iterates over keys by default.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
blank()
cmd("for key in device:")
cmd("    print(key)")
blank()
for key in device:
    out(key)
blank()

pause()

section("5.2 — Iterating Keys and Values with .items()")

explain(".items() gives you (key, value) pairs — the most useful loop.")
blank()

cmd("for key, value in device.items():")
cmd("    print(f'{key}: {value}')")
blank()
for key, value in device.items():
    out(f"{key}: {value}")
blank()

pause()

explain("Practical use — generate config from a dict:")
blank()
cmd("for key, value in device.items():")
cmd("    print(f'  set device {key} {value}')")
blank()
for key, value in device.items():
    out(f"  set device {key} {value}")
blank()

pause()

section("5.3 — Iterating Values Only")

cmd("for value in device.values():")
cmd("    print(value)")
blank()
for value in device.values():
    out(value)
blank()

pause()

section("5.4 — Iterating a List of Dicts")

explain("The most common IaC pattern — a list of device dicts.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'status': 'down'},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'status': 'up'},")
cmd("]")
blank()
cmd("for device in inventory:")
cmd("    print(f\"{device['hostname']:<15} {device['platform']:<10} {device['status']}\")")
blank()
for device in inventory:
    out(f"{device['hostname']:<15} {device['platform']:<10} {device['status']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Building Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Building Dicts")

section("6.1 — Building in a Loop")

explain("Start with an empty dict, add keys as you go.")
blank()

cmd("device = {}")
device = {}
cmd("device['hostname'] = 'nyc-rtr-01'")
device["hostname"] = "nyc-rtr-01"
cmd("device['platform'] = 'IOS-XE'")
device["platform"] = "IOS-XE"
cmd("device['ip']       = '10.0.0.1'")
device["ip"] = "10.0.0.1"
cmd("print(device)")
out(device)
blank()

pause()

explain("Build a lookup dict from a list:")
blank()
hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
ips       = ["10.0.0.1",   "10.1.0.1",  "10.2.0.1"]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("ips       = ['10.0.0.1',   '10.1.0.1',  '10.2.0.1']")
blank()
cmd("ip_map = {}")
ip_map = {}
cmd("for hostname, ip in zip(hostnames, ips):")
cmd("    ip_map[hostname] = ip")
for hostname, ip in zip(hostnames, ips):
    ip_map[hostname] = ip
cmd("print(ip_map)")
out(ip_map)
blank()

pause()

section("6.2 — dict() Constructor and zip()")

explain("Use dict(zip()) to build a dict from two lists in one line.")
blank()

cmd("ip_map = dict(zip(hostnames, ips))")
ip_map = dict(zip(hostnames, ips))
cmd("print(ip_map)")
out(ip_map)
blank()

pause()

explain("dict() constructor from keyword arguments:")
blank()
cmd("device = dict(hostname='nyc-rtr-01', platform='IOS-XE', status='up')")
device = dict(hostname="nyc-rtr-01", platform="IOS-XE", status="up")
cmd("print(device)")
out(device)
blank()

pause()

section("6.3 — Dict Comprehensions")

explain("Syntax: {key_expr: value_expr for item in iterable}")
explain("Same idea as list comprehensions — one clean line.")
blank()

pause()

explain("Build hostname → ip mapping:")
blank()
inventory = [
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
cmd("ip_map = {d['hostname']: d['ip'] for d in inventory}")
ip_map = {d["hostname"]: d["ip"] for d in inventory}
cmd("print(ip_map)")
out(ip_map)
blank()

pause()

explain("Build hostname → platform, uppercase:")
blank()
cmd("platform_map = {d['hostname']: d['platform'].upper() for d in inventory}")
platform_map = {d["hostname"]: d["platform"].upper() for d in inventory}
cmd("print(platform_map)")
out(platform_map)
blank()

pause()

explain("With a filter — only IOS-XE devices:")
blank()
cmd("iosxe_map = {d['hostname']: d['ip']")
cmd("            for d in inventory if d['platform'] == 'IOS-XE'}")
iosxe_map = {d["hostname"]: d["ip"] for d in inventory if d["platform"] == "IOS-XE"}
cmd("print(iosxe_map)")
out(iosxe_map)
blank()

pause()

explain("Invert a dict — swap keys and values:")
blank()
cmd("ip_map = {'nyc-rtr-01': '10.0.0.1', 'lon-sw-01': '10.1.0.1'}")
ip_map = {"nyc-rtr-01": "10.0.0.1", "lon-sw-01": "10.1.0.1"}
cmd("inverted = {v: k for k, v in ip_map.items()}")
inverted = {v: k for k, v in ip_map.items()}
cmd("print(inverted)")
out(inverted)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Nested Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Nested Dicts")

section("7.1 — Dict of Dicts")

explain("Each value is itself a dict.")
explain("The most common structure for device configs in IaC.")
blank()

sites = {
    "NYC": {"router": "nyc-rtr-01", "ip": "10.0.0.1", "vlans": [10, 20, 30]},
    "LON": {"router": "lon-sw-01",  "ip": "10.1.0.1", "vlans": [10, 20]},
    "SIN": {"router": "sin-fw-01",  "ip": "10.2.0.1", "vlans": [30, 40]},
}
cmd("sites = {")
cmd("    'NYC': {'router': 'nyc-rtr-01', 'ip': '10.0.0.1', 'vlans': [10,20,30]},")
cmd("    'LON': {'router': 'lon-sw-01',  'ip': '10.1.0.1', 'vlans': [10,20]},")
cmd("    'SIN': {'router': 'sin-fw-01',  'ip': '10.2.0.1', 'vlans': [30,40]},")
cmd("}")
blank()

pause()

cmd("print(sites['NYC'])")
out(sites["NYC"])
cmd("print(sites['NYC']['router'])")
out(sites["NYC"]["router"])
cmd("print(sites['LON']['vlans'])")
out(sites["LON"]["vlans"])
blank()

pause()

explain("Iterate over all sites:")
blank()
cmd("for site_name, config in sites.items():")
cmd("    print(f\"{site_name}: {config['router']} → {config['ip']}\")")
blank()
for site_name, config in sites.items():
    out(f"{site_name}: {config['router']} → {config['ip']}")
blank()

pause()

section("7.2 — Dict of Lists")

explain("Each value is a list — common for grouping devices by platform.")
blank()

platform_groups = {
    "IOS-XE": ["nyc-rtr-01", "ams-rtr-02", "syd-rtr-01"],
    "NX-OS":  ["lon-sw-01",  "tok-sw-01"],
    "ASA":    ["sin-fw-01",  "dub-fw-01"],
}
cmd("platform_groups = {")
cmd("    'IOS-XE': ['nyc-rtr-01', 'ams-rtr-02', 'syd-rtr-01'],")
cmd("    'NX-OS':  ['lon-sw-01',  'tok-sw-01'],")
cmd("    'ASA':    ['sin-fw-01',  'dub-fw-01'],")
cmd("}")
blank()

pause()

cmd("print(platform_groups['IOS-XE'])")
out(platform_groups["IOS-XE"])
cmd("print(platform_groups['NX-OS'][0])")
out(platform_groups["NX-OS"][0])
blank()

pause()

explain("Iterate over groups:")
blank()
cmd("for platform, devices in platform_groups.items():")
cmd("    print(f'{platform}: {len(devices)} devices')")
cmd("    for d in devices:")
cmd("        print(f'    - {d}')")
blank()
for platform, devices in platform_groups.items():
    out(f"{platform}: {len(devices)} devices")
    for d in devices:
        out(f"    - {d}")
blank()

pause()

section("7.3 — Building Nested Dicts")

explain("Build a nested dict from a flat list of dicts.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "ip": "10.3.0.1"},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'ip': '10.1.0.1'},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'ip': '10.3.0.1'},")
cmd("]")
blank()

pause()

explain("Build hostname → full config lookup:")
blank()
cmd("device_map = {d['hostname']: d for d in inventory}")
device_map = {d["hostname"]: d for d in inventory}
cmd("print(device_map['nyc-rtr-01'])")
out(device_map["nyc-rtr-01"])
cmd("print(device_map['nyc-rtr-01']['ip'])")
out(device_map["nyc-rtr-01"]["ip"])
blank()

pause()

explain("Group by platform using .setdefault():")
blank()
cmd("by_platform = {}")
by_platform = {}
cmd("for d in inventory:")
cmd("    by_platform.setdefault(d['platform'], [])")
cmd("    by_platform[d['platform']].append(d['hostname'])")
for d in inventory:
    by_platform.setdefault(d["platform"], [])
    by_platform[d["platform"]].append(d["hostname"])
cmd("print(by_platform)")
out(by_platform)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Merging and Copying
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Merging and Copying")

section("8.1 — Merging Dicts")

explain("Three ways to merge dicts.")
blank()

defaults = {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"}
site_cfg  = {"hostname": "nyc-rtr-01", "ntp": "10.1.0.100"}
cmd("defaults = {'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
cmd("site_cfg  = {'hostname': 'nyc-rtr-01', 'ntp': '10.1.0.100'}")
blank()

pause()

explain("Method 1 — .update() — site_cfg values win:")
blank()
cmd("merged = defaults.copy()")
merged = defaults.copy()
cmd("merged.update(site_cfg)")
merged.update(site_cfg)
cmd("print(merged)")
out(merged)
blank()

pause()

explain("Method 2 — {**a, **b} unpacking — right side wins:")
blank()
cmd("merged = {**defaults, **site_cfg}")
merged = {**defaults, **site_cfg}
cmd("print(merged)")
out(merged)
blank()

pause()

explain("Method 3 — | operator (Python 3.9+):")
blank()
cmd("merged = defaults | site_cfg")
merged = defaults | site_cfg
cmd("print(merged)")
out(merged)
blank()

pause()

section("8.2 — Copying Dicts")

explain("For flat dicts — .copy() is sufficient.")
explain("For nested dicts — use copy.deepcopy().")
blank()

flat = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("flat      = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
cmd("flat_copy = flat.copy()")
flat_copy = flat.copy()
cmd("flat_copy['hostname'] = 'lon-sw-01'")
flat_copy["hostname"] = "lon-sw-01"
cmd("print(flat)")
out(flat)
cmd("print(flat_copy)")
out(flat_copy)
blank()

pause()

explain("Nested dict — must use deepcopy:")
blank()
import copy
nested = {"hostname": "nyc-rtr-01", "bgp": {"as_number": 65001, "neighbors": ["10.0.0.2"]}}
cmd("import copy")
cmd("nested = {'hostname': 'nyc-rtr-01', 'bgp': {'as_number': 65001, 'neighbors': ['10.0.0.2']}}")
cmd("deep   = copy.deepcopy(nested)")
deep = copy.deepcopy(nested)
cmd("deep['bgp']['neighbors'].append('10.0.0.3')")
deep["bgp"]["neighbors"].append("10.0.0.3")
cmd("print(nested['bgp'])")
out(nested["bgp"])
cmd("print(deep['bgp'])")
out(deep["bgp"])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Common Dict Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Common Dict Patterns")

section("9.1 — Counting Occurrences")

explain("Count how many times each platform appears.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS"},
    {"hostname": "sin-fw-01",  "platform": "ASA"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS"},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE"},
]
cmd("inventory = [  # 8 devices across 3 platforms")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS'},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA'},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE'},")
cmd("    {'hostname': 'tok-sw-01',  'platform': 'NX-OS'},")
cmd("    {'hostname': 'syd-rtr-01', 'platform': 'IOS-XE'},")
cmd("]")
blank()

pause()

cmd("counts = {}")
counts = {}
cmd("for d in inventory:")
cmd("    platform = d['platform']")
cmd("    counts[platform] = counts.get(platform, 0) + 1")
for d in inventory:
    platform = d["platform"]
    counts[platform] = counts.get(platform, 0) + 1
cmd("print(counts)")
out(counts)
blank()

pause()

explain("Same thing as a dict comprehension:")
blank()
platforms = set(d["platform"] for d in inventory)
cmd("platforms = set(d['platform'] for d in inventory)")
cmd("counts = {p: sum(1 for d in inventory if d['platform'] == p)")
cmd("         for p in platforms}")
counts_c = {p: sum(1 for d in inventory if d["platform"] == p) for p in platforms}
cmd("print(counts_c)")
out(counts_c)
blank()

pause()

section("9.2 — Grouping by a Field")

explain("Group devices by platform into a dict of lists.")
blank()

cmd("groups = {}")
groups = {}
cmd("for d in inventory:")
cmd("    groups.setdefault(d['platform'], [])")
cmd("    groups[d['platform']].append(d['hostname'])")
for d in inventory:
    groups.setdefault(d["platform"], [])
    groups[d["platform"]].append(d["hostname"])
cmd("print(groups)")
out(groups)
blank()

pause()

section("9.3 — Building a Lookup Dict")

explain("Index a list of dicts by a unique key for O(1) lookup.")
blank()

cmd("lookup = {d['hostname']: d for d in inventory}")
lookup = {d["hostname"]: d for d in inventory}
cmd("print(lookup['nyc-rtr-01'])")
out(lookup["nyc-rtr-01"])
blank()

pause()

explain("Without lookup — O(n) search every time:")
blank()
cmd("# Slow — scans entire list every time")
cmd("target = next((d for d in inventory if d['hostname'] == 'nyc-rtr-01'), None)")
cmd("print(target)")
target = next((d for d in inventory if d["hostname"] == "nyc-rtr-01"), None)
out(target)
blank()

pause()

explain("With lookup — O(1) direct access:")
blank()
cmd("# Fast — direct key access")
cmd("target = lookup.get('nyc-rtr-01')")
cmd("print(target)")
out(lookup.get("nyc-rtr-01"))
blank()

pause()

section("9.4 — Template Config Pattern")

explain("Define a base config dict, then customize per site.")
blank()

BASE = {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net", "vlans": [1, 10]}
sites_data = [
    {"name": "NYC", "hostname": "nyc-rtr-01", "ntp_override": "10.1.0.100"},
    {"name": "LON", "hostname": "lon-sw-01",  "ntp_override": None},
]
cmd("BASE = {'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
cmd("sites_data = [")
cmd("    {'name': 'NYC', 'hostname': 'nyc-rtr-01', 'ntp_override': '10.1.0.100'},")
cmd("    {'name': 'LON', 'hostname': 'lon-sw-01',  'ntp_override': None},")
cmd("]")
blank()

pause()

cmd("configs = []")
configs = []
cmd("for site in sites_data:")
cmd("    cfg = {**BASE}                    # copy base")
cmd("    cfg['hostname'] = site['hostname']")
cmd("    if site['ntp_override']:")
cmd("        cfg['ntp'] = site['ntp_override']")
cmd("    configs.append(cfg)")
for site in sites_data:
    cfg = {**BASE}
    cfg["hostname"] = site["hostname"]
    if site["ntp_override"]:
        cfg["ntp"] = site["ntp_override"]
    configs.append(cfg)
cmd("for c in configs:")
cmd("    print(c['hostname'], '→ ntp:', c['ntp'])")
blank()
for c in configs:
    out(f"{c['hostname']} → ntp: {c['ntp']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — KeyError")

explain("Accessing a missing key raises KeyError.")
explain("Always use .get() when unsure if a key exists.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()
cmd("print(device['vendor'])   # KeyError!")
blank()
try:
    print(device["vendor"])
except KeyError as e:
    warn(f"KeyError: {e}")
blank()
cmd("print(device.get('vendor', 'unknown'))   # safe")
out(device.get("vendor", "unknown"))
blank()

pause()

section("10.2 — Mutating While Iterating")

explain("Never add or remove keys while iterating a dict.")
explain("It raises RuntimeError in Python 3.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "debug": True, "verbose": False}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'debug': True, 'verbose': False}")
blank()
cmd("# Wrong — mutating while iterating")
cmd("for key in device:")
cmd("    if key in ('debug', 'verbose'):")
cmd("        del device[key]   # RuntimeError!")
blank()
try:
    for key in device:
        if key in ("debug", "verbose"):
            del device[key]
except RuntimeError as e:
    warn(f"RuntimeError: {e}")
blank()

pause()

explain("Fix — iterate over a copy of the keys:")
blank()
device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "debug": True, "verbose": False}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'debug': True, 'verbose': False}")
cmd("for key in list(device.keys()):")
cmd("    if key in ('debug', 'verbose'):")
cmd("        del device[key]")
for key in list(device.keys()):
    if key in ("debug", "verbose"):
        del device[key]
cmd("print(device)")
out(device)
blank()

pause()

explain("Or use a dict comprehension — cleanest way:")
blank()
device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "debug": True, "verbose": False}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'debug': True, 'verbose': False}")
cmd("device = {k: v for k, v in device.items()")
cmd("          if k not in ('debug', 'verbose')}")
device = {k: v for k, v in device.items() if k not in ("debug", "verbose")}
cmd("print(device)")
out(device)
blank()

pause()

section("10.3 — Shallow Copy Trap")

explain("dict.copy() is shallow — nested objects are still shared.")
explain("Use copy.deepcopy() for nested dicts.")
blank()

base = {"hostname": "nyc-rtr-01", "bgp": {"as_number": 65001}}
cmd("base      = {'hostname': 'nyc-rtr-01', 'bgp': {'as_number': 65001}}")
cmd("site_copy = base.copy()              # shallow!")
site_copy = base.copy()
cmd("site_copy['bgp']['as_number'] = 65002")
site_copy["bgp"]["as_number"] = 65002
cmd("print(base['bgp'])                  # also changed!")
warn(base["bgp"])
blank()
cmd("deep_copy = copy.deepcopy(base)     # safe")
base["bgp"]["as_number"] = 65001
deep_copy = copy.deepcopy(base)
cmd("deep_copy['bgp']['as_number'] = 65002")
deep_copy["bgp"]["as_number"] = 65002
cmd("print(base['bgp'])                  # untouched")
out(base["bgp"])
blank()

pause()

section("10.4 — Key Order Is Preserved (Python 3.7+)")

explain("In Python 3.7+ dicts maintain insertion order.")
explain("You can rely on this for config generation.")
blank()

cmd("config = {}")
config = {}
cmd("config['hostname'] = 'nyc-rtr-01'")
config["hostname"] = "nyc-rtr-01"
cmd("config['platform'] = 'IOS-XE'")
config["platform"] = "IOS-XE"
cmd("config['ip']       = '10.0.0.1'")
config["ip"] = "10.0.0.1"
cmd("for k, v in config.items():")
cmd("    print(k, ':', v)")
blank()
for k, v in config.items():
    out(f"{k} : {v}")
blank()
explain("Keys always print in the order they were inserted.")
blank()

pause()

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
print(f"  {BOLD}Ch 1{RESET}   What is a dict — create, len, key types, dict vs list")
print(f"  {BOLD}Ch 2{RESET}   Accessing — d['key'], .get(), nested access")
print(f"  {BOLD}Ch 3{RESET}   Checking — in, .keys(), .values(), .items()")
print(f"  {BOLD}Ch 4{RESET}   Modifying — add, update, del, .pop(), .setdefault()")
print(f"  {BOLD}Ch 5{RESET}   Iterating — keys, .items(), .values(), list of dicts")
print(f"  {BOLD}Ch 6{RESET}   Building — loop, dict(), zip(), comprehensions, invert")
print(f"  {BOLD}Ch 7{RESET}   Nested — dict of dicts, dict of lists, lookup by hostname")
print(f"  {BOLD}Ch 8{RESET}   Merging — .update(), {{**a, **b}}, | operator, deepcopy")
print(f"  {BOLD}Ch 9{RESET}   Patterns — counting, grouping, lookup, template config")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — KeyError, mutate while iterate, shallow copy")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  device configs, site mappings, platform groups,")
print(f"  BGP neighbors, interface tables, template configs.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()