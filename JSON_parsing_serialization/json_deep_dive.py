# json_deep_dive.py
# JSON Parsing & Serialization — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

import json
import copy
from datetime import datetime

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
print(f"{BOLD}         JSON PARSING & SERIALIZATION{RESET}")
print(f"{BOLD}         Zero to Expert — Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is JSON and Why It Matters in IaC
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is JSON and Why It Matters in IaC")

section("1.1 — Definition")

explain("JSON — JavaScript Object Notation.")
explain("A text format for representing structured data.")
explain("Human-readable. Language-independent.")
blank()
explain("In Cisco IaC, JSON is everywhere:")
blank()
explain("  — NX-OS, IOS-XE, EOS return 'show' commands as JSON")
explain("  — RESTCONF/NETCONF APIs return JSON payloads")
explain("  — Ansible, Nornir, Netmiko all use JSON")
explain("  — Device inventories, config diffs, audit results")
blank()
explain("Knowing JSON deeply means you can parse any API")
explain("response and produce any payload a device expects.")
blank()

pause()

section("1.2 — JSON Structure")

explain("JSON has six data types:")
blank()
explain("  Object  → { \"key\": value }   ← maps to Python dict")
explain("  Array   → [ value, value ]    ← maps to Python list")
explain("  String  → \"hello\"             ← maps to Python str")
explain("  Number  → 42  or  3.14        ← maps to Python int/float")
explain("  Boolean → true  or  false     ← maps to Python True/False")
explain("  Null    → null                ← maps to Python None")
blank()

pause()

explain("A real Cisco device JSON response looks like this:")
blank()
cmd("json_response = '''")
cmd("{")
cmd("  \"hostname\": \"nyc-rtr-01\",")
cmd("  \"platform\": \"IOS-XE\",")
cmd("  \"version\": \"17.3.4\",")
cmd("  \"uptime_seconds\": 864000,")
cmd("  \"reachable\": true,")
cmd("  \"last_backup\": null,")
cmd("  \"interfaces\": [")
cmd("    {\"name\": \"Gi0/0\", \"vlan\": 10, \"state\": \"up\"},")
cmd("    {\"name\": \"Gi0/1\", \"vlan\": 20, \"state\": \"down\"}")
cmd("  ]")
cmd("}")
cmd("'''")
blank()
explain("Every key is a string in double quotes.")
explain("Values can be any JSON type including nested objects.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — json.loads() and json.dumps()
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "json.loads() and json.dumps()")

section("2.1 — json.loads() — Parse a JSON String")

explain("loads() = 'load string'")
explain("Takes a JSON-formatted STRING and returns a Python object.")
explain("This is what you use when an API returns a response body.")
blank()

json_str = '{"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}'
cmd(f'json_str = \'{json_str}\'')
blank()
cmd("device = json.loads(json_str)")
device = json.loads(json_str)
cmd("print(device)")
out(device)
cmd("print(type(device))")
out(type(device))
cmd("print(device['hostname'])")
out(device["hostname"])
blank()

pause()

explain("Parse a JSON string containing an array:")
blank()
json_array = '[10, 20, 30, 40, 50]'
cmd(f"vlans_str = '{json_array}'")
cmd("vlans = json.loads(vlans_str)")
vlans = json.loads(json_array)
cmd("print(vlans)")
out(vlans)
cmd("print(type(vlans))")
out(type(vlans))
blank()

pause()

section("2.2 — json.dumps() — Serialize to a JSON String")

explain("dumps() = 'dump string'")
explain("Takes a Python object and returns a JSON-formatted STRING.")
explain("This is what you use to build a payload for an API call.")
blank()

device = {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "status":   "up",
    "vlans":    [10, 20, 30],
}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'status': 'up', 'vlans': [10, 20, 30]}")
blank()

cmd("json_str = json.dumps(device)")
json_str = json.dumps(device)
cmd("print(json_str)")
out(json_str)
cmd("print(type(json_str))")
out(type(json_str))
blank()

