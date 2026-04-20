# functions_deep_dive.py
# Functions in Python — Zero to Expert
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
print(f"{BOLD}         FUNCTIONS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a Function
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a Function")

section("1.1 — Definition and Purpose")

explain("A function is a named, reusable block of code.")
explain("It takes INPUTS (parameters), does something,")
explain("and optionally returns an OUTPUT (return value).")
blank()
explain("Why functions matter in Cisco IaC:")
blank()
explain("  DRY — Don't Repeat Yourself. Write once, call many times.")
explain("  Clarity — give a name to a concept: validate_device().")
explain("  Testing — test a function in isolation.")
explain("  Reuse — same function works on any device dict.")
blank()

pause()

explain("Without functions — repeated logic everywhere:")
blank()
cmd("# Without function — copy-paste for every device")
cmd("d1 = {'hostname': 'nyc-rtr-01', 'status': 'up', 'platform': 'IOS-XE'}")
cmd("d2 = {'hostname': 'lon-sw-01',  'status': 'down','platform': 'NX-OS'}")
cmd("if d1['status']=='up' and d1['platform'] in ('IOS-XE','NX-OS'):")
cmd("    print(f\"Push config to {d1['hostname']}\")")
cmd("if d2['status']=='up' and d2['platform'] in ('IOS-XE','NX-OS'):")
cmd("    print(f\"Push config to {d2['hostname']}\")")
blank()
d1 = {"hostname": "nyc-rtr-01", "status": "up",   "platform": "IOS-XE"}
d2 = {"hostname": "lon-sw-01",  "status": "down",  "platform": "NX-OS"}
if d1["status"] == "up" and d1["platform"] in ("IOS-XE", "NX-OS"):
    out(f"Push config to {d1['hostname']}")
if d2["status"] == "up" and d2["platform"] in ("IOS-XE", "NX-OS"):
    out(f"Push config to {d2['hostname']}")
blank()

pause()

explain("With a function — write once, reuse everywhere:")
blank()
cmd("def should_push(device):")
cmd("    return (device['status'] == 'up'")
cmd("            and device['platform'] in ('IOS-XE', 'NX-OS'))")
blank()

def should_push(device):
    return (device["status"] == "up"
            and device["platform"] in ("IOS-XE", "NX-OS"))

cmd("for d in [d1, d2]:")
cmd("    if should_push(d):")
cmd("        print(f\"Push config to {d['hostname']}\")")
blank()
for d in [d1, d2]:
    if should_push(d):
        out(f"Push config to {d['hostname']}")
blank()

pause()

section("1.2 — Anatomy of a Function")

explain("def       — keyword that defines a function")
explain("name      — what you call it")
explain("parameters— inputs listed in parentheses")
explain("body      — indented code block")
explain("return    — sends a value back to the caller")
blank()

cmd("def classify_device(hostname):")
cmd("    #     ^name         ^parameter")
cmd("    if 'rtr' in hostname:")
cmd("        return 'router'    # <-- return value")
cmd("    elif 'sw' in hostname:")
cmd("        return 'switch'")
cmd("    elif 'fw' in hostname:")
cmd("        return 'firewall'")
cmd("    return 'unknown'")
blank()

def classify_device(hostname):
    if "rtr" in hostname:
        return "router"
    elif "sw" in hostname:
        return "switch"
    elif "fw" in hostname:
        return "firewall"
    return "unknown"

cmd("print(classify_device('nyc-rtr-01'))")
out(classify_device("nyc-rtr-01"))
cmd("print(classify_device('lon-sw-01'))")
out(classify_device("lon-sw-01"))
cmd("print(classify_device('sin-fw-01'))")
out(classify_device("sin-fw-01"))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Defining and Calling
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Defining and Calling")

section("2.1 — A Function Without Return")

explain("Functions without return still run their body.")
explain("They implicitly return None.")
blank()

cmd("def print_device_summary(device):")
cmd("    print(f\"Hostname : {device['hostname']}\")")
cmd("    print(f\"Platform : {device['platform']}\")")
cmd("    print(f\"Status   : {device['status']}\")")
blank()

def print_device_summary(device):
    print(f"    {GREEN}Hostname : {device['hostname']}{RESET}")
    print(f"    {GREEN}Platform : {device['platform']}{RESET}")
    print(f"    {GREEN}Status   : {device['status']}{RESET}")

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'}")
cmd("print_device_summary(device)")
blank()
print_device_summary(device)
blank()

pause()

cmd("result = print_device_summary(device)")
result = None  # simulate
cmd("print(result)   # None — no return statement")
out(result)
blank()

pause()

section("2.2 — A Function With Return")

explain("return sends a value back to whoever called the function.")
explain("The caller can store, print, or use it directly.")
blank()

cmd("def get_device_label(device):")
cmd("    dtype = classify_device(device['hostname'])")
cmd("    return f\"{device['hostname']} ({dtype}) [{device['status']}]\"")
blank()

def get_device_label(device):
    dtype = classify_device(device["hostname"])
    return f"{device['hostname']} ({dtype}) [{device['status']}]"

cmd("label = get_device_label(device)")
label = get_device_label(device)
cmd("print(label)")
out(label)
blank()

pause()

explain("Call the function directly inside print():")
blank()
cmd("print(get_device_label(device))")
out(get_device_label(device))
blank()

explain("Use the return value in a list comprehension:")
blank()
inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
]
cmd("inventory = [...]")
cmd("labels = [get_device_label(d) for d in inventory]")
labels = [get_device_label(d) for d in inventory]
cmd("for l in labels: print(l)")
blank()
for l in labels:
    out(l)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Parameters Deep Dive
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Parameters Deep Dive")

