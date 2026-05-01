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
explain("The nested version keeps all interface data attached to its device.")
explain("The flat version requires a separate table and a join to link them.")
explain("Nested structures eliminate that complexity entirely.")
blank()

pause()

section("1.2 — How Python Stores Nested Structures")

explain("Python containers store REFERENCES — not copies.")
explain("A list of dicts holds references to dict objects.")
explain("This is why mutation through one name affects another.")
blank()
explain("When you write lst = [a, a, a], you are not storing three copies of a.")
explain("You are storing three references that all point to the exact same dict.")
explain("Changing that dict through any one reference changes it for all of them.")
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
explain("A comprehension with {} inside evaluates the expression once per iteration.")
explain("Each iteration produces a brand-new, independent dict object.")
explain("Now changing lst[0] does not affect lst[1] or lst[2].")
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
explain("Each inner list is one row of data.")
explain("All inner lists share the same column structure —")
explain("position 0 is name, position 1 is mode, and so on.")
explain("This mirrors CSV data loaded from a file.")
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
explain("interfaces[0]       → the whole first row.")
explain("interfaces[0][0]    → row 0, column 0 → interface name.")
explain("interfaces[2][1]    → row 2, column 1 → mode ('trunk').")
explain("interfaces[-1][-1]  → last row, last column → state of Gi0/3.")
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
explain("Each iteration yields one inner list — one row of interface data.")
explain("The row variable is itself a list you can index or unpack.")
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
explain("Python assigns the four items to four variables in one step.")
explain("This is far more readable than row[0], row[1], row[2], row[3].")
explain("The !s in {vlan!s} converts None to the string 'None' cleanly.")
explain("If any row has a different number of items, Python raises ValueError.")
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
explain("A list comprehension extracts one field from every row.")
explain("row[0] picks the first column (name) from every row.")
explain("row[3] picks the fourth column (state) from every row.")
explain("This is the equivalent of selecting a column in a database query.")
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
explain("row[3] is the state column — we keep only rows where it equals 'up'.")
explain("The full row dict is preserved in the result, not just the state.")
explain("This is equivalent to a SQL WHERE clause on a table.")
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
explain("Combine filtering and extraction in one comprehension.")
explain("Only 'up' interfaces pass the filter; row[0] extracts their names.")
explain("Gi0/2 is excluded because its state is 'down'.")
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
explain("Each site has its own VLAN list — we want one combined list.")
explain("The nested comprehension visits every sublist and every item in it.")
explain("After flattening we deduplicate with set() and sort for clean output.")
blank()

site_vlans = [
    [10, 20, 30],
    [10, 40],
    [20, 30, 50],
]
cmd("site_vlans = [[10,20,30], [10,40], [20,30,50]]")
blank()
explain("Nested comprehension: 'for sublist in site_vlans' is the outer loop,")
explain("'for v in sublist' is the inner loop, 'v' is what gets collected.")
explain("This is equivalent to two nested for loops with an append.")
blank()
cmd("all_vlans = [v for sublist in site_vlans for v in sublist]")
all_vlans = [v for sublist in site_vlans for v in sublist]
cmd("print(all_vlans)")
out(all_vlans)
blank()
explain("all_vlans still has duplicates (10 appears twice, 20 and 30 also).")
explain("set() removes duplicates; sorted() puts them in ascending order.")
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

