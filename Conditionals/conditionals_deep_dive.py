# conditionals_deep_dive.py
# Conditionals in Python — Zero to Expert
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
print(f"{BOLD}         CONDITIONALS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a Conditional
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a Conditional")

section("1.1 — Definition")

explain("A conditional lets your code make decisions.")
explain("It runs one block of code or another depending")
explain("on whether a condition is True or False.")
blank()
explain("In Cisco IaC, conditionals decide things like:")
explain("  — Is this device up or down?")
explain("  — Is this platform IOS-XE or NX-OS?")
explain("  — Does this interface have the right VLAN?")
blank()

pause()

section("1.2 — if, elif, else")

explain("Basic syntax — three keywords:")
blank()
explain("  if   — runs if condition is True")
explain("  elif — runs if previous conditions were False")
explain("         and this condition is True")
explain("  else — runs if ALL previous conditions were False")
blank()

pause()

status = "up"
cmd("status = 'up'")
blank()
cmd("if status == 'up':")
cmd("    print('Device is reachable')")
cmd("elif status == 'down':")
cmd("    print('Device is unreachable')")
cmd("else:")
cmd("    print('Unknown status')")
blank()
if status == "up":
    out("Device is reachable")
elif status == "down":
    out("Device is unreachable")
else:
    out("Unknown status")
blank()

pause()

explain("Only ONE block ever runs — the first True condition wins.")
blank()

platform = "NX-OS"
cmd("platform = 'NX-OS'")
blank()
cmd("if platform == 'IOS-XE':")
cmd("    print('Catalyst / ISR')")
cmd("elif platform == 'NX-OS':")
cmd("    print('Nexus switch')")
cmd("elif platform == 'ASA':")
cmd("    print('Firewall')")
cmd("else:")
cmd("    print('Unknown platform')")
blank()
if platform == "IOS-XE":
    out("Catalyst / ISR")
elif platform == "NX-OS":
    out("Nexus switch")
elif platform == "ASA":
    out("Firewall")
else:
    out("Unknown platform")
blank()

pause()

explain("else is optional — you do not need it if there")
explain("is nothing to do when all conditions are False:")
blank()

vlan = 10
cmd("vlan = 10")
blank()
cmd("if vlan == 1:")
cmd("    print('Warning: using native VLAN')")
blank()
if vlan == 1:
    out("Warning: using native VLAN")
blank()
explain("Nothing printed — vlan is not 1, and there is no else.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Comparison Operators
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Comparison Operators")

section("2.1 — Equality and Inequality")

explain("== checks if two values are EQUAL.")
explain("!= checks if two values are NOT EQUAL.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'}")
blank()
cmd("print(device['platform'] == 'IOS-XE')")
out(device["platform"] == "IOS-XE")
cmd("print(device['platform'] == 'NX-OS')")
out(device["platform"] == "NX-OS")
cmd("print(device['status'] != 'down')")
out(device["status"] != "down")
blank()

pause()

section("2.2 — Numeric Comparisons")

explain("< > <= >= work on numbers.")
blank()

vlan = 30
cmd("vlan = 30")
blank()
cmd("print(vlan > 20)")
out(vlan > 20)
cmd("print(vlan < 10)")
out(vlan < 10)
cmd("print(vlan >= 30)")
out(vlan >= 30)
cmd("print(vlan <= 29)")
out(vlan <= 29)
blank()

pause()

explain("Practical use — validate VLAN range:")
blank()
cmd("if 1 <= vlan <= 4094:")
cmd("    print(f'VLAN {vlan} is valid')")
cmd("else:")
cmd("    print(f'VLAN {vlan} is out of range')")
blank()
if 1 <= vlan <= 4094:
    out(f"VLAN {vlan} is valid")
else:
    out(f"VLAN {vlan} is out of range")
blank()

pause()

section("2.3 — in and not in")

explain("'in' checks if a value exists in a sequence.")
explain("Works on lists, tuples, strings, dicts, sets.")
blank()

vlans = [10, 20, 30, 40]
cmd("vlans = [10, 20, 30, 40]")
blank()
cmd("print(10 in vlans)")
out(10 in vlans)
cmd("print(99 in vlans)")
out(99 in vlans)
cmd("print(99 not in vlans)")
out(99 not in vlans)
blank()

pause()

explain("Check if a key exists in a dict:")
blank()
device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()
cmd("print('hostname' in device)")
out("hostname" in device)
cmd("print('vendor' in device)")
out("vendor" in device)
blank()

pause()

explain("Check if a substring exists in a string:")
blank()
hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
blank()
cmd("print('rtr' in hostname)")
out("rtr" in hostname)
cmd("print('sw' in hostname)")
out("sw" in hostname)
blank()

pause()

explain("Practical use — classify device by hostname:")
blank()
cmd("if 'rtr' in hostname:")
cmd("    print('This is a router')")
cmd("elif 'sw' in hostname:")
cmd("    print('This is a switch')")
cmd("elif 'fw' in hostname:")
cmd("    print('This is a firewall')")
blank()
if "rtr" in hostname:
    out("This is a router")
elif "sw" in hostname:
    out("This is a switch")
elif "fw" in hostname:
    out("This is a firewall")
blank()

pause()

section("2.4 — is and is not")

explain("'is' checks if two names point to the SAME object.")
explain("'==' checks if two values are EQUAL.")
explain("Always use 'is' for None, True, False.")
explain("Always use '==' for strings, numbers, lists.")
blank()

cmd("x = None")
x = None
cmd("print(x is None)")
out(x is None)
cmd("print(x == None)   # works but not recommended")
out(x == None)
blank()

pause()

cmd("status = True")
status = True
cmd("print(status is True)")
out(status is True)
blank()

explain("Never use 'is' to compare strings or numbers:")
blank()
cmd("hostname = 'nyc-rtr-01'")
hostname = "nyc-rtr-01"
cmd("print(hostname == 'nyc-rtr-01')   # correct")
out(hostname == "nyc-rtr-01")
cmd("print(hostname is 'nyc-rtr-01')   # wrong — unreliable")
out(hostname is "nyc-rtr-01")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Boolean Operators
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Boolean Operators")

section("3.1 — and")

explain("'and' — both conditions must be True.")
explain("If the first is False, the second is never checked.")
explain("This is called short-circuit evaluation.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'}")
blank()
cmd("if device['platform'] == 'IOS-XE' and device['status'] == 'up':")
cmd("    print('IOS-XE device is up — safe to push config')")
blank()
if device["platform"] == "IOS-XE" and device["status"] == "up":
    out("IOS-XE device is up — safe to push config")
blank()

pause()

explain("Short-circuit — second condition not evaluated if first is False:")
blank()
cmd("config = None")
config = None
cmd("if config is not None and len(config) > 0:")
cmd("    print('Config is present')")
cmd("else:")
cmd("    print('No config')")
blank()
if config is not None and len(config) > 0:
    out("Config is present")
else:
    out("No config")
blank()
explain("len(config) never runs because 'config is not None' is False.")
explain("This prevents a TypeError on None.")

pause()

section("3.2 — or")

explain("'or' — at least one condition must be True.")
explain("If the first is True, the second is never checked.")
blank()

platform = "ASA"
cmd("platform = 'ASA'")
blank()
cmd("if platform == 'ASA' or platform == 'FTD':")
cmd("    print('This is a firewall')")
blank()
if platform == "ASA" or platform == "FTD":
    out("This is a firewall")
blank()

pause()

explain("'or' for default values — a classic Python pattern:")
blank()
cmd("vendor = None")
vendor = None
cmd("display_vendor = vendor or 'Unknown'")
display_vendor = vendor or "Unknown"
cmd("print(display_vendor)")
out(display_vendor)
blank()
cmd("vendor = 'Cisco'")
vendor = "Cisco"
cmd("display_vendor = vendor or 'Unknown'")
display_vendor = vendor or "Unknown"
cmd("print(display_vendor)")
out(display_vendor)
blank()

pause()

section("3.3 — not")

explain("'not' inverts a boolean — True becomes False, False becomes True.")
blank()

status = "down"
cmd("status = 'down'")
blank()
cmd("if not status == 'up':")
cmd("    print('Device is not up')")
blank()
if not status == "up":
    out("Device is not up")
blank()

pause()

explain("More readable with != in this case — but 'not' shines")
explain("when negating complex conditions:")
blank()

vlans = [10, 20, 30]
cmd("vlans = [10, 20, 30]")
blank()
cmd("if not (10 in vlans and 20 in vlans):")
cmd("    print('Missing required VLANs')")
cmd("else:")
cmd("    print('Required VLANs present')")
blank()
if not (10 in vlans and 20 in vlans):
    out("Missing required VLANs")
else:
    out("Required VLANs present")
blank()

pause()

section("3.4 — Combining and, or, not")

explain("Combine operators for complex conditions.")
explain("Use parentheses to make precedence explicit.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE",
          "status": "up", "vlans": [10, 20, 30]}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'status': 'up', 'vlans': [10, 20, 30]}")
blank()
cmd("if (device['platform'] == 'IOS-XE' or device['platform'] == 'NX-OS')")
cmd("   and device['status'] == 'up'")
cmd("   and 10 in device['vlans']:")
cmd("    print('Device eligible for VLAN 10 config push')")
blank()
if ((device["platform"] == "IOS-XE" or device["platform"] == "NX-OS")
        and device["status"] == "up"
        and 10 in device["vlans"]):
    out("Device eligible for VLAN 10 config push")
blank()

pause()

explain("Tip — use 'in' with a set or tuple for multiple OR checks:")
blank()
cmd("if device['platform'] in ('IOS-XE', 'NX-OS', 'IOS-XR'):")
cmd("    print('Cisco OS platform')")
blank()
if device["platform"] in ("IOS-XE", "NX-OS", "IOS-XR"):
    out("Cisco OS platform")
blank()
explain("Much cleaner than: platform == 'IOS-XE' or platform == 'NX-OS' or ...")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Truthy and Falsy
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Truthy and Falsy")

section("4.1 — What Python Considers False")

explain("In Python you do not always need == True or == False.")
explain("Python evaluates any object as True or False directly.")
blank()
explain("These values are FALSY — treated as False:")
explain("  False, None, 0, 0.0, '', [], {}, set(), tuple()")
blank()
explain("Everything else is TRUTHY — treated as True.")
blank()

pause()

cmd("print(bool(False))")
out(bool(False))
cmd("print(bool(None))")
out(bool(None))
cmd("print(bool(0))")
out(bool(0))
cmd("print(bool(''))")
out(bool(""))
cmd("print(bool([]))")
out(bool([]))
cmd("print(bool({}))")
out(bool({}))
blank()

pause()

cmd("print(bool(True))")
out(bool(True))
cmd("print(bool(1))")
out(bool(1))
cmd("print(bool('hello'))")
out(bool("hello"))
cmd("print(bool([1, 2]))")
out(bool([1, 2]))
cmd("print(bool({'key': 'val'}))")
out(bool({"key": "val"}))
blank()

pause()

section("4.2 — Using Truthiness in Conditionals")

explain("Instead of checking == [] or == None,")
explain("let Python evaluate the object directly:")
blank()

vlans = []
cmd("vlans = []")
blank()
cmd("if vlans:")
cmd("    print('VLANs configured')")
cmd("else:")
cmd("    print('No VLANs configured')")
blank()
if vlans:
    out("VLANs configured")
else:
    out("No VLANs configured")
blank()

pause()

vlans = [10, 20, 30]
cmd("vlans = [10, 20, 30]")
blank()
cmd("if vlans:")
cmd("    print(f'Found {len(vlans)} VLANs')")
blank()
if vlans:
    out(f"Found {len(vlans)} VLANs")
blank()

pause()

config = {}
cmd("config = {}")
blank()
cmd("if not config:")
cmd("    print('Config is empty — applying defaults')")
blank()
if not config:
    out("Config is empty — applying defaults")
blank()

pause()

hostname = None
cmd("hostname = None")
blank()
cmd("if hostname:")
cmd("    print(f'Hostname is {hostname}')")
cmd("else:")
cmd("    print('Hostname not set')")
blank()
if hostname:
    out(f"Hostname is {hostname}")
else:
    out("Hostname not set")
blank()

pause()

explain("Practical use — check before processing:")
blank()
inventory = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20]},
    {"hostname": "lon-sw-01",  "vlans": []},
    {"hostname": "sin-fw-01",  "vlans": [30, 40]},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'vlans': [10, 20]},")