section("3.1 — Positional Parameters")

explain("Arguments passed in order — position determines which")
explain("parameter receives which value.")
blank()

cmd("def build_interface_config(name, vlan, state):")
cmd("    return f'interface {name}\\n  switchport vlan {vlan}\\n  {state}'")
blank()

def build_interface_config(name, vlan, state):
    return f"interface {name}\n  switchport vlan {vlan}\n  {state}"

cmd("print(build_interface_config('Gi0/0', 10, 'no shutdown'))")
out(build_interface_config("Gi0/0", 10, "no shutdown"))
blank()

pause()

explain("Order matters — swapping gives wrong result:")
blank()
cmd("print(build_interface_config(10, 'Gi0/0', 'no shutdown'))  # wrong!")
out(build_interface_config(10, "Gi0/0", "no shutdown"))
blank()

pause()

section("3.2 — Keyword Arguments")

explain("Name the argument explicitly when calling.")
explain("Order no longer matters when using keyword args.")
blank()

cmd("print(build_interface_config(name='Gi0/0', vlan=10, state='no shutdown'))")
out(build_interface_config(name="Gi0/0", vlan=10, state="no shutdown"))
blank()
cmd("print(build_interface_config(vlan=10, state='no shutdown', name='Gi0/0'))")
out(build_interface_config(vlan=10, state="no shutdown", name="Gi0/0"))
blank()

pause()

section("3.3 — Default Parameter Values")

explain("Provide a default so the caller doesn't have to.")
explain("Parameters with defaults must come AFTER those without.")
blank()

cmd("def build_ntp_config(server, version=4, prefer=False):")
cmd("    line = f'ntp server {server} version {version}'")
cmd("    if prefer:")
cmd("        line += ' prefer'")
cmd("    return line")
blank()

def build_ntp_config(server, version=4, prefer=False):
    line = f"ntp server {server} version {version}"
    if prefer:
        line += " prefer"
    return line

cmd("print(build_ntp_config('10.0.0.100'))")
out(build_ntp_config("10.0.0.100"))
cmd("print(build_ntp_config('10.0.0.100', prefer=True))")
out(build_ntp_config("10.0.0.100", prefer=True))
cmd("print(build_ntp_config('10.0.0.100', version=3, prefer=True))")
out(build_ntp_config("10.0.0.100", version=3, prefer=True))
blank()

pause()

explain("DANGER — never use a mutable default (list or dict):")
blank()
cmd("# Wrong — same list shared across all calls!")
cmd("def add_vlan(vlan, vlan_list=[]):")
cmd("    vlan_list.append(vlan)")
cmd("    return vlan_list")
blank()

def add_vlan_bad(vlan, vlan_list=[]):
    vlan_list.append(vlan)
    return vlan_list

cmd("print(add_vlan(10))")
out(add_vlan_bad(10))
cmd("print(add_vlan(20))   # 10 is still there!")
warn(add_vlan_bad(20))
blank()

pause()

cmd("# Fix — use None as default")
cmd("def add_vlan(vlan, vlan_list=None):")
cmd("    if vlan_list is None:")
cmd("        vlan_list = []")
cmd("    vlan_list.append(vlan)")
cmd("    return vlan_list")
blank()

