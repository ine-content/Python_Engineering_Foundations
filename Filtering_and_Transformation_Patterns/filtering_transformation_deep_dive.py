# filtering_transformation_deep_dive.py
# Filtering and Transformation Patterns — Zero to Expert
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
print(f"{BOLD}         FILTERING AND TRANSFORMATION PATTERNS{RESET}")
print(f"{BOLD}         Zero to Expert — Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is Filtering vs Transformation
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is Filtering vs Transformation")

section("1.1 — Definitions")

explain("FILTERING — reduce a collection to only the items")
explain("that meet a condition. The number of items shrinks.")
explain("The shape and type of each item stays the same.")
blank()
explain("TRANSFORMATION — change the shape or value of each")
explain("item. Every item produces an output. Nothing is removed.")
blank()
explain("BOTH TOGETHER — filter first, then transform.")
explain("Or transform first, then filter. Or interleave.")
blank()

pause()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40,50]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up',   'vlans': [10,20,30]},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'status': 'down', 'vlans': [10,20]},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'status': 'up',   'vlans': [30,40,50]},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'status': 'up',   'vlans': [10,20,30,40]},")
cmd("]")
blank()

pause()

explain("FILTERING — keep only 'up' devices (4 in → 3 out):")
blank()
cmd("up_devices = [d for d in inventory if d['status'] == 'up']")
up_devices = [d for d in inventory if d["status"] == "up"]
cmd("print(len(up_devices))")
out(len(up_devices))
blank()

pause()

explain("TRANSFORMATION — extract hostname from each (4 in → 4 out):")
blank()
cmd("hostnames = [d['hostname'] for d in inventory]")
hostnames = [d["hostname"] for d in inventory]
cmd("print(hostnames)")
out(hostnames)
blank()

pause()

explain("BOTH — extract hostname only from 'up' devices (4 in → 3 out):")
blank()
cmd("up_hostnames = [d['hostname'] for d in inventory if d['status'] == 'up']")
up_hostnames = [d["hostname"] for d in inventory if d["status"] == "up"]
cmd("print(up_hostnames)")
out(up_hostnames)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Filtering Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Filtering Patterns")

section("2.1 — Single Condition")

explain("The simplest filter — one condition after 'if'.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40,50]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [20,30]},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,40,50]},
]
cmd("inventory = [  # 6 devices ]")
blank()

cmd("# Keep only IOS-XE devices")
cmd("iosxe = [d for d in inventory if d['platform'] == 'IOS-XE']")
iosxe = [d for d in inventory if d["platform"] == "IOS-XE"]
cmd("print([d['hostname'] for d in iosxe])")
out([d["hostname"] for d in iosxe])
blank()

pause()

cmd("# Keep only devices with more than 2 VLANs")
cmd("many_vlans = [d for d in inventory if len(d['vlans']) > 2]")
many_vlans = [d for d in inventory if len(d["vlans"]) > 2]
cmd("print([d['hostname'] for d in many_vlans])")
out([d["hostname"] for d in many_vlans])
blank()

pause()

cmd("# Keep only devices whose hostname contains 'rtr'")
cmd("routers = [d for d in inventory if 'rtr' in d['hostname']]")
routers = [d for d in inventory if "rtr" in d["hostname"]]
cmd("print([d['hostname'] for d in routers])")
out([d["hostname"] for d in routers])
blank()

pause()

section("2.2 — Multiple Conditions")

explain("Combine with 'and', 'or', 'not':")
blank()

cmd("# Up AND IOS-XE")
cmd("up_iosxe = [d for d in inventory")
cmd("           if d['status'] == 'up' and d['platform'] == 'IOS-XE']")
up_iosxe = [d for d in inventory
            if d["status"] == "up" and d["platform"] == "IOS-XE"]
cmd("print([d['hostname'] for d in up_iosxe])")
out([d["hostname"] for d in up_iosxe])
blank()

pause()

cmd("# ASA OR NX-OS (all non-IOS-XE platforms)")
cmd("non_iosxe = [d for d in inventory")
cmd("            if d['platform'] in ('ASA', 'NX-OS')]")
non_iosxe = [d for d in inventory
             if d["platform"] in ("ASA", "NX-OS")]
cmd("print([d['hostname'] for d in non_iosxe])")
out([d["hostname"] for d in non_iosxe])
blank()

pause()

