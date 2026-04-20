# nested_deep_dive.py
# Nested Structures in Python — Zero to Expert
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
print(f"{BOLD}         NESTED STRUCTURES — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a Nested Structure
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a Nested Structure")

section("1.1 — Definition")

explain("A nested structure is any container that holds")
explain("other containers as its elements.")
blank()
explain("Python containers — list, dict, tuple, set — can all")
explain("hold other containers. Any combination is valid:")
blank()
explain("  list of lists       → 2D table, matrix")
explain("  list of dicts       → rows of records")
explain("  dict of dicts       → keyed configs")
explain("  dict of lists       → grouped data")
explain("  dict of dicts of lists → full site inventory")
blank()

pause()

explain("In Cisco IaC, almost everything is nested.")
explain("A site has devices. A device has interfaces.")
explain("An interface has VLANs. A VLAN has members.")
blank()
explain("Flat:    {'hostname': 'nyc-rtr-01', 'vlan': 10}")
explain("Nested:  {'hostname': 'nyc-rtr-01',")
explain("          'interfaces': [")
explain("              {'name': 'Gi0/0', 'vlans': [10, 20]},")
explain("              {'name': 'Gi0/1', 'vlans': [30]},")
explain("          ]}")
blank()

pause()

section("1.2 — How Python Stores Nested Structures")

explain("Python containers store REFERENCES — not copies.")
explain("A list of dicts holds references to dict objects.")
explain("This is why mutation through one name affects another.")
blank()

cmd("a = {'hostname': 'nyc-rtr-01'}")
a = {"hostname": "nyc-rtr-01"}
cmd("lst = [a, a, a]   # three references to the SAME dict")
lst = [a, a, a]
cmd("lst[0]['hostname'] = 'CHANGED'")
lst[0]["hostname"] = "CHANGED"
cmd("print(lst)")
out(lst)
blank()
warn("All three changed — they all point to the same dict.")
blank()

pause()

explain("Always create fresh dicts in a loop — never reuse one:")
blank()
cmd("lst = [{'hostname': f'device-{i}'} for i in range(3)]")
lst = [{"hostname": f"device-{i}"} for i in range(3)]
cmd("lst[0]['hostname'] = 'CHANGED'")
lst[0]["hostname"] = "CHANGED"
cmd("print(lst)")
out(lst)
blank()
explain("Only index 0 changed — each dict is a separate object.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — List of Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "List of Lists")

section("2.1 — Creating and Accessing")

explain("A list where each element is itself a list.")
explain("Think of it as a table — rows and columns.")
blank()

interfaces = [
    ["Gi0/0", "access", 10,  "up"],
    ["Gi0/1", "access", 20,  "up"],
    ["Gi0/2", "trunk",  None,"down"],
    ["Gi0/3", "access", 30,  "up"],
]
cmd("interfaces = [")
cmd("    ['Gi0/0', 'access', 10,   'up'],")
cmd("    ['Gi0/1', 'access', 20,   'up'],")
cmd("    ['Gi0/2', 'trunk',  None, 'down'],")
cmd("    ['Gi0/3', 'access', 30,   'up'],")
cmd("]")
blank()

pause()

explain("Access: outer index first, then inner index.")
blank()
cmd("print(interfaces[0])         # first row")
out(interfaces[0])
cmd("print(interfaces[0][0])      # row 0, col 0 — name")
out(interfaces[0][0])
cmd("print(interfaces[2][1])      # row 2, col 1 — mode")
out(interfaces[2][1])
cmd("print(interfaces[-1][-1])    # last row, last col")
out(interfaces[-1][-1])
blank()

pause()

section("2.2 — Iterating Rows and Columns")

explain("Iterate rows with a for loop:")
blank()
cmd("for row in interfaces:")
cmd("    print(row)")
blank()
for row in interfaces:
    out(row)
blank()

pause()

explain("Unpack each row into named variables:")
blank()
cmd("for name, mode, vlan, state in interfaces:")
cmd("    print(f'{name:<8} mode={mode:<8} vlan={vlan!s:<5} state={state}')")
blank()
for name, mode, vlan, state in interfaces:
    out(f"{name:<8} mode={mode:<8} vlan={str(vlan):<5} state={state}")
blank()

pause()

explain("Iterate columns — get all names, all states:")
blank()
cmd("names  = [row[0] for row in interfaces]")
names = [row[0] for row in interfaces]
cmd("states = [row[3] for row in interfaces]")
states = [row[3] for row in interfaces]
cmd("print(names)")
out(names)
cmd("print(states)")
out(states)
blank()

pause()

section("2.3 — Filtering Rows")

explain("Filter rows based on a column value:")
blank()
cmd("up_interfaces = [row for row in interfaces if row[3] == 'up']")
up_interfaces = [row for row in interfaces if row[3] == "up"]
cmd("for row in up_interfaces:")
cmd("    print(row)")
blank()
for row in up_interfaces:
    out(row)
blank()

pause()

explain("Filter and extract a specific column:")
blank()
cmd("up_names = [row[0] for row in interfaces if row[3] == 'up']")
up_names = [row[0] for row in interfaces if row[3] == "up"]
cmd("print(up_names)")
out(up_names)
blank()

pause()

section("2.4 — Flattening a List of Lists")

explain("Collapse nested lists into a single flat list.")
blank()

site_vlans = [
    [10, 20, 30],
    [10, 40],
    [20, 30, 50],
]
cmd("site_vlans = [[10,20,30], [10,40], [20,30,50]]")
blank()
cmd("all_vlans = [v for sublist in site_vlans for v in sublist]")
all_vlans = [v for sublist in site_vlans for v in sublist]
cmd("print(all_vlans)")
out(all_vlans)
blank()
cmd("unique_vlans = sorted(set(all_vlans))")
unique_vlans = sorted(set(all_vlans))
cmd("print(unique_vlans)")
out(unique_vlans)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — List of Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "List of Dicts — Deeper Patterns")

section("3.1 — Sorting by a Nested Key")

inventory = [
    {"hostname": "sin-fw-01",  "platform": "ASA",    "vlans": [30,40,50], "status": "up"},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "vlans": [10,20,30], "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "vlans": [10,20],    "status": "down"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "vlans": [10,20,30,40], "status": "up"},
]
cmd("inventory = [")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'vlans': [30,40,50],    'status': 'up'},")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'vlans': [10,20,30],    'status': 'up'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'vlans': [10,20],       'status': 'down'},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'vlans': [10,20,30,40], 'status': 'up'},")
cmd("]")
blank()

