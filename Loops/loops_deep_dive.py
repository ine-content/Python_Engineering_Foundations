# loops_deep_dive.py
# Loops in Python — Zero to Expert
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
print(f"{BOLD}         LOOPS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a Loop
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a Loop")

section("1.1 — Definition")

explain("A loop repeats a block of code multiple times.")
explain("Without loops you would have to write the same")
explain("code once for every device, every interface,")
explain("every VLAN — which is impossible at scale.")
blank()
explain("Python has two kinds of loop:")
blank()
explain("  for   — iterates over a sequence of items.")
explain("          You know in advance what to iterate over.")
blank()
explain("  while — repeats as long as a condition is True.")
explain("          You don't know how many times upfront.")
blank()

pause()

section("1.2 — The Loop Variable")

explain("In a for loop, the loop variable takes the value")
explain("of each item in the sequence one at a time.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
cmd("for device in devices:")
cmd("    print(device)")
blank()
for device in devices:
    out(device)
blank()

pause()

explain("'device' is the loop variable — it changes each iteration.")
explain("The name is arbitrary. 'for d in devices' works too.")
explain("After the loop, 'device' holds the LAST value:")
blank()
cmd("print(device)   # last value after loop ends")
out(device)
blank()

pause()

explain("Use _ when you don't need the loop variable:")
blank()
cmd("for _ in range(3):")
cmd("    print('Retrying connection...')")
blank()
for _ in range(3):
    out("Retrying connection...")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — for Loop Deep Dive
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "for Loop Deep Dive")

section("2.1 — Iterating Different Types")

explain("for loops work on any iterable — lists, tuples,")
explain("strings, dicts, sets, ranges, and more.")
blank()

explain("Iterating a tuple:")
blank()
ntp_servers = ("10.0.0.100", "10.0.0.101", "10.0.0.102")
cmd("ntp_servers = ('10.0.0.100', '10.0.0.101', '10.0.0.102')")
cmd("for ntp in ntp_servers:")
cmd("    print(ntp)")
blank()
for ntp in ntp_servers:
    out(ntp)
blank()

pause()

explain("Iterating a string — character by character:")
blank()
hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
cmd("for char in hostname:")
cmd("    print(char, end=' ')")
blank()
out(" ".join(hostname))
blank()

pause()

explain("Iterating a set — order is not guaranteed:")
blank()
platforms = {"IOS-XE", "NX-OS", "ASA"}
cmd("platforms = {'IOS-XE', 'NX-OS', 'ASA'}")
cmd("for p in sorted(platforms):   # sort for consistent order")
cmd("    print(p)")
blank()
for p in sorted(platforms):
    out(p)
blank()

pause()

section("2.2 — range() Patterns")

explain("range(stop)           → 0 to stop-1")
explain("range(start, stop)    → start to stop-1")
explain("range(start, stop, step) → with step size")
blank()

cmd("for i in range(5):")
cmd("    print(i, end=' ')")
blank()
out(" ".join(str(i) for i in range(5)))
blank()

pause()

cmd("for i in range(1, 6):")
cmd("    print(i, end=' ')")
blank()
out(" ".join(str(i) for i in range(1, 6)))
blank()

cmd("for i in range(0, 50, 10):")
cmd("    print(i, end=' ')")
blank()
out(" ".join(str(i) for i in range(0, 50, 10)))
blank()

pause()

explain("Countdown — negative step:")
blank()
cmd("for i in range(5, 0, -1):")
cmd("    print(f'Retry {i}...')")
blank()
for i in range(5, 0, -1):
    out(f"Retry {i}...")
blank()

pause()

explain("Use range(len()) to iterate with index access:")
blank()
interfaces = ["Gi0/0", "Gi0/1", "Gi0/2"]
cmd("interfaces = ['Gi0/0', 'Gi0/1', 'Gi0/2']")
cmd("for i in range(len(interfaces)):")
cmd("    print(f'Index {i}: {interfaces[i]}')")
blank()
for i in range(len(interfaces)):
    out(f"Index {i}: {interfaces[i]}")
blank()

pause()

section("2.3 — Unpacking in a for Loop")

explain("Unpack tuples or lists directly in the loop header:")
blank()

pairs = [("nyc-rtr-01", "10.0.0.1"), ("lon-sw-01", "10.1.0.1")]
cmd("pairs = [('nyc-rtr-01', '10.0.0.1'), ('lon-sw-01', '10.1.0.1')]")
cmd("for hostname, ip in pairs:")
cmd("    print(f'{hostname} → {ip}')")
blank()
for hostname, ip in pairs:
    out(f"{hostname} → {ip}")
blank()

pause()

explain("Unpack three values at once:")
blank()
records = [
    ("nyc-rtr-01", "IOS-XE", "up"),
    ("lon-sw-01",  "NX-OS",  "down"),
]
cmd("records = [('nyc-rtr-01','IOS-XE','up'), ('lon-sw-01','NX-OS','down')]")
cmd("for hostname, platform, status in records:")
cmd("    print(f'{hostname}: {platform} [{status}]')")
blank()
for hostname, platform, status in records:
    out(f"{hostname}: {platform} [{status}]")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — while Loop Deep Dive
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "while Loop Deep Dive")