cmd("# Up AND more than 2 VLANs AND not ASA")
cmd("eligible = [d for d in inventory")
cmd("           if d['status'] == 'up'")
cmd("           and len(d['vlans']) > 2")
cmd("           and d['platform'] != 'ASA']")
eligible = [d for d in inventory
            if d["status"] == "up"
            and len(d["vlans"]) > 2
            and d["platform"] != "ASA"]
cmd("print([d['hostname'] for d in eligible])")
out([d["hostname"] for d in eligible])
blank()

pause()

section("2.3 — Filtering on Nested Fields")

explain("Access nested fields inside the filter condition:")
blank()

inventory_cfg = [
    {"hostname": "nyc-rtr-01", "status": "up",
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "lon-sw-01",  "status": "down",
     "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"}},
    {"hostname": "sin-fw-01",  "status": "up",
     "config": {"ntp": "10.0.0.100", "dns": "1.1.1.1"}},
    {"hostname": "ams-rtr-02", "status": "up",
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
]
cmd("inventory_cfg = [")
cmd("    {'hostname': 'nyc-rtr-01', 'status': 'up',")
cmd("     'config': {'ntp': '10.0.0.100', 'dns': '8.8.8.8'}},")
cmd("    {'hostname': 'lon-sw-01',  'status': 'down',")
cmd("     'config': {'ntp': '10.1.0.100', 'dns': '8.8.8.8'}},")
cmd("    {'hostname': 'sin-fw-01',  'status': 'up',")
cmd("     'config': {'ntp': '10.0.0.100', 'dns': '1.1.1.1'}},")
cmd("    {'hostname': 'ams-rtr-02', 'status': 'up',")
cmd("     'config': {'ntp': '10.0.0.100', 'dns': '8.8.8.8'}},")
cmd("]")
blank()

pause()

cmd("# Devices with non-standard NTP")
cmd("custom_ntp = [d for d in inventory_cfg")
cmd("             if d['config']['ntp'] != '10.0.0.100']")
custom_ntp = [d for d in inventory_cfg
              if d["config"]["ntp"] != "10.0.0.100"]
cmd("print([d['hostname'] for d in custom_ntp])")
out([d["hostname"] for d in custom_ntp])
blank()

pause()

cmd("# Up devices with non-standard DNS")
cmd("custom_dns_up = [d for d in inventory_cfg")
cmd("                if d['status'] == 'up'")
cmd("                and d['config']['dns'] != '8.8.8.8']")
custom_dns_up = [d for d in inventory_cfg
                 if d["status"] == "up"
                 and d["config"]["dns"] != "8.8.8.8"]
cmd("print([d['hostname'] for d in custom_dns_up])")
out([d["hostname"] for d in custom_dns_up])
blank()

pause()

section("2.4 — any() and all() as Filter Conditions")

explain("Use any()/all() to filter based on a sub-collection:")
blank()

inventory_vlans = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "vlans": [10, 20]},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50]},
    {"hostname": "ams-rtr-02", "vlans": [10, 20, 30, 40]},
]
cmd("inventory_vlans = [...]")
blank()

cmd("# Devices that have VLAN 30 on ANY of their VLANs")
cmd("has_vlan30 = [d for d in inventory_vlans if 30 in d['vlans']]")
has_vlan30 = [d for d in inventory_vlans if 30 in d["vlans"]]
cmd("print([d['hostname'] for d in has_vlan30])")
out([d["hostname"] for d in has_vlan30])
blank()

pause()

cmd("# Devices where ALL VLANs are below 40")
cmd("all_small = [d for d in inventory_vlans")
cmd("            if all(v < 40 for v in d['vlans'])]")
all_small = [d for d in inventory_vlans
             if all(v < 40 for v in d["vlans"])]
cmd("print([d['hostname'] for d in all_small])")
out([d["hostname"] for d in all_small])
blank()

pause()

cmd("# Devices that have ANY vlan over 30")
cmd("any_large = [d for d in inventory_vlans")
cmd("            if any(v > 30 for v in d['vlans'])]")
any_large = [d for d in inventory_vlans
             if any(v > 30 for v in d["vlans"])]
cmd("print([d['hostname'] for d in any_large])")
out([d["hostname"] for d in any_large])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Transformation Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Transformation Patterns")

section("3.1 — Extracting a Field")

explain("Pull one field out of each item — most common transform.")
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

cmd("hostnames  = [d['hostname'] for d in inventory]")
hostnames = [d["hostname"] for d in inventory]
cmd("platforms  = [d['platform'] for d in inventory]")
platforms = [d["platform"] for d in inventory]
cmd("ips        = [d['ip'] for d in inventory]")
ips = [d["ip"] for d in inventory]
blank()
cmd("print(hostnames)")
out(hostnames)
cmd("print(platforms)")
out(platforms)
cmd("print(ips)")
out(ips)
blank()