explain("sorted() with a key= function works on any field in each dict.")
explain("The key function is called once per item and its return value")
explain("is what Python compares to determine the sort order.")
blank()

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
explain("lambda d: d['hostname'] extracts the hostname string from each dict.")
explain("sorted() compares those strings alphabetically.")
explain("sorted() returns a new list — inventory itself is not modified.")
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
explain("len(d['vlans']) returns the VLAN count for each device.")
explain("reverse=True flips the order — most VLANs first.")
explain("ams-rtr-02 has 4 VLANs and comes first; lon-sw-01 has 2 and comes last.")
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
explain("d['vlans'] is a list — '20 in d[\"vlans\"]' checks membership in that list.")
explain("This is an O(n) scan of the inner VLAN list for each device.")
explain("For very large VLAN lists, convert to a set first for O(1) lookup.")
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
explain("all(v < 40 for v in d['vlans']) is True only if every VLAN in the")
explain("device's list is below 40. If any single VLAN is >= 40, the device")
explain("is excluded. sin-fw-01 has VLANs 30, 40, 50 — 40 and 50 fail,")
explain("so sin-fw-01 is excluded. ams-rtr-02 has VLAN 40 — also excluded.")
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
explain("The comprehension iterates inventory and builds a new dict for each device.")
explain("We pick and reshape the fields we want — not just copying the whole dict.")
explain("'hostname'.upper() normalises casing; len(d['vlans']) summarises the list.")
explain("The original inventory is not modified — we are producing a new structure.")
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
explain("This converts a flat list of dicts into a nested dict-of-lists structure.")
explain("The first time a platform appears, .setdefault() creates an empty list.")
explain("Every subsequent device on that platform is appended to the existing list.")
explain("The output maps each platform to its list of hostnames — ready for")
explain("platform-scoped operations like bulk config pushes.")
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
explain("The outer dict is indexed by hostname — a natural unique identifier.")
explain("Each value is an inner dict holding all config for that device.")
explain("This structure is ideal when you frequently need 'give me everything")
explain("about nyc-rtr-01' — one key lookup returns the full config.")
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

explain("Access patterns:")
blank()
explain("devices['nyc-rtr-01']          → the inner dict for nyc-rtr-01.")
explain("devices['nyc-rtr-01']['ip']    → two levels deep to the IP address.")
explain("devices['sin-fw-01']['vlans']  → the inner list of VLANs for sin-fw-01.")
blank()
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
explain("devices['lon-sw-01'] returns the inner dict object.")
explain("['status'] = 'up' then modifies that inner dict in place.")
explain("The outer dict is not touched — only the inner value changes.")
blank()
cmd("devices['lon-sw-01']['status'] = 'up'")
devices["lon-sw-01"]["status"] = "up"
cmd("print(devices['lon-sw-01'])")
out(devices["lon-sw-01"])
blank()

pause()

explain("Add a new key to every nested dict:")
blank()
explain("devices.items() yields (hostname, cfg) pairs.")
explain("We modify cfg directly — no need to write back to the outer dict.")
explain("cfg IS the inner dict object; modifying it modifies devices in place.")
explain("After the loop, every device has a 'vendor' key.")
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
explain(".pop('vendor', None) removes 'vendor' if present; returns None if not.")
explain("The None default prevents KeyError when a device lacks the key.")
explain("We iterate .values() because we don't need the hostname here.")
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
explain("devices.items() gives (hostname, cfg) pairs.")
explain("We filter on cfg['status'] and collect the hostname (h) when it matches.")
explain("The result is a plain list of hostnames — not the full dicts.")
blank()
cmd("up_hosts = [h for h, cfg in devices.items() if cfg['status'] == 'up']")
up_hosts = [h for h, cfg in devices.items() if cfg["status"] == "up"]
cmd("print(up_hosts)")
out(up_hosts)
blank()

pause()

explain("Build a filtered sub-dict — only 'up' devices:")
blank()
explain("A dict comprehension where h becomes the key and cfg the value.")
explain("Only pairs where cfg['status'] == 'up' are included.")
explain("The result is a new dict of dicts — a subset of the original.")
explain("The inner cfg dicts are NOT copied — they are the same objects.")
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
explain("cfg['vlans'] is a list — 'in' performs a linear scan of that list.")
explain("Only hostnames whose VLAN list contains 10 are collected.")
explain("sin-fw-01 has vlans [30, 40, 50] — 10 is not there, so it is excluded.")
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
explain("{**site_a, **site_b} unpacks both dicts into a new one.")
explain("Keys in site_b overwrite matching keys from site_a.")
explain("lon-sw-01 exists in both — site_b's version (status: 'up') wins.")
explain("nyc-rtr-01 is only in site_a — it is included unchanged.")
explain("sin-fw-01 is only in site_b — it is added as a new entry.")
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
explain("The input is a flat list of (site, vlan) tuples.")
explain("We want to transform this into site → [vlan, vlan, ...] mappings.")
explain("The first time a site appears, .setdefault() creates an empty list.")
explain("Every tuple for that site appends its VLAN to the same list.")
explain("This is the canonical Python pattern for building a dict of lists.")
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
explain("site_vlans.items() yields (site, vlans) pairs.")
explain("len(vlans) tells you how many VLANs each site has.")
explain("This is the standard pattern for producing per-site summaries.")
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
explain("'10 in vlans' scans each site's VLAN list for the value 10.")
explain("Only sites whose list contains 10 pass the filter.")
explain("SIN does not have VLAN 10 — its list starts at 30.")
blank()
cmd("has_vlan10 = [site for site, vlans in site_vlans.items() if 10 in vlans]")
has_vlan10 = [site for site, vlans in site_vlans.items() if 10 in vlans]
cmd("print(has_vlan10)")
out(has_vlan10)
blank()

