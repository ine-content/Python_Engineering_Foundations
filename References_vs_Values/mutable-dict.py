# mutable_dicts_proof.py
# Proving dict mutability in Python
# Cisco IaC perspective
# Press ENTER to advance through each step

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"    # >>> commands
GREEN  = "\033[92m"    # output values
YELLOW = "\033[93m"    # ids
WHITE  = "\033[97m"    # explanations
RED    = "\033[91m"    # errors / warnings
BOLD   = "\033[1m"
DIM    = "\033[2m"

def pause():
    input(f"\n{DIM}  [ Press ENTER to continue ]{RESET} ")
    print()

def cmd(command):
    print(f"    {CYAN}>>> {command}{RESET}")

def out(value):
    print(f"    {GREEN}{value}{RESET}")

def out_id(value):
    print(f"    {YELLOW}{value}{RESET}")

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

# ─────────────────────────────────────────────────────────────────────────────
print()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}█         PROVING DICT MUTABILITY IN PYTHON                  █{RESET}")
print(f"{BOLD}█         Cisco IaC Perspective                              █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 1 — Key assignment and deletion mutate in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 1 — Key assignment and deletion mutate in place")

explain("We have a Cisco device config dict.")
explain("We add, update, and delete keys directly.")
explain("Watch the id — it never changes.")
explain("Same id before and after means the SAME object was modified.")
blank()

pause()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'ip': '10.0.0.1'}")
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

explain("Add a new key:")
blank()
cmd("device['vendor'] = 'Cisco'")
device["vendor"] = "Cisco"
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

explain("Same id — the same dict object was modified in place.")
blank()

pause()

explain("Update an existing key:")
blank()
cmd("device['hostname'] = 'nyc-rtr-01-core'")
device["hostname"] = "nyc-rtr-01-core"
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

explain("Same id again — still the same object.")
blank()

pause()

explain("Delete a key:")
blank()
cmd("del device['ip']")
del device["ip"]
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

explain("✔ The id never changed across any of these operations.")
explain("  Adding, updating, and deleting keys all modified")
explain("  the same dict object in place.")
explain("  This is what mutability means for dicts.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 2 — Update methods mutate in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 2 — Update methods mutate in place")

explain("We have a device config dict.")
explain("We call dict mutation methods on it.")
explain("Every method modifies the same object — id never changes.")
blank()

pause()

config = {"hostname": "lon-sw-01", "platform": "NX-OS", "mgmt_ip": "10.1.0.1"}
cmd("config = {'hostname': 'lon-sw-01', 'platform': 'NX-OS', 'mgmt_ip': '10.1.0.1'}")
cmd("print(config)")
out(config)
cmd("print(id(config))")
out_id(id(config))
blank()

pause()

explain("Call .update() — merge new key-value pairs in place:")
blank()
cmd("config.update({'vendor': 'Cisco', 'port_count': 48})")
config.update({"vendor": "Cisco", "port_count": 48})
cmd("print(config)")
out(config)
cmd("print(id(config))")
out_id(id(config))
blank()

pause()

explain("Same id — .update() modified the object in place.")
blank()

pause()

explain("Call .pop() — remove a key and return its value:")
blank()
cmd("removed = config.pop('mgmt_ip')")
removed = config.pop("mgmt_ip")
cmd("print(removed)")
out(removed)
cmd("print(config)")
out(config)
cmd("print(id(config))")
out_id(id(config))
blank()

pause()

explain("Same id — .pop() modified the object in place.")
blank()

pause()

explain("Call .setdefault() — add key only if it does not exist:")
blank()
cmd("config.setdefault('ntp', '10.0.0.100')")
config.setdefault("ntp", "10.0.0.100")
cmd("print(config)")
out(config)
cmd("print(id(config))")
out_id(id(config))
blank()

pause()

explain("Call .clear() — remove all keys in place:")
blank()
cmd("config.clear()")
config.clear()
cmd("print(config)")
out(config)
cmd("print(id(config))")
out_id(id(config))
blank()