pause()

section("3.2 — Normalising Values")

explain("Transform each value into a standard form:")
blank()

raw = [
    {"hostname": "  NYC-RTR-01  ", "status": "UP"},
    {"hostname": "LON-SW-01",      "status": "Down"},
    {"hostname": "sin-fw-01 ",     "status": "up"},
]
cmd("raw = [")
cmd("    {'hostname': '  NYC-RTR-01  ', 'status': 'UP'},")
cmd("    {'hostname': 'LON-SW-01',      'status': 'Down'},")
cmd("    {'hostname': 'sin-fw-01 ',     'status': 'up'},")
cmd("]")
blank()

cmd("normalised = [")
cmd("    {'hostname': d['hostname'].strip().lower(),")
cmd("     'status':   d['status'].lower()}")
cmd("    for d in raw")
cmd("]")
normalised = [
    {"hostname": d["hostname"].strip().lower(),
     "status":   d["status"].lower()}
    for d in raw
]
cmd("for n in normalised: print(n)")
blank()
for n in normalised:
    out(n)
blank()

pause()

section("3.3 — Adding Computed Fields")

explain("Add a new field to each item based on existing fields:")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "vlans": [10, 20]},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50]},
    {"hostname": "ams-rtr-02", "vlans": [10, 20, 30, 40]},
]
cmd("inventory = [...]")
blank()

cmd("enriched = [")
cmd("    {")
cmd("        **d,                                   # keep all existing fields")
cmd("        'vlan_count':  len(d['vlans']),")
cmd("        'vlan_size':   'large' if len(d['vlans']) > 2 else 'small',")
cmd("    }")
cmd("    for d in inventory")
cmd("]")
enriched = [
    {
        **d,
        "vlan_count": len(d["vlans"]),
        "vlan_size":  "large" if len(d["vlans"]) > 2 else "small",
    }
    for d in inventory
]
cmd("for e in enriched: print(e)")
blank()
for e in enriched:
    out(e)
blank()

pause()

section("3.4 — Reshaping a Dict")

explain("Change which fields are kept and how they're named:")
blank()

cmd("# Full device dict → slim summary dict")
cmd("summary = [")
cmd("    {'host': d['hostname'], 'platform': d['platform']}")
cmd("    for d in inventory")
cmd("]")
inventory2 = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1", "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "ip": "10.2.0.1", "vlans": [30,40,50]},
]
summary = [
    {"host": d["hostname"], "platform": d["platform"]}
    for d in inventory2
]
cmd("for s in summary: print(s)")
blank()
for s in summary:
    out(s)
blank()

pause()

explain("Build a flat string from a nested dict:")
blank()
cmd("config_lines = [")
cmd("    f\"hostname {d['hostname']}\\n\"")
cmd("    f\"  ip address {d['ip']}\\n\"")
cmd("    f\"  platform {d['platform']}\"")
cmd("    for d in inventory2")
cmd("]")
config_lines = [
    f"hostname {d['hostname']}\n"
    f"  ip address {d['ip']}\n"
    f"  platform {d['platform']}"
    for d in inventory2
]
cmd("for cfg in config_lines: print(cfg)")
blank()
for cfg in config_lines:
    out(cfg)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Filter + Transform Together
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Filter + Transform Together")

section("4.1 — In One Comprehension")

explain("Filter with 'if', transform with the expression.")
explain("Read left to right: WHAT to produce, WHERE from, WHEN to include.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "ip": "10.3.0.1"},
]
cmd("inventory = [  # 4 devices ]")
blank()

cmd("# IPs of up IOS-XE devices only")
cmd("target_ips = [d['ip'] for d in inventory")
cmd("             if d['status'] == 'up' and d['platform'] == 'IOS-XE']")
target_ips = [d["ip"] for d in inventory
              if d["status"] == "up" and d["platform"] == "IOS-XE"]
cmd("print(target_ips)")
out(target_ips)
blank()

pause()

cmd("# Config snippet for each up device")
cmd("config_snippets = [")
cmd("    f\"hostname {d['hostname']}\\n ntp server 10.0.0.100\"")
cmd("    for d in inventory if d['status'] == 'up'")
cmd("]")
config_snippets = [
    f"hostname {d['hostname']}\n ntp server 10.0.0.100"
    for d in inventory if d["status"] == "up"
]
cmd("for s in config_snippets: print(s)")
blank()
for s in config_snippets:
    out(s)