cmd("    {'hostname': 'lon-sw-01',  'vlans': []},")
cmd("    {'hostname': 'sin-fw-01',  'vlans': [30, 40]},")
cmd("]")
blank()
cmd("for d in inventory:")
cmd("    if d['vlans']:")
cmd("        print(f\"{d['hostname']}: {d['vlans']}\")")
cmd("    else:")
cmd("        print(f\"{d['hostname']}: no VLANs assigned\")")
blank()
for d in inventory:
    if d["vlans"]:
        out(f"{d['hostname']}: {d['vlans']}")
    else:
        out(f"{d['hostname']}: no VLANs assigned")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Nested Conditionals
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Nested Conditionals")

section("5.1 — if Inside if")

explain("You can put an if block inside another if block.")
explain("Use this when the inner condition only makes")
explain("sense to check after the outer one passes.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE",
          "status": "up", "vlans": [10, 20, 30]}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'status': 'up', 'vlans': [10, 20, 30]}")
blank()
cmd("if device['status'] == 'up':")
cmd("    print('Device is up')")
cmd("    if device['platform'] == 'IOS-XE':")
cmd("        print('Running IOS-XE config push')")
cmd("        if 10 in device['vlans']:")
cmd("            print('VLAN 10 confirmed — pushing access config')")
blank()
if device["status"] == "up":
    out("Device is up")
    if device["platform"] == "IOS-XE":
        out("Running IOS-XE config push")
        if 10 in device["vlans"]:
            out("VLAN 10 confirmed — pushing access config")