pause()

explain("Sort by hostname:")
blank()
cmd("by_name = sorted(inventory, key=lambda d: d['hostname'])")
by_name = sorted(inventory, key=lambda d: d["hostname"])
cmd("for d in by_name: print(d['hostname'])")
blank()
for d in by_name:
    out(d["hostname"])
blank()

pause()

explain("Sort by number of VLANs descending:")
blank()
cmd("by_vlans = sorted(inventory, key=lambda d: len(d['vlans']), reverse=True)")
by_vlans = sorted(inventory, key=lambda d: len(d["vlans"]), reverse=True)
cmd("for d in by_vlans: print(d['hostname'], len(d['vlans']), 'vlans')")
blank()
for d in by_vlans:
    out(f"{d['hostname']} {len(d['vlans'])} vlans")
blank()

pause()

section("3.2 — Filtering on a Nested Field")

explain("Filter where a nested list contains a value:")
blank()
cmd("has_vlan_20 = [d for d in inventory if 20 in d['vlans']]")
has_vlan_20 = [d for d in inventory if 20 in d["vlans"]]
cmd("for d in has_vlan_20: print(d['hostname'])")
blank()
for d in has_vlan_20:
    out(d["hostname"])
blank()

pause()

explain("Filter where all VLANs are under 40:")
blank()
cmd("small_vlans = [d for d in inventory if all(v < 40 for v in d['vlans'])]")
small_vlans = [d for d in inventory if all(v < 40 for v in d["vlans"])]
cmd("for d in small_vlans: print(d['hostname'], d['vlans'])")
blank()
for d in small_vlans:
    out(f"{d['hostname']} {d['vlans']}")
blank()

pause()

section("3.3 — Transforming Nested Values")

explain("Build a new list of dicts with transformed values:")
blank()
cmd("summary = [")
cmd("    {")
cmd("        'hostname':  d['hostname'].upper(),")
cmd("        'platform':  d['platform'],")
cmd("        'vlan_count': len(d['vlans']),")
cmd("        'status':    d['status'],")
cmd("    }")
cmd("    for d in inventory")
cmd("]")
summary = [
    {
        "hostname":   d["hostname"].upper(),
        "platform":   d["platform"],
        "vlan_count": len(d["vlans"]),
        "status":     d["status"],
    }
    for d in inventory
]
cmd("for s in summary: print(s)")
blank()
for s in summary:
    out(s)