blank()

pause()

section("4.2 — When to Split Into Steps")

explain("One complex comprehension is hard to read.")
explain("Split into steps when logic gets complex:")
blank()

cmd("# Hard to read in one line")
cmd("result = [{'host': d['hostname'].upper(),")
cmd("           'vlans': [v for v in d.get('vlans',[]) if v > 10]}")
cmd("          for d in inventory")
cmd("          if d['status']=='up' and d['platform']!='ASA']")
blank()

explain("Cleaner as steps:")
blank()
cmd("# Step 1 — filter")
cmd("step1 = [d for d in inventory")
cmd("         if d['status'] == 'up' and d['platform'] != 'ASA']")
blank()
cmd("# Step 2 — transform")
cmd("result = [{'host': d['hostname'].upper(),")
cmd("           'vlans': [v for v in d.get('vlans',[]) if v > 10]}")
cmd("          for d in step1]")
blank()

inventory_with_vlans = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
]
step1 = [d for d in inventory_with_vlans
         if d["status"] == "up" and d["platform"] != "ASA"]
result = [{"host": d["hostname"].upper(),
           "vlans": [v for v in d.get("vlans", []) if v > 10]}
          for d in step1]
cmd("for r in result: print(r)")
blank()
for r in result:
    out(r)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — map() and filter()
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "map() and filter()")

section("5.1 — map() — Apply a Function to Every Item")

explain("map(function, iterable) applies a function to each item.")
explain("Returns a map object — wrap in list() to see results.")
blank()

hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()

cmd("upper = list(map(str.upper, hostnames))")
upper = list(map(str.upper, hostnames))
cmd("print(upper)")
out(upper)
blank()

pause()

explain("map() with a lambda for more complex transforms:")
blank()
cmd("short = list(map(lambda h: h[:3].upper(), hostnames))")
short = list(map(lambda h: h[:3].upper(), hostnames))
cmd("print(short)")
out(short)
blank()

pause()

explain("map() on a list of dicts:")
blank()
inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS"},
]
cmd("inventory = [{'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'},")
cmd("             {'hostname': 'lon-sw-01',  'platform': 'NX-OS'}]")
blank()
cmd("platforms = list(map(lambda d: d['platform'], inventory))")
platforms = list(map(lambda d: d["platform"], inventory))
cmd("print(platforms)")
out(platforms)
blank()

pause()

section("5.2 — filter() — Keep Items That Pass a Test")

explain("filter(function, iterable) keeps items where")
explain("the function returns True.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "status": "up"},
    {"hostname": "lon-sw-01",  "status": "down"},
    {"hostname": "sin-fw-01",  "status": "up"},
]
cmd("inventory = [{'hostname': 'nyc-rtr-01', 'status': 'up'},")
cmd("             {'hostname': 'lon-sw-01',  'status': 'down'},")
cmd("             {'hostname': 'sin-fw-01',  'status': 'up'}]")
blank()

cmd("up_devices = list(filter(lambda d: d['status'] == 'up', inventory))")
up_devices = list(filter(lambda d: d["status"] == "up", inventory))
cmd("print([d['hostname'] for d in up_devices])")
out([d["hostname"] for d in up_devices])
blank()

pause()

section("5.3 — map() vs filter() vs Comprehension")

explain("All three accomplish the same goals.")
explain("Comprehensions are generally preferred in Python")
explain("because they are more readable.")
blank()

cmd("# These three are equivalent:")
blank()
cmd("# map()")
cmd("upper1 = list(map(lambda h: h.upper(), hostnames))")
hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
upper1 = list(map(lambda h: h.upper(), hostnames))
cmd("# Comprehension")
cmd("upper2 = [h.upper() for h in hostnames]")
upper2 = [h.upper() for h in hostnames]
cmd("print(upper1 == upper2)")
out(upper1 == upper2)
blank()

pause()

explain("Use map()/filter() when:")
explain("  — applying an existing named function: map(str.upper, lst)")
explain("  — passing to another function that expects an iterable")
explain("  — working in a functional style with chained operations")
blank()
explain("Use comprehensions when:")
explain("  — the logic is clear and readable")
explain("  — you want filtering and transformation together")
explain("  — you are building a list, dict, or set in one step")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Chaining Transformations
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Chaining Transformations")

section("6.1 — Multiple Steps in Sequence")

explain("Apply multiple transformations one after another.")
explain("Each step produces a new collection fed into the next.")
blank()