def add_vlan(vlan, vlan_list=None):
    if vlan_list is None:
        vlan_list = []
    vlan_list.append(vlan)
    return vlan_list

cmd("print(add_vlan(10))")
out(add_vlan(10))
cmd("print(add_vlan(20))")
out(add_vlan(20))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — *args and **kwargs
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "*args and **kwargs")

section("4.1 — *args — Variable Positional Arguments")

explain("*args collects any number of positional arguments")
explain("into a TUPLE. You don't know in advance how many.")
blank()

cmd("def push_to_devices(*hostnames):")
cmd("    print(f'Pushing to {len(hostnames)} device(s):')")
cmd("    for h in hostnames:")
cmd("        print(f'  → {h}')")
blank()

def push_to_devices(*hostnames):
    out(f"Pushing to {len(hostnames)} device(s):")
    for h in hostnames:
        out(f"  → {h}")

cmd("push_to_devices('nyc-rtr-01')")
push_to_devices("nyc-rtr-01")
blank()
cmd("push_to_devices('nyc-rtr-01', 'lon-sw-01', 'sin-fw-01')")
push_to_devices("nyc-rtr-01", "lon-sw-01", "sin-fw-01")
blank()

pause()

explain("Unpack a list into positional args with *:")
blank()
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("push_to_devices(*devices)   # unpack list as args")
push_to_devices(*devices)
blank()

pause()

section("4.2 — **kwargs — Variable Keyword Arguments")

explain("**kwargs collects any number of keyword arguments")
explain("into a DICT. Useful for flexible config builders.")
blank()

cmd("def build_device_config(hostname, **settings):")
cmd("    lines = [f'hostname {hostname}']")
cmd("    for key, value in settings.items():")
cmd("        lines.append(f'  {key} {value}')")
cmd("    return '\\n'.join(lines)")
blank()

def build_device_config(hostname, **settings):
    lines = [f"hostname {hostname}"]
    for key, value in settings.items():
        lines.append(f"  {key} {value}")
    return "\n".join(lines)

cmd("config = build_device_config(")
cmd("    'nyc-rtr-01',")
cmd("    ntp='10.0.0.100',")
cmd("    dns='8.8.8.8',")
cmd("    domain='corp.net'")
cmd(")")
cmd("print(config)")
config = build_device_config(
    "nyc-rtr-01",
    ntp="10.0.0.100",
    dns="8.8.8.8",
    domain="corp.net"
)
blank()
for line in config.split("\n"):
    out(line)
blank()

pause()

explain("Unpack a dict into keyword args with **:")
blank()
settings = {"ntp": "10.0.0.100", "dns": "8.8.8.8", "domain": "corp.net"}
cmd("settings = {'ntp': '10.0.0.100', 'dns': '8.8.8.8', 'domain': 'corp.net'}")
cmd("config = build_device_config('lon-sw-01', **settings)")
config = build_device_config("lon-sw-01", **settings)
cmd("print(config)")
blank()
for line in config.split("\n"):
    out(line)
blank()

pause()

section("4.3 — Combining *args and **kwargs")

explain("Use both together for maximum flexibility.")
explain("Order: positional, *args, keyword with defaults, **kwargs")
blank()

cmd("def deploy(platform, *hostnames, dry_run=False, **config):")
cmd("    mode = 'DRY RUN' if dry_run else 'LIVE'")
cmd("    print(f'[{mode}] Deploying to {len(hostnames)} {platform} device(s)')")
cmd("    for h in hostnames:")
cmd("        print(f'  Target: {h}')")
cmd("    if config:")
cmd("        print(f'  Config: {config}')")
blank()

def deploy(platform, *hostnames, dry_run=False, **config):
    mode = "DRY RUN" if dry_run else "LIVE"
    out(f"[{mode}] Deploying to {len(hostnames)} {platform} device(s)")
    for h in hostnames:
        out(f"  Target: {h}")
    if config:
        out(f"  Config: {config}")

cmd("deploy('IOS-XE', 'nyc-rtr-01', 'ams-rtr-02', dry_run=True, ntp='10.0.0.100')")
deploy("IOS-XE", "nyc-rtr-01", "ams-rtr-02", dry_run=True, ntp="10.0.0.100")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Return Values
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Return Values")

section("5.1 — Returning a Single Value")