blank()

pause()

section("5.2 — When to Use elif Instead")

explain("Three levels of nesting gets hard to read.")
explain("If conditions are independent — use elif instead:")
blank()

cmd("# Hard to read — deeply nested")
cmd("if device['status'] == 'up':")
cmd("    if device['platform'] == 'IOS-XE':")
cmd("        if 10 in device['vlans']:")
cmd("            print('All checks passed')")
blank()

cmd("# Cleaner — combined with 'and'")
cmd("if (device['status'] == 'up'")
cmd("        and device['platform'] == 'IOS-XE'")
cmd("        and 10 in device['vlans']):")
cmd("    print('All checks passed')")
blank()
if (device["status"] == "up"
        and device["platform"] == "IOS-XE"
        and 10 in device["vlans"]):
    out("All checks passed")
blank()

pause()

explain("Rule of thumb: if conditions MUST be checked in sequence")
explain("(inner depends on outer) → nest them.")
explain("If they are independent checks → combine with 'and'.")

pause()

section("5.3 — Early Return Pattern")

explain("In a function, return early when a check fails.")
explain("This flattens nesting and makes logic easier to follow.")
blank()

cmd("def validate_device(device):")
cmd("    if device['status'] != 'up':")
cmd("        return 'SKIP: device is down'")
cmd("    if device['platform'] not in ('IOS-XE', 'NX-OS'):")
cmd("        return 'SKIP: unsupported platform'")
cmd("    if not device['vlans']:")
cmd("        return 'SKIP: no VLANs configured'")
cmd("    return 'OK: device ready for config push'")
blank()