pause()

explain("Pretty print with indent:")
blank()
cmd("json_pretty = json.dumps(device, indent=2)")
json_pretty = json.dumps(device, indent=2)
cmd("print(json_pretty)")
blank()
for line in json_pretty.splitlines():
    out(line)
blank()

pause()

section("2.3 — load/dump vs loads/dumps")

explain("The four JSON functions — easy to confuse:")
blank()
explain("  json.load(f)       — read from FILE object  → Python")
explain("  json.dump(obj, f)  — write Python           → FILE object")
blank()
explain("  json.loads(s)      — parse JSON STRING      → Python")
explain("  json.dumps(obj)    — serialize Python       → JSON STRING")
blank()
explain("In IaC:")
explain("  API response body  → json.loads()  (it's a string)")
explain("  Reading inventory  → json.load()   (it's a file)")
explain("  Building payload   → json.dumps()  (need a string)")
explain("  Saving inventory   → json.dump()   (writing to file)")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Python ↔ JSON Type Mapping
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Python ↔ JSON Type Mapping")

section("3.1 — The Full Mapping")

explain("Python → JSON:")
blank()
explain("  dict        →  object   { }")
explain("  list, tuple →  array    [ ]")
explain("  str         →  string   \"\"")
explain("  int, float  →  number")
explain("  True        →  true")
explain("  False       →  false")
explain("  None        →  null")
blank()

pause()

python_obj = {
    "hostname": "nyc-rtr-01",
    "vlans":    [10, 20, 30],
    "active":   True,
    "backup":   None,
    "latency":  1.5,
    "port":     22,
}
cmd("python_obj = {")
cmd("    'hostname': 'nyc-rtr-01',")
cmd("    'vlans':    [10, 20, 30],")
cmd("    'active':   True,")
cmd("    'backup':   None,")
cmd("    'latency':  1.5,")
cmd("    'port':     22,")
cmd("}")
cmd("print(json.dumps(python_obj, indent=2))")
blank()
for line in json.dumps(python_obj, indent=2).splitlines():
    out(line)
blank()

pause()

explain("JSON → Python (the reverse):")
blank()
json_in = '{"active": true, "backup": null, "vlans": [10, 20]}'
cmd(f"parsed = json.loads('{json_in}')")
parsed = json.loads(json_in)
cmd("print(parsed)")
out(parsed)
cmd("print(type(parsed['active']))")
out(type(parsed["active"]))
cmd("print(type(parsed['backup']))")
out(type(parsed["backup"]))
blank()

pause()

section("3.2 — Tuples Become Lists")

explain("Python tuples serialize to JSON arrays.")
explain("When you parse them back you get a LIST, not a tuple.")
blank()

data = {"vlans": (10, 20, 30)}
cmd("data = {'vlans': (10, 20, 30)}   # tuple")
cmd("print(type(data['vlans']))")
out(type(data["vlans"]))
blank()

serialized = json.dumps(data)
cmd("serialized = json.dumps(data)")
cmd("parsed = json.loads(serialized)")
parsed = json.loads(serialized)
cmd("print(type(parsed['vlans']))  # list — not tuple!")
out(type(parsed["vlans"]))
cmd("print(parsed['vlans'])")
out(parsed["vlans"])
blank()

pause()

section("3.3 — Dict Keys Are Always Strings in JSON")

explain("JSON object keys MUST be strings.")
explain("If you use int keys in Python they become string keys in JSON.")
blank()

data_int_keys = {10: "vlan10", 20: "vlan20"}
cmd("data = {10: 'vlan10', 20: 'vlan20'}   # int keys")
cmd("serialized = json.dumps(data)")
serialized = json.dumps(data_int_keys)
cmd("print(serialized)")
out(serialized)
blank()