section("3.1 — Basic while Loop")

explain("while repeats as long as the condition is True.")
explain("Use it when you don't know how many iterations upfront.")
blank()

cmd("count = 0")
count = 0
cmd("while count < 3:")
cmd("    print(f'Polling device... attempt {count + 1}')")
cmd("    count += 1")
blank()
count = 0
while count < 3:
    out(f"Polling device... attempt {count + 1}")
    count += 1
blank()

pause()

section("3.2 — Retry Pattern")

explain("A common IaC pattern — retry until success or max retries:")
blank()

cmd("max_retries = 3")
cmd("attempt     = 0")
cmd("connected   = False")
blank()
cmd("while attempt < max_retries and not connected:")
cmd("    attempt += 1")
cmd("    print(f'Attempt {attempt}: connecting to nyc-rtr-01...')")
cmd("    if attempt == 2:")
cmd("        connected = True")
cmd("        print('Connected!')")
blank()
max_retries = 3
attempt     = 0
connected   = False
while attempt < max_retries and not connected:
    attempt += 1
    out(f"Attempt {attempt}: connecting to nyc-rtr-01...")
    if attempt == 2:
        connected = True
        out("Connected!")
blank()

pause()

section("3.3 — while True with break")

explain("'while True' creates an infinite loop.")
explain("Use break to exit when a condition is met.")
explain("This is cleaner than a flag variable in many cases.")
blank()

devices_to_process = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices_to_process = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
cmd("while True:")
cmd("    if not devices_to_process:")
cmd("        print('Queue empty — done.')")
cmd("        break")
cmd("    device = devices_to_process.pop(0)")
cmd("    print(f'Processing {device}')")
blank()
devices_to_process = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
while True:
    if not devices_to_process:
        out("Queue empty — done.")
        break
    device = devices_to_process.pop(0)
    out(f"Processing {device}")
blank()

pause()

section("3.4 — while...else")

explain("The else block on a while runs ONLY if the loop")
explain("condition became False naturally — not from break.")
blank()

cmd("attempts = 0")
cmd("max_attempts = 3")
blank()
cmd("while attempts < max_attempts:")
cmd("    attempts += 1")
cmd("    print(f'Attempt {attempts}')")
cmd("else:")
cmd("    print('Max attempts reached — giving up')")
blank()
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    out(f"Attempt {attempts}")
else:
    out("Max attempts reached — giving up")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — enumerate() and zip()
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "enumerate() and zip()")

section("4.1 — enumerate() — Index and Value Together")

explain("enumerate() gives (index, value) pairs.")
explain("No need to manage an index counter manually.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "status": "up"},
    {"hostname": "lon-sw-01",  "status": "down"},
    {"hostname": "sin-fw-01",  "status": "up"},
]
cmd("inventory = [...]   # 3 devices")
blank()
cmd("for i, device in enumerate(inventory):")
cmd("    print(f'{i}: {device[\"hostname\"]} [{device[\"status\"]}]')")
blank()
for i, device in enumerate(inventory):
    out(f"{i}: {device['hostname']} [{device['status']}]")