explain("return sends exactly one object back to the caller.")
explain("That object can be anything — string, int, list, dict, bool.")
blank()

cmd("def count_up_devices(inventory):")
cmd("    return sum(1 for d in inventory if d['status'] == 'up')")
blank()

def count_up_devices(inventory):
    return sum(1 for d in inventory if d["status"] == "up")

inventory = [
    {"hostname": "nyc-rtr-01", "status": "up"},
    {"hostname": "lon-sw-01",  "status": "down"},
    {"hostname": "sin-fw-01",  "status": "up"},
]
cmd("inventory = [...]")
cmd("print(count_up_devices(inventory))")
out(count_up_devices(inventory))
blank()

pause()

section("5.2 — Returning Multiple Values")

explain("Python functions can return multiple values as a tuple.")
explain("The caller unpacks them in one line.")
blank()

cmd("def partition_inventory(inventory):")
cmd("    up   = [d['hostname'] for d in inventory if d['status'] == 'up']")
cmd("    down = [d['hostname'] for d in inventory if d['status'] == 'down']")
cmd("    return up, down   # returns a tuple")
blank()

def partition_inventory(inventory):
    up   = [d["hostname"] for d in inventory if d["status"] == "up"]
    down = [d["hostname"] for d in inventory if d["status"] == "down"]
    return up, down

cmd("up_hosts, down_hosts = partition_inventory(inventory)")
up_hosts, down_hosts = partition_inventory(inventory)
cmd("print('Up:',   up_hosts)")
out(f"Up:   {up_hosts}")
cmd("print('Down:', down_hosts)")
out(f"Down: {down_hosts}")
blank()

pause()

explain("Or capture as a single tuple:")
blank()
cmd("result = partition_inventory(inventory)")
result = partition_inventory(inventory)
cmd("print(result)         # tuple")
out(result)
cmd("print(result[0])      # up list")
out(result[0])
blank()

pause()

section("5.3 — Early Return")

explain("Return as soon as you know the answer.")
explain("This is the guard clause pattern — flattens nesting.")
blank()

cmd("def validate_vlan(vlan):")
cmd("    if not isinstance(vlan, int):")
cmd("        return False, 'VLAN must be an integer'")
cmd("    if vlan < 1 or vlan > 4094:")
cmd("        return False, f'VLAN {vlan} out of range (1-4094)'")
cmd("    if vlan in {1, 1002, 1003, 1004, 1005}:")
cmd("        return False, f'VLAN {vlan} is reserved'")
cmd("    return True, 'valid'")
blank()

def validate_vlan(vlan):
    if not isinstance(vlan, int):
        return False, "VLAN must be an integer"
    if vlan < 1 or vlan > 4094:
        return False, f"VLAN {vlan} out of range (1-4094)"
    if vlan in {1, 1002, 1003, 1004, 1005}:
        return False, f"VLAN {vlan} is reserved"
    return True, "valid"

pause()

for test in [10, 0, 1002, "twenty", 4095]:
    cmd(f"print(validate_vlan({test!r}))")
    out(validate_vlan(test))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Scope
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Scope")

section("6.1 — Local vs Global")

explain("Variables defined INSIDE a function are LOCAL.")
explain("They only exist while the function runs.")
explain("Variables defined OUTSIDE are GLOBAL.")
blank()

cmd("ntp_server = '10.0.0.100'   # global")
ntp_server = "10.0.0.100"
blank()
cmd("def get_ntp():")
cmd("    local_var = 'I only exist here'")
cmd("    return ntp_server   # can READ global")
blank()

def get_ntp():
    local_var = "I only exist here"
    return ntp_server

cmd("print(get_ntp())")
out(get_ntp())
blank()
cmd("print(local_var)   # NameError — local_var doesn't exist here")
blank()
try:
    print(local_var)
except NameError as e:
    warn(f"NameError: {e}")
blank()

pause()

section("6.2 — The LEGB Rule")

explain("Python searches for a name in this order:")
blank()
explain("  L — Local       (inside current function)")
explain("  E — Enclosing   (outer function if nested)")
explain("  G — Global      (module level)")
explain("  B — Built-in    (Python's built-in names)")
blank()