parsed_str_keys = json.loads(serialized)
cmd("parsed = json.loads(serialized)")
cmd("print(parsed)")
out(parsed_str_keys)
cmd("print(type(list(parsed.keys())[0]))   # str — not int!")
out(type(list(parsed_str_keys.keys())[0]))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Navigating Parsed JSON
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Navigating Parsed JSON")

section("4.1 — Accessing Nested Keys")

explain("Chain square brackets to navigate nested JSON.")
blank()

api_response = json.loads('''
{
  "device": {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "bgp": {
      "as_number": 65001,
      "neighbors": ["10.0.0.2", "10.0.0.3"],
      "state": "established"
    }
  },
  "timestamp": "2024-01-15T10:30:00"
}
''')

cmd("api_response = json.loads(response_str)")
blank()
cmd("print(api_response['device']['hostname'])")
out(api_response["device"]["hostname"])
cmd("print(api_response['device']['bgp']['as_number'])")
out(api_response["device"]["bgp"]["as_number"])
cmd("print(api_response['device']['bgp']['neighbors'][0])")
out(api_response["device"]["bgp"]["neighbors"][0])
cmd("print(api_response['timestamp'])")
out(api_response["timestamp"])
blank()

pause()

section("4.2 — Safe Access with .get()")

explain("API responses often have optional fields.")
explain("Use .get() to avoid KeyError on missing keys.")
blank()

cmd("# Safe nested access — chain .get() with {} defaults")
cmd("as_num = api_response.get('device', {}).get('bgp', {}).get('as_number')")
as_num = api_response.get("device", {}).get("bgp", {}).get("as_number")
cmd("print(as_num)")
out(as_num)
blank()

cmd("# Missing key returns None — no error")
cmd("vendor = api_response.get('device', {}).get('vendor', 'unknown')")
vendor = api_response.get("device", {}).get("vendor", "unknown")
cmd("print(vendor)")
out(vendor)
blank()

pause()

section("4.3 — Iterating a JSON Array")

explain("A parsed JSON array is a Python list — iterate normally.")
blank()

interfaces_json = json.loads('''
[
  {"name": "Gi0/0", "vlan": 10, "state": "up"},
  {"name": "Gi0/1", "vlan": 20, "state": "down"},
  {"name": "Gi0/2", "vlan": 30, "state": "up"}
]
''')
cmd("interfaces = json.loads(interfaces_str)")
blank()
cmd("for iface in interfaces:")
cmd("    print(f\"{iface['name']}: vlan={iface['vlan']} state={iface['state']}\")")
blank()
for iface in interfaces_json:
    out(f"{iface['name']}: vlan={iface['vlan']} state={iface['state']}")
blank()

pause()

cmd("# Filter and extract — just like any list of dicts")
cmd("up_ifaces = [i['name'] for i in interfaces if i['state'] == 'up']")
up_ifaces = [i["name"] for i in interfaces_json if i["state"] == "up"]
cmd("print(up_ifaces)")
out(up_ifaces)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Parsing Real Device Output
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Parsing Real Device Output")

section("5.1 — Parsing show version JSON")

explain("NX-OS and IOS-XE can return 'show version' as JSON.")
explain("This is what the response looks like after parsing.")
blank()

show_version = {
    "Cisco-IOS-XE-native:native": {
        "version": {
            "version-string": "17.03.04",
            "platform": "Virtual XE",
            "hostname": "nyc-rtr-01",
            "uptime": "2 weeks, 3 days",
        }
    }
}
cmd("show_version = {  # parsed from API response }")
cmd("    'Cisco-IOS-XE-native:native': {")
cmd("        'version': {")
cmd("            'version-string': '17.03.04',")
cmd("            'platform':       'Virtual XE',")
cmd("            'hostname':       'nyc-rtr-01',")
cmd("            'uptime':         '2 weeks, 3 days',")
cmd("        }")
cmd("    }")
cmd("}")
blank()

pause()