blank()

pause()

explain("Start numbering from 1:")
blank()
cmd("for i, device in enumerate(inventory, start=1):")
cmd("    print(f'Device {i} of {len(inventory)}: {device[\"hostname\"]}')")
blank()
for i, device in enumerate(inventory, start=1):
    out(f"Device {i} of {len(inventory)}: {device['hostname']}")
blank()

pause()

explain("Use index to modify specific items safely:")
blank()
vlans = [10, 20, 30, 40]
cmd("vlans = [10, 20, 30, 40]")
cmd("for i, vlan in enumerate(vlans):")
cmd("    if vlan == 20:")
cmd("        vlans[i] = 200")
cmd("print(vlans)")
for i, vlan in enumerate(vlans):
    if vlan == 20:
        vlans[i] = 200
out(vlans)
blank()

pause()

section("4.2 — zip() — Iterate Two Lists Together")

explain("zip() pairs items from two or more iterables.")
explain("Stops at the shortest one.")
blank()

hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
ips       = ["10.0.0.1",   "10.1.0.1",  "10.2.0.1"]
platforms = ["IOS-XE",     "NX-OS",     "ASA"]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("ips       = ['10.0.0.1',   '10.1.0.1',  '10.2.0.1']")
cmd("platforms = ['IOS-XE',     'NX-OS',     'ASA']")
blank()
cmd("for h, ip, p in zip(hostnames, ips, platforms):")
cmd("    print(f'{h}: {ip} ({p})')")
blank()
for h, ip, p in zip(hostnames, ips, platforms):
    out(f"{h}: {ip} ({p})")
blank()

pause()

explain("Build a list of dicts from parallel lists:")
blank()
cmd("devices = [")
cmd("    {'hostname': h, 'ip': ip, 'platform': p}")
cmd("    for h, ip, p in zip(hostnames, ips, platforms)")
cmd("]")
devices = [
    {"hostname": h, "ip": ip, "platform": p}
    for h, ip, p in zip(hostnames, ips, platforms)
]
cmd("for d in devices: print(d)")
blank()
for d in devices:
    out(d)
blank()

pause()

section("4.3 — zip_longest() — Pad Shorter Lists")

explain("zip_longest() from itertools continues until the")
explain("LONGEST list is exhausted, filling gaps with a default.")
blank()

