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

explain("A simple status check — the most common conditional in IaC:")
blank()
explain("status == 'up' evaluates to True, so the if block runs.")
explain("Python never evaluates elif or else once the if block fires.")
blank()
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
explain("Python tests each condition from top to bottom.")
explain("As soon as one evaluates to True its block runs and the rest are skipped.")
explain("Here platform is 'NX-OS' so the first elif fires.")
explain("The ASA elif and the else are never reached.")
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
explain("vlan is 10, not 1, so the if condition is False.")
explain("There is no else, so nothing happens — no output, no error.")
explain("Use this pattern when silence is the correct response to a non-match.")
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
explain("These are the most common operators in IaC conditionals.")
explain("== compares the VALUE of two objects — not their identity in memory.")
explain("!= is simply the negation of == — True when they differ.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'}")
blank()
cmd("print(device['platform'] == 'IOS-XE')")
out(device["platform"] == "IOS-XE")
explain("  → True — the platform value exactly matches the string 'IOS-XE'.")
blank()
cmd("print(device['platform'] == 'NX-OS')")
out(device["platform"] == "NX-OS")
explain("  → False — 'IOS-XE' does not equal 'NX-OS'.")
blank()
cmd("print(device['status'] != 'down')")
out(device["status"] != "down")
explain("  → True — status is 'up', which is not equal to 'down'.")
blank()

pause()

section("2.2 — Numeric Comparisons")

explain("< > <= >= work on numbers.")
blank()
explain("These are used for range checks — VLAN IDs, port numbers, counts.")
explain("Python compares numerically — 30 > 20 is True just as in maths.")
blank()

vlan = 30
cmd("vlan = 30")
blank()
cmd("print(vlan > 20)")
out(vlan > 20)
explain("  → True — 30 is greater than 20.")
blank()
cmd("print(vlan < 10)")
out(vlan < 10)
explain("  → False — 30 is not less than 10.")
blank()
cmd("print(vlan >= 30)")
out(vlan >= 30)
explain("  → True — 30 is equal to 30, which satisfies >=.")
blank()
cmd("print(vlan <= 29)")
out(vlan <= 29)
explain("  → False — 30 is not less than or equal to 29.")
blank()

pause()

explain("Practical use — validate VLAN range:")
blank()
explain("Python supports chained comparisons: 1 <= vlan <= 4094 is valid syntax.")
explain("It is equivalent to (1 <= vlan) and (vlan <= 4094) but reads naturally.")
explain("This is a clean way to express 'vlan is between 1 and 4094 inclusive'.")
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
explain("On a list or tuple, 'in' scans each item — O(n).")
explain("On a set or dict, 'in' uses a hash lookup — O(1).")
explain("For membership checks you repeat often, prefer sets over lists.")
blank()

vlans = [10, 20, 30, 40]
cmd("vlans = [10, 20, 30, 40]")
blank()
cmd("print(10 in vlans)")
out(10 in vlans)
explain("  → True — 10 is in the list.")
blank()
cmd("print(99 in vlans)")
out(99 in vlans)
explain("  → False — 99 is not in the list.")
blank()
cmd("print(99 not in vlans)")
out(99 not in vlans)
explain("  → True — 99 is absent, so 'not in' is True.")
blank()

pause()

explain("Check if a key exists in a dict:")
blank()
explain("'in' on a dict checks KEYS — not values.")
explain("This is O(1) — Python uses the dict's hash table directly.")
blank()
device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
blank()
cmd("print('hostname' in device)")
out("hostname" in device)
explain("  → True — 'hostname' is a key in device.")
blank()
cmd("print('vendor' in device)")
out("vendor" in device)
explain("  → False — 'vendor' has not been added to this dict.")
blank()

pause()

explain("Check if a substring exists in a string:")
blank()
explain("'in' on a string checks for a substring match.")
explain("'rtr' in 'nyc-rtr-01' is True because 'rtr' appears inside the string.")
explain("This is case-sensitive — 'RTR' would return False.")
blank()
hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
blank()
cmd("print('rtr' in hostname)")
out("rtr" in hostname)
explain("  → True — 'rtr' is found inside 'nyc-rtr-01'.")
blank()
cmd("print('sw' in hostname)")
out("sw" in hostname)
explain("  → False — 'sw' does not appear anywhere in 'nyc-rtr-01'.")
blank()