def validate_device(device):
    if device["status"] != "up":
        return "SKIP: device is down"
    if device["platform"] not in ("IOS-XE", "NX-OS"):
        return "SKIP: unsupported platform"
    if not device["vlans"]:
        return "SKIP: no VLANs configured"
    return "OK: device ready for config push"

pause()

test_devices = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [10]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": []},
]
cmd("for d in test_devices:")
cmd("    result = validate_device(d)")
cmd("    print(f\"{d['hostname']}: {result}\")")
blank()
for d in test_devices:
    result = validate_device(d)
    out(f"{d['hostname']}: {result}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Conditional Expressions (Ternary)
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Conditional Expressions (Ternary)")

section("6.1 — Syntax and Basic Use")

explain("A conditional expression returns one of two values")
explain("on a single line.")
blank()
explain("Syntax:  value_if_true  if  condition  else  value_if_false")
blank()

pause()

status = "up"
cmd("status = 'up'")
blank()
cmd("label = 'reachable' if status == 'up' else 'unreachable'")
label = "reachable" if status == "up" else "unreachable"
cmd("print(label)")
out(label)
blank()

pause()

explain("Equivalent to:")
blank()
cmd("if status == 'up':")
cmd("    label = 'reachable'")
cmd("else:")
cmd("    label = 'unreachable'")
blank()
explain("Use the ternary form when the logic is simple.")
explain("Use the full if/else when logic is complex.")

pause()

section("6.2 — Ternary in Practice")

explain("Set a config value based on platform:")
blank()
platform = "NX-OS"
cmd("platform = 'NX-OS'")
blank()
cmd("ssh_timeout = 30 if platform == 'IOS-XE' else 60")
ssh_timeout = 30 if platform == "IOS-XE" else 60
cmd("print(ssh_timeout)")
out(ssh_timeout)
blank()

pause()

explain("Build a status label with color coding:")
blank()
inventory = [
    {"hostname": "nyc-rtr-01", "status": "up"},
    {"hostname": "lon-sw-01",  "status": "down"},
    {"hostname": "sin-fw-01",  "status": "up"},
]
cmd("inventory = [...]")
blank()
cmd("for d in inventory:")
cmd("    label = '✔ UP' if d['status'] == 'up' else '✘ DOWN'")
cmd("    print(f\"{d['hostname']:<15} {label}\")")
blank()
for d in inventory:
    label = "✔ UP" if d["status"] == "up" else "✘ DOWN"
    out(f"{d['hostname']:<15} {label}")
blank()

pause()

section("6.3 — Ternary in Comprehensions")

explain("Transform values conditionally inside a list comprehension:")
blank()
vlans = [10, 1, 20, 1002, 30]
cmd("vlans = [10, 1, 20, 1002, 30]")
blank()
cmd("labels = ['RESERVED' if v in (1, 1002, 1003, 1004, 1005) else str(v)")
cmd("          for v in vlans]")
labels = ["RESERVED" if v in (1, 1002, 1003, 1004, 1005) else str(v)
          for v in vlans]
cmd("print(labels)")
out(labels)
blank()

pause()

explain("Normalize status to a standard string:")
blank()
raw_statuses = ["up", "UP", "Up", "down", "DOWN", "unknown"]
cmd("raw_statuses = ['up', 'UP', 'Up', 'down', 'DOWN', 'unknown']")
blank()
cmd("normalized = ['up' if s.lower() == 'up' else")
cmd("              'down' if s.lower() == 'down' else")
cmd("              'unknown'")
cmd("              for s in raw_statuses]")
normalized = ["up" if s.lower() == "up" else
              "down" if s.lower() == "down" else
              "unknown"
              for s in raw_statuses]
cmd("print(normalized)")
out(normalized)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Conditionals in Loops
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Conditionals in Loops")

section("7.1 — Filtering with if")

explain("Use if inside a loop to skip items that don't qualify.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up"},
]
cmd("inventory = [  # 4 devices")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'status': 'down'},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'status': 'up'},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'status': 'up'},")
cmd("]")
blank()
cmd("for d in inventory:")
cmd("    if d['status'] == 'up' and d['platform'] == 'IOS-XE':")
cmd("        print(f\"Pushing config to {d['hostname']}\")")
blank()
for d in inventory:
    if d["status"] == "up" and d["platform"] == "IOS-XE":
        out(f"Pushing config to {d['hostname']}")