raw_inventory = [
    {"hostname": "  NYC-RTR-01  ", "platform": "ios-xe", "status": "UP",   "vlans": [10,20,30,1]},
    {"hostname": "LON-SW-01",      "platform": "nx-os",  "status": "DOWN", "vlans": [10,20]},
    {"hostname": " SIN-FW-01",     "platform": "asa",    "status": "UP",   "vlans": [30,40,50]},
    {"hostname": "AMS-RTR-02",     "platform": "ios-xe", "status": "UP",   "vlans": [10,20,30,40]},
]
cmd("raw_inventory = [")
cmd("    {'hostname': '  NYC-RTR-01  ', 'platform': 'ios-xe', 'status': 'UP',   'vlans': [10,20,30,1]},")
cmd("    {'hostname': 'LON-SW-01',      'platform': 'nx-os',  'status': 'DOWN', 'vlans': [10,20]},")
cmd("    {'hostname': ' SIN-FW-01',     'platform': 'asa',    'status': 'UP',   'vlans': [30,40,50]},")
cmd("    {'hostname': 'AMS-RTR-02',     'platform': 'ios-xe', 'status': 'UP',   'vlans': [10,20,30,40]},")
cmd("]")
blank()

pause()

cmd("# Step 1 — normalise strings")
cmd("step1 = [")
cmd("    {**d, 'hostname': d['hostname'].strip().lower(),")
cmd("          'platform': d['platform'].upper(),")
cmd("          'status':   d['status'].lower()}")
cmd("    for d in raw_inventory")
cmd("]")
step1 = [
    {**d, "hostname": d["hostname"].strip().lower(),
          "platform": d["platform"].upper(),
          "status":   d["status"].lower()}
    for d in raw_inventory
]
cmd("print(step1[0])")
out(step1[0])
blank()

pause()

cmd("# Step 2 — filter: keep only 'up' devices")
cmd("step2 = [d for d in step1 if d['status'] == 'up']")
step2 = [d for d in step1 if d["status"] == "up"]
cmd("print([d['hostname'] for d in step2])")
out([d["hostname"] for d in step2])
blank()

pause()

cmd("# Step 3 — remove reserved VLAN 1 from each device")
RESERVED = {1, 1002, 1003, 1004, 1005}
cmd("RESERVED = {1, 1002, 1003, 1004, 1005}")
cmd("step3 = [{**d, 'vlans': [v for v in d['vlans'] if v not in RESERVED]}")
cmd("         for d in step2]")
step3 = [{**d, "vlans": [v for v in d["vlans"] if v not in RESERVED]}
         for d in step2]
cmd("for d in step3: print(d['hostname'], d['vlans'])")
blank()
for d in step3:
    out(f"{d['hostname']} {d['vlans']}")
blank()

pause()

section("6.2 — Pipeline as a Function")

explain("Wrap the pipeline in a function for reuse:")
blank()

cmd("def process_inventory(raw):")
cmd("    clean  = [{**d, 'hostname': d['hostname'].strip().lower(),")
cmd("               'platform': d['platform'].upper(),")
cmd("               'status': d['status'].lower()} for d in raw]")
cmd("    active = [d for d in clean if d['status'] == 'up']")
cmd("    result = [{**d, 'vlans': [v for v in d['vlans']")
cmd("               if v not in RESERVED]} for d in active]")
cmd("    return result")
blank()

def process_inventory(raw):
    clean  = [{**d, "hostname": d["hostname"].strip().lower(),
               "platform": d["platform"].upper(),
               "status":   d["status"].lower()} for d in raw]
    active = [d for d in clean if d["status"] == "up"]
    result = [{**d, "vlans": [v for v in d["vlans"]
               if v not in RESERVED]} for d in active]
    return result

cmd("result = process_inventory(raw_inventory)")
result = process_inventory(raw_inventory)
cmd("for d in result: print(d['hostname'], d['platform'], d['vlans'])")
blank()
for d in result:
    out(f"{d['hostname']} {d['platform']} {d['vlans']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Grouping and Partitioning
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Grouping and Partitioning")

section("7.1 — Partitioning into Two Groups")

explain("Split a list into YES and NO groups based on a condition.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down"},
]
cmd("inventory = [  # 5 devices ]")
blank()