cmd("x = 'global'")
x = "global"
blank()
cmd("def outer():")
cmd("    x = 'enclosing'")
cmd("    def inner():")
cmd("        x = 'local'")
cmd("        print(x)   # finds 'local' first")
cmd("    inner()")
cmd("    print(x)       # finds 'enclosing'")
cmd("outer()")
cmd("print(x)           # finds 'global'")
blank()

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        out(x)
    inner()
    out(x)

outer()
out(x)
blank()

pause()

section("6.3 — global Keyword and Why to Avoid It")

explain("'global' lets a function modify a global variable.")
explain("Avoid it in IaC — it creates hidden dependencies.")
blank()

cmd("push_count = 0")
push_count = 0
blank()
cmd("def push_config(hostname):")
cmd("    global push_count   # modify the global")
cmd("    push_count += 1")
cmd("    print(f'Pushing to {hostname} (total: {push_count})')")
blank()

def push_config(hostname):
    global push_count
    push_count += 1
    out(f"Pushing to {hostname} (total: {push_count})")

cmd("push_config('nyc-rtr-01')")
push_config("nyc-rtr-01")
cmd("push_config('lon-sw-01')")
push_config("lon-sw-01")
blank()

pause()

explain("Better — pass state as a parameter, return updated state:")
blank()
cmd("def push_config(hostname, count):")
cmd("    count += 1")
cmd("    print(f'Pushing to {hostname} (total: {count})')")
cmd("    return count")
blank()

def push_config_clean(hostname, count):
    count += 1
    out(f"Pushing to {hostname} (total: {count})")
    return count

cmd("count = 0")
count = 0
cmd("count = push_config('nyc-rtr-01', count)")
count = push_config_clean("nyc-rtr-01", count)
cmd("count = push_config('lon-sw-01', count)")
count = push_config_clean("lon-sw-01", count)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Docstrings and Type Hints
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Docstrings and Type Hints")

section("7.1 — Docstrings")

explain("A docstring is the first string inside a function.")
explain("It documents what the function does, its parameters,")
explain("and what it returns. Triple quotes, any length.")
blank()

cmd("def validate_device(device, global_ntp='10.0.0.100'):")
cmd("    \"\"\"")
cmd("    Validate a device dict against standard IaC rules.")
cmd("")
cmd("    Args:")
cmd("        device (dict): Device dict with hostname, platform,")
cmd("                       status, vlans, config keys.")
cmd("        global_ntp (str): Expected NTP server. Default 10.0.0.100.")
cmd("")
cmd("    Returns:")
cmd("        tuple: (bool, str) — (is_valid, message)")
cmd("    \"\"\"")
cmd("    if device['status'] != 'up':")
cmd("        return False, 'device is down'")
cmd("    return True, 'valid'")
blank()

def validate_device_doc(device, global_ntp="10.0.0.100"):
    """
    Validate a device dict against standard IaC rules.

    Args:
        device (dict): Device dict with hostname, platform,
                       status, vlans, config keys.
        global_ntp (str): Expected NTP server. Default 10.0.0.100.

    Returns:
        tuple: (bool, str) — (is_valid, message)
    """
    if device["status"] != "up":
        return False, "device is down"
    return True, "valid"

cmd("print(validate_device_doc.__doc__)")
out(validate_device_doc.__doc__)
blank()

pause()

section("7.2 — Type Hints")

explain("Type hints annotate what types parameters and")
explain("return values should be. Python does NOT enforce them —")
explain("they are documentation and help IDE tools.")
blank()

cmd("def get_platform_devices(")
cmd("        inventory: list[dict],")
cmd("        platform: str")
cmd(") -> list[str]:")
cmd("    \"\"\"Return hostnames of devices matching platform.\"\"\"")
cmd("    return [d['hostname'] for d in inventory")
cmd("            if d['platform'] == platform]")
blank()

def get_platform_devices(
        inventory: list,
        platform: str
) -> list:
    """Return hostnames of devices matching platform."""
    return [d["hostname"] for d in inventory
            if d["platform"] == platform]

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE"},
]
cmd("print(get_platform_devices(inventory, 'IOS-XE'))")
out(get_platform_devices(inventory, "IOS-XE"))
blank()

pause()

explain("Common type hints in IaC:")
blank()
cmd("def example(")
cmd("    hostname: str,")
cmd("    vlan: int,")
cmd("    vlans: list[int],")
cmd("    config: dict[str, str],")
cmd("    enabled: bool = True,")
cmd("    ntp: str | None = None,")
cmd(") -> dict:")
cmd("    ...")
blank()
explain("str | None means 'either a string or None' (Python 3.10+)")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — First-Class Functions
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "First-Class Functions")