blank()

pause()

section("3.4 — Grouping a List of Dicts")

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
cmd("for platform, hosts in groups.items():")
cmd("    print(f'{platform}: {hosts}')")
blank()
for platform, hosts in groups.items():
    out(f"{platform}: {hosts}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Dict of Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Dict of Dicts — Deeper Patterns")

section("4.1 — Building and Navigating")

explain("Keyed by hostname — direct O(1) lookup.")
blank()

devices = {
    "nyc-rtr-01": {"platform": "IOS-XE", "ip": "10.0.0.1", "status": "up",   "vlans": [10,20,30]},
    "lon-sw-01":  {"platform": "NX-OS",  "ip": "10.1.0.1", "status": "down", "vlans": [10,20]},
    "sin-fw-01":  {"platform": "ASA",    "ip": "10.2.0.1", "status": "up",   "vlans": [30,40,50]},
}
cmd("devices = {")
cmd("    'nyc-rtr-01': {'platform': 'IOS-XE', 'ip': '10.0.0.1', 'status': 'up',   'vlans': [10,20,30]},")
cmd("    'lon-sw-01':  {'platform': 'NX-OS',  'ip': '10.1.0.1', 'status': 'down', 'vlans': [10,20]},")
cmd("    'sin-fw-01':  {'platform': 'ASA',    'ip': '10.2.0.1', 'status': 'up',   'vlans': [30,40,50]},")
cmd("}")
blank()

pause()

cmd("print(devices['nyc-rtr-01'])")
out(devices["nyc-rtr-01"])
cmd("print(devices['nyc-rtr-01']['ip'])")
out(devices["nyc-rtr-01"]["ip"])
cmd("print(devices['sin-fw-01']['vlans'])")
out(devices["sin-fw-01"]["vlans"])
blank()

pause()

section("4.2 — Updating Nested Keys Safely")

explain("Update a single field in a nested dict:")
blank()
cmd("devices['lon-sw-01']['status'] = 'up'")
devices["lon-sw-01"]["status"] = "up"
cmd("print(devices['lon-sw-01'])")
out(devices["lon-sw-01"])
blank()

pause()

explain("Add a new key to every nested dict:")
blank()
cmd("for hostname, cfg in devices.items():")
cmd("    cfg['vendor'] = 'Cisco'")
for hostname, cfg in devices.items():
    cfg["vendor"] = "Cisco"
cmd("print(devices['nyc-rtr-01'])")
out(devices["nyc-rtr-01"])
blank()

pause()

explain("Remove a key from every nested dict:")
blank()
cmd("for cfg in devices.values():")
cmd("    cfg.pop('vendor', None)   # None = no error if missing")
for cfg in devices.values():
    cfg.pop("vendor", None)
cmd("print(devices['nyc-rtr-01'])")
out(devices["nyc-rtr-01"])
blank()

pause()

section("4.3 — Querying a Dict of Dicts")

explain("Find all hostnames where status is 'up':")
blank()
cmd("up_hosts = [h for h, cfg in devices.items() if cfg['status'] == 'up']")
up_hosts = [h for h, cfg in devices.items() if cfg["status"] == "up"]
cmd("print(up_hosts)")
out(up_hosts)
blank()

pause()

explain("Build a filtered sub-dict — only 'up' devices:")
blank()
cmd("up_devices = {h: cfg for h, cfg in devices.items() if cfg['status'] == 'up'}")
up_devices = {h: cfg for h, cfg in devices.items() if cfg["status"] == "up"}
cmd("for h, cfg in up_devices.items():")
cmd("    print(h, '->', cfg['ip'])")
blank()
for h, cfg in up_devices.items():
    out(f"{h} -> {cfg['ip']}")
blank()

pause()

explain("Find all hostnames that have VLAN 10:")
blank()
cmd("vlan10_hosts = [h for h, cfg in devices.items() if 10 in cfg['vlans']]")
vlan10_hosts = [h for h, cfg in devices.items() if 10 in cfg["vlans"]]
cmd("print(vlan10_hosts)")
out(vlan10_hosts)
blank()

pause()