blank()

pause()

section("7.2 — break — Stop the Loop Early")

explain("break exits the loop immediately.")
explain("Use it to stop searching once you find what you need.")
blank()

cmd("target = 'lon-sw-01'")
target = "lon-sw-01"
blank()
cmd("for d in inventory:")
cmd("    if d['hostname'] == target:")
cmd("        print(f\"Found: {d}\")")
cmd("        break")
cmd("else:")
cmd("    print(f\"{target} not found in inventory\")")
blank()
for d in inventory:
    if d["hostname"] == target:
        out(f"Found: {d}")
        break
else:
    out(f"{target} not found in inventory")
blank()

pause()

section("7.3 — continue — Skip to Next Iteration")

explain("continue skips the rest of the current iteration")
explain("and moves straight to the next one.")
blank()

cmd("for d in inventory:")
cmd("    if d['status'] == 'down':")
cmd("        print(f\"Skipping {d['hostname']} — device is down\")")
cmd("        continue")
cmd("    print(f\"Processing {d['hostname']}\")")
blank()
for d in inventory:
    if d["status"] == "down":
        out(f"Skipping {d['hostname']} — device is down")
        continue
    out(f"Processing {d['hostname']}")
blank()

pause()

section("7.4 — for...else")

explain("The else block on a for loop runs ONLY if the loop")
explain("completed without hitting a break.")
explain("Use it to handle the 'not found' case cleanly.")
blank()