pause()

explain("Find all unique VLANs across all sites:")
blank()
explain("site_vlans.values() yields each VLAN list.")
explain("The inner 'for v in vlans' iterates every item in each list.")
explain("set() removes duplicates that appear in multiple sites.")
explain("sorted() puts them in ascending numeric order.")
explain("This gives you the complete network-wide VLAN inventory.")
blank()
cmd("all_vlans = sorted(set(v for vlans in site_vlans.values() for v in vlans))")
all_vlans = sorted(set(v for vlans in site_vlans.values() for v in vlans))
cmd("print(all_vlans)")
out(all_vlans)
blank()

pause()

explain("Find sites that share VLAN 10 and VLAN 20:")
blank()
explain("Both conditions must be True — 'and' requires each site to have")
explain("both VLAN 10 and VLAN 20 in its list.")
explain("SIN has neither, so it is excluded. NYC and LON both have 10 and 20.")
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
explain("Level 1: network — dict keyed by site name (NYC, LON).")
explain("Level 2: devices — list of device dicts inside each site.")
explain("Level 3: interfaces — list of interface dicts inside each device.")
explain("This mirrors how Ansible group_vars and host_vars nest in real projects.")
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
explain("network['NYC']['region']                         → level 1 then level 2 key.")
explain("network['NYC']['devices'][0]['hostname']         → level 3 via list index 0.")
explain("network['NYC']['devices'][0]['interfaces'][1]['vlan'] → level 4: VLAN on Gi0/1.")
explain("network['LON']['devices'][0]['interfaces'][0]['state'] → first LON interface state.")
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
explain("Three nested for loops — one per level.")
explain("The outer loop visits sites; the middle loop visits devices in each site;")
explain("the inner loop visits interfaces on each device.")
explain("Each iteration of the innermost loop has access to all three levels —")
explain("site name, device hostname, and interface details — all in scope.")
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
explain("A nested comprehension with three for clauses and one if clause.")
explain("Each for clause corresponds to one level of the structure.")
explain("The result is a list of tuples: (site, hostname, interface_name).")
explain("This gives you a complete picture of every fault across your network.")
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
explain("any(iface['vlan'] == 10 for iface in device['interfaces']) returns True")
explain("if at least one interface on this device carries VLAN 10.")
explain("network.values() skips the site names — we only need device lists here.")
explain("The result is a flat list of hostnames regardless of which site they are in.")
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
explain("Three nested loops reach the innermost interface dicts.")
explain("iface IS the inner dict object — assigning to iface['state']")
explain("modifies the dict inside the network structure directly.")
explain("No copy, no write-back needed — mutation propagates automatically.")
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
explain("We only need two loops here — site and device.")
explain("device is a reference to the dict inside network, so adding")
explain("device['vendor'] = 'Cisco' modifies the structure in place.")
explain("After the loop, every device at every site has a 'vendor' key.")
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
explain("Each 'for' clause in a comprehension corresponds to one level of nesting.")
explain("The 'if' clause at the end filters across all levels simultaneously.")
explain("When logic is too complex for one line, always use a nested for loop.")
explain("Readability matters more than brevity — a clear loop beats a cryptic one-liner.")
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
explain("Two for clauses: outer iterates devices, inner iterates interfaces.")
explain("The if clause filters on iface['state'].")
explain("We collect a (hostname, interface_name) tuple for each match.")
explain("Result gives us every fault location in one flat list.")
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
explain("A dict comprehension — one key-value pair per device.")
explain("The key is the hostname; the value is a count of down interfaces.")
explain("sum(1 for i in ... if ...) counts matching items without building a list.")
explain("lon-sw-01 has 0 down interfaces; nyc-rtr-01 has 1; sin-fw-01 has 1.")
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
explain("any() short-circuits — it stops as soon as it finds one 'down' interface.")
explain("This is more efficient than counting all down interfaces when you only")
explain("need to know whether at least one exists.")
explain("lon-sw-01 has no down interfaces so it is excluded.")
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
explain("all() short-circuits — it stops as soon as it finds one non-'up' interface.")
explain("A device only qualifies if every single interface passes the check.")
explain("nyc-rtr-01 has Gi0/1 as 'down' so it fails; lon-sw-01 passes.")
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
explain("Two for clauses flatten the nested structure:")
explain("  'for d in inventory'        → visits each device.")
explain("  'for i in d['interfaces']'  → visits each interface on that device.")
explain("set() removes duplicates (VLAN 10 appears on multiple devices).")
explain("sorted() gives a clean ascending list of the unique VLAN IDs in use.")
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
explain("APIs, databases, and CSV files commonly return one row per interface.")
explain("Every row repeats the hostname and platform even though they belong")
explain("to the same device — this is the unnormalised/flat form.")
explain("IaC templates expect nested form: one device entry with all its interfaces.")
explain("We use .setdefault() to build the nested structure in a single pass.")
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
explain("For each flat row:")
explain("  1. Extract the hostname as the outer key.")
explain("  2. .setdefault() creates the device entry the first time we see it.")
explain("     The default value is a dict with platform and an empty interfaces list.")
explain("  3. We then append the interface dict to that device's interfaces list.")
explain("nyc-rtr-01 appears three times — one entry is created, three interfaces added.")
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
explain("The reverse operation — take the nested structure and produce one")
explain("row per interface, with the hostname and platform repeated on each row.")
explain("Two for clauses in the comprehension unwind two levels of nesting.")
explain("Each combination of (hostname, interface) becomes one flat dict.")
explain("This is useful for exporting to CSV, feeding a database, or diff-checking.")
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
explain("Both devices share the exact same iface dict object.")
explain("There is only one dict in memory — two references point to it.")
explain("Changing iface['vlan'] through devices[0] also changes devices[1]")
explain("because they are not two copies — they are two names for one object.")
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
explain("  ↑ WARNING: both devices now show VLAN 99 — we only intended to change one.")
blank()