cmd("up_devices   = [d for d in inventory if d['status'] == 'up']")
cmd("down_devices = [d for d in inventory if d['status'] == 'down']")
up_devices   = [d for d in inventory if d["status"] == "up"]
down_devices = [d for d in inventory if d["status"] == "down"]
cmd("print('Up:',   [d['hostname'] for d in up_devices])")
out(f"Up:   {[d['hostname'] for d in up_devices]}")
cmd("print('Down:', [d['hostname'] for d in down_devices])")
out(f"Down: {[d['hostname'] for d in down_devices]}")
blank()

pause()

explain("One-pass partition using a loop (more efficient):")
blank()
cmd("up, down = [], []")
up, down = [], []
cmd("for d in inventory:")
cmd("    (up if d['status'] == 'up' else down).append(d['hostname'])")
for d in inventory:
    (up if d["status"] == "up" else down).append(d["hostname"])
cmd("print('Up:', up)")
out(f"Up: {up}")
cmd("print('Down:', down)")
out(f"Down: {down}")
blank()

pause()

section("7.2 — Grouping by a Field")

explain("Group items into a dict of lists based on a field value:")
blank()

cmd("groups = {}")
groups = {}
cmd("for d in inventory:")
cmd("    groups.setdefault(d['platform'], [])")
cmd("    groups[d['platform']].append(d['hostname'])")
cmd("for platform, hosts in groups.items():")
cmd("    print(f'{platform}: {hosts}')")
for d in inventory:
    groups.setdefault(d["platform"], [])
    groups[d["platform"]].append(d["hostname"])
blank()
for platform, hosts in groups.items():
    out(f"{platform}: {hosts}")
blank()

pause()

explain("Same thing as a dict comprehension:")
blank()
platforms_unique = sorted(set(d["platform"] for d in inventory))
cmd("platforms = sorted(set(d['platform'] for d in inventory))")
cmd("groups = {")
cmd("    p: [d['hostname'] for d in inventory if d['platform'] == p]")
cmd("    for p in platforms")
cmd("}")
groups = {
    p: [d["hostname"] for d in inventory if d["platform"] == p]
    for p in platforms_unique
}
cmd("for platform, hosts in groups.items():")
cmd("    print(f'{platform}: {hosts}')")
blank()
for platform, hosts in groups.items():
    out(f"{platform}: {hosts}")
blank()

pause()

section("7.3 — Grouping by Computed Key")

explain("Group by a value derived from the item, not a raw field:")
blank()

inventory_v = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "vlans": [10, 20]},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50]},
    {"hostname": "ams-rtr-02", "vlans": [10, 20, 30, 40]},
]
cmd("inventory_v = [...]")
blank()

cmd("by_size = {}")
by_size = {}
cmd("for d in inventory_v:")
cmd("    key = 'large' if len(d['vlans']) > 2 else 'small'")
cmd("    by_size.setdefault(key, [])")
cmd("    by_size[key].append(d['hostname'])")
cmd("print(by_size)")
for d in inventory_v:
    key = "large" if len(d["vlans"]) > 2 else "small"
    by_size.setdefault(key, [])
    by_size[key].append(d["hostname"])
out(by_size)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Aggregation After Filtering
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Aggregation After Filtering")

section("8.1 — Count, Sum, Min, Max on Filtered Data")

explain("Filter first, then aggregate the result.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40,50]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [20,30]},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,40,50]},
]
cmd("inventory = [  # 6 devices ]")
blank()

cmd("# Count of up devices")
cmd("up_count = sum(1 for d in inventory if d['status'] == 'up')")
up_count = sum(1 for d in inventory if d["status"] == "up")
cmd("print(up_count)")
out(up_count)
blank()

pause()

cmd("# Total VLANs across all up IOS-XE devices")
cmd("total_vlans = sum(")
cmd("    len(d['vlans'])")
cmd("    for d in inventory")
cmd("    if d['status'] == 'up' and d['platform'] == 'IOS-XE'")
cmd(")")
total_vlans = sum(
    len(d["vlans"])
    for d in inventory
    if d["status"] == "up" and d["platform"] == "IOS-XE"
)
cmd("print(total_vlans)")
out(total_vlans)
blank()

pause()

cmd("# Max VLAN count among up devices")
cmd("max_vlans = max(len(d['vlans']) for d in inventory if d['status'] == 'up')")
max_vlans = max(len(d["vlans"]) for d in inventory if d["status"] == "up")
cmd("print(max_vlans)")
out(max_vlans)
blank()

pause()

cmd("# Device with the most VLANs (among up devices)")
cmd("busiest = max(")
cmd("    (d for d in inventory if d['status'] == 'up'),")
cmd("    key=lambda d: len(d['vlans'])")
cmd(")")
busiest = max(
    (d for d in inventory if d["status"] == "up"),
    key=lambda d: len(d["vlans"])
)
cmd("print(busiest['hostname'], len(busiest['vlans']))")
out(f"{busiest['hostname']} {len(busiest['vlans'])}")
blank()