cmd("# Navigate deeply nested response")
cmd("ver = show_version['Cisco-IOS-XE-native:native']['version']")
ver = show_version["Cisco-IOS-XE-native:native"]["version"]
cmd("print(ver['hostname'])")
out(ver["hostname"])
cmd("print(ver['version-string'])")
out(ver["version-string"])
cmd("print(ver['uptime'])")
out(ver["uptime"])
blank()

pause()

section("5.2 — Parsing show interfaces JSON (NX-OS Style)")

explain("NX-OS returns interface data in this structure.")
explain("Parse and extract what you need from the nested response.")
blank()

show_interfaces = {
    "TABLE_interface": {
        "ROW_interface": [
            {
                "interface":       "Ethernet1/1",
                "state":           "up",
                "eth_speed":       "1000 Mb/s",
                "eth_bw":          1000000,
                "vlan":            "10",
                "eth_ip_addr":     "10.0.0.1",
            },
            {
                "interface":       "Ethernet1/2",
                "state":           "down",
                "eth_speed":       "1000 Mb/s",
                "eth_bw":          1000000,
                "vlan":            "20",
                "eth_ip_addr":     "10.0.1.1",
            },
        ]
    }
}
cmd("show_interfaces = {  # NX-OS interface JSON response }")
blank()

cmd("rows = show_interfaces['TABLE_interface']['ROW_interface']")
rows = show_interfaces["TABLE_interface"]["ROW_interface"]
cmd("for iface in rows:")
cmd("    print(f\"{iface['interface']}: {iface['state']} vlan={iface['vlan']}\")")
blank()
for iface in rows:
    out(f"{iface['interface']}: {iface['state']} vlan={iface['vlan']}")
blank()

pause()

explain("Normalize to a standard flat dict — drop vendor specifics:")
blank()
cmd("normalized = [")
cmd("    {")
cmd("        'name':    i['interface'],")
cmd("        'state':   i['state'],")
cmd("        'vlan':    int(i['vlan']),")
cmd("        'ip':      i['eth_ip_addr'],")
cmd("    }")
cmd("    for i in rows")
cmd("]")
normalized = [
    {
        "name":  i["interface"],
        "state": i["state"],
        "vlan":  int(i["vlan"]),
        "ip":    i["eth_ip_addr"],
    }
    for i in rows
]
cmd("for n in normalized: print(n)")
blank()
for n in normalized:
    out(n)
blank()

pause()

section("5.3 — Parsing a RESTCONF Response")

explain("RESTCONF wraps data in a namespace key.")
explain("You need to unwrap it before processing.")
blank()

restconf_response = {
    "Cisco-IOS-XE-native:interface": {
        "GigabitEthernet": [
            {"name": "1", "ip": {"address": {"primary": {"address": "10.0.0.1", "mask": "255.255.255.0"}}}},
            {"name": "2", "ip": {"address": {"primary": {"address": "10.0.1.1", "mask": "255.255.255.0"}}}},
        ]
    }
}
cmd("restconf = {  # RESTCONF response }")
blank()

cmd("interfaces = restconf['Cisco-IOS-XE-native:interface']['GigabitEthernet']")
interfaces = restconf_response["Cisco-IOS-XE-native:interface"]["GigabitEthernet"]
cmd("for iface in interfaces:")
cmd("    name = iface['name']")
cmd("    ip   = iface['ip']['address']['primary']['address']")
cmd("    print(f'Gi{name}: {ip}')")
blank()
for iface in interfaces:
    name = iface["name"]
    ip   = iface["ip"]["address"]["primary"]["address"]
    out(f"Gi{name}: {ip}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Serialization Control
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Serialization Control")

section("6.1 — indent — Human-Readable Output")

explain("indent=N adds N spaces per level of nesting.")
explain("Use indent=2 or indent=4 for config files and reports.")
blank()

device = {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30], "config": {"ntp": "10.0.0.100"}}
cmd("device = {'hostname': 'nyc-rtr-01', 'vlans': [10,20,30], 'config': {'ntp': '10.0.0.100'}}")
blank()
cmd("print(json.dumps(device, indent=2))")
blank()
for line in json.dumps(device, indent=2).splitlines():
    out(line)