pause()

explain("Practical use — classify device by hostname:")
blank()
explain("This lets you infer the device role from a naming convention.")
explain("'rtr' in hostname matches 'nyc-rtr-01' — the if block fires.")
explain("The elif and else are never evaluated after the first match.")
explain("This works because IaC hostnames follow a structured naming standard.")
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
explain("None is a singleton — there is exactly one None object in Python.")
explain("'is None' is the canonical way to test for it because it checks")
explain("identity rather than equality, which is both faster and unambiguous.")
blank()

cmd("x = None")
x = None
cmd("print(x is None)")
out(x is None)
explain("  → True — x and None are the exact same object.")
blank()
cmd("print(x == None)   # works but not recommended")
out(x == None)
explain("  → Also True here, but == can be overridden by custom classes.")
explain("    'is None' is always safe and communicates clear intent.")
blank()

pause()

cmd("status = True")
status = True
cmd("print(status is True)")
out(status is True)
explain("  → True and False are also singletons — 'is True' is reliable.")
blank()

explain("Never use 'is' to compare strings or numbers:")
blank()
explain("Small strings and integers are cached by Python's interpreter,")
explain("so 'is' may happen to work in interactive sessions.")
explain("But this is an implementation detail — it breaks in many real scenarios.")
explain("Always use '==' for value comparisons.")
blank()
cmd("hostname = 'nyc-rtr-01'")
hostname = "nyc-rtr-01"
cmd("print(hostname == 'nyc-rtr-01')   # correct")
out(hostname == "nyc-rtr-01")
explain("  → True — value comparison, always reliable.")
blank()
cmd("print(hostname is 'nyc-rtr-01')   # wrong — unreliable")
out(hostname is "nyc-rtr-01")
explain("  → May be True here due to string interning, but do not rely on it.")
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
explain("Short-circuiting is not just a performance optimisation.")
explain("It lets you safely chain conditions where the second check")
explain("would crash if the first condition were False — like checking")
explain("a key exists before accessing its value.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'}")
blank()
explain("Both conditions must be True to enter the block.")
explain("platform == 'IOS-XE' is True AND status == 'up' is True → block runs.")
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
explain("config is None — so 'config is not None' is False.")
explain("Because 'and' short-circuits, Python stops there.")
explain("len(config) is NEVER called — which is critical because")
explain("len(None) would raise a TypeError.")
explain("Short-circuiting is the correct defence against this crash.")
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
explain("'or' short-circuits in the opposite direction to 'and'.")
explain("As soon as one True is found, the result is True and evaluation stops.")
explain("This means expensive or side-effecting checks can be skipped.")
blank()

platform = "ASA"
cmd("platform = 'ASA'")
blank()
explain("platform == 'ASA' is True, so the block runs.")
explain("Python never evaluates platform == 'FTD' because the first was True.")
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
explain("In Python, 'or' returns the first truthy value it finds.")
explain("vendor is None — None is falsy — so 'or' moves to the right side.")
explain("'Unknown' is truthy — so it is returned as the result.")
explain("When vendor is 'Cisco' (truthy), 'or' returns 'Cisco' immediately.")
explain("This is a compact way to provide a fallback value.")
blank()
cmd("vendor = None")
vendor = None
cmd("display_vendor = vendor or 'Unknown'")
display_vendor = vendor or "Unknown"
cmd("print(display_vendor)")
out(display_vendor)
explain("  → 'Unknown' — vendor is falsy so the right side is returned.")
blank()
cmd("vendor = 'Cisco'")
vendor = "Cisco"
cmd("display_vendor = vendor or 'Unknown'")
display_vendor = vendor or "Unknown"
cmd("print(display_vendor)")
out(display_vendor)
explain("  → 'Cisco' — vendor is truthy so it is returned immediately.")
blank()

pause()

section("3.3 — not")