pause()

section("8.2 — Aggregation Per Group")

explain("Count/sum within each group:")
blank()

cmd("platforms_unique = sorted(set(d['platform'] for d in inventory))")
platforms_unique = sorted(set(d["platform"] for d in inventory))
cmd("platform_stats = {")
cmd("    p: {")
cmd("        'total': sum(1 for d in inventory if d['platform'] == p),")
cmd("        'up':    sum(1 for d in inventory if d['platform'] == p")
cmd("                     and d['status'] == 'up'),")
cmd("    }")
cmd("    for p in platforms_unique")
cmd("}")
platform_stats = {
    p: {
        "total": sum(1 for d in inventory if d["platform"] == p),
        "up":    sum(1 for d in inventory if d["platform"] == p
                     and d["status"] == "up"),
    }
    for p in platforms_unique
}
cmd("for p, stats in platform_stats.items(): print(p, stats)")
blank()
for p, stats in platform_stats.items():
    out(f"{p} {stats}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Transforming Nested Structures
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Transforming Nested Structures")

section("9.1 — Filter/Transform on Nested Lists")

explain("Apply filtering and transformation to the inner lists too:")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "status": "up",
     "interfaces": [
         {"name": "Gi0/0", "vlan": 10, "state": "up"},
         {"name": "Gi0/1", "vlan": 20, "state": "down"},
         {"name": "Gi0/2", "vlan": 30, "state": "up"},
     ]},
    {"hostname": "lon-sw-01", "status": "down",
     "interfaces": [
         {"name": "Gi0/0", "vlan": 10, "state": "up"},
         {"name": "Gi0/1", "vlan": 20, "state": "down"},
     ]},
    {"hostname": "sin-fw-01", "status": "up",
     "interfaces": [
         {"name": "Gi0/0", "vlan": 30, "state": "up"},
         {"name": "Gi0/1", "vlan": 40, "state": "up"},
     ]},
]
cmd("inventory = [  # devices with interfaces ]")
blank()

pause()

explain("Keep only up devices AND only their up interfaces:")
blank()
cmd("result = [")
cmd("    {")
cmd("        'hostname':   d['hostname'],")
cmd("        'interfaces': [i for i in d['interfaces'] if i['state'] == 'up']")
cmd("    }")
cmd("    for d in inventory if d['status'] == 'up'")
cmd("]")
result = [
    {
        "hostname":   d["hostname"],
        "interfaces": [i for i in d["interfaces"] if i["state"] == "up"]
    }
    for d in inventory if d["status"] == "up"
]
cmd("for r in result: print(r['hostname'], [i['name'] for i in r['interfaces']])")
blank()
for r in result:
    out(f"{r['hostname']} {[i['name'] for i in r['interfaces']]}")
blank()

pause()

section("9.2 — Flatten + Filter")

explain("Collapse nested lists into flat results, with filtering:")
blank()

cmd("# All (hostname, interface_name) pairs where interface is 'down'")
cmd("down_pairs = [")
cmd("    (d['hostname'], i['name'])")
cmd("    for d in inventory")
cmd("    for i in d['interfaces']")
cmd("    if i['state'] == 'down'")
cmd("]")
down_pairs = [
    (d["hostname"], i["name"])
    for d in inventory
    for i in d["interfaces"]
    if i["state"] == "down"
]
cmd("print(down_pairs)")
out(down_pairs)
blank()

pause()

cmd("# All unique VLANs used on up interfaces across up devices")
cmd("active_vlans = sorted(set(")
cmd("    i['vlan']")
cmd("    for d in inventory if d['status'] == 'up'")
cmd("    for i in d['interfaces'] if i['state'] == 'up'")
cmd("))")
active_vlans = sorted(set(
    i["vlan"]
    for d in inventory if d["status"] == "up"
    for i in d["interfaces"] if i["state"] == "up"
))
cmd("print(active_vlans)")
out(active_vlans)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — Filtering on Wrong Type")

explain("Comparing a string to an int silently returns False.")
explain("Always check your types match the data.")
blank()

vlans = [10, "20", 30, "40", 50]
cmd("vlans = [10, '20', 30, '40', 50]   # mixed types!")
blank()
cmd("# Wrong — '20' != 20")
cmd("result = [v for v in vlans if v > 15]")
blank()
try:
    result = [v for v in vlans if v > 15]
    out(result)