section("8.1 — Functions Are Objects")

explain("In Python, functions are objects like any other.")
explain("You can assign them to variables, store them in lists,")
explain("pass them as arguments, and return them from functions.")
blank()

cmd("def classify_router(hostname):")
cmd("    return 'rtr' in hostname")
blank()
cmd("def classify_switch(hostname):")
cmd("    return 'sw' in hostname")
blank()

def classify_router(hostname):
    return "rtr" in hostname

def classify_switch(hostname):
    return "sw" in hostname

cmd("# Assign function to a variable")
cmd("check = classify_router")
check = classify_router
cmd("print(check('nyc-rtr-01'))")
out(check("nyc-rtr-01"))
blank()

cmd("# Store functions in a list")
cmd("classifiers = [classify_router, classify_switch]")
classifiers = [classify_router, classify_switch]
cmd("for fn in classifiers:")
cmd("    print(fn('nyc-rtr-01'))")
blank()
for fn in classifiers:
    out(fn("nyc-rtr-01"))
blank()

pause()

section("8.2 — Passing Functions as Arguments")

explain("Pass a function in as a parameter — the caller decides")
explain("what behaviour to use.")
blank()

cmd("def filter_inventory(inventory, condition):")
cmd("    return [d for d in inventory if condition(d)]")
blank()

def filter_inventory(inventory, condition):
    return [d for d in inventory if condition(d)]

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
]
cmd("inventory = [  # 3 devices ]")
blank()

cmd("def is_up(d): return d['status'] == 'up'")
cmd("def is_iosxe(d): return d['platform'] == 'IOS-XE'")
blank()

def is_up(d):    return d["status"] == "up"
def is_iosxe(d): return d["platform"] == "IOS-XE"

cmd("up    = filter_inventory(inventory, is_up)")
up = filter_inventory(inventory, is_up)
cmd("iosxe = filter_inventory(inventory, is_iosxe)")
iosxe = filter_inventory(inventory, is_iosxe)
cmd("print([d['hostname'] for d in up])")
out([d["hostname"] for d in up])
cmd("print([d['hostname'] for d in iosxe])")
out([d["hostname"] for d in iosxe])
blank()

pause()

section("8.3 — key= in sorted() and max()")

explain("The key= parameter takes a function.")
explain("That function extracts the sort/comparison value.")
blank()