explain("'not' inverts a boolean — True becomes False, False becomes True.")
blank()
explain("'not' is useful when the positive form of a condition is awkward to write.")
explain("'if not status == \"up\"' is equivalent to 'if status != \"up\"'.")
explain("Both work — choose whichever reads more naturally in context.")
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
explain("'not (10 in vlans and 20 in vlans)' negates the entire compound condition.")
explain("De Morgan's law says this is equivalent to: 10 not in vlans or 20 not in vlans.")
explain("Using 'not (...)' keeps the original logic visible and easy to verify.")
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
explain("Python's precedence: 'not' binds tightest, then 'and', then 'or'.")
explain("Without parentheses, 'a or b and c' means 'a or (b and c)'.")
explain("Always add parentheses around 'or' groups to make intent clear.")
blank()

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE",
          "status": "up", "vlans": [10, 20, 30]}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'status': 'up', 'vlans': [10, 20, 30]}")
blank()
explain("The parentheses around the 'or' group are essential here.")
explain("Without them 'and' would bind tighter and the logic would be wrong.")
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
explain("Checking 'platform in (\"IOS-XE\", \"NX-OS\", \"IOS-XR\")' is equivalent to")
explain("platform == 'IOS-XE' or platform == 'NX-OS' or platform == 'IOS-XR'.")
explain("The tuple form is cleaner, shorter, and easier to extend.")
explain("Using a set {\"IOS-XE\", \"NX-OS\", \"IOS-XR\"} is even faster for large groups.")
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
explain("This is why 'if vlans:' works — an empty list is falsy,")
explain("a non-empty list is truthy. No == [] needed.")
blank()

pause()

explain("bool() converts any value to its boolean equivalent:")
blank()
explain("These all evaluate to False in a conditional:")
blank()
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

explain("These all evaluate to True in a conditional:")
blank()
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
explain("'if vlans:' is the idiomatic Python way to check 'is this list non-empty?'.")
explain("It is shorter, reads naturally, and works for any container type.")
explain("Avoid 'if len(vlans) > 0:' or 'if vlans != []:' — they are redundant.")
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
explain("  → 'No VLANs configured' — empty list is falsy, else block runs.")
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
explain("  → 'Found 3 VLANs' — non-empty list is truthy, if block runs.")
blank()

pause()

config = {}
cmd("config = {}")
blank()
explain("An empty dict is falsy — 'not config' is True when the dict is empty.")
explain("This is the standard check for 'was this dict populated?'")
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
explain("None is falsy — 'if hostname:' is False when hostname is None.")
explain("This also catches empty string '' — both are falsy.")
explain("If you need to distinguish None from '', use 'if hostname is not None:'.")
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
explain("lon-sw-01 has an empty VLAN list — falsy — so the else branch runs.")
explain("nyc-rtr-01 and sin-fw-01 have non-empty lists — truthy — if branch runs.")
explain("This pattern avoids processing empty data without an explicit len() check.")
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
explain("Here checking the platform only makes sense if the device is up.")
explain("Checking the VLAN only makes sense if the platform is IOS-XE.")
explain("Each level gates the next — outer must pass before inner is evaluated.")
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
explain("The nested version forces the reader to track indentation levels.")
explain("Combining with 'and' collapses three levels into one flat check.")
explain("Both versions produce identical results — the flat version is cleaner.")
explain("Use nesting only when the inner check genuinely depends on the outer.")
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
explain("Each guard clause at the top handles one failure case and returns.")
explain("By the time you reach the final return, all guards have passed.")
explain("This is the 'fail fast' pattern — invalid inputs are rejected early.")
explain("The alternative is a deeply nested if/elif/else — much harder to read.")
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

explain("Each test device hits a different guard:")
explain("nyc-rtr-01 — passes all guards → 'OK'.")
explain("lon-sw-01  — status is 'down' → first guard fires.")
explain("sin-fw-01  — platform is 'ASA' → second guard fires.")
explain("ams-rtr-02 — vlans is empty → third guard fires.")
blank()
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
explain("Read it left to right: 'give me this value IF condition, ELSE that value'.")
explain("The expression evaluates to exactly one of the two values.")
explain("It does not run a block — it produces a value that can be assigned.")
blank()

pause()