section("4.4 — Merging Two Dicts of Dicts")

explain("Merge site_a and site_b into one combined dict.")
explain("If a hostname exists in both — site_b wins.")
blank()

site_a = {
    "nyc-rtr-01": {"platform": "IOS-XE", "status": "up"},
    "lon-sw-01":  {"platform": "NX-OS",  "status": "down"},
}
site_b = {
    "lon-sw-01":  {"platform": "NX-OS",  "status": "up"},   # updated
    "sin-fw-01":  {"platform": "ASA",    "status": "up"},   # new
}
cmd("site_a = {'nyc-rtr-01': {'platform': 'IOS-XE', 'status': 'up'},")
cmd("          'lon-sw-01':  {'platform': 'NX-OS',  'status': 'down'}}")
cmd("site_b = {'lon-sw-01':  {'platform': 'NX-OS',  'status': 'up'},")
cmd("          'sin-fw-01':  {'platform': 'ASA',    'status': 'up'}}")
blank()
cmd("combined = {**site_a, **site_b}")
combined = {**site_a, **site_b}
cmd("for h, cfg in combined.items(): print(h, cfg)")
blank()
for h, cfg in combined.items():
    out(f"{h} {cfg}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Dict of Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Dict of Lists")

section("5.1 — Building and Appending Safely")

explain("Group VLANs by site using .setdefault():")
blank()

vlan_assignments = [
    ("NYC", 10), ("NYC", 20), ("NYC", 30),
    ("LON", 10), ("LON", 20),
    ("SIN", 30), ("SIN", 40), ("SIN", 50),
]
cmd("vlan_assignments = [")
cmd("    ('NYC', 10), ('NYC', 20), ('NYC', 30),")
cmd("    ('LON', 10), ('LON', 20),")
cmd("    ('SIN', 30), ('SIN', 40), ('SIN', 50),")
cmd("]")
blank()
cmd("site_vlans = {}")
site_vlans = {}
cmd("for site, vlan in vlan_assignments:")
cmd("    site_vlans.setdefault(site, [])")
cmd("    site_vlans[site].append(vlan)")
for site, vlan in vlan_assignments:
    site_vlans.setdefault(site, [])
    site_vlans[site].append(vlan)
cmd("print(site_vlans)")
out(site_vlans)
blank()

pause()

section("5.2 — Iterating and Querying")

explain("Iterate over all groups:")
blank()
cmd("for site, vlans in site_vlans.items():")
cmd("    print(f'{site}: {len(vlans)} vlans — {vlans}')")
blank()
for site, vlans in site_vlans.items():
    out(f"{site}: {len(vlans)} vlans — {vlans}")
blank()

pause()

explain("Find sites that have VLAN 10:")
blank()
cmd("has_vlan10 = [site for site, vlans in site_vlans.items() if 10 in vlans]")
has_vlan10 = [site for site, vlans in site_vlans.items() if 10 in vlans]
cmd("print(has_vlan10)")
out(has_vlan10)
blank()

pause()

explain("Find all unique VLANs across all sites:")
blank()
cmd("all_vlans = sorted(set(v for vlans in site_vlans.values() for v in vlans))")
all_vlans = sorted(set(v for vlans in site_vlans.values() for v in vlans))
cmd("print(all_vlans)")
out(all_vlans)
blank()

pause()

explain("Find sites that share VLAN 10 and VLAN 20:")
blank()
cmd("shared = [s for s, v in site_vlans.items() if 10 in v and 20 in v]")
shared = [s for s, v in site_vlans.items() if 10 in v and 20 in v]
cmd("print(shared)")
out(shared)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Three-Level Nesting
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Three-Level Nesting")

section("6.1 — Site → Devices → Interfaces")

explain("Real IaC structure — three levels deep.")
explain("Site contains devices. Devices contain interfaces.")
blank()