target = "tok-sw-01"
cmd("target = 'tok-sw-01'")
blank()
cmd("for d in inventory:")
cmd("    if d['hostname'] == target:")
cmd("        print(f\"Found {target}: {d['platform']}\")")
cmd("        break")
cmd("else:")
cmd("    print(f\"{target} not found — check your inventory\")")
blank()
for d in inventory:
    if d["hostname"] == target:
        out(f"Found {target}: {d['platform']}")
        break
else:
    out(f"{target} not found — check your inventory")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Conditionals in Comprehensions
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Conditionals in Comprehensions")

section("8.1 — Filter with if at the End")

explain("[expression for item in iterable if condition]")
explain("The if at the end FILTERS — items that fail are excluded.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down"},
]
cmd("inventory = [  # 5 devices]")
blank()

cmd("up_hosts = [d['hostname'] for d in inventory if d['status'] == 'up']")
up_hosts = [d["hostname"] for d in inventory if d["status"] == "up"]
cmd("print(up_hosts)")
out(up_hosts)
blank()

pause()

cmd("iosxe_up = [d['hostname'] for d in inventory")
cmd("            if d['platform'] == 'IOS-XE' and d['status'] == 'up']")
iosxe_up = [d["hostname"] for d in inventory
            if d["platform"] == "IOS-XE" and d["status"] == "up"]
cmd("print(iosxe_up)")
out(iosxe_up)
blank()

pause()

section("8.2 — Ternary Transform in Comprehension")

explain("[true_val if condition else false_val for item in iterable]")
explain("Every item is included — the condition transforms the value.")
blank()

cmd("status_labels = [")
cmd("    f\"{d['hostname']}: UP\" if d['status'] == 'up'")
cmd("    else f\"{d['hostname']}: DOWN\"")
cmd("    for d in inventory")
cmd("]")
status_labels = [
    f"{d['hostname']}: UP" if d["status"] == "up"
    else f"{d['hostname']}: DOWN"
    for d in inventory
]
cmd("for label in status_labels: print(label)")
blank()
for label in status_labels:
    out(label)