explain("The condition is status == 'up'.")
explain("It is True, so the expression evaluates to 'reachable'.")
explain("If status were 'down', it would evaluate to 'unreachable'.")
blank()
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
explain("Use the ternary form when the logic is simple and fits on one clear line.")
explain("Use the full if/else when there are multiple statements or complex logic.")

pause()

section("6.2 — Ternary in Practice")

explain("Set a config value based on platform:")
blank()
explain("platform is 'NX-OS' — not 'IOS-XE' — so the else value (60) is used.")
explain("This is a concise way to pick between two config values without")
explain("a four-line if/else block.")
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
explain("The ternary inside the loop picks '✔ UP' or '✘ DOWN' per device.")
explain("The result is stored in label and embedded in the f-string.")
explain("{:<15} left-aligns the hostname in a 15-character column.")
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
explain("The ternary expression goes on the LEFT of 'for' — it is the value.")
explain("Every item is processed; the condition controls what VALUE it maps to.")
explain("VLANs 1 and 1002 are in the reserved tuple — they map to 'RESERVED'.")
explain("All others are converted to strings with str(v).")
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
explain("Chained ternaries: 'a if c1 else b if c2 else c'.")
explain("Python evaluates left to right — first checks if s.lower() == 'up',")
explain("then 'down', then falls back to 'unknown'.")
explain("This normalises all case variations ('UP', 'Up', 'up') to lowercase.")
explain("Chained ternaries beyond two levels get hard to read — consider a dict map.")
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
explain("The if acts as a gate — only devices that pass both conditions")
explain("reach the print statement (or the real config push logic).")
explain("lon-sw-01 is down — it fails the status check and is skipped.")
explain("sin-fw-01 is up but ASA — it fails the platform check and is skipped.")
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
explain("Once lon-sw-01 is found, there is no reason to keep scanning.")
explain("break exits the for loop entirely — ams-rtr-02 is never visited.")
explain("The for...else clause (see 7.4) tells you when break was NOT hit.")
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
explain("When lon-sw-01 is reached, status is 'down' — continue fires.")
explain("The 'Processing ...' line is skipped for that device.")
explain("The loop resumes from the top with the next item — sin-fw-01.")
explain("continue is useful when the 'skip' logic is simpler than the 'process' logic.")
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
explain("tok-sw-01 is not in inventory — the loop completes normally.")
explain("No break fires, so the else block runs and reports it was not found.")
explain("This eliminates the need for a 'found' flag variable.")
explain("Without for...else you would write: found = False, then check after the loop.")
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
explain("The if clause is evaluated for every item.")
explain("Only items where the condition is True contribute to the result.")
explain("Items that fail the condition are silently skipped — no else branch here.")
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

explain("Collect only hostnames where status is 'up':")
blank()
cmd("up_hosts = [d['hostname'] for d in inventory if d['status'] == 'up']")
up_hosts = [d["hostname"] for d in inventory if d["status"] == "up"]
cmd("print(up_hosts)")
out(up_hosts)
explain("  → lon-sw-01 and tok-sw-01 are excluded because their status is 'down'.")
blank()

pause()

explain("Chain two conditions with 'and':")
blank()
explain("Both conditions must be True — platform IOS-XE AND status up.")
explain("sin-fw-01 is up but ASA — fails the platform check.")
explain("lon-sw-01 is NX-OS and down — fails both checks.")
blank()
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
explain("This is different from filtering: ALL devices appear in the output.")
explain("The ternary decides WHAT each device maps to, not WHETHER it is included.")
explain("Devices with status 'up' get 'UP' appended; others get 'DOWN'.")
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
explain("The if clause after 'for' filters which devices become keys.")
explain("Only 'up' devices are included in the result dict.")
explain("d.get('ip', 'N/A') safely handles any device missing an 'ip' key.")
explain("The result maps each reachable hostname to its IP address.")
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
explain("  → Only the three 'up' devices appear; lon-sw-01 and tok-sw-01 are excluded.")
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
explain("match/case was introduced in Python 3.10.")
explain("It is more powerful than a simple switch statement — each case")
explain("can match a value, a type, a structure, or a combination.")
explain("The wildcard case _ catches everything that no earlier case matched.")
explain("It is equivalent to the final 'else' in an if/elif/else chain.")
blank()