inventory_v = [
    {"hostname": "sin-fw-01",  "vlans": [30,40,50]},
    {"hostname": "nyc-rtr-01", "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "vlans": [10,20]},
    {"hostname": "ams-rtr-02", "vlans": [10,20,30,40]},
]
cmd("inventory_v = [  # 4 devices ]")
blank()

cmd("# Sort by number of VLANs")
cmd("sorted_v = sorted(inventory_v, key=lambda d: len(d['vlans']))")
sorted_v = sorted(inventory_v, key=lambda d: len(d["vlans"]))
cmd("for d in sorted_v: print(d['hostname'], len(d['vlans']))")
blank()
for d in sorted_v:
    out(f"{d['hostname']} {len(d['vlans'])}")
blank()

pause()

cmd("# Device with most VLANs")
cmd("busiest = max(inventory_v, key=lambda d: len(d['vlans']))")
busiest = max(inventory_v, key=lambda d: len(d["vlans"]))
cmd("print(busiest['hostname'])")
out(busiest["hostname"])
blank()

cmd("# Sort by hostname alphabetically")
cmd("by_name = sorted(inventory_v, key=lambda d: d['hostname'])")
by_name = sorted(inventory_v, key=lambda d: d["hostname"])
cmd("print([d['hostname'] for d in by_name])")
out([d["hostname"] for d in by_name])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Lambda Functions
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Lambda Functions")

section("9.1 — Syntax and Basic Use")

explain("A lambda is an anonymous function — one expression,")
explain("no def, no return keyword, no name required.")
blank()
explain("Syntax:  lambda parameters: expression")
blank()

cmd("# Named function")
cmd("def double(x):")
cmd("    return x * 2")
blank()
cmd("# Equivalent lambda")
cmd("double = lambda x: x * 2")
double = lambda x: x * 2
cmd("print(double(5))")
out(double(5))
blank()

pause()

explain("Lambda with multiple parameters:")
blank()
cmd("make_label = lambda hostname, status: f'{hostname}: {status}'")
make_label = lambda hostname, status: f"{hostname}: {status}"
cmd("print(make_label('nyc-rtr-01', 'up'))")
out(make_label("nyc-rtr-01", "up"))
blank()

pause()

section("9.2 — Lambda in Practice")

explain("Lambda shines when a short function is passed inline.")
blank()

inventory = [
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
]
cmd("inventory = [  # 3 devices ]")
blank()

cmd("# Sort by platform")
cmd("by_platform = sorted(inventory, key=lambda d: d['platform'])")
by_platform = sorted(inventory, key=lambda d: d["platform"])
cmd("print([d['hostname'] for d in by_platform])")
out([d["hostname"] for d in by_platform])
blank()

pause()

cmd("# Sort by status then hostname")
cmd("by_status = sorted(inventory, key=lambda d: (d['status'], d['hostname']))")
by_status = sorted(inventory, key=lambda d: (d["status"], d["hostname"]))
cmd("for d in by_status: print(d['status'], d['hostname'])")
blank()
for d in by_status:
    out(f"{d['status']} {d['hostname']}")
blank()

pause()

section("9.3 — When to Use Lambda vs Named Function")

explain("Use LAMBDA when:")
explain("  — the function is short (one expression)")
explain("  — it is only used once, inline")
explain("  — it is passed to sorted(), max(), map(), filter()")
blank()
explain("Use a NAMED FUNCTION when:")
explain("  — the logic spans more than one expression")
explain("  — you need a docstring")
explain("  — you will reuse it in multiple places")
explain("  — the name makes the code more readable")
blank()

cmd("# Lambda — clean and appropriate")
cmd("sorted(inventory, key=lambda d: d['hostname'])")
blank()

cmd("# Lambda — too complex, use named function instead")
cmd("sorted(inventory, key=lambda d: (d['status']!='up', d['platform'], d['hostname']))")
blank()

cmd("# Named function — clearer intent")
cmd("def sort_key(d):")
cmd("    # up devices first, then by platform, then by hostname")
cmd("    return (d['status'] != 'up', d['platform'], d['hostname'])")
cmd("sorted(inventory, key=sort_key)")
blank()

def sort_key(d):
    return (d["status"] != "up", d["platform"], d["hostname"])

result = sorted(inventory, key=sort_key)
cmd("for d in sorted(inventory, key=sort_key):")
cmd("    print(d['status'], d['platform'], d['hostname'])")
blank()
for d in result:
    out(f"{d['status']} {d['platform']} {d['hostname']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common IaC Function Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common IaC Function Patterns")

section("10.1 — Validator")

explain("A validator checks a device or config and returns")
explain("(is_valid, reason). Uses early returns.")
blank()

cmd("def validate_device(device, global_ntp='10.0.0.100'):")
cmd("    if device['status'] != 'up':")
cmd("        return False, 'device is down'")
cmd("    if device['platform'] not in ('IOS-XE','NX-OS','ASA'):")
cmd("        return False, 'unsupported platform'")
cmd("    if not device.get('vlans'):")
cmd("        return False, 'no VLANs configured'")
cmd("    if device.get('config',{}).get('ntp') != global_ntp:")
cmd("        return False, 'non-standard NTP'")
cmd("    return True, 'valid'")
blank()

def validate_device(device, global_ntp="10.0.0.100"):
    if device["status"] != "up":
        return False, "device is down"
    if device["platform"] not in ("IOS-XE", "NX-OS", "ASA"):
        return False, "unsupported platform"
    if not device.get("vlans"):
        return False, "no VLANs configured"
    if device.get("config", {}).get("ntp") != global_ntp:
        return False, "non-standard NTP"
    return True, "valid"

pause()

test_devices = [
    {"hostname": "nyc-rtr-01", "status": "up",   "platform": "IOS-XE",
     "vlans": [10,20], "config": {"ntp": "10.0.0.100"}},
    {"hostname": "lon-sw-01",  "status": "down",  "platform": "NX-OS",
     "vlans": [10],    "config": {"ntp": "10.0.0.100"}},
    {"hostname": "mum-rtr-01", "status": "up",   "platform": "IOS-XE",
     "vlans": [20,30], "config": {"ntp": "10.7.0.100"}},
]
cmd("for d in test_devices:")
cmd("    ok, msg = validate_device(d)")
cmd("    print(f\"{d['hostname']}: {msg}\")")
blank()
for d in test_devices:
    ok, msg = validate_device(d)
    out(f"{d['hostname']}: {msg}")
blank()

pause()

section("10.2 — Config Generator")

explain("Takes a device dict and returns config text.")
blank()

cmd("def generate_ntp_config(device, ntp_servers):")
cmd("    \"\"\"Generate NTP config block for a device.\"\"\"")
cmd("    lines = [f\"! NTP config for {device['hostname']}\"")
cmd("    for ntp in ntp_servers:")
cmd("        lines.append(f'ntp server {ntp}')")
cmd("    lines.append('ntp update-calendar')")
cmd("    return '\\n'.join(lines)")
blank()

def generate_ntp_config(device, ntp_servers):
    """Generate NTP config block for a device."""
    lines = [f"! NTP config for {device['hostname']}"]
    for ntp in ntp_servers:
        lines.append(f"ntp server {ntp}")
    lines.append("ntp update-calendar")
    return "\n".join(lines)

device = {"hostname": "nyc-rtr-01", "platform": "IOS-XE"}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE'}")
cmd("config = generate_ntp_config(device, ['10.0.0.100', '10.0.0.101'])")
config = generate_ntp_config(device, ["10.0.0.100", "10.0.0.101"])
cmd("print(config)")
blank()
for line in config.split("\n"):
    out(line)
blank()

pause()

section("10.3 — Function as a Pipeline Step")

explain("Small, focused functions chained together.")
explain("Each does one thing — easy to test, easy to swap.")
blank()

cmd("def load_inventory(raw):        return [{**d} for d in raw]")
cmd("def filter_up(inventory):       return [d for d in inventory if d['status']=='up']")
cmd("def filter_supported(inventory):")
cmd("    return [d for d in inventory if d['platform'] in ('IOS-XE','NX-OS','ASA')]")
cmd("def enrich(inventory):")
cmd("    return [{**d,'vlan_count':len(d.get('vlans',[]))} for d in inventory]")
cmd("def sort_by_hostname(inventory): return sorted(inventory, key=lambda d: d['hostname'])")
blank()

def load_inventory(raw):        return [{**d} for d in raw]
def filter_up(inventory):       return [d for d in inventory if d["status"] == "up"]
def filter_supported(inventory):
    return [d for d in inventory if d["platform"] in ("IOS-XE", "NX-OS", "ASA")]
def enrich(inventory):
    return [{**d, "vlan_count": len(d.get("vlans", []))} for d in inventory]
def sort_by_hostname(inventory): return sorted(inventory, key=lambda d: d["hostname"])

pause()

raw = [
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40]},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
]
cmd("raw = [  # 4 devices ]")
blank()
cmd("result = sort_by_hostname(")
cmd("            enrich(")
cmd("                filter_supported(")
cmd("                    filter_up(")
cmd("                        load_inventory(raw)))))")
result = sort_by_hostname(enrich(filter_supported(filter_up(load_inventory(raw)))))
cmd("for d in result:")
cmd("    print(d['hostname'], d['platform'], d['vlan_count'], 'vlans')")
blank()
for d in result:
    out(f"{d['hostname']} {d['platform']} {d['vlan_count']} vlans")
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
print(f"  {BOLD}Ch 1{RESET}   What is a function — DRY, anatomy, def/return")
print(f"  {BOLD}Ch 2{RESET}   Defining and calling — with/without return, reuse")
print(f"  {BOLD}Ch 3{RESET}   Parameters — positional, keyword, defaults, mutable default bug")
print(f"  {BOLD}Ch 4{RESET}   *args and **kwargs — variable args, unpacking with */**, combining")
print(f"  {BOLD}Ch 5{RESET}   Return values — single, multiple, early return, guard clauses")
print(f"  {BOLD}Ch 6{RESET}   Scope — local/global, LEGB rule, avoid global keyword")
print(f"  {BOLD}Ch 7{RESET}   Docstrings and type hints — document, annotate, IDE support")
print(f"  {BOLD}Ch 8{RESET}   First-class functions — pass as arg, key=, callbacks")
print(f"  {BOLD}Ch 9{RESET}   Lambda — syntax, inline use, when to use named function instead")
print(f"  {BOLD}Ch 10{RESET}  IaC patterns — validator, config generator, function pipeline")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  device dicts, NTP configs, VLAN validation,")
print(f"  config generation, deployment pipelines.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()