from itertools import zip_longest
primaries   = ["10.0.0.100", "10.1.0.100"]
secondaries = ["10.0.0.101", "10.1.0.101", "10.2.0.101"]
cmd("from itertools import zip_longest")
cmd("primaries   = ['10.0.0.100', '10.1.0.100']")
cmd("secondaries = ['10.0.0.101', '10.1.0.101', '10.2.0.101']")
blank()
cmd("for pri, sec in zip_longest(primaries, secondaries, fillvalue='N/A'):")
cmd("    print(f'primary={pri}  secondary={sec}')")
blank()
for pri, sec in zip_longest(primaries, secondaries, fillvalue="N/A"):
    out(f"primary={pri}  secondary={sec}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Nested Loops
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Nested Loops")

section("5.1 — Double Loop")

explain("A loop inside a loop.")
explain("The inner loop runs completely for each outer iteration.")
blank()

sites     = ["NYC", "LON", "SIN"]
platforms = ["IOS-XE", "NX-OS"]
cmd("sites     = ['NYC', 'LON', 'SIN']")
cmd("platforms = ['IOS-XE', 'NX-OS']")
blank()
cmd("for site in sites:")
cmd("    for platform in platforms:")
cmd("        print(f'{site} — {platform}')")
blank()
for site in sites:
    for platform in platforms:
        out(f"{site} — {platform}")
blank()

pause()

section("5.2 — Nested Loop Over Real IaC Data")

explain("Iterate over sites, then devices, then interfaces:")
blank()

network = {
    "NYC": {
        "devices": [
            {"hostname": "nyc-rtr-01", "interfaces": ["Gi0/0", "Gi0/1"]},
            {"hostname": "nyc-sw-01",  "interfaces": ["Gi0/0", "Gi0/2"]},
        ]
    },
    "LON": {
        "devices": [
            {"hostname": "lon-sw-01", "interfaces": ["Gi0/0"]},
        ]
    },
}
cmd("network = {")
cmd("    'NYC': {'devices': [")
cmd("        {'hostname': 'nyc-rtr-01', 'interfaces': ['Gi0/0', 'Gi0/1']},")
cmd("        {'hostname': 'nyc-sw-01',  'interfaces': ['Gi0/0', 'Gi0/2']},")
cmd("    ]},")
cmd("    'LON': {'devices': [")
cmd("        {'hostname': 'lon-sw-01', 'interfaces': ['Gi0/0']},")
cmd("    ]},")
cmd("}")
blank()
cmd("for site, cfg in network.items():")
cmd("    for device in cfg['devices']:")
cmd("        for iface in device['interfaces']:")
cmd("            print(f'{site} | {device[\"hostname\"]} | {iface}')")
blank()
for site, cfg in network.items():
    for device in cfg["devices"]:
        for iface in device["interfaces"]:
            out(f"{site} | {device['hostname']} | {iface}")
blank()

pause()

section("5.3 — Breaking Out of Nested Loops")

explain("break only exits the INNERMOST loop.")
explain("To exit multiple levels use a flag or a function.")
blank()

cmd("found = False")
cmd("for site, cfg in network.items():")
cmd("    for device in cfg['devices']:")
cmd("        if device['hostname'] == 'nyc-sw-01':")
cmd("            print(f\"Found nyc-sw-01 in {site}\")")
cmd("            found = True")
cmd("            break")
cmd("    if found:")
cmd("        break")
blank()
found = False
for site, cfg in network.items():
    for device in cfg["devices"]:
        if device["hostname"] == "nyc-sw-01":
            out(f"Found nyc-sw-01 in {site}")
            found = True
            break
    if found:
        break
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Loop Control
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Loop Control")

section("6.1 — break, continue, pass")

inventory = [
    {"hostname": "nyc-rtr-01", "status": "up",   "platform": "IOS-XE"},
    {"hostname": "lon-sw-01",  "status": "down",  "platform": "NX-OS"},
    {"hostname": "sin-fw-01",  "status": "up",    "platform": "ASA"},
    {"hostname": "ams-rtr-02", "status": "up",    "platform": "IOS-XE"},
]
cmd("inventory = [  # 4 devices ]")
blank()

explain("continue — skip this item, move to the next:")
blank()
cmd("for d in inventory:")
cmd("    if d['status'] == 'down':")
cmd("        continue")
cmd("    print(f\"Processing {d['hostname']}\")")
blank()
for d in inventory:
    if d["status"] == "down":
        continue
    out(f"Processing {d['hostname']}")
blank()

pause()

explain("break — stop the loop immediately:")
blank()
cmd("for d in inventory:")
cmd("    if d['platform'] == 'ASA':")
cmd("        print(f\"Found first firewall: {d['hostname']}\")")
cmd("        break")
blank()
for d in inventory:
    if d["platform"] == "ASA":
        out(f"Found first firewall: {d['hostname']}")
        break
blank()

pause()

explain("pass — do nothing, placeholder for empty blocks:")
blank()
cmd("for d in inventory:")
cmd("    if d['status'] == 'down':")
cmd("        pass   # TODO: add alerting")
cmd("    else:")
cmd("        print(f\"{d['hostname']} is up\")")
blank()
for d in inventory:
    if d["status"] == "down":
        pass
    else:
        out(f"{d['hostname']} is up")
blank()

pause()

section("6.2 — for...else")

explain("The else block runs ONLY if the loop finished")
explain("without hitting a break.")
explain("Use it for 'not found' cases.")
blank()

target = "tok-sw-01"
cmd("target = 'tok-sw-01'")
blank()
cmd("for d in inventory:")
cmd("    if d['hostname'] == target:")
cmd("        print(f'Found: {d}')")
cmd("        break")
cmd("else:")
cmd("    print(f'{target} not found in inventory')")
blank()
for d in inventory:
    if d["hostname"] == target:
        out(f"Found: {d}")
        break
else:
    out(f"{target} not found in inventory")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Accumulator Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Accumulator Patterns")

section("7.1 — Building a List")

explain("Start with an empty list, append inside the loop.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up"},
]
cmd("inventory = [  # 4 devices ]")
blank()