blank()

pause()

section("6.2 — sort_keys — Consistent Output")

explain("sort_keys=True sorts keys alphabetically.")
explain("Use for config files that go into version control —")
explain("no random key order means cleaner diffs.")
blank()

cmd("print(json.dumps(device, indent=2, sort_keys=True))")
blank()
for line in json.dumps(device, indent=2, sort_keys=True).splitlines():
    out(line)
blank()

pause()

section("6.3 — separators — Compact Output")

explain("separators=(',', ':') removes all spaces.")
explain("Use for API payloads where size matters.")
blank()

cmd("compact = json.dumps(device, separators=(',', ':'))")
compact = json.dumps(device, separators=(",", ":"))
cmd("print(compact)")
out(compact)
blank()

cmd("# Default has spaces after separators")
cmd("default = json.dumps(device)")
default_str = json.dumps(device)
cmd("print(default)")
out(default_str)
blank()

pause()

section("6.4 — ensure_ascii=False — Unicode Support")

explain("ensure_ascii=False allows non-ASCII characters.")
explain("Use when device descriptions contain special characters.")
blank()

data = {"site": "São Paulo", "country": "Brasil", "status": "✔"}
cmd("data = {'site': 'São Paulo', 'country': 'Brasil', 'status': '✔'}")
blank()
cmd("print(json.dumps(data, ensure_ascii=True))   # default")
out(json.dumps(data, ensure_ascii=True))
blank()
cmd("print(json.dumps(data, ensure_ascii=False))  # readable")
out(json.dumps(data, ensure_ascii=False))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Handling Non-Serializable Types
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Handling Non-Serializable Types")

section("7.1 — The Problem")

explain("json.dumps() fails on types JSON doesn't know:")
explain("  datetime, set, bytes, custom objects")
blank()

data_bad = {"hostname": "nyc-rtr-01", "vlans": {10, 20, 30}}
cmd("data = {'hostname': 'nyc-rtr-01', 'vlans': {10, 20, 30}}  # set!")
cmd("json.dumps(data)")
blank()
try:
    json.dumps(data_bad)
except TypeError as e:
    warn(f"TypeError: {e}")
blank()

data_dt = {"hostname": "nyc-rtr-01", "checked_at": datetime(2024, 1, 15, 10, 30)}
cmd("data = {'hostname': 'nyc-rtr-01', 'checked_at': datetime(2024,1,15,10,30)}")
cmd("json.dumps(data)")
blank()
try:
    json.dumps(data_dt)
except TypeError as e:
    warn(f"TypeError: {e}")
blank()

pause()

section("7.2 — The default= Parameter")

explain("Pass a function to default= that converts unknown types.")
explain("Called only when json.dumps() can't serialize a value.")
blank()

cmd("def iac_default(obj):")
cmd("    if isinstance(obj, set):")
cmd("        return sorted(obj)         # set → sorted list")
cmd("    if isinstance(obj, datetime):")
cmd("        return obj.isoformat()     # datetime → ISO string")
cmd("    raise TypeError(f'Cannot serialize {type(obj)}')")
blank()

def iac_default(obj):
    if isinstance(obj, set):
        return sorted(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj)}")

data_mixed = {
    "hostname":   "nyc-rtr-01",
    "vlans":      {10, 20, 30},
    "checked_at": datetime(2024, 1, 15, 10, 30),
}
cmd("data = {")
cmd("    'hostname':   'nyc-rtr-01',")
cmd("    'vlans':      {10, 20, 30},        # set")
cmd("    'checked_at': datetime(2024,1,15), # datetime")
cmd("}")
blank()
cmd("print(json.dumps(data, default=iac_default, indent=2))")
blank()
for line in json.dumps(data_mixed, default=iac_default, indent=2).splitlines():
    out(line)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Validating JSON Structure
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Validating JSON Structure")