blank()

pause()

section("8.3 — Dict Comprehension with Condition")

explain("Same pattern works for dict comprehensions:")
blank()

cmd("up_ip_map = {d['hostname']: d.get('ip', 'N/A')")
cmd("            for d in inventory if d['status'] == 'up'}")
inventory_with_ip = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "ip": "10.2.0.1"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "ip": "10.3.0.1"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down", "ip": "10.4.0.1"},
]
up_ip_map = {d["hostname"]: d.get("ip", "N/A")
             for d in inventory_with_ip if d["status"] == "up"}
cmd("print(up_ip_map)")
out(up_ip_map)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — match / case (Python 3.10+)
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "match / case  (Python 3.10+)")

section("9.1 — Basic match / case")

explain("match/case is structural pattern matching.")
explain("It replaces long if/elif chains cleanly.")
explain("Each 'case' matches a pattern — not just a value.")
blank()

pause()

platform = "NX-OS"
cmd("platform = 'NX-OS'")
blank()
cmd("match platform:")
cmd("    case 'IOS-XE':")
cmd("        print('Catalyst / ISR — use ios_xe module')")
cmd("    case 'NX-OS':")
cmd("        print('Nexus — use nxos module')")
cmd("    case 'ASA':")
cmd("        print('Firewall — use asa module')")
cmd("    case 'IOS-XR':")
cmd("        print('Service provider — use iosxr module')")
cmd("    case _:")
cmd("        print('Unknown platform — manual review needed')")
blank()
match platform:
    case "IOS-XE":
        out("Catalyst / ISR — use ios_xe module")
    case "NX-OS":
        out("Nexus — use nxos module")
    case "ASA":
        out("Firewall — use asa module")
    case "IOS-XR":
        out("Service provider — use iosxr module")
    case _:
        out("Unknown platform — manual review needed")
blank()

pause()

section("9.2 — Matching Multiple Values")

explain("Use | to match multiple values in one case:")
blank()

platform = "FTD"
cmd("platform = 'FTD'")
blank()
cmd("match platform:")
cmd("    case 'ASA' | 'FTD':")
cmd("        print('Firewall platform')")
cmd("    case 'IOS-XE' | 'IOS-XR' | 'NX-OS':")
cmd("        print('Routing / switching platform')")
cmd("    case _:")
cmd("        print('Other')")
blank()
match platform:
    case "ASA" | "FTD":
        out("Firewall platform")
    case "IOS-XE" | "IOS-XR" | "NX-OS":
        out("Routing / switching platform")
    case _:
        out("Other")
blank()

pause()

section("9.3 — Matching on Dict Structure")

explain("match/case can pattern-match dict contents:")
blank()

device = {"hostname": "nyc-rtr-01", "status": "up", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'status': 'up', 'platform': 'IOS-XE'}")
blank()
cmd("match device:")
cmd("    case {'status': 'down'}:")
cmd("        print('Device is down — skipping')")
cmd("    case {'platform': 'IOS-XE', 'status': 'up'}:")
cmd("        print('IOS-XE device is up — push config')")
cmd("    case {'platform': 'NX-OS', 'status': 'up'}:")
cmd("        print('NX-OS device is up — push config')")
cmd("    case _:")
cmd("        print('Unhandled device state')")
blank()
match device:
    case {"status": "down"}:
        out("Device is down — skipping")
    case {"platform": "IOS-XE", "status": "up"}:
        out("IOS-XE device is up — push config")
    case {"platform": "NX-OS", "status": "up"}:
        out("NX-OS device is up — push config")
    case _:
        out("Unhandled device state")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Patterns and Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Patterns and Pitfalls")

section("10.1 — Chained Comparisons")

explain("Python allows chaining comparisons naturally:")
blank()

vlan = 25
cmd("vlan = 25")
blank()
cmd("print(1 <= vlan <= 4094)   # valid VLAN range")
out(1 <= vlan <= 4094)
cmd("print(1 <= vlan <= 10)     # access VLAN range")
out(1 <= vlan <= 10)
blank()