cmd("up_hosts = []")
up_hosts = []
cmd("for d in inventory:")
cmd("    if d['status'] == 'up':")
cmd("        up_hosts.append(d['hostname'])")
cmd("print(up_hosts)")
for d in inventory:
    if d["status"] == "up":
        up_hosts.append(d["hostname"])
out(up_hosts)
blank()

pause()

section("7.2 — Building a Dict")

explain("Start with an empty dict, add keys inside the loop.")
blank()

cmd("hostname_map = {}")
hostname_map = {}
cmd("for d in inventory:")
cmd("    hostname_map[d['hostname']] = d['platform']")
cmd("print(hostname_map)")
for d in inventory:
    hostname_map[d["hostname"]] = d["platform"]
out(hostname_map)
blank()

pause()

section("7.3 — Building a Set")

explain("Collect unique values — set handles deduplication.")
blank()

inventory_vlans = [
    {"hostname": "nyc-rtr-01", "vlans": [10, 20, 30]},
    {"hostname": "lon-sw-01",  "vlans": [10, 20]},
    {"hostname": "sin-fw-01",  "vlans": [30, 40, 50]},
]
cmd("inventory_vlans = [")
cmd("    {'hostname': 'nyc-rtr-01', 'vlans': [10,20,30]},")
cmd("    {'hostname': 'lon-sw-01',  'vlans': [10,20]},")
cmd("    {'hostname': 'sin-fw-01',  'vlans': [30,40,50]},")
cmd("]")
blank()
cmd("all_vlans = set()")
all_vlans = set()
cmd("for d in inventory_vlans:")
cmd("    for vlan in d['vlans']:")
cmd("        all_vlans.add(vlan)")
cmd("print(sorted(all_vlans))")
for d in inventory_vlans:
    for vlan in d["vlans"]:
        all_vlans.add(vlan)
out(sorted(all_vlans))
blank()

pause()

section("7.4 — Counter Pattern")

explain("Count occurrences of each platform:")
blank()

cmd("counts = {}")
counts = {}
cmd("for d in inventory:")
cmd("    p = d['platform']")
cmd("    counts[p] = counts.get(p, 0) + 1")
cmd("print(counts)")
for d in inventory:
    p = d["platform"]
    counts[p] = counts.get(p, 0) + 1
out(counts)
blank()

pause()

section("7.5 — Running Total and Running Max")

explain("Accumulate a sum or track a maximum across iterations:")
blank()

interface_counts = [
    {"hostname": "nyc-rtr-01", "iface_count": 5},
    {"hostname": "lon-sw-01",  "iface_count": 12},
    {"hostname": "sin-fw-01",  "iface_count": 3},
    {"hostname": "ams-rtr-02", "iface_count": 8},
]
cmd("interface_counts = [")
cmd("    {'hostname': 'nyc-rtr-01', 'iface_count': 5},")
cmd("    {'hostname': 'lon-sw-01',  'iface_count': 12},")
cmd("    {'hostname': 'sin-fw-01',  'iface_count': 3},")
cmd("    {'hostname': 'ams-rtr-02', 'iface_count': 8},")
cmd("]")
blank()

cmd("total   = 0")
cmd("max_val = 0")
cmd("max_host = ''")
total = max_val = 0
max_host = ""
cmd("for d in interface_counts:")
cmd("    total += d['iface_count']")
cmd("    if d['iface_count'] > max_val:")
cmd("        max_val  = d['iface_count']")
cmd("        max_host = d['hostname']")
for d in interface_counts:
    total += d["iface_count"]
    if d["iface_count"] > max_val:
        max_val  = d["iface_count"]
        max_host = d["hostname"]
cmd("print(f'Total: {total}, Max: {max_host} ({max_val})')")
out(f"Total: {total}, Max: {max_host} ({max_val})")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Looping Over Dicts
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Looping Over Dicts")

section("8.1 — Keys, Values, Items")