network = {
    "NYC": {
        "region": "us-east",
        "devices": [
            {
                "hostname": "nyc-rtr-01",
                "platform": "IOS-XE",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "up"},
                ],
            },
            {
                "hostname": "nyc-sw-01",
                "platform": "IOS-XE",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10,  "state": "up"},
                    {"name": "Gi0/1", "vlan": 30,  "state": "down"},
                ],
            },
        ],
    },
    "LON": {
        "region": "eu-west",
        "devices": [
            {
                "hostname": "lon-sw-01",
                "platform": "NX-OS",
                "interfaces": [
                    {"name": "Gi0/0", "vlan": 10, "state": "up"},
                    {"name": "Gi0/1", "vlan": 20, "state": "down"},
                ],
            },
        ],
    },
}
cmd("network = {")
cmd("    'NYC': {")
cmd("        'region': 'us-east',")
cmd("        'devices': [")
cmd("            {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("             'interfaces': [{'name':'Gi0/0','vlan':10,'state':'up'},")
cmd("                            {'name':'Gi0/1','vlan':20,'state':'up'}]},")
cmd("            {'hostname': 'nyc-sw-01',  'platform': 'IOS-XE',")
cmd("             'interfaces': [{'name':'Gi0/0','vlan':10,'state':'up'},")
cmd("                            {'name':'Gi0/1','vlan':30,'state':'down'}]},")
cmd("        ],")
cmd("    },")
cmd("    'LON': {")
cmd("        'region': 'eu-west',")
cmd("        'devices': [")
cmd("            {'hostname': 'lon-sw-01', 'platform': 'NX-OS',")
cmd("             'interfaces': [{'name':'Gi0/0','vlan':10,'state':'up'},")
cmd("                            {'name':'Gi0/1','vlan':20,'state':'down'}]},")
cmd("        ],")
cmd("    },")
cmd("}")
blank()

pause()

section("6.2 — Navigating Three Levels")

explain("Access by chaining keys and indexes:")
blank()
cmd("print(network['NYC']['region'])")
out(network["NYC"]["region"])
cmd("print(network['NYC']['devices'][0]['hostname'])")
out(network["NYC"]["devices"][0]["hostname"])
cmd("print(network['NYC']['devices'][0]['interfaces'][1]['vlan'])")
out(network["NYC"]["devices"][0]["interfaces"][1]["vlan"])
cmd("print(network['LON']['devices'][0]['interfaces'][0]['state'])")
out(network["LON"]["devices"][0]["interfaces"][0]["state"])
blank()

pause()

section("6.3 — Iterating All Three Levels")

explain("Loop through every interface in every device in every site:")
blank()
cmd("for site, site_cfg in network.items():")
cmd("    for device in site_cfg['devices']:")
cmd("        for iface in device['interfaces']:")
cmd("            print(f\"{site} | {device['hostname']} | {iface['name']} | vlan={iface['vlan']} | {iface['state']}\")")
blank()
for site, site_cfg in network.items():
    for device in site_cfg["devices"]:
        for iface in device["interfaces"]:
            out(f"{site} | {device['hostname']} | {iface['name']} | vlan={iface['vlan']} | {iface['state']}")
blank()

pause()

section("6.4 — Querying Across All Three Levels")

explain("Find all interfaces that are 'down' across all sites:")
blank()
cmd("down_ifaces = [")
cmd("    (site, device['hostname'], iface['name'])")
cmd("    for site, site_cfg in network.items()")
cmd("    for device in site_cfg['devices']")
cmd("    for iface in device['interfaces']")
cmd("    if iface['state'] == 'down'")
cmd("]")
down_ifaces = [
    (site, device["hostname"], iface["name"])
    for site, site_cfg in network.items()
    for device in site_cfg["devices"]
    for iface in device["interfaces"]
    if iface["state"] == "down"
]
cmd("for item in down_ifaces: print(item)")
blank()
for item in down_ifaces:
    out(item)
blank()

pause()

explain("Find all devices that have VLAN 10 on any interface:")
blank()
cmd("vlan10_devices = [")
cmd("    device['hostname']")
cmd("    for site_cfg in network.values()")
cmd("    for device in site_cfg['devices']")
cmd("    if any(iface['vlan'] == 10 for iface in device['interfaces'])")
cmd("]")
vlan10_devices = [
    device["hostname"]
    for site_cfg in network.values()
    for device in site_cfg["devices"]
    if any(iface["vlan"] == 10 for iface in device["interfaces"])
]
cmd("print(vlan10_devices)")
out(vlan10_devices)
blank()

pause()

section("6.5 — Modifying Nested Data")

explain("Update all 'down' interfaces to 'up':")
blank()
cmd("for site_cfg in network.values():")
cmd("    for device in site_cfg['devices']:")
cmd("        for iface in device['interfaces']:")
cmd("            if iface['state'] == 'down':")
cmd("                iface['state'] = 'up'")
for site_cfg in network.values():
    for device in site_cfg["devices"]:
        for iface in device["interfaces"]:
            if iface["state"] == "down":
                iface["state"] = "up"
blank()
cmd("# Verify — check LON interface that was down")
cmd("print(network['LON']['devices'][0]['interfaces'][1])")
out(network["LON"]["devices"][0]["interfaces"][1])
blank()

pause()

explain("Add a new key to every device across all sites:")
blank()
cmd("for site_cfg in network.values():")
cmd("    for device in site_cfg['devices']:")
cmd("        device['vendor'] = 'Cisco'")
for site_cfg in network.values():
    for device in site_cfg["devices"]:
        device["vendor"] = "Cisco"
cmd("print(network['NYC']['devices'][0])")
out(network["NYC"]["devices"][0])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Querying Nested Structures
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Querying Nested Structures")

section("7.1 — The General Query Pattern")

explain("The pattern that appears constantly in IaC:")
blank()
explain("  [collect  for level1 in data")
explain("            for level2 in level1[key]")
explain("            for level3 in level2[key]")
explain("            if condition]")
blank()
explain("Or as a nested for loop when logic is complex.")
blank()

pause()

inventory = [
    {
        "hostname": "nyc-rtr-01",
        "platform": "IOS-XE",
        "status":   "up",
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "down"},
            {"name": "Gi0/2", "vlan": 30, "state": "up"},
        ],
    },
    {
        "hostname": "lon-sw-01",
        "platform": "NX-OS",
        "status":   "down",
        "interfaces": [
            {"name": "Gi0/0", "vlan": 10, "state": "up"},
            {"name": "Gi0/1", "vlan": 20, "state": "up"},
        ],
    },
    {
        "hostname": "sin-fw-01",
        "platform": "ASA",
        "status":   "up",
        "interfaces": [
            {"name": "Gi0/0", "vlan": 30, "state": "up"},
            {"name": "Gi0/1", "vlan": 40, "state": "down"},
        ],
    },
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up',")
cmd("     'interfaces': [{'name':'Gi0/0','vlan':10,'state':'up'},")
cmd("                    {'name':'Gi0/1','vlan':20,'state':'down'},")
cmd("                    {'name':'Gi0/2','vlan':30,'state':'up'}]},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'status': 'down',")
cmd("     'interfaces': [{'name':'Gi0/0','vlan':10,'state':'up'},")
cmd("                    {'name':'Gi0/1','vlan':20,'state':'up'}]},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'status': 'up',")
cmd("     'interfaces': [{'name':'Gi0/0','vlan':30,'state':'up'},")
cmd("                    {'name':'Gi0/1','vlan':40,'state':'down'}]},")
cmd("]")
blank()

pause()

section("7.2 — Common Queries")

explain("Q1 — All interface names that are 'down':")
blank()
cmd("down = [(d['hostname'], i['name'])")
cmd("        for d in inventory")
cmd("        for i in d['interfaces']")
cmd("        if i['state'] == 'down']")
down = [(d["hostname"], i["name"])
        for d in inventory
        for i in d["interfaces"]
        if i["state"] == "down"]
cmd("print(down)")
out(down)
blank()

pause()

explain("Q2 — Count of down interfaces per device:")
blank()
cmd("down_count = {")
cmd("    d['hostname']: sum(1 for i in d['interfaces'] if i['state'] == 'down')")
cmd("    for d in inventory")
cmd("}")
down_count = {
    d["hostname"]: sum(1 for i in d["interfaces"] if i["state"] == "down")
    for d in inventory
}
cmd("print(down_count)")
out(down_count)
blank()

pause()

explain("Q3 — Devices with at least one down interface:")
blank()
cmd("has_down = [d['hostname'] for d in inventory")
cmd("            if any(i['state'] == 'down' for i in d['interfaces'])]")
has_down = [d["hostname"] for d in inventory
            if any(i["state"] == "down" for i in d["interfaces"])]
cmd("print(has_down)")
out(has_down)
blank()

pause()

explain("Q4 — Devices where ALL interfaces are up:")
blank()
cmd("all_up = [d['hostname'] for d in inventory")
cmd("          if all(i['state'] == 'up' for i in d['interfaces'])]")
all_up = [d["hostname"] for d in inventory
          if all(i["state"] == "up" for i in d["interfaces"])]
cmd("print(all_up)")
out(all_up)
blank()

pause()

explain("Q5 — All VLANs in use across all devices:")
blank()
cmd("all_vlans = sorted(set(")
cmd("    i['vlan']")
cmd("    for d in inventory")
cmd("    for i in d['interfaces']")
cmd("))")
all_vlans = sorted(set(i["vlan"] for d in inventory for i in d["interfaces"]))
cmd("print(all_vlans)")
out(all_vlans)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Building Nested Structures from Flat Data
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Building Nested Structures from Flat Data")

section("8.1 — Flat to Nested")

explain("Real data often arrives flat — one row per record.")
explain("IaC needs it nested — grouped by device or site.")
blank()

flat = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/0", "vlan": 10},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/1", "vlan": 20},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "iface": "Gi0/2", "vlan": 30},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/0", "vlan": 10},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "iface": "Gi0/1", "vlan": 20},
]
cmd("flat = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'iface': 'Gi0/0', 'vlan': 10},")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'iface': 'Gi0/1', 'vlan': 20},")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'iface': 'Gi0/2', 'vlan': 30},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'iface': 'Gi0/0', 'vlan': 10},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'iface': 'Gi0/1', 'vlan': 20},")
cmd("]")
blank()