section("8.1 — Check Required Keys Exist")

explain("API responses may be missing keys — always validate")
explain("before accessing nested data in IaC.")
blank()

cmd("def validate_device_json(data):")
cmd("    required = {'hostname', 'platform', 'status', 'interfaces'}")
cmd("    missing  = required - set(data.keys())")
cmd("    if missing:")
cmd("        return False, f'Missing keys: {missing}'")
cmd("    if not isinstance(data['interfaces'], list):")
cmd("        return False, 'interfaces must be a list'")
cmd("    return True, 'valid'")
blank()

def validate_device_json(data):
    required = {"hostname", "platform", "status", "interfaces"}
    missing  = required - set(data.keys())
    if missing:
        return False, f"Missing keys: {missing}"
    if not isinstance(data["interfaces"], list):
        return False, "interfaces must be a list"
    return True, "valid"

pause()

test_cases = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "interfaces": [{"name": "Gi0/0"}]},
    {"hostname": "lon-sw-01", "platform": "NX-OS"},
    {"hostname": "sin-fw-01", "platform": "ASA", "status": "up", "interfaces": "Gi0/0"},
]
cmd("for d in test_cases:")
cmd("    ok, msg = validate_device_json(d)")
cmd("    print(f\"{d['hostname']}: {msg}\")")
blank()
for d in test_cases:
    ok, msg = validate_device_json(d)
    out(f"{d['hostname']}: {msg}")
blank()

pause()

section("8.2 — Safe Parsing with try/except")

explain("Always wrap json.loads() in try/except when the source")
explain("is external — API responses can be malformed.")
blank()

cmd("def safe_parse(json_string):")
cmd("    try:")
cmd("        return json.loads(json_string), None")
cmd("    except json.JSONDecodeError as e:")
cmd("        return None, f'Invalid JSON: {e}'")
blank()

def safe_parse(json_string):
    try:
        return json.loads(json_string), None
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON: {e}"

pause()