device = {
    "hostname": "nyc-rtr-01",
    "platform": "IOS-XE",
    "ip":       "10.0.0.1",
    "status":   "up",
}
cmd("device = {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE',")
cmd("          'ip': '10.0.0.1', 'status': 'up'}")
blank()

explain("Iterating keys (default):")
blank()
cmd("for key in device:")
cmd("    print(key)")
blank()
for key in device:
    out(key)
blank()

pause()

explain("Iterating values:")
blank()
cmd("for value in device.values():")
cmd("    print(value)")
blank()
for value in device.values():
    out(value)
blank()

pause()

explain("Iterating key-value pairs — most common:")
blank()
cmd("for key, value in device.items():")
cmd("    print(f'  {key}: {value}')")
blank()
for key, value in device.items():
    out(f"  {key}: {value}")
blank()

pause()

section("8.2 — Looping Over a Dict of Dicts")

explain("Iterate the outer dict, access the inner dict:")
blank()

sites = {
    "NYC": {"region": "us-east", "device_count": 5},
    "LON": {"region": "eu-west", "device_count": 3},
    "SIN": {"region": "ap-se",   "device_count": 2},
}
cmd("sites = {")
cmd("    'NYC': {'region': 'us-east', 'device_count': 5},")
cmd("    'LON': {'region': 'eu-west', 'device_count': 3},")
cmd("    'SIN': {'region': 'ap-se',   'device_count': 2},")
cmd("}")
blank()
cmd("for site, config in sites.items():")
cmd("    print(f\"{site}: {config['region']} — {config['device_count']} devices\")")
blank()
for site, config in sites.items():
    out(f"{site}: {config['region']} — {config['device_count']} devices")
blank()

pause()

section("8.3 — Modifying Dict Values Safely While Iterating")

explain("You can modify VALUES while iterating .items().")
explain("Do NOT add or remove KEYS — that raises RuntimeError.")
blank()

configs = {
    "nyc-rtr-01": {"ntp": "10.0.0.100", "updated": False},
    "lon-sw-01":  {"ntp": "10.1.0.100", "updated": False},
}
cmd("configs = {")
cmd("    'nyc-rtr-01': {'ntp': '10.0.0.100', 'updated': False},")
cmd("    'lon-sw-01':  {'ntp': '10.1.0.100', 'updated': False},")
cmd("}")
blank()
cmd("for hostname, cfg in configs.items():")
cmd("    cfg['updated'] = True   # modifying value — safe")
for hostname, cfg in configs.items():
    cfg["updated"] = True
cmd("print(configs)")
out(configs)
blank()

pause()

explain("To add/remove keys — iterate a copy of the keys:")
blank()
cmd("for key in list(configs.keys()):")
cmd("    if configs[key]['ntp'] != '10.0.0.100':")
cmd("        del configs[key]")
for key in list(configs.keys()):
    if configs[key]["ntp"] != "10.0.0.100":
        del configs[key]
cmd("print(configs)")
out(configs)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Common Loop Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Common Loop Patterns")

section("9.1 — Chunking a List")

explain("Process a large list in fixed-size batches.")
explain("Common in IaC when pushing config to many devices.")
blank()

devices = ["nyc-rtr-01","lon-sw-01","sin-fw-01","ams-rtr-02",
           "tok-sw-01","syd-rtr-01","dub-fw-01","mum-rtr-01"]
cmd("devices = ['nyc-rtr-01','lon-sw-01','sin-fw-01','ams-rtr-02',")
cmd("           'tok-sw-01','syd-rtr-01','dub-fw-01','mum-rtr-01']")
blank()
cmd("chunk_size = 3")
chunk_size = 3
cmd("for i in range(0, len(devices), chunk_size):")
cmd("    batch = devices[i:i+chunk_size]")
cmd("    print(f'Pushing batch: {batch}')")
blank()
for i in range(0, len(devices), chunk_size):
    batch = devices[i:i+chunk_size]
    out(f"Pushing batch: {batch}")
blank()

pause()

section("9.2 — Sliding Window")