pause()

explain("Build nested: hostname → {platform, interfaces: [...]}")
blank()
cmd("nested = {}")
nested = {}
cmd("for row in flat:")
cmd("    h = row['hostname']")
cmd("    nested.setdefault(h, {'platform': row['platform'], 'interfaces': []})")
cmd("    nested[h]['interfaces'].append({'name': row['iface'], 'vlan': row['vlan']})")
for row in flat:
    h = row["hostname"]
    nested.setdefault(h, {"platform": row["platform"], "interfaces": []})
    nested[h]["interfaces"].append({"name": row["iface"], "vlan": row["vlan"]})
cmd("for hostname, cfg in nested.items():")
cmd("    print(hostname, cfg)")
blank()
for hostname, cfg in nested.items():
    out(f"{hostname} {cfg}")
blank()

pause()

section("8.2 — Nested to Flat")

explain("Convert nested back to a flat list of records.")
blank()
cmd("flat_again = [")
cmd("    {'hostname': hostname, 'platform': cfg['platform'],")
cmd("     'iface': iface['name'], 'vlan': iface['vlan']}")
cmd("    for hostname, cfg in nested.items()")
cmd("    for iface in cfg['interfaces']")
cmd("]")
flat_again = [
    {"hostname": hostname, "platform": cfg["platform"],
     "iface": iface["name"], "vlan": iface["vlan"]}
    for hostname, cfg in nested.items()
    for iface in cfg["interfaces"]
]
cmd("for row in flat_again: print(row)")
blank()
for row in flat_again:
    out(row)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Common Pitfalls")