pause()

import copy
explain("The fix: deepcopy() before inserting into each container.")
explain("deepcopy() recursively duplicates every nested object.")
explain("Now each device has its own independent iface dict.")
explain("Changing one does not affect the other.")
blank()
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
explain("  → 10, not 99 — the deepcopy made each iface independent.")
blank()

pause()

section("9.2 — The Shallow Copy Trap in Nested Structures")

explain(".copy() only copies the outer layer.")
explain("Inner lists and dicts are still shared.")
blank()
explain("device.copy() creates a new outer dict.")
explain("But 'interfaces' value is a list — that list is NOT copied.")
explain("Both device and copy_d['interfaces'] point to the same list object.")
explain("Changing copy_d['hostname'] is safe — strings are immutable.")
explain("But copy_d['interfaces'][0]['vlan'] = 99 mutates the shared inner list.")
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
explain("  ↑ WARNING: device was unexpectedly mutated through the shallow copy.")
blank()

pause()

explain("Use deepcopy() whenever the structure has nested mutable objects.")
explain("deepcopy() walks the entire object graph and copies every container.")
explain("After deepcopy, device and deep_d share no objects — fully independent.")
blank()
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
explain("  → 10, not 99 — deepcopy fully insulated device from the change.")
blank()

pause()

section("9.3 — KeyError in Deeply Nested Access")

explain("Accessing a missing key at any level raises KeyError.")
explain("Use .get() with empty container defaults for safe access.")
blank()
explain("When you chain multiple [] accesses, a missing key at ANY level crashes.")
explain("device['bgp'] raises KeyError immediately — we never reach 'as_number'.")
explain("The traceback only tells you which key was missing, not which level.")
explain("Use .get() with {} as the default at every level to descend safely.")
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

explain("Safe chaining with .get():")
explain("device.get('bgp', {}) returns {} if 'bgp' is missing.")
explain("{}.get('as_number', 'not configured') then returns the fallback string.")
explain("No KeyError, no crash — the default propagates cleanly up the chain.")
blank()
cmd("# Safe — chain .get() with empty dict defaults")
cmd("print(device.get('bgp', {}).get('as_number', 'not configured'))")
out(device.get("bgp", {}).get("as_number", "not configured"))
blank()
explain("Alternative: check with 'in' before accessing:")
explain("This is more verbose but makes the logic explicit and easy to debug.")
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