explain("Look at consecutive pairs or triplets of items.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("for i in range(len(vlans) - 1):")
cmd("    current = vlans[i]")
cmd("    next_v  = vlans[i + 1]")
cmd("    print(f'Gap between {current} and {next_v}: {next_v - current}')")
blank()
for i in range(len(vlans) - 1):
    current = vlans[i]
    next_v  = vlans[i + 1]
    out(f"Gap between {current} and {next_v}: {next_v - current}")
blank()

pause()

section("9.3 — First-Match Pattern")

explain("Find the first item that satisfies a condition.")
explain("Use break to stop as soon as it's found.")
blank()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30]},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down", "vlans": [10,20]},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",   "vlans": [30,40,50]},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",   "vlans": [10,20,30,40]},
]
cmd("inventory = [  # 4 devices ]")
blank()
cmd("first_iosxe_up = None")
first_iosxe_up = None
cmd("for d in inventory:")
cmd("    if d['platform'] == 'IOS-XE' and d['status'] == 'up':")
cmd("        first_iosxe_up = d['hostname']")
cmd("        break")
cmd("print(first_iosxe_up)")
for d in inventory:
    if d["platform"] == "IOS-XE" and d["status"] == "up":
        first_iosxe_up = d["hostname"]
        break
out(first_iosxe_up)
blank()

pause()

explain("Or use next() with a generator — one line:")
blank()
cmd("first = next((d['hostname'] for d in inventory")
cmd("              if d['platform'] == 'IOS-XE' and d['status'] == 'up'),")
cmd("             None)")
cmd("print(first)")
first = next((d["hostname"] for d in inventory
              if d["platform"] == "IOS-XE" and d["status"] == "up"),
             None)
out(first)
blank()

pause()

section("9.4 — Deduplication While Preserving Order")

explain("set() deduplicates but loses order.")
explain("Use a loop with a seen set to deduplicate in order:")
blank()

vlans_with_dups = [10, 20, 10, 30, 20, 40, 10]
cmd("vlans_with_dups = [10, 20, 10, 30, 20, 40, 10]")
blank()
cmd("seen   = set()")
cmd("unique = []")
seen   = set()
unique = []
cmd("for v in vlans_with_dups:")
cmd("    if v not in seen:")
cmd("        unique.append(v)")
cmd("        seen.add(v)")
cmd("print(unique)")
for v in vlans_with_dups:
    if v not in seen:
        unique.append(v)
        seen.add(v)
out(unique)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Common Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Common Pitfalls")

section("10.1 — Modifying a List While Iterating It")

explain("Never add or remove items from a list you are")
explain("currently iterating — items get skipped or repeated.")
blank()

vlans = [10, 1, 20, 1002, 30]
cmd("vlans = [10, 1, 20, 1002, 30]")
blank()
cmd("# Wrong — items get skipped")
cmd("for v in vlans:")
cmd("    if v in (1, 1002):")
cmd("        vlans.remove(v)")
cmd("print(vlans)   # 1002 was NOT removed!")
for v in vlans:
    if v in (1, 1002):
        vlans.remove(v)
warn(f"{vlans}   # 1002 was NOT removed!")
blank()

pause()

vlans = [10, 1, 20, 1002, 30]
cmd("# Fix 1 — iterate a copy")
cmd("vlans = [10, 1, 20, 1002, 30]")
cmd("for v in vlans.copy():")
cmd("    if v in (1, 1002):")
cmd("        vlans.remove(v)")
cmd("print(vlans)")
for v in vlans.copy():
    if v in (1, 1002):
        vlans.remove(v)
out(vlans)
blank()

pause()

vlans = [10, 1, 20, 1002, 30]
cmd("# Fix 2 — list comprehension (cleanest)")
cmd("vlans = [10, 1, 20, 1002, 30]")
cmd("vlans = [v for v in vlans if v not in (1, 1002)]")
vlans = [v for v in vlans if v not in (1, 1002)]
cmd("print(vlans)")
out(vlans)
blank()

pause()

section("10.2 — Loop Variable Leaks Into Outer Scope")

explain("Python loop variables are accessible AFTER the loop.")
explain("This can cause bugs if you reuse the variable name.")
blank()

cmd("for device in ['nyc-rtr-01', 'lon-sw-01']:")
cmd("    pass")
cmd("print(device)   # 'lon-sw-01' — last value!")
for device in ["nyc-rtr-01", "lon-sw-01"]:
    pass