section("9.1 — Shared References in Nested Structures")

explain("The most dangerous pitfall — reusing the same")
explain("inner dict or list across multiple outer containers.")
blank()

cmd("# Wrong — same interface dict reused")
cmd("iface = {'name': 'Gi0/0', 'vlan': 10}")
iface = {"name": "Gi0/0", "vlan": 10}
cmd("devices = [")
cmd("    {'hostname': 'nyc-rtr-01', 'interface': iface},")
cmd("    {'hostname': 'lon-sw-01',  'interface': iface},")
cmd("]")
devices = [
    {"hostname": "nyc-rtr-01", "interface": iface},
    {"hostname": "lon-sw-01",  "interface": iface},
]
cmd("devices[0]['interface']['vlan'] = 99")
devices[0]["interface"]["vlan"] = 99
cmd("print(devices[1]['interface']['vlan'])   # also changed!")
warn(devices[1]["interface"]["vlan"])
blank()

pause()

import copy
cmd("# Fix — deepcopy to make each device independent")
cmd("iface = {'name': 'Gi0/0', 'vlan': 10}")
iface = {"name": "Gi0/0", "vlan": 10}
cmd("import copy")
cmd("devices = [")
cmd("    {'hostname': 'nyc-rtr-01', 'interface': copy.deepcopy(iface)},")
cmd("    {'hostname': 'lon-sw-01',  'interface': copy.deepcopy(iface)},")
cmd("]")
devices = [
    {"hostname": "nyc-rtr-01", "interface": copy.deepcopy(iface)},
    {"hostname": "lon-sw-01",  "interface": copy.deepcopy(iface)},
]
cmd("devices[0]['interface']['vlan'] = 99")
devices[0]["interface"]["vlan"] = 99
cmd("print(devices[1]['interface']['vlan'])   # untouched")
out(devices[1]["interface"]["vlan"])
blank()

