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
explain("Use {} with no contents to create an empty dict.")
explain("You can confirm it is a dict by calling type().")
explain("len() returns 0 because there are no key-value pairs yet.")
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
explain("Each line inside the braces is one key-value pair.")
explain("The key is a string on the left of the colon.")
explain("The value is on the right — also strings here.")
explain("Trailing commas after the last pair are allowed and keep diffs clean.")
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
explain("'name' maps to a string — the interface identifier.")
explain("'vlan' maps to an int — VLAN IDs are numbers, not strings.")
explain("'enabled' maps to a bool — True/False is cleaner than 'yes'/'no'.")
explain("'peers' maps to a list — one interface can connect to multiple peers.")
explain("Mixing value types in one dict is completely normal.")
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
explain("String keys are the most common — human-readable field names.")
explain("Int keys work when you naturally index by number (e.g. VLAN ID).")
explain("Tuple keys are useful for composite lookups like (site, device_id).")
explain("Lists are mutable so Python cannot hash them — they are forbidden as keys.")
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
explain("    — just hostnames, no extra fields per item.")
blank()
explain("  Use a DICT when each item has named fields:")
explain("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
explain("    — multiple attributes that belong to one thing.")
blank()
explain("  Rule of thumb: if you catch yourself writing parallel lists")
explain("  (one list of hostnames, another of IPs), use a list of dicts instead.")
blank()

pause()

explain("Length — how many key-value pairs:")
blank()
explain("len() on a dict returns the number of keys.")
explain("This is useful for sanity-checking config size or inventory counts.")
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
explain("d['key'] is the direct lookup syntax.")
explain("Python hashes the key and retrieves the value in O(1) time —")
explain("it does not scan through the dict looking for a match.")
explain("Use this when you are certain the key exists.")
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
explain("'vendor' was never added to this dict.")
explain("Python raises KeyError with the missing key name.")
explain("In automation scripts this crashes the run — always handle it.")
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
explain("Use .get() whenever a key might be missing — for example when")
explain("reading device data loaded from external YAML or JSON where")
explain("not every device has the same fields filled in.")
blank()

cmd("print(device.get('hostname'))")
out(device.get("hostname"))
blank()
explain("'hostname' exists so .get() returns its value normally.")
blank()
cmd("print(device.get('vendor'))")
out(device.get("vendor"))
blank()
explain("'vendor' is missing — .get() returns None instead of crashing.")
blank()
cmd("print(device.get('vendor', 'Cisco'))")
out(device.get("vendor", "Cisco"))
blank()
explain("The second argument is the fallback value.")
explain("'Cisco' is returned because 'vendor' is absent.")
explain("The dict itself is NOT modified — no key is added.")
blank()

pause()

explain("Practical use — safe access in a loop:")
blank()
explain("inventory has three dicts, but only one has a 'vendor' key.")
explain("Without .get() the loop would crash on the first missing 'vendor'.")
explain("With .get('platform', 'UNKNOWN') we get a safe fallback.")
explain("sin-fw-01 has no 'platform' key, so it prints UNKNOWN.")
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
explain("site contains a 'router' key whose value is another dict.")
explain("That inner dict contains a 'bgp' key with yet another dict.")
explain("Each [] goes one level deeper into the structure.")
explain("This mirrors real Ansible/Nornir host_vars that nest by feature.")
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

explain("Accessing each level of nesting:")
blank()
explain("site['name']                          — top level, returns a string.")
explain("site['router']['hostname']            — two levels deep.")
explain("site['router']['bgp']['as_number']    — three levels deep.")
explain("site['router']['bgp']['neighbors'][0] — three levels then list index.")
blank()
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
explain("Chain .get() calls to safely descend into nested structures.")
explain("Each .get() uses {} as the fallback so the next .get() has")
explain("something to call against, rather than crashing on None.")
explain("If 'firewall' does not exist, .get('firewall', {}) returns {}.")
explain("Calling .get('ip', 'N/A') on {} then returns 'N/A' safely.")
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

explain("Use 'in' to test whether a key exists before accessing it.")
explain("This is O(1) — Python checks the hash table, not every key.")
blank()
explain("'in' checks keys only, not values.")
explain("'not in' is just the logical negation — reads naturally in if-statements.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
blank()
cmd("print('hostname' in device)")
out("hostname" in device)
explain("  → True because 'hostname' is a key in device.")
blank()
cmd("print('vendor' in device)")
out("vendor" in device)
explain("  → False because 'vendor' has not been added yet.")
blank()
cmd("print('vendor' not in device)")
out("vendor" not in device)
explain("  → True — equivalent to 'not (\"vendor\" in device)'.")
blank()

pause()

explain("Practical use — add a key only if it does not exist:")
blank()
explain("This pattern prevents overwriting a value that was already set.")
explain("Useful when applying default settings without clobbering site overrides.")
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

explain(".keys()  — a view of all keys in insertion order.")
explain(".values() — a view of all values in insertion order.")
explain(".items()  — a view of (key, value) tuples — the most useful of the three.")
blank()
explain("These return 'view objects', not plain lists.")
explain("A view stays in sync with the dict — if the dict changes, the view reflects it.")
explain("Convert to list when you need indexing or slicing.")
blank()

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
explain("list(device.keys()) gives a plain list you can index with [0], [1:], etc.")
explain("This is handy when you need the first key or a subset of keys.")
blank()
cmd("print(list(device.keys()))")
out(list(device.keys()))
cmd("print(list(device.values()))")
out(list(device.values()))
blank()

pause()

explain("Check if a value exists:")
blank()
explain("'in' on a dict normally checks keys.")
explain("Use 'in device.values()' to search values instead.")
explain("Note: this is O(n) — it scans every value — unlike key lookup.")
blank()
cmd("print('IOS-XE' in device.values())")
out("IOS-XE" in device.values())
explain("  → True because 'IOS-XE' is the value for the 'platform' key.")
blank()
cmd("print('ASA' in device.values())")
out("ASA" in device.values())
explain("  → False — no key in this dict has the value 'ASA'.")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Modifying Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Modifying Dicts")

section("4.1 — Adding and Updating Keys")

explain("Dicts are mutable — you can add, change, or remove keys at any time.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()

explain("Add a new key:")
blank()
explain("Assignment with a key that does not exist creates it.")
explain("The dict grows by one key-value pair.")
blank()
cmd("device['ip'] = '10.0.0.1'")
device["ip"] = "10.0.0.1"
cmd("print(device)")
out(device)
blank()

pause()

explain("Update an existing key:")
blank()
explain("Assignment with an existing key replaces its value in place.")
explain("The number of keys stays the same — no duplicate is created.")
blank()
cmd("device['hostname'] = 'nyc-rtr-01-core'")
device["hostname"] = "nyc-rtr-01-core"
cmd("print(device)")
out(device)
blank()

pause()

explain("Add multiple keys at once with .update():")
blank()
explain(".update() merges another dict (or keyword args) into this dict.")
explain("Existing keys are overwritten; new keys are added.")
explain("This is cleaner than three separate assignment lines.")
blank()
cmd("device.update({'vendor': 'Cisco', 'status': 'up', 'vlans': [10, 20]})")
device.update({"vendor": "Cisco", "status": "up", "vlans": [10, 20]})
cmd("print(device)")
out(device)
blank()

pause()

section("4.2 — Removing Keys")

explain("Three ways to remove keys: del, .pop(), and .pop() with a default.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'ip': '10.0.0.1', 'status': 'up'}")
blank()

explain("del — remove a key:")
blank()
explain("del is a statement, not a method call.")
explain("Use it when you just want the key gone and don't need its value.")
explain("Raises KeyError if the key is missing.")
blank()
cmd("del device['status']")
del device["status"]
cmd("print(device)")
out(device)
blank()

pause()

explain(".pop(key) — remove and return the value:")
blank()
explain(".pop() removes the key AND returns the value in one step.")
explain("Useful when you need to both extract and remove a field —")
explain("for example, popping 'password' before logging a config dict.")
explain("Raises KeyError if the key is missing (same risk as del).")
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
explain("The second argument is returned if the key does not exist.")
explain("Use this when the key's presence is optional.")
explain("'vendor' was never in device, so 'not set' is returned.")
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
explain("This is the cleanest way to initialise a key with a default")
explain("without accidentally overwriting a value that was already set.")
explain("Commonly used to initialise an empty list before appending to it.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()
explain("'status' does not exist yet, so it is added with the value 'up'.")
blank()
cmd("device.setdefault('status', 'up')")
device.setdefault("status", "up")
cmd("print(device)")
out(device)
blank()

pause()

explain("'status' already exists with value 'up'.")
explain(".setdefault() sees it and does nothing — 'up' is NOT replaced by 'down'.")
explain("This is the key difference from a plain assignment.")
blank()
cmd("device.setdefault('status', 'down')   # key exists — not overwritten")
device.setdefault("status", "down")
cmd("print(device['status'])")
out(device["status"])
blank()

pause()

explain("Practical use — build a dict of lists safely:")
blank()
explain("We want to group hostnames by platform.")
explain("The first time we see a platform, the key does not exist yet.")
explain(".setdefault(platform, []) creates an empty list for that platform.")
explain("On subsequent devices with the same platform, the list already")
explain("exists so .setdefault() leaves it alone and we just append.")
explain("This avoids an if/else check before every append.")
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
explain("'for key in device' is equivalent to 'for key in device.keys()'.")
explain("Keys are yielded in insertion order (Python 3.7+).")
explain("Use this when you only need the key names, not the values.")
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
explain(".items() unpacks each pair into two variables in one step.")
explain("This is more readable than device[key] inside the loop.")
explain("It is the standard pattern for generating config from a dict.")
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
explain("Each key-value pair maps to one config line.")
explain("This pattern scales to any size dict without changing the loop.")
explain("Real IaC tools like Jinja2 do exactly this under the hood.")
blank()
cmd("for key, value in device.items():")
cmd("    print(f'  set device {key} {value}')")
blank()
for key, value in device.items():
    out(f"  set device {key} {value}")
blank()

pause()

section("5.3 — Iterating Values Only")

explain("Use .values() when you only care about the values, not their keys.")
explain("A common use case: checking if any value meets a condition,")
explain("or building a list of all values from a column of data.")
blank()
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
explain("Each element of the list is its own dict.")
explain("The outer loop moves through devices; inside, we access fields by key.")
explain("String formatting with {:<15} left-aligns text in a column of width 15,")
explain("making the output line up neatly like a table.")
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
explain("This is the most explicit approach — easy to read and debug.")
explain("Each assignment is a separate, traceable step.")
explain("Use this when building logic is too complex for a comprehension.")
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
explain("Two separate lists — one of hostnames, one of IPs.")
explain("zip() pairs them up element by element: ('nyc-rtr-01', '10.0.0.1'), etc.")
explain("The loop unpacks each pair and assigns it as a key-value entry.")
explain("The result maps each hostname directly to its IP for O(1) lookup.")
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
explain("dict() can accept an iterable of (key, value) pairs.")
explain("zip(hostnames, ips) produces exactly that — (key, value) tuples.")
explain("dict(zip(...)) combines both into one expression.")
explain("Same result as the loop above, but more concise.")
blank()

cmd("ip_map = dict(zip(hostnames, ips))")
ip_map = dict(zip(hostnames, ips))
cmd("print(ip_map)")
out(ip_map)
blank()

pause()

explain("dict() constructor from keyword arguments:")
blank()
explain("You can also pass keyword arguments directly to dict().")
explain("Each keyword becomes a key, each argument value becomes a value.")
explain("Limitation: keys must be valid Python identifiers (no hyphens).")
explain("For keys like 'as-number' or 'ios-xe', use {} literals instead.")
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
explain("A dict comprehension is a single-pass loop that builds the dict")
explain("in one expression. The left side of the colon is the key,")
explain("the right side is the value, and the for clause drives the loop.")
explain("They are fast, readable, and the preferred style in IaC scripts.")
blank()

pause()

explain("Build hostname → ip mapping:")
blank()
explain("For each device dict d in inventory, use d['hostname'] as the key")
explain("and d['ip'] as the value. Result is a flat hostname-to-IP lookup.")
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
explain("Transform the value on the fly — .upper() is called inside the comprehension.")
explain("The key stays as-is; only the value is processed.")
explain("Any expression that produces a value can go on the right side of the colon.")
blank()
cmd("platform_map = {d['hostname']: d['platform'].upper() for d in inventory}")
platform_map = {d["hostname"]: d["platform"].upper() for d in inventory}
cmd("print(platform_map)")
out(platform_map)
blank()

pause()

explain("With a filter — only IOS-XE devices:")
blank()
explain("Add 'if condition' after the for clause to filter items.")
explain("Only devices where platform == 'IOS-XE' contribute to the result.")
explain("This is equivalent to putting an if-statement inside a regular loop.")
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
explain("Iterate over .items() to get (key, value) pairs, then swap them.")
explain("This creates a reverse lookup: given an IP, find the hostname.")
explain("Only works correctly if values are unique — otherwise some entries")
explain("will be silently dropped since a key can only appear once.")
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
explain("The outer dict is keyed by site name — a natural label.")
explain("Each site's value is an inner dict with all its properties.")
explain("This mirrors Ansible group_vars or Nornir inventory structure.")
explain("You can add any number of inner keys without changing the outer shape.")
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

explain("Access patterns for nested dicts:")
blank()
explain("sites['NYC']           → returns the entire inner dict for NYC.")
explain("sites['NYC']['router'] → goes two levels deep to the router name.")
explain("sites['LON']['vlans']  → returns the list of VLANs for London.")
blank()
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
explain("sites.items() yields (site_name, config) pairs.")
explain("The loop unpacks both in one line — no need to access by index.")
explain("This is the standard way to generate per-site config output.")
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
explain("The outer dict is keyed by platform name.")
explain("Each value is a list of hostnames on that platform.")
explain("This is the natural output shape when you group a flat inventory.")
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

explain("Access the list for a platform, or a specific device in that list:")
blank()
explain("platform_groups['IOS-XE']    → the entire list for IOS-XE.")
explain("platform_groups['NX-OS'][0]  → the first NX-OS device by index.")
blank()
cmd("print(platform_groups['IOS-XE'])")
out(platform_groups["IOS-XE"])
cmd("print(platform_groups['NX-OS'][0])")
out(platform_groups["NX-OS"][0])
blank()

pause()

explain("Iterate over groups:")
blank()
explain("The outer loop iterates platforms and their device lists.")
explain("len(devices) tells you how many devices are on that platform.")
explain("The inner loop prints each hostname under its platform header.")
explain("This is useful for generating platform-scoped config sections.")
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
explain("The input is a flat list — all devices at the same level.")
explain("We will transform it into two different nested shapes:")
explain("  1. A hostname-keyed lookup dict (fast random access).")
explain("  2. A platform-grouped dict of lists (for batch operations).")
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
explain("d['hostname'] becomes the key; the entire dict d becomes the value.")
explain("Now any field for any device is one lookup away.")
explain("device_map['nyc-rtr-01']['ip'] is O(1) — no scanning required.")
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
explain("We iterate the flat list and build a platform → [hostnames] dict.")
explain("The first time a platform appears, .setdefault creates an empty list.")
explain("On every visit we append the hostname to that platform's list.")
explain("The result groups all hostnames by their platform in one pass.")
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
explain("In IaC, merging is the foundation of the 'defaults + overrides' pattern.")
explain("You define a base config, then each site overrides only what differs.")
explain("The right side always wins when the same key appears in both dicts.")
blank()

defaults = {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"}
site_cfg  = {"hostname": "nyc-rtr-01", "ntp": "10.1.0.100"}
cmd("defaults = {'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
cmd("site_cfg  = {'hostname': 'nyc-rtr-01', 'ntp': '10.1.0.100'}")
blank()

pause()

explain("Method 1 — .update() — site_cfg values win:")
blank()
explain("Start with a copy of defaults so we do not modify the original.")
explain(".update() writes all of site_cfg into merged.")
explain("'ntp' exists in both — site_cfg's value '10.1.0.100' overwrites defaults.")
explain("'hostname' is new — it is added from site_cfg.")
explain("'dns' and 'domain' stay from defaults since site_cfg does not have them.")
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
explain("{**defaults} unpacks all key-value pairs from defaults into a new dict.")
explain("{**defaults, **site_cfg} merges both — site_cfg keys overwrite defaults.")
explain("This creates a brand-new dict without touching either source.")
explain("Cleaner than method 1 because no .copy() step is needed.")
blank()
cmd("merged = {**defaults, **site_cfg}")
merged = {**defaults, **site_cfg}
cmd("print(merged)")
out(merged)
blank()

pause()

explain("Method 3 — | operator (Python 3.9+):")
blank()
explain("The | operator merges two dicts into a new one — rightmost wins.")
explain("Equivalent to {**a, **b} but reads more naturally.")
explain("Use |= to merge in place (like += for lists).")
explain("Requires Python 3.9 or newer.")
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
explain("A shallow copy duplicates the top-level dict.")
explain("All values are copied by reference, not by value.")
explain("For flat dicts (only string/int/bool values) this is fine — those")
explain("types are immutable, so a reference and a copy behave the same.")
explain("For nested dicts or lists as values, shallow copy is dangerous.")
blank()

flat = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("flat      = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
cmd("flat_copy = flat.copy()")
flat_copy = flat.copy()
cmd("flat_copy['hostname'] = 'lon-sw-01'")
flat_copy["hostname"] = "lon-sw-01"
explain("  Changing flat_copy['hostname'] does NOT affect flat.")
explain("  Strings are immutable — each dict holds its own reference.")
blank()
cmd("print(flat)")
out(flat)
cmd("print(flat_copy)")
out(flat_copy)
blank()

pause()

explain("Nested dict — must use deepcopy:")
blank()
explain("nested has a 'bgp' key whose value is a dict (a mutable object).")
explain("After .copy(), nested and site_copy both point to the SAME bgp dict.")
explain("Changing site_copy['bgp']['as_number'] therefore also changes nested.")
explain("copy.deepcopy() recursively copies every nested object,")
explain("so the two dicts are fully independent from each other.")
blank()
import copy
nested = {"hostname": "nyc-rtr-01", "bgp": {"as_number": 65001, "neighbors": ["10.0.0.2"]}}
cmd("import copy")
cmd("nested = {'hostname': 'nyc-rtr-01', 'bgp': {'as_number': 65001, 'neighbors': ['10.0.0.2']}}")
cmd("deep   = copy.deepcopy(nested)")
deep = copy.deepcopy(nested)
cmd("deep['bgp']['neighbors'].append('10.0.0.3')")
deep["bgp"]["neighbors"].append("10.0.0.3")
cmd("print(nested['bgp'])                  # also changed!")
warn(nested["bgp"])
explain("  ↑ WARNING: shallow copy would have mutated nested here too.")
explain("  With deepcopy, nested is unchanged — only deep was modified.")
blank()
cmd("deep_copy = copy.deepcopy(nested)     # safe")
nested["bgp"]["as_number"] = 65001
deep_copy = copy.deepcopy(nested)
cmd("deep_copy['bgp']['as_number'] = 65002")
deep_copy["bgp"]["as_number"] = 65002
cmd("print(nested['bgp'])                  # untouched")
out(nested["bgp"])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Common Dict Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Common Dict Patterns")

section("9.1 — Counting Occurrences")

explain("Count how many times each platform appears.")
explain("Start with an empty dict.")
explain("For each device, use .get() to read the current count.")
explain("If the platform is new, .get() returns 0.")
explain("Add 1 and store the result back.")
blank()

inventory = [
    {"hostname": "rtr-01", "platform": "IOS-XE"},
    {"hostname": "sw-01",  "platform": "NX-OS"},
    {"hostname": "rtr-02", "platform": "IOS-XE"},
    {"hostname": "fw-01",  "platform": "ASA"},
    {"hostname": "rtr-03", "platform": "IOS-XE"},
]
cmd("inventory = [")
cmd("    {'hostname': 'rtr-01', 'platform': 'IOS-XE'},")
cmd("    {'hostname': 'sw-01',  'platform': 'NX-OS'},")
cmd("    {'hostname': 'rtr-02', 'platform': 'IOS-XE'},")
cmd("    {'hostname': 'fw-01',  'platform': 'ASA'},")
cmd("    {'hostname': 'rtr-03', 'platform': 'IOS-XE'},")
cmd("]")
blank()

pause()

cmd("counts = {}")
counts = {}
cmd("for d in inventory:")
cmd("    p = d['platform']")
cmd("    counts[p] = counts.get(p, 0) + 1")
for d in inventory:
    p = d["platform"]
    counts[p] = counts.get(p, 0) + 1
cmd("print(counts)")
out(counts)
blank()
explain("IOS-XE appears 3 times, NX-OS once, ASA once.")

pause()

section("9.2 — Grouping by a Field")

explain("Group hostnames by platform.")
explain("Use .setdefault() to create an empty list the first time")
explain("a platform appears, then append to it every time.")
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
explain("Each platform key now maps to a list of its hostnames.")

pause()

section("9.3 — Building a Lookup Dict")

explain("A lookup dict lets you find a device by hostname instantly.")
explain("Without it you would have to scan the whole list every time.")
blank()

cmd("lookup = {}")
lookup = {}
cmd("for d in inventory:")
cmd("    lookup[d['hostname']] = d")
for d in inventory:
    lookup[d["hostname"]] = d
cmd("print(lookup['rtr-01'])")
out(lookup["rtr-01"])
blank()
explain("One key lookup — no loop needed.")
blank()

pause()

explain("Searching without a lookup dict:")
blank()
cmd("for d in inventory:")
cmd("    if d['hostname'] == 'rtr-01':")
cmd("        print(d)")
cmd("        break")
blank()
for d in inventory:
    if d["hostname"] == "rtr-01":
        out(d)
        break
blank()
explain("This works, but scans every device from the start each time.")
explain("With many devices and many searches, a lookup dict is much faster.")

pause()

section("9.4 — Template Config Pattern")

explain("Define shared defaults in a BASE dict.")
explain("Copy BASE for each site, then apply any site-specific changes.")
blank()

BASE = {"ntp": "10.0.0.1", "dns": "8.8.8.8"}
cmd("BASE = {'ntp': '10.0.0.1', 'dns': '8.8.8.8'}")
blank()
cmd("sites = [")
cmd("    {'hostname': 'rtr-01', 'ntp': '10.1.0.1'},")
cmd("    {'hostname': 'rtr-02', 'ntp': None},")
cmd("]")
sites = [
    {"hostname": "rtr-01", "ntp": "10.1.0.1"},
    {"hostname": "rtr-02", "ntp": None},
]
blank()

pause()

cmd("for site in sites:")
cmd("    cfg = dict(BASE)               # fresh copy of defaults")
cmd("    cfg['hostname'] = site['hostname']")
cmd("    if site['ntp']:                # override only if set")
cmd("        cfg['ntp'] = site['ntp']")
cmd("    print(cfg['hostname'], '->', cfg['ntp'])")
blank()
for site in sites:
    cfg = dict(BASE)
    cfg["hostname"] = site["hostname"]
    if site["ntp"]:
        cfg["ntp"] = site["ntp"]
    out(f"{cfg['hostname']} -> {cfg['ntp']}")
blank()
explain("rtr-01 gets its own NTP server.")
explain("rtr-02 keeps the BASE default because ntp is None.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — KeyError")

explain("Accessing a key that does not exist raises KeyError.")
explain("The script crashes immediately.")
explain("Use .get() to avoid this.")
blank()

device = {"hostname": "rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'rtr-01', 'platform': 'IOS-XE'}")
blank()
cmd("print(device['vendor'])   # KeyError — 'vendor' not in dict")
blank()
try:
    print(device["vendor"])
except KeyError as e:
    warn(f"KeyError: {e}")
blank()
cmd("print(device.get('vendor', 'unknown'))   # safe — returns default")
out(device.get("vendor", "unknown"))
blank()

pause()

section("10.2 — Mutating While Iterating")

explain("Never delete keys from a dict while looping over it.")
explain("Python raises RuntimeError to stop you.")
blank()

device = {"hostname": "rtr-01", "platform": "IOS-XE", "debug": True, "tmp": False}
cmd("device = {'hostname': 'rtr-01', 'platform': 'IOS-XE', 'debug': True, 'tmp': False}")
blank()
cmd("# Wrong — crashes with RuntimeError")
cmd("for key in device:")
cmd("    if key in ('debug', 'tmp'):")
cmd("        del device[key]")
blank()
try:
    for key in device:
        if key in ("debug", "tmp"):
            del device[key]
except RuntimeError as e:
    warn(f"RuntimeError: {e}")
blank()

pause()

explain("Fix — loop over a copy of the keys:")
blank()
device = {"hostname": "rtr-01", "platform": "IOS-XE", "debug": True, "tmp": False}
cmd("device = {'hostname': 'rtr-01', 'platform': 'IOS-XE', 'debug': True, 'tmp': False}")
cmd("for key in list(device.keys()):")
cmd("    if key in ('debug', 'tmp'):")
cmd("        del device[key]")
for key in list(device.keys()):
    if key in ("debug", "tmp"):
        del device[key]
cmd("print(device)")
out(device)
blank()
explain("list(device.keys()) takes a snapshot of the keys upfront.")
explain("The loop works on that snapshot — safe to delete from the original.")

pause()

section("10.3 — Shallow Copy Trap")

explain("dict.copy() only copies the top level.")
explain("Nested dicts inside are still shared.")
blank()

device = {"hostname": "rtr-01", "bgp": {"asn": 65001}}
cmd("device    = {'hostname': 'rtr-01', 'bgp': {'asn': 65001}}")
cmd("copy_dev  = device.copy()")
copy_dev = device.copy()
blank()
cmd("copy_dev['bgp']['asn'] = 99999")
copy_dev["bgp"]["asn"] = 99999
cmd("print(device['bgp'])   # also changed!")
warn(device["bgp"])
explain("  ↑ Both dicts share the same inner 'bgp' dict — changing one changes both.")
blank()

pause()

explain("Fix — use copy.deepcopy() for nested dicts:")
blank()
device = {"hostname": "rtr-01", "bgp": {"asn": 65001}}
cmd("device    = {'hostname': 'rtr-01', 'bgp': {'asn': 65001}}")
cmd("deep_dev  = copy.deepcopy(device)")
deep_dev = copy.deepcopy(device)
cmd("deep_dev['bgp']['asn'] = 99999")
deep_dev["bgp"]["asn"] = 99999
cmd("print(device['bgp'])   # untouched")
out(device["bgp"])
explain("  deepcopy makes a completely independent copy — safe to modify.")

pause()

section("10.4 — Key Order Is Preserved (Python 3.7+)")

explain("Dicts remember the order keys were inserted.")
explain("They always come out in that same order.")
blank()

cmd("d = {}")
d = {}
cmd("d['hostname'] = 'rtr-01'")
d["hostname"] = "rtr-01"
cmd("d['platform'] = 'IOS-XE'")
d["platform"] = "IOS-XE"
cmd("d['status']   = 'up'")
d["status"] = "up"
cmd("for k, v in d.items():")
cmd("    print(k, ':', v)")
blank()
for k, v in d.items():
    out(f"{k} : {v}")
blank()
explain("hostname, platform, status — always in insertion order.")
explain("You can rely on this when generating config output.")

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