test_strings = [
    '{"hostname": "nyc-rtr-01", "status": "up"}',
    '{"hostname": "bad-device", "status":}',
    'not json at all',
    '{"hostname": "incomplete"',
]
cmd("for s in test_strings:")
cmd("    data, err = safe_parse(s)")
cmd("    if err:")
cmd("        print(f'ERROR: {err}')")
cmd("    else:")
cmd("        print(f'OK: {data[\"hostname\"]}')")
blank()
for s in test_strings:
    data, err = safe_parse(s)
    if err:
        warn(f"ERROR: {err}")
    else:
        out(f"OK: {data['hostname']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Transforming JSON Data
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Transforming JSON Data")

section("9.1 — Reshape API Response to Standard Dict")

explain("API responses rarely match your internal data model.")
explain("Transform them to a standard shape immediately after parsing.")
blank()

raw_api = {
    "ietf-interfaces:interfaces": {
        "interface": [
            {
                "name":        "GigabitEthernet0/0",
                "type":        "iana-if-type:ethernetCsmacd",
                "enabled":     True,
                "ietf-ip:ipv4": {
                    "address": [{"ip": "10.0.0.1", "prefix-length": 24}]
                }
            },
            {
                "name":    "GigabitEthernet0/1",
                "type":    "iana-if-type:ethernetCsmacd",
                "enabled": False,
                "ietf-ip:ipv4": {
                    "address": [{"ip": "10.0.1.1", "prefix-length": 24}]
                }
            },
        ]
    }
}
cmd("raw_api = {  # IETF YANG interface response }")
blank()

cmd("def normalize_interfaces(raw):")
cmd("    ifaces = raw['ietf-interfaces:interfaces']['interface']")
cmd("    return [")
cmd("        {")
cmd("            'name':    i['name'],")
cmd("            'state':   'up' if i['enabled'] else 'down',")
cmd("            'ip':      i['ietf-ip:ipv4']['address'][0]['ip'],")
cmd("            'prefix':  i['ietf-ip:ipv4']['address'][0]['prefix-length'],")
cmd("        }")
cmd("        for i in ifaces")
cmd("    ]")
blank()

def normalize_interfaces(raw):
    ifaces = raw["ietf-interfaces:interfaces"]["interface"]
    return [
        {
            "name":   i["name"],
            "state":  "up" if i["enabled"] else "down",
            "ip":     i["ietf-ip:ipv4"]["address"][0]["ip"],
            "prefix": i["ietf-ip:ipv4"]["address"][0]["prefix-length"],
        }
        for i in ifaces
    ]

pause()

cmd("result = normalize_interfaces(raw_api)")
result = normalize_interfaces(raw_api)
cmd("for r in result: print(r)")
blank()
for r in result:
    out(r)
blank()

pause()

section("9.2 — Flatten Nested JSON")

explain("Collapse nested structure into a flat list for analysis:")
blank()

inventory_nested = {
    "sites": {
        "NYC": {
            "devices": [
                {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "vlans": [10,20,30]},
                {"hostname": "nyc-sw-01",  "platform": "IOS-XE", "vlans": [10,20]},
            ]
        },
        "LON": {
            "devices": [
                {"hostname": "lon-sw-01",  "platform": "NX-OS",  "vlans": [10,20]},
            ]
        },
    }
}
cmd("inventory_nested = {  # site → devices structure }")
blank()

cmd("flat = [")
cmd("    {**device, 'site': site}")
cmd("    for site, cfg in inventory_nested['sites'].items()")
cmd("    for device in cfg['devices']")
cmd("]")
flat = [
    {**device, "site": site}
    for site, cfg in inventory_nested["sites"].items()
    for device in cfg["devices"]
]
cmd("for d in flat: print(d['site'], d['hostname'], d['platform'])")
blank()
for d in flat:
    out(f"{d['site']} {d['hostname']} {d['platform']}")
blank()

pause()

section("9.3 — Extract Specific Fields")

explain("Build a lean summary dict from a large response:")
blank()

large_response = [
    {
        "hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
        "ip": "10.0.0.1", "vlans": [10,20,30],
        "serial": "FTX1234A", "model": "ISR4451",
        "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"},
        "interfaces": [{"name": "Gi0/0", "vlan": 10}],
    },
    {
        "hostname": "lon-sw-01",  "platform": "NX-OS", "status": "down",
        "ip": "10.1.0.1", "vlans": [10,20],
        "serial": "FTX5678B", "model": "N9K-C9300v",
        "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"},
        "interfaces": [{"name": "Gi0/0", "vlan": 10}],
    },
]
cmd("large_response = [  # full device response with many fields ]")
blank()

cmd("# Extract only what we need")
cmd("KEEP = {'hostname', 'platform', 'status', 'ip'}")
KEEP = {"hostname", "platform", "status", "ip"}
cmd("summary = [{k: d[k] for k in KEEP} for d in large_response]")
summary = [{k: d[k] for k in KEEP} for d in large_response]
cmd("for s in summary: print(s)")
blank()
for s in summary:
    out(s)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — loads vs load — The Most Common Mistake")

explain("loads() takes a STRING. load() takes a FILE.")
explain("Passing a string to load() raises TypeError.")
blank()

json_string = '{"hostname": "nyc-rtr-01"}'
cmd("json_string = '{\"hostname\": \"nyc-rtr-01\"}'")
blank()
cmd("# Wrong — load() expects a file object, not a string")
cmd("json.load(json_string)   # TypeError!")
blank()
try:
    json.load(json_string)
except (TypeError, AttributeError) as e:
    warn(f"Error: {e}")