pause()

section("9.2 — The Shallow Copy Trap in Nested Structures")

explain(".copy() only copies the outer layer.")
explain("Inner lists and dicts are still shared.")
blank()

device = {
    "hostname":   "nyc-rtr-01",
    "interfaces": [{"name": "Gi0/0", "vlan": 10}],
}
cmd("device = {'hostname': 'nyc-rtr-01',")
cmd("          'interfaces': [{'name': 'Gi0/0', 'vlan': 10}]}")
blank()
cmd("copy_d = device.copy()          # shallow!")
copy_d = device.copy()
cmd("copy_d['hostname'] = 'changed'  # safe — string is outer key")
copy_d["hostname"] = "changed"
cmd("copy_d['interfaces'][0]['vlan'] = 99  # NOT safe — inner list shared!")
copy_d["interfaces"][0]["vlan"] = 99
cmd("print(device['interfaces'][0]['vlan'])   # also changed!")
warn(device["interfaces"][0]["vlan"])
blank()

pause()

device = {
    "hostname":   "nyc-rtr-01",
    "interfaces": [{"name": "Gi0/0", "vlan": 10}],
}
cmd("# Fix — deepcopy for full independence")
cmd("device = {'hostname': 'nyc-rtr-01',")
cmd("          'interfaces': [{'name': 'Gi0/0', 'vlan': 10}]}")
cmd("deep_d = copy.deepcopy(device)")
deep_d = copy.deepcopy(device)
cmd("deep_d['interfaces'][0]['vlan'] = 99")
deep_d["interfaces"][0]["vlan"] = 99
cmd("print(device['interfaces'][0]['vlan'])   # untouched")
out(device["interfaces"][0]["vlan"])
blank()

pause()

section("9.3 — KeyError in Deeply Nested Access")

explain("Accessing a missing key at any level raises KeyError.")
explain("Use .get() with empty container defaults for safe access.")
blank()

device = {"hostname": "nyc-rtr-01"}
cmd("device = {'hostname': 'nyc-rtr-01'}   # no 'bgp' key")
blank()
cmd("# Wrong — KeyError if key missing at any level")
cmd("print(device['bgp']['as_number'])")
blank()
try:
    print(device["bgp"]["as_number"])
except KeyError as e:
    warn(f"KeyError: {e}")
blank()

pause()

cmd("# Safe — chain .get() with empty dict defaults")
cmd("print(device.get('bgp', {}).get('as_number', 'not configured'))")
out(device.get("bgp", {}).get("as_number", "not configured"))
blank()
cmd("# Or check before accessing")
cmd("if 'bgp' in device and 'as_number' in device['bgp']:")
cmd("    print(device['bgp']['as_number'])")
cmd("else:")
cmd("    print('BGP not configured')")
blank()
if "bgp" in device and "as_number" in device["bgp"]:
    out(device["bgp"]["as_number"])
else:
    out("BGP not configured")
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
print(f"  {BOLD}Ch 1{RESET}   What is nesting — references not copies, shared object trap")
print(f"  {BOLD}Ch 2{RESET}   List of lists — access, iterate, filter, flatten")
print(f"  {BOLD}Ch 3{RESET}   List of dicts — sort, filter nested, transform, group")
print(f"  {BOLD}Ch 4{RESET}   Dict of dicts — build, update, query, merge")
print(f"  {BOLD}Ch 5{RESET}   Dict of lists — setdefault, iterate, query across groups")
print(f"  {BOLD}Ch 6{RESET}   Three-level — site→devices→interfaces, navigate, iterate, modify")
print(f"  {BOLD}Ch 7{RESET}   Querying — all/any, count, collect across multiple levels")
print(f"  {BOLD}Ch 8{RESET}   Reshaping — flat to nested, nested to flat")
print(f"  {BOLD}Ch 9{RESET}   Pitfalls — shared refs, shallow copy trap, safe nested access")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  sites, devices, interfaces, VLANs, BGP,")
print(f"  platform groups, config templates.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()