pause()

explain("platform is 'NX-OS' — Python tests each case in order.")
explain("case 'IOS-XE' → no match. case 'NX-OS' → match! Block runs.")
explain("The remaining cases are never evaluated after the first match.")
blank()
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
explain("The | operator inside a case means 'or' — match any of these.")
explain("'ASA' | 'FTD' matches if platform is either 'ASA' or 'FTD'.")
explain("This is much cleaner than: elif platform == 'ASA' or platform == 'FTD'.")
explain("platform is 'FTD' — it matches the first case and that block runs.")
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
explain("This is where match/case goes beyond what if/elif can express cleanly.")
explain("Each case checks whether the dict CONTAINS those key-value pairs.")
explain("It is a structural match — extra keys in the dict are ignored.")
explain("Python tests cases in order — the first matching structure wins.")
explain("device has status='up' and platform='IOS-XE' — the second case matches.")
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
explain("1 <= vlan <= 4094 is syntactic sugar for (1 <= vlan) and (vlan <= 4094).")
explain("Python evaluates it left to right and short-circuits if any part is False.")
explain("This is unique to Python — in most other languages you need the 'and' form.")
blank()

vlan = 25
cmd("vlan = 25")
blank()
cmd("print(1 <= vlan <= 4094)   # valid VLAN range")
out(1 <= vlan <= 4094)
explain("  → True — 25 is between 1 and 4094 inclusive.")
blank()
cmd("print(1 <= vlan <= 10)     # access VLAN range")
out(1 <= vlan <= 10)
explain("  → False — 25 is not <= 10.")
blank()

pause()

explain("Use this to validate ranges cleanly:")
blank()
explain("The outer check validates the VLAN is in the legal range.")
explain("The inner check catches the reserved block (1002–1005).")
explain("range(1002, 1006) generates [1002, 1003, 1004, 1005] — stop is exclusive.")
explain("vlan is 25 — it passes the outer check and is not in the reserved range.")
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
explain("None is a singleton — only one None object ever exists in Python.")
explain("'is None' checks identity: is this the one None object? Always correct.")
explain("'== None' checks equality: can be overridden by __eq__ in custom classes.")
explain("In practice == None usually works, but 'is None' is the right habit.")
blank()

ip = None
cmd("ip = None")
blank()
cmd("# Wrong")
cmd("if ip == None:")
cmd("    print('no ip')")
blank()
explain("  This works but signals unclear intent and can break with custom objects.")
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
explain("Deeply nested if blocks are sometimes called 'arrow code' because")
explain("the indentation forms an arrow shape pointing right.")
explain("Both techniques below produce identical behaviour — one level of indentation.")
blank()

explain("Technique 1 — Guard clauses (early return/continue):")
blank()
explain("continue immediately skips to the next iteration when a check fails.")
explain("Each failed check is handled at the top — the happy path has no nesting.")
explain("This mirrors the early-return pattern from Chapter 5 but in a loop.")
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
explain("A single if with both conditions joined by 'and'.")
explain("Python short-circuits — if status != 'up' it never checks platform.")
explain("This produces exactly the same output as Technique 1.")
explain("Choose based on readability — more conditions favour Technique 1.")
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
explain("Python interns (caches) short strings as an optimisation.")
explain("For simple literals like 'nyc-rtr-01', 'is' often works in testing.")
explain("But strings built at runtime (from file reads, API calls, f-strings)")
explain("are not interned — 'is' returns False even when values match.")
explain("This creates a bug that only appears in production, not in tests.")
explain("'==' always compares the string characters — always correct.")
blank()

hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
blank()
cmd("# Wrong — 'is' compares identity not value")
cmd("if hostname is 'nyc-rtr-01':")
cmd("    print('found')")
blank()
explain("  → May work here due to interning, but breaks silently in real code.")
blank()
cmd("# Correct")
cmd("if hostname == 'nyc-rtr-01':")
cmd("    print('found')")
blank()
if hostname == "nyc-rtr-01":
    out("found")
explain("  → Always correct — compares character by character.")
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