pause()

explain("✔ .update(), .pop(), .setdefault(), .clear() — all")
explain("  modified the same dict object in place.")
explain("  The id is identical across every single operation.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 3 — Aliasing: two names, one object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 3 — Aliasing: two names, one object")

explain("We have a device config dict.")
explain("We assign it to a second variable — this is an alias.")
explain("Both names point to the same object.")
explain("Mutating through one name is visible through the other.")
blank()

pause()

base_config = {"hostname": "sin-rtr-01", "platform": "IOS-XE", "env": "prod"}
cmd("base_config = {'hostname': 'sin-rtr-01', 'platform': 'IOS-XE', 'env': 'prod'}")
cmd("print(base_config)")
out(base_config)
cmd("print(id(base_config))")
out_id(id(base_config))
blank()

pause()

site_config = base_config
cmd("site_config = base_config   # alias — same object")
cmd("print(site_config)")
out(site_config)
cmd("print(id(site_config))")
out_id(id(site_config))
blank()

pause()

explain("Both ids are identical — one object, two names.")
blank()

pause()

explain("Mutate through site_config — add a key:")
blank()
cmd("site_config['region'] = 'ap-southeast-1'")
site_config["region"] = "ap-southeast-1"
cmd("print(site_config)")
out(site_config)
cmd("print(id(site_config))")
out_id(id(site_config))
blank()

pause()

explain("Check base_config — did it change?")
blank()
cmd("print(base_config)")
out(base_config)
cmd("print(id(base_config))")
out_id(id(base_config))
blank()

pause()

warn("⚠ YES — base_config also changed.")
warn("  Both names point to the same dict object.")
warn("  Mutating through site_config mutated the shared object.")
warn("  base_config and site_config have the same id — always.")
blank()

pause()

explain("Now mutate through base_config — change env to staging:")
blank()
cmd("base_config['env'] = 'staging'")
base_config["env"] = "staging"
cmd("print(base_config)")
out(base_config)
cmd("print(id(base_config))")
out_id(id(base_config))
blank()

pause()

explain("Check site_config — did it change?")
blank()
cmd("print(site_config)")
out(site_config)
cmd("print(id(site_config))")
out_id(id(site_config))
blank()

pause()