warn(f"'{device}'   # last value leaks out!")
blank()
explain("Wrap loops in functions to contain scope.")

pause()

section("10.3 — Mutable Default Accumulator Bug")

explain("Never reuse a mutable object (list, dict) as an")
explain("accumulator across multiple calls — always create fresh.")
blank()

cmd("# Wrong — same list reused every call")
cmd("def get_up_hosts(inventory, result=[]):   # mutable default!")
cmd("    for d in inventory:")
cmd("        if d['status'] == 'up':")
cmd("            result.append(d['hostname'])")
cmd("    return result")
blank()

def get_up_hosts_bad(inventory, result=[]):
    for d in inventory:
        if d["status"] == "up":
            result.append(d["hostname"])
    return result

inv1 = [{"hostname": "nyc-rtr-01", "status": "up"}]
inv2 = [{"hostname": "lon-sw-01",  "status": "up"}]
cmd("print(get_up_hosts([{'hostname': 'nyc-rtr-01', 'status': 'up'}]))")
out(get_up_hosts_bad(inv1))
cmd("print(get_up_hosts([{'hostname': 'lon-sw-01',  'status': 'up'}]))")
warn(get_up_hosts_bad(inv2))
blank()
warn("Second call includes results from first call!")
blank()

pause()

cmd("# Fix — use None as default, create fresh list inside")
cmd("def get_up_hosts(inventory, result=None):")
cmd("    if result is None:")
cmd("        result = []")
cmd("    for d in inventory:")
cmd("        if d['status'] == 'up':")
cmd("            result.append(d['hostname'])")
cmd("    return result")
blank()

def get_up_hosts_good(inventory, result=None):
    if result is None:
        result = []
    for d in inventory:
        if d["status"] == "up":
            result.append(d["hostname"])
    return result

cmd("print(get_up_hosts([{'hostname': 'nyc-rtr-01', 'status': 'up'}]))")
out(get_up_hosts_good(inv1))
cmd("print(get_up_hosts([{'hostname': 'lon-sw-01',  'status': 'up'}]))")
out(get_up_hosts_good(inv2))
blank()

pause()

section("10.4 — Off-by-One in range()")

explain("range(n) gives 0 to n-1 — not 0 to n.")
explain("This is the most common loop indexing mistake.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]   # 5 items, indexes 0-4")
blank()
cmd("# Wrong — IndexError on last iteration")
cmd("for i in range(len(vlans) + 1):")
cmd("    print(vlans[i])")
blank()
try:
    for i in range(len(vlans) + 1):
        print(vlans[i])
except IndexError as e:
    warn(f"IndexError: {e}")
blank()

pause()

cmd("# Correct")
cmd("for i in range(len(vlans)):   # 0 to 4")
cmd("    print(vlans[i])")
blank()
for i in range(len(vlans)):
    out(vlans[i])
blank()
explain("Or better — iterate directly: for v in vlans")

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
print(f"  {BOLD}Ch 1{RESET}   What is a loop — for vs while, loop variable, _")
print(f"  {BOLD}Ch 2{RESET}   for deep dive — strings, sets, range(), tuple unpack")
print(f"  {BOLD}Ch 3{RESET}   while deep dive — retry, while True + break, while...else")
print(f"  {BOLD}Ch 4{RESET}   enumerate(), zip(), zip_longest()")
print(f"  {BOLD}Ch 5{RESET}   Nested loops — double/triple, break from nested")
print(f"  {BOLD}Ch 6{RESET}   Loop control — break, continue, pass, for...else")
print(f"  {BOLD}Ch 7{RESET}   Accumulators — list, dict, set, counter, running max")
print(f"  {BOLD}Ch 8{RESET}   Looping over dicts — keys/values/items, modify safely")
print(f"  {BOLD}Ch 9{RESET}   Patterns — chunking, sliding window, first-match, dedup")
print(f"  {BOLD}Ch 10{RESET}  Pitfalls — mutate while iterate, variable leak, mutable default")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  device inventories, interface tables, VLAN lists,")
print(f"  site configs, retry/polling patterns.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()