except TypeError as e:
    warn(f"TypeError: {e}")
blank()

pause()

cmd("# Fix — normalise types first")
cmd("clean_vlans = [int(v) for v in vlans]")
clean_vlans = [int(v) for v in vlans]
cmd("result = [v for v in clean_vlans if v > 15]")
result = [v for v in clean_vlans if v > 15]
cmd("print(result)")
out(result)
blank()

pause()

section("10.2 — Transforming In Place vs Returning New")

explain("Do NOT modify items while iterating them.")
explain("Always produce a new collection.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "ios-xe"},
    {"hostname": "lon-sw-01",  "platform": "nx-os"},
]
cmd("inventory = [{'hostname': 'nyc-rtr-01', 'platform': 'ios-xe'},")
cmd("             {'hostname': 'lon-sw-01',  'platform': 'nx-os'}]")
blank()

cmd("# Wrong — mutates original dict while iterating")
cmd("for d in inventory:")
cmd("    d['platform'] = d['platform'].upper()")
blank()
explain("This works but mutates the original — caller's data changes.")
explain("Unpredictable when the same dict is referenced elsewhere.")
blank()

pause()

cmd("# Correct — produce a new list, original untouched")
cmd("normalised = [{**d, 'platform': d['platform'].upper()}")
cmd("              for d in inventory]")
inventory2 = [
    {"hostname": "nyc-rtr-01", "platform": "ios-xe"},
    {"hostname": "lon-sw-01",  "platform": "nx-os"},
]
normalised = [{**d, "platform": d["platform"].upper()}
              for d in inventory2]
cmd("print(normalised)")
out(normalised)
cmd("print(inventory2)   # original unchanged")
out(inventory2)
blank()

pause()

section("10.3 — Silently Losing Data in a Filter")

explain("A filter condition that is always True or always False")
explain("silently returns everything or nothing.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()

cmd("# Bug — wrong variable name in condition")
cmd("threshold = 25")
threshold = 25
cmd("result = [v for v in vlans if threshold > 20]   # always True!")
result = [v for v in vlans if threshold > 20]
cmd("print(result)   # all items kept — not what we wanted")
warn(result)
blank()

pause()

cmd("# Fix — reference the loop variable")
cmd("result = [v for v in vlans if v > 20]")
result = [v for v in vlans if v > 20]
cmd("print(result)")
out(result)
blank()
explain("Always test your filter with data that should be excluded.")
explain("If nothing is excluded — the condition may be wrong.")

pause()

section("10.4 — Comprehension vs Generator")

explain("A list comprehension creates the full list immediately.")
explain("A generator expression creates items one at a time.")
explain("Use generators when you only need to iterate once")
explain("and don't need all results in memory at once.")
blank()

cmd("# List comprehension — all in memory at once")
cmd("total = sum([len(d['vlans']) for d in inventory_v])")
blank()
cmd("# Generator expression — one at a time, more efficient")
cmd("total = sum(len(d['vlans']) for d in inventory_v)")
inventory_v = [
    {"hostname": "nyc-rtr-01", "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "vlans": [10,20]},
]
total = sum(len(d["vlans"]) for d in inventory_v)
cmd("print(total)")
out(total)
blank()
explain("Notice: no square brackets inside sum() — that is a generator.")
explain("For sum(), max(), min(), any(), all() — prefer generators.")

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
print(f"  {BOLD}Ch 1{RESET}   Filter vs Transform — definitions, what each does")
print(f"  {BOLD}Ch 2{RESET}   Filtering — single, multiple, nested fields, any/all")
print(f"  {BOLD}Ch 3{RESET}   Transformation — extract, normalise, add field, reshape")
print(f"  {BOLD}Ch 4{RESET}   Filter + Transform together — one line or split steps")
print(f"  {BOLD}Ch 5{RESET}   map() and filter() — when to use vs comprehensions")
print(f"  {BOLD}Ch 6{RESET}   Chaining — multi-step pipelines, pipeline as function")
print(f"  {BOLD}Ch 7{RESET}   Grouping — partition into 2, group by field, computed key")
print(f"  {BOLD}Ch 8{RESET}   Aggregation — count/sum/max after filtering, per group")
print(f"  {BOLD}Ch 9{RESET}   Nested structures — filter inner lists, flatten + filter")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — wrong type, mutate in place, silent filter bug")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  device inventories, interface tables, VLAN lists,")
print(f"  config normalisation, platform classification.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()