warn("⚠ YES — site_config also changed.")
warn("  It does not matter which name you mutate through.")
warn("  There is only one dict. Both names see every change.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 4 — Functions CAN mutate a dict you pass in
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 4 — Functions CAN mutate a dict you pass in")

explain("We pass a device config dict into a function.")
explain("The function adds and modifies keys directly.")
explain("Watch the id — it is the same inside and outside the function.")
explain("The caller's dict is modified.")
blank()

pause()

def apply_defaults(config):
    """
    Applies default values directly to the config dict.
    The caller's dict is directly modified.
    Same object — same id inside and outside.
    """
    config["ntp"]    = "10.0.0.100"
    config["dns"]    = "8.8.8.8"
    config["domain"] = "corp.example.com"

explain("Here is the function we will call:")
blank()
cmd("def apply_defaults(config):")
cmd("    config['ntp']    = '10.0.0.100'")
cmd("    config['dns']    = '8.8.8.8'")
cmd("    config['domain'] = 'corp.example.com'")
blank()
explain("It adds keys directly to the dict.")
explain("It receives a reference to the same dict object.")
explain("Any mutation inside is visible outside.")
blank()

pause()

device = {"hostname": "ams-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'ams-rtr-01', 'platform': 'IOS-XE'}")
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

explain("Now call apply_defaults(device):")
blank()
cmd("apply_defaults(device)")
apply_defaults(device)
blank()

pause()

explain("Check device after the function ran:")
blank()
cmd("print(device)")
out(device)
cmd("print(id(device))")
out_id(id(device))
blank()

pause()

warn("⚠ device was modified by the function.")
warn("  The function received a reference to the same dict.")
warn("  Key assignments inside mutated the shared object.")
warn("  The id is identical — before, during, and after the call.")
blank()

pause()

explain("Call it again — keys are overwritten:")
blank()
cmd("device2 = {'hostname': 'tok-sw-01', 'platform': 'NX-OS'}")
device2 = {"hostname": "tok-sw-01", "platform": "NX-OS"}
cmd("apply_defaults(device2)")
apply_defaults(device2)
cmd("print(device2)")
out(device2)
cmd("print(id(device2))")
out_id(id(device2))
blank()

pause()

explain("✔ Same pattern every time — same id before and after.")
explain("  The dict was never copied — the same object")
explain("  was passed in and mutated every single time.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 5 — The gotcha: nested dict inside a dict
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 5 — The gotcha: nested dict inside a dict")

explain("This is the most dangerous pattern in Cisco IaC.")
explain("Device configs are almost always nested dicts.")
explain(".copy() is SHALLOW — it copies the outer dict")
explain("but inner dicts are still shared.")
explain("Mutating an inner dict is visible in both copies.")
blank()

pause()

base = {
    "hostname": "nyc-rtr-01",
    "bgp":      {"as_number": 65001, "neighbors": ["10.0.0.2"]},
    "ntp":      ["10.0.0.100", "10.0.0.101"],
}
cmd("base = {")
cmd("    'hostname': 'nyc-rtr-01',")
cmd("    'bgp':      {'as_number': 65001, 'neighbors': ['10.0.0.2']},")
cmd("    'ntp':      ['10.0.0.100', '10.0.0.101'],")
cmd("}")
cmd("print(base)")
out(base)
cmd("print(id(base))")
out_id(id(base))
blank()
cmd("print(id(base['bgp']))   # id of the inner bgp dict")
out_id(id(base["bgp"]))
blank()

pause()

site = base.copy()
cmd("site = base.copy()")
cmd("print(site)")
out(site)
cmd("print(id(site))")
out_id(id(site))
blank()
cmd("print(id(site['bgp']))   # id of bgp dict in the copy")
out_id(id(site["bgp"]))
blank()

pause()

explain("The outer dicts have DIFFERENT ids — good so far.")
explain("But look at the bgp inner dict — SAME id in both.")
explain("That inner dict is still shared.")
blank()

pause()

explain("Now mutate the inner bgp dict through site:")
blank()
cmd("site['bgp']['neighbors'].append('10.0.0.3')")
site["bgp"]["neighbors"].append("10.0.0.3")
cmd("site['bgp']['as_number'] = 65002")
site["bgp"]["as_number"] = 65002
blank()

pause()

explain("Check site:")
blank()
cmd("print(site['bgp'])")
out(site["bgp"])
cmd("print(id(site['bgp']))")
out_id(id(site["bgp"]))
blank()

pause()

explain("Now check base — did the inner bgp dict change?")
blank()
cmd("print(base['bgp'])")
out(base["bgp"])
cmd("print(id(base['bgp']))")
out_id(id(base["bgp"]))
blank()

pause()

warn("⚠ YES — base['bgp'] was also modified.")
warn("  .copy() only copied the outer dict.")
warn("  The inner bgp dict is the same object in both.")
warn("  Mutating it through site also mutated it in base.")
blank()

pause()

explain("The fix — use copy.deepcopy() for nested structures:")
blank()
import copy

base2 = {
    "hostname": "nyc-rtr-01",
    "bgp":      {"as_number": 65001, "neighbors": ["10.0.0.2"]},
    "ntp":      ["10.0.0.100", "10.0.0.101"],
}
cmd("import copy")
cmd("base2 = {")
cmd("    'hostname': 'nyc-rtr-01',")
cmd("    'bgp':      {'as_number': 65001, 'neighbors': ['10.0.0.2']},")
cmd("    'ntp':      ['10.0.0.100', '10.0.0.101'],")
cmd("}")
cmd("print(id(base2))")
out_id(id(base2))
cmd("print(id(base2['bgp']))")
out_id(id(base2["bgp"]))
blank()

pause()

site2 = copy.deepcopy(base2)
cmd("site2 = copy.deepcopy(base2)")
cmd("print(id(site2))")
out_id(id(site2))
cmd("print(id(site2['bgp']))")
out_id(id(site2["bgp"]))
blank()

pause()

explain("Both the outer dict AND the inner bgp dict have DIFFERENT ids.")
explain("Every object was copied recursively — nothing is shared.")
blank()

pause()

explain("Now mutate the inner bgp dict through site2:")
blank()
cmd("site2['bgp']['neighbors'].append('10.0.0.3')")
site2["bgp"]["neighbors"].append("10.0.0.3")
cmd("site2['bgp']['as_number'] = 65002")
site2["bgp"]["as_number"] = 65002
blank()

pause()

explain("Check site2:")
blank()
cmd("print(site2['bgp'])")
out(site2["bgp"])
blank()

pause()

explain("Check base2 — is it still untouched?")
blank()
cmd("print(base2['bgp'])")
out(base2["bgp"])
cmd("print(id(base2['bgp']))")
out_id(id(base2["bgp"]))
blank()

pause()

explain("✔ base2['bgp'] is completely untouched.")
explain("  deepcopy created independent objects at every level.")
explain("  No mutation to site2 can reach base2.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 6 — The fix: .copy() vs deepcopy() side by side
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 6 — The fix: .copy() vs deepcopy() — side by side")

explain("A clear comparison of what each copy method gives you.")
explain("Flat dicts — .copy() is sufficient.")
explain("Nested dicts — deepcopy() is required.")
blank()

pause()

explain("FLAT dict — .copy() is safe:")
blank()

flat = {"hostname": "nyc-rtr-01", "env": "prod", "platform": "IOS-XE"}
cmd("flat = {'hostname': 'nyc-rtr-01', 'env': 'prod', 'platform': 'IOS-XE'}")
cmd("print(id(flat))")
out_id(id(flat))
blank()

flat_copy = flat.copy()
cmd("flat_copy = flat.copy()")
cmd("print(id(flat_copy))")
out_id(id(flat_copy))
blank()

flat_copy["env"] = "staging"
flat_copy["hostname"] = "nyc-rtr-02"
cmd("flat_copy['env'] = 'staging'")
cmd("flat_copy['hostname'] = 'nyc-rtr-02'")
cmd("print(flat_copy)")
out(flat_copy)
blank()
cmd("print(flat)")
out(flat)
blank()

pause()

explain("✔ flat is untouched — .copy() was sufficient here.")
explain("  All values were strings (immutable), so no shared objects.")
blank()

pause()

explain("NESTED dict — .copy() is NOT safe:")
blank()

nested = {"hostname": "lon-sw-01", "vlans": [10, 20, 30], "snmp": {"community": "public"}}
cmd("nested = {'hostname': 'lon-sw-01', 'vlans': [10,20,30], 'snmp': {'community': 'public'}}")
cmd("print(id(nested))")
out_id(id(nested))
cmd("print(id(nested['vlans']))   # inner list id")
out_id(id(nested["vlans"]))
cmd("print(id(nested['snmp']))    # inner dict id")
out_id(id(nested["snmp"]))
blank()

nested_copy = nested.copy()
cmd("nested_copy = nested.copy()")
cmd("print(id(nested_copy))")
out_id(id(nested_copy))
cmd("print(id(nested_copy['vlans']))   # same as nested['vlans']?")
out_id(id(nested_copy["vlans"]))
cmd("print(id(nested_copy['snmp']))    # same as nested['snmp']?")
out_id(id(nested_copy["snmp"]))
blank()

pause()

warn("⚠ The inner vlans list and snmp dict have the SAME ids.")
warn("  They are shared between nested and nested_copy.")
blank()

nested_copy["vlans"].append(40)
nested_copy["snmp"]["community"] = "secret"
cmd("nested_copy['vlans'].append(40)")
cmd("nested_copy['snmp']['community'] = 'secret'")
cmd("print(nested)")
out(nested)
blank()

pause()

warn("⚠ nested was also modified — shallow copy is not enough.")
blank()

pause()

explain("NESTED dict — deepcopy() IS safe:")
blank()

nested2 = {"hostname": "lon-sw-01", "vlans": [10, 20, 30], "snmp": {"community": "public"}}
cmd("nested2 = {'hostname': 'lon-sw-01', 'vlans': [10,20,30], 'snmp': {'community': 'public'}}")
cmd("print(id(nested2))")
out_id(id(nested2))
cmd("print(id(nested2['vlans']))")
out_id(id(nested2["vlans"]))
cmd("print(id(nested2['snmp']))")
out_id(id(nested2["snmp"]))
blank()

deep_copy = copy.deepcopy(nested2)
cmd("deep_copy = copy.deepcopy(nested2)")
cmd("print(id(deep_copy))")
out_id(id(deep_copy))
cmd("print(id(deep_copy['vlans']))   # different from nested2?")
out_id(id(deep_copy["vlans"]))
cmd("print(id(deep_copy['snmp']))    # different from nested2?")
out_id(id(deep_copy["snmp"]))
blank()

pause()

explain("All three ids are different — fully independent at every level.")
blank()

deep_copy["vlans"].append(40)
deep_copy["snmp"]["community"] = "secret"
cmd("deep_copy['vlans'].append(40)")
cmd("deep_copy['snmp']['community'] = 'secret'")
cmd("print(nested2)")
out(nested2)
blank()

pause()

explain("✔ nested2 is completely untouched.")
explain("  deepcopy created independent objects at every level.")
explain("  Use .copy() for flat dicts.")
explain("  Use deepcopy() whenever nested dicts or lists are present.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}█   SUMMARY — WHAT WE PROVED                                 █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
blank()
print(f"  {BOLD}Proof 1{RESET}  Key assignment and deletion mutate in place")
print(f"  {DIM}         d['key'] = val, del d['key'] — id never changes{RESET}")
blank()
print(f"  {BOLD}Proof 2{RESET}  Update methods mutate in place")
print(f"  {DIM}         .update(), .pop(), .setdefault(), .clear() — same id{RESET}")
blank()
print(f"  {BOLD}Proof 3{RESET}  Aliasing — two names, one object")
print(f"  {DIM}         b = a then mutate through b — a sees every change{RESET}")
blank()
print(f"  {BOLD}Proof 4{RESET}  Functions CAN mutate a dict you pass in")
print(f"  {DIM}         id is identical inside and outside the function{RESET}")
print(f"  {DIM}         key assignments inside modify the caller's dict{RESET}")
blank()
print(f"  {BOLD}Proof 5{RESET}  The gotcha — nested dict inside a dict")
print(f"  {DIM}         .copy() is shallow — inner dicts are still shared{RESET}")
print(f"  {DIM}         deepcopy() copies every level — nothing shared{RESET}")
blank()
print(f"  {BOLD}Proof 6{RESET}  .copy() vs deepcopy() — side by side")
print(f"  {DIM}         Flat dict — .copy() is sufficient{RESET}")
print(f"  {DIM}         Nested dict — deepcopy() is required{RESET}")
blank()
print(f"  {WHITE}In Cisco IaC — device configs are almost always nested")
print(f"  dicts. BGP neighbors, interface configs, SNMP settings")
print(f"  are all inner dicts or lists. Always use deepcopy()")
print(f"  when copying a config template. .copy() will silently")
print(f"  share inner objects and corrupt your base config.{RESET}")
blank()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█   Proof complete.                                          █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
print()