blank()
cmd("# Correct — loads() for strings")
cmd("data = json.loads(json_string)")
data = json.loads(json_string)
out(data)
blank()

pause()

section("10.2 — JSON Uses true/false/null — Not Python Names")

explain("In a JSON string, booleans are 'true'/'false'.")
explain("In Python they are 'True'/'False'.")
explain("json.loads() handles this — don't do it manually.")
blank()

cmd("# Wrong — manually replacing Python names in a string")
cmd("bad = '{\"active\": True}'   # not valid JSON!")
cmd("json.loads(bad)")
blank()
try:
    json.loads('{"active": True}')
except json.JSONDecodeError as e:
    warn(f"JSONDecodeError: {e}")
blank()

cmd("# Correct — valid JSON uses lowercase true")
cmd("good = '{\"active\": true}'")
cmd("print(json.loads(good))")
good = json.loads('{"active": true}')
out(good)
blank()

pause()

section("10.3 — JSON Requires Double Quotes")

explain("JSON strings MUST use double quotes.")
explain("Single quotes are not valid JSON.")
blank()

cmd("# Wrong — single quotes")
cmd("json.loads(\"{'hostname': 'nyc-rtr-01'}\")")
blank()
try:
    json.loads("{'hostname': 'nyc-rtr-01'}")
except json.JSONDecodeError as e:
    warn(f"JSONDecodeError: {e}")
blank()

cmd("# Correct — double quotes")
cmd("json.loads('{\"hostname\": \"nyc-rtr-01\"}')")
out(json.loads('{"hostname": "nyc-rtr-01"}'))
blank()

pause()

section("10.4 — Mutating Parsed Data Mutates the Original")

explain("json.loads() returns a real Python object.")
explain("If you pass it around and mutate it — all references")
explain("see the change. Use copy.deepcopy() for independence.")
blank()

cmd("raw = json.loads('{\"vlans\": [10, 20, 30]}')")
raw = json.loads('{"vlans": [10, 20, 30]}')
cmd("copy_a = raw")
copy_a = raw
cmd("copy_a['vlans'].append(40)")
copy_a["vlans"].append(40)
cmd("print(raw['vlans'])    # also changed!")
warn(raw["vlans"])
blank()

pause()

import copy
cmd("raw = json.loads('{\"vlans\": [10, 20, 30]}')")
raw = json.loads('{"vlans": [10, 20, 30]}')
cmd("import copy")
cmd("copy_b = copy.deepcopy(raw)")
copy_b = copy.deepcopy(raw)
cmd("copy_b['vlans'].append(40)")
copy_b["vlans"].append(40)
cmd("print(raw['vlans'])    # untouched")
out(raw["vlans"])
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
print(f"  {BOLD}Ch 1{RESET}   What is JSON — 6 types, why it's central to IaC")
print(f"  {BOLD}Ch 2{RESET}   loads/dumps — parse string, serialize to string")
print(f"  {BOLD}Ch 3{RESET}   Type mapping — dict/list/str/int/bool/None ↔ JSON")
print(f"  {BOLD}Ch 4{RESET}   Navigating — nested keys, .get() chains, iterate arrays")
print(f"  {BOLD}Ch 5{RESET}   Real device output — show version, NX-OS, RESTCONF")
print(f"  {BOLD}Ch 6{RESET}   Serialization control — indent, sort_keys, separators, ensure_ascii")
print(f"  {BOLD}Ch 7{RESET}   Non-serializable types — set/datetime, default= function")
print(f"  {BOLD}Ch 8{RESET}   Validation — required keys, isinstance checks, safe_parse")
print(f"  {BOLD}Ch 9{RESET}   Transformation — normalize, flatten, extract fields")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — loads vs load, true/false/null, double quotes, deepcopy")
blank()
print(f"  {WHITE}Every example used real Cisco IaC patterns —")
print(f"  API responses, show command output, RESTCONF,")
print(f"  IETF YANG, NX-OS TABLE/ROW structures.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()