pause()

explain("Use this to validate ranges cleanly:")
blank()
cmd("if 1 <= vlan <= 4094:")
cmd("    if vlan in range(1002, 1006):")
cmd("        print('Reserved VLAN — do not use')")
cmd("    else:")
cmd("        print(f'VLAN {vlan} is valid')")
blank()
if 1 <= vlan <= 4094:
    if vlan in range(1002, 1006):
        out("Reserved VLAN — do not use")
    else:
        out(f"VLAN {vlan} is valid")
blank()

pause()

section("10.2 — Checking None Correctly")

explain("Always use 'is None' or 'is not None'.")
explain("Never use == None.")
blank()

ip = None
cmd("ip = None")
blank()
cmd("# Wrong")
cmd("if ip == None:")
cmd("    print('no ip')")
blank()
cmd("# Correct")
cmd("if ip is None:")
cmd("    print('IP not assigned')")
blank()
if ip is None:
    out("IP not assigned")
blank()

pause()

explain("Why? == None works but can give wrong results with")
explain("objects that override the == operator.")
explain("'is None' is always safe and signals clear intent.")

pause()

section("10.3 — Avoiding Deeply Nested Conditions")

explain("Deep nesting is hard to read and maintain.")
explain("Two techniques to flatten it:")
blank()

explain("Technique 1 — Guard clauses (early return/continue):")
blank()
cmd("for d in inventory:")
cmd("    if d['status'] != 'up': continue")
cmd("    if d['platform'] not in ('IOS-XE', 'NX-OS'): continue")
cmd("    print(f\"Push config to {d['hostname']}\")")
blank()
for d in inventory:
    if d["status"] != "up":
        continue
    if d["platform"] not in ("IOS-XE", "NX-OS"):
        continue
    out(f"Push config to {d['hostname']}")
blank()

pause()

explain("Technique 2 — Combine conditions with 'and':")
blank()
cmd("for d in inventory:")
cmd("    if d['status'] == 'up' and d['platform'] in ('IOS-XE', 'NX-OS'):")
cmd("        print(f\"Push config to {d['hostname']}\")")
blank()
for d in inventory:
    if d["status"] == "up" and d["platform"] in ("IOS-XE", "NX-OS"):
        out(f"Push config to {d['hostname']}")
blank()

pause()

section("10.4 — is vs == for Strings")

explain("Never use 'is' to compare strings.")
explain("Always use '=='.")
blank()

hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
blank()
cmd("# Wrong — 'is' compares identity not value")
cmd("if hostname is 'nyc-rtr-01':")
cmd("    print('found')")
blank()
cmd("# Correct")
cmd("if hostname == 'nyc-rtr-01':")
cmd("    print('found')")
blank()
if hostname == "nyc-rtr-01":
    out("found")
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
print(f"  {BOLD}Ch 1{RESET}   if / elif / else — syntax, only one block runs")
print(f"  {BOLD}Ch 2{RESET}   Comparison operators — == != < > in not in is")
print(f"  {BOLD}Ch 3{RESET}   Boolean operators — and, or, not, short-circuit")
print(f"  {BOLD}Ch 4{RESET}   Truthy / Falsy — [], {{}}, None, 0 are falsy")
print(f"  {BOLD}Ch 5{RESET}   Nested conditionals — guard clauses, early return")
print(f"  {BOLD}Ch 6{RESET}   Ternary — value_if_true if condition else value_if_false")
print(f"  {BOLD}Ch 7{RESET}   In loops — filter, break, continue, for...else")
print(f"  {BOLD}Ch 8{RESET}   In comprehensions — filter if, ternary transform")
print(f"  {BOLD}Ch 9{RESET}   match / case — platform routing, | multi-match, dict patterns")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — chained comparisons, is None, avoid deep nesting")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  platform checks, status filtering, VLAN validation,")
print(f"  config routing, device classification.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()