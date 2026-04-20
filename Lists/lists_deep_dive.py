# lists_deep_dive.py
# Lists in Python — Zero to Expert
# Cisco IaC perspective
# Press ENTER to advance through each step

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"    # >>> commands
GREEN  = "\033[92m"    # output values
YELLOW = "\033[93m"    # ids / highlights
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
print()
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON LISTS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is a List
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is a List")

section("1.1 — Definition")

explain("A list is an ordered, mutable sequence of items.")
explain("Ordered   — items have a fixed position (index).")
explain("Mutable   — you can add, remove, or change items.")
explain("Sequence  — you can iterate through it item by item.")
blank()
explain("In Cisco IaC, lists hold device inventories,")
explain("interface names, VLAN IDs, NTP servers — any")
explain("collection of things that belong together.")
blank()

pause()

section("1.2 — Creating Lists")

explain("An empty list:")
blank()
cmd("devices = []")
devices = []
cmd("print(devices)")
out(devices)
cmd("print(type(devices))")
out(type(devices))
blank()

pause()

explain("A list of device hostnames:")
blank()
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("print(devices)")
out(devices)
blank()

pause()

explain("A list of VLAN IDs:")
blank()
cmd("vlans = [10, 20, 30, 40, 50]")
vlans = [10, 20, 30, 40, 50]
cmd("print(vlans)")
out(vlans)
blank()

pause()

explain("Lists can hold mixed types — strings, ints, bools:")
blank()
cmd("mixed = ['Gi0/0', 1, True, 'up', 100]")
mixed = ["Gi0/0", 1, True, "up", 100]
cmd("print(mixed)")
out(mixed)
blank()

pause()

explain("A list of lists — nested structure:")
blank()
cmd("sites = [['NYC', 'nyc-rtr-01'], ['LON', 'lon-sw-01'], ['SIN', 'sin-fw-01']]")
sites = [["NYC", "nyc-rtr-01"], ["LON", "lon-sw-01"], ["SIN", "sin-fw-01"]]
cmd("print(sites)")
out(sites)
blank()

pause()

explain("Length of a list — how many items it holds:")
blank()
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("print(len(devices))")
out(len(devices))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Accessing Elements
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "Accessing Elements")

section("2.1 — Indexing")

explain("Each item in a list has an index — its position.")
explain("Python uses ZERO-BASED indexing.")
explain("First item is at index 0, not index 1.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()
cmd("#         index: 0            1            2            3")
blank()

pause()

cmd("print(devices[0])")
out(devices[0])
cmd("print(devices[1])")
out(devices[1])
cmd("print(devices[3])")
out(devices[3])
blank()

pause()

explain("Negative indexes count from the END:")
blank()
cmd("print(devices[-1])   # last item")
out(devices[-1])
cmd("print(devices[-2])   # second to last")
out(devices[-2])
cmd("print(devices[-4])   # same as devices[0]")
out(devices[-4])
blank()

pause()

explain("Accessing an index that does not exist raises IndexError:")
blank()
cmd("print(devices[10])")
blank()
try:
    print(devices[10])
except IndexError as e:
    warn(f"IndexError: {e}")
blank()

pause()

section("2.2 — Slicing")

explain("Slicing extracts a portion of a list.")
explain("Syntax: list[start:stop:step]")
explain("start — index to begin at (inclusive)")
explain("stop  — index to end at   (exclusive)")
explain("step  — how many to skip   (default 1)")
blank()

vlans = [10, 20, 30, 40, 50, 60, 70, 80]
cmd("vlans = [10, 20, 30, 40, 50, 60, 70, 80]")
blank()

pause()

cmd("print(vlans[0:3])    # items at index 0, 1, 2")
out(vlans[0:3])
cmd("print(vlans[2:5])    # items at index 2, 3, 4")
out(vlans[2:5])
cmd("print(vlans[:4])     # from start to index 3")
out(vlans[:4])
cmd("print(vlans[4:])     # from index 4 to end")
out(vlans[4:])
cmd("print(vlans[:])      # entire list — a shallow copy")
out(vlans[:])
blank()

pause()

explain("Step — skip every N items:")
blank()
cmd("print(vlans[::2])    # every 2nd item")
out(vlans[::2])
cmd("print(vlans[1::2])   # every 2nd item starting at index 1")
out(vlans[1::2])
cmd("print(vlans[::-1])   # reverse the list")
out(vlans[::-1])
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Iterating
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Iterating")

section("3.1 — Basic for Loop")

explain("A for loop visits each item in the list one by one.")
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

explain("Real use case — print a config command per device:")
blank()
cmd("for device in devices:")
cmd("    print(f'hostname {device}')")
blank()
for device in devices:
    out(f"hostname {device}")
blank()

pause()

section("3.2 — enumerate() — Index and Value Together")

explain("enumerate() gives you the index AND the item")
explain("at the same time. No need to track index manually.")
blank()

cmd("for index, device in enumerate(devices):")
cmd("    print(f'{index}: {device}')")
blank()
for index, device in enumerate(devices):
    out(f"{index}: {device}")
blank()

pause()

explain("Start index at 1 instead of 0:")
blank()
cmd("for index, device in enumerate(devices, start=1):")
cmd("    print(f'Device {index}: {device}')")
blank()
for index, device in enumerate(devices, start=1):
    out(f"Device {index}: {device}")
blank()

pause()

section("3.3 — zip() — Iterate Two Lists Together")

explain("zip() pairs up items from two lists side by side.")
explain("Stops at the shorter list.")
blank()

hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
ips       = ["10.0.0.1",   "10.1.0.1",  "10.2.0.1"]

cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("ips       = ['10.0.0.1',   '10.1.0.1',  '10.2.0.1']")
blank()
cmd("for hostname, ip in zip(hostnames, ips):")
cmd("    print(f'{hostname} --> {ip}')")
blank()
for hostname, ip in zip(hostnames, ips):
    out(f"{hostname} --> {ip}")
blank()

pause()

explain("Build a dict from two lists using zip:")
blank()
cmd("device_map = dict(zip(hostnames, ips))")
device_map = dict(zip(hostnames, ips))
cmd("print(device_map)")
out(device_map)
blank()

pause()

section("3.4 — range() — Index-Based Iteration")

explain("range() generates a sequence of numbers.")
explain("Use it when you need the index to do something")
explain("beyond just reading the item.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("for i in range(len(vlans)):")
cmd("    print(f'index {i} → vlan {vlans[i]}')")
blank()
for i in range(len(vlans)):
    out(f"index {i} → vlan {vlans[i]}")
blank()

pause()

explain("range(start, stop, step):")
blank()
cmd("for i in range(0, 10, 2):")
cmd("    print(i)")
blank()
for i in range(0, 10, 2):
    out(i)
blank()

pause()

section("3.5 — while Loop Over a List")

explain("A while loop gives you more control —")
explain("you manage the index yourself.")
blank()

interfaces = ["Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3"]
cmd("interfaces = ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3']")
blank()
cmd("i = 0")
cmd("while i < len(interfaces):")
cmd("    print(f'Configuring {interfaces[i]}')")
cmd("    i += 1")
blank()
i = 0
while i < len(interfaces):
    out(f"Configuring {interfaces[i]}")
    i += 1
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Checking and Searching
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Checking and Searching")

section("4.1 — in and not in")

explain("Check if an item exists in a list.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
cmd("print('nyc-rtr-01' in devices)")
out("nyc-rtr-01" in devices)
cmd("print('tok-sw-01' in devices)")
out("tok-sw-01" in devices)
cmd("print('tok-sw-01' not in devices)")
out("tok-sw-01" not in devices)
blank()

pause()

explain("Practical use — only add if not already present:")
blank()
cmd("if 'tok-sw-01' not in devices:")
cmd("    devices.append('tok-sw-01')")
cmd("print(devices)")
if "tok-sw-01" not in devices:
    devices.append("tok-sw-01")
out(devices)
blank()

pause()

section("4.2 — .index() and .count()")

vlans = [10, 20, 30, 20, 40, 20, 50]
cmd("vlans = [10, 20, 30, 20, 40, 20, 50]")
blank()
explain(".index() — find position of first occurrence:")
blank()
cmd("print(vlans.index(20))")
out(vlans.index(20))
cmd("print(vlans.index(40))")
out(vlans.index(40))
blank()

pause()

explain(".count() — how many times does a value appear:")
blank()
cmd("print(vlans.count(20))")
out(vlans.count(20))
cmd("print(vlans.count(99))")
out(vlans.count(99))
blank()

pause()

section("4.3 — any() and all()")

explain("any() — True if AT LEAST ONE item passes the condition.")
explain("all() — True if EVERY item passes the condition.")
blank()

statuses = ["up", "up", "down", "up"]
cmd("statuses = ['up', 'up', 'down', 'up']")
blank()
cmd("print(any(s == 'down' for s in statuses))   # any down?")
out(any(s == "down" for s in statuses))
cmd("print(all(s == 'up'   for s in statuses))   # all up?")
out(all(s == "up" for s in statuses))
blank()

pause()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("print(any(v > 45 for v in vlans))   # any vlan over 45?")
out(any(v > 45 for v in vlans))
cmd("print(all(v < 100 for v in vlans))  # all vlans under 100?")
out(all(v < 100 for v in vlans))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Modifying Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Modifying Lists")

section("5.1 — Adding Items")

devices = ["nyc-rtr-01", "lon-sw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01']")
blank()

explain(".append() — add one item to the end:")
blank()
cmd("devices.append('sin-fw-01')")
devices.append("sin-fw-01")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".insert(index, item) — add at a specific position:")
blank()
cmd("devices.insert(1, 'ams-rtr-02')")
devices.insert(1, "ams-rtr-02")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".extend() — add all items from another list:")
blank()
cmd("new_devices = ['tok-sw-01', 'syd-rtr-01']")
new_devices = ["tok-sw-01", "syd-rtr-01"]
cmd("devices.extend(new_devices)")
devices.extend(new_devices)
cmd("print(devices)")
out(devices)
blank()

pause()

explain("Difference between append and extend:")
blank()
cmd("a = [1, 2, 3]")
a = [1, 2, 3]
cmd("a.append([4, 5])   # adds the list as ONE item")
a.append([4, 5])
cmd("print(a)")
out(a)
blank()
cmd("b = [1, 2, 3]")
b = [1, 2, 3]
cmd("b.extend([4, 5])   # adds each item individually")
b.extend([4, 5])
cmd("print(b)")
out(b)
blank()

pause()

section("5.2 — Removing Items")

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()

explain(".remove(value) — remove first occurrence of value:")
blank()
cmd("devices.remove('lon-sw-01')")
devices.remove("lon-sw-01")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".pop() — remove and return last item:")
blank()
cmd("removed = devices.pop()")
removed = devices.pop()
cmd("print(removed)")
out(removed)
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".pop(index) — remove and return item at index:")
blank()
cmd("removed = devices.pop(0)")
removed = devices.pop(0)
cmd("print(removed)")
out(removed)
cmd("print(devices)")
out(devices)
blank()

pause()

explain("del — delete by index or slice:")
blank()
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
cmd("del devices[1]")
del devices[1]
cmd("print(devices)")
out(devices)
blank()
cmd("del devices[0:2]")
del devices[0:2]
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".clear() — remove everything:")
blank()
cmd("devices.clear()")
devices.clear()
cmd("print(devices)")
out(devices)
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Ordering
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Ordering")

section("6.1 — .sort() vs sorted()")

devices = ["sin-fw-01", "nyc-rtr-01", "ams-rtr-02", "lon-sw-01"]
cmd("devices = ['sin-fw-01', 'nyc-rtr-01', 'ams-rtr-02', 'lon-sw-01']")
blank()

explain(".sort() — sorts IN PLACE — modifies original:")
blank()
cmd("devices.sort()")
devices.sort()
cmd("print(devices)")
out(devices)
blank()

pause()

devices = ["sin-fw-01", "nyc-rtr-01", "ams-rtr-02", "lon-sw-01"]
cmd("devices = ['sin-fw-01', 'nyc-rtr-01', 'ams-rtr-02', 'lon-sw-01']")
blank()
explain("sorted() — returns a NEW list — original untouched:")
blank()
cmd("sorted_devices = sorted(devices)")
sorted_devices = sorted(devices)
cmd("print(sorted_devices)")
out(sorted_devices)
cmd("print(devices)   # original unchanged")
out(devices)
blank()

pause()

explain("Reverse order — sort descending:")
blank()
cmd("devices.sort(reverse=True)")
devices.sort(reverse=True)
cmd("print(devices)")
out(devices)
blank()

pause()

section("6.2 — Custom Sort with key=")

explain("Sort by a specific part of each item.")
explain("key= takes a function applied to each element.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()

explain("Sort by the last 2 characters (the number):")
blank()
cmd("devices.sort(key=lambda d: d[-2:])")
devices.sort(key=lambda d: d[-2:])
cmd("print(devices)")
out(devices)
blank()

pause()

explain("Sort a list of dicts by a specific key:")
blank()
inventory = [
    {"hostname": "sin-fw-01",  "platform": "ASA",    "vlans": 5},
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "vlans": 12},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "vlans": 30},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "vlans": 8},
]
cmd("inventory = [")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'vlans': 5},")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'vlans': 12},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'vlans': 30},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'vlans': 8},")
cmd("]")
blank()
cmd("inventory.sort(key=lambda d: d['vlans'])")
inventory.sort(key=lambda d: d["vlans"])
cmd("for d in inventory:")
cmd("    print(d['hostname'], '→', d['vlans'], 'vlans')")
blank()
for d in inventory:
    out(f"{d['hostname']} → {d['vlans']} vlans")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Transformation: The Manual Way
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Transformation: The Manual Way")

section("7.1 — Building a New List With for + append")

explain("The most common pattern in Python — take a list,")
explain("apply something to each item, collect the results.")
explain("The manual way: empty list + loop + append.")
blank()

pause()

explain("Normalise all hostnames to uppercase:")
blank()
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
cmd("upper_devices = []")
cmd("for d in devices:")
cmd("    upper_devices.append(d.upper())")
cmd("print(upper_devices)")
upper_devices = []
for d in devices:
    upper_devices.append(d.upper())
out(upper_devices)
blank()

pause()

explain("Extract just the site code (first 3 chars):")
blank()
cmd("sites = []")
cmd("for d in devices:")
cmd("    sites.append(d[:3])")
cmd("print(sites)")
sites = []
for d in devices:
    sites.append(d[:3])
out(sites)
blank()

pause()

explain("This works — but it is verbose.")
explain("Four lines to do something simple.")
explain("Python has a better way — list comprehensions.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — List Comprehensions
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "List Comprehensions")

section("8.1 — Basic Syntax")

explain("A list comprehension collapses the loop + append")
explain("pattern into a single expressive line.")
blank()
explain("Syntax:  [expression  for  item  in  iterable]")
blank()
explain("Read it as:")
explain("  'give me expression, for each item in iterable'")
blank()

pause()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()

explain("Manual way (4 lines):")
blank()
cmd("upper = []")
cmd("for d in devices:")
cmd("    upper.append(d.upper())")
blank()

explain("List comprehension (1 line — same result):")
blank()
cmd("upper = [d.upper() for d in devices]")
upper = [d.upper() for d in devices]
cmd("print(upper)")
out(upper)
blank()

pause()

explain("Extract site codes:")
blank()
cmd("sites = [d[:3] for d in devices]")
sites = [d[:3] for d in devices]
cmd("print(sites)")
out(sites)
blank()

pause()

explain("Add a prefix to every hostname:")
blank()
cmd("prefixed = [f'cisco-{d}' for d in devices]")
prefixed = [f"cisco-{d}" for d in devices]
cmd("print(prefixed)")
out(prefixed)
blank()

pause()

section("8.2 — With a Condition (Filtering)")

explain("Syntax:  [expression  for  item  in  iterable  if  condition]")
blank()
explain("The if at the end FILTERS — only items that pass")
explain("the condition are included in the result.")
blank()

pause()

inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up"},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up"},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down"},
]
cmd("inventory = [")
cmd("    {'hostname': 'nyc-rtr-01', 'platform': 'IOS-XE', 'status': 'up'},")
cmd("    {'hostname': 'lon-sw-01',  'platform': 'NX-OS',  'status': 'down'},")
cmd("    {'hostname': 'sin-fw-01',  'platform': 'ASA',    'status': 'up'},")
cmd("    {'hostname': 'ams-rtr-02', 'platform': 'IOS-XE', 'status': 'up'},")
cmd("    {'hostname': 'tok-sw-01',  'platform': 'NX-OS',  'status': 'down'},")
cmd("]")
blank()

pause()

explain("Get hostnames of all devices that are 'up':")
blank()
cmd("up_devices = [d['hostname'] for d in inventory if d['status'] == 'up']")
up_devices = [d["hostname"] for d in inventory if d["status"] == "up"]
cmd("print(up_devices)")
out(up_devices)
blank()

pause()

explain("Get only IOS-XE devices:")
blank()
cmd("iosxe = [d['hostname'] for d in inventory if d['platform'] == 'IOS-XE']")
iosxe = [d["hostname"] for d in inventory if d["platform"] == "IOS-XE"]
cmd("print(iosxe)")
out(iosxe)
blank()

pause()

explain("Filter VLANs — exclude reserved ones:")
blank()
RESERVED = {1, 1002, 1003, 1004, 1005}
vlans = [1, 10, 20, 30, 1002, 40, 1003, 50]
cmd("RESERVED = {1, 1002, 1003, 1004, 1005}")
cmd("vlans = [1, 10, 20, 30, 1002, 40, 1003, 50]")
blank()
cmd("safe_vlans = [v for v in vlans if v not in RESERVED]")
safe_vlans = [v for v in vlans if v not in RESERVED]
cmd("print(safe_vlans)")
out(safe_vlans)
blank()

pause()

section("8.3 — Multiple Conditions")

explain("Chain conditions with 'and' and 'or':")
blank()

cmd("# IOS-XE devices that are up")
cmd("result = [d['hostname'] for d in inventory")
cmd("          if d['platform'] == 'IOS-XE' and d['status'] == 'up']")
result = [d["hostname"] for d in inventory
          if d["platform"] == "IOS-XE" and d["status"] == "up"]
cmd("print(result)")
out(result)
blank()

pause()

cmd("# Devices that are down OR are ASA platform")
cmd("result = [d['hostname'] for d in inventory")
cmd("          if d['status'] == 'down' or d['platform'] == 'ASA']")
result = [d["hostname"] for d in inventory
          if d["status"] == "down" or d["platform"] == "ASA"]
cmd("print(result)")
out(result)
blank()

pause()

section("8.4 — Transformation + Filtering Together")

explain("You can transform AND filter in one comprehension.")
blank()

cmd("# Uppercase hostname of every device that is 'up'")
cmd("result = [d['hostname'].upper() for d in inventory if d['status'] == 'up']")
result = [d["hostname"].upper() for d in inventory if d["status"] == "up"]
cmd("print(result)")
out(result)
blank()

pause()

cmd("# Build config snippet for each IOS-XE device that is up")
cmd("configs = [f\"hostname {d['hostname']}\" for d in inventory")
cmd("           if d['platform'] == 'IOS-XE' and d['status'] == 'up']")
configs = [f"hostname {d['hostname']}" for d in inventory
           if d["platform"] == "IOS-XE" and d["status"] == "up"]
cmd("for c in configs:")
cmd("    print(c)")
blank()
for c in configs:
    out(c)
blank()

pause()

section("8.5 — Nested List Comprehensions")

explain("A comprehension inside a comprehension.")
explain("Use when you need to flatten or process nested lists.")
blank()

sites = [
    ["Gi0/0", "Gi0/1", "Gi0/2"],
    ["Te1/0/1", "Te1/0/2"],
    ["Gi0/0", "Gi0/3"],
]
cmd("sites = [")
cmd("    ['Gi0/0', 'Gi0/1', 'Gi0/2'],")
cmd("    ['Te1/0/1', 'Te1/0/2'],")
cmd("    ['Gi0/0', 'Gi0/3'],")
cmd("]")
blank()

pause()

explain("Flatten — get every interface from every site:")
blank()
cmd("all_interfaces = [iface for site in sites for iface in site]")
all_interfaces = [iface for site in sites for iface in site]
cmd("print(all_interfaces)")
out(all_interfaces)
blank()

pause()

explain("Read nested comprehension left to right:")
explain("'for site in sites' — outer loop")
explain("'for iface in site' — inner loop")
explain("'iface'             — what to collect")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Built-ins That Work on Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(9, "Built-ins That Work on Lists")

section("9.1 — len, sum, min, max")

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("print(len(vlans))")
out(len(vlans))
cmd("print(sum(vlans))")
out(sum(vlans))
cmd("print(min(vlans))")
out(min(vlans))
cmd("print(max(vlans))")
out(max(vlans))
blank()

pause()

explain("Practical use — count enabled interfaces:")
blank()
statuses = ["up", "up", "down", "up", "down"]
cmd("statuses = ['up', 'up', 'down', 'up', 'down']")
cmd("up_count = sum(1 for s in statuses if s == 'up')")
up_count = sum(1 for s in statuses if s == "up")
cmd("print(f'{up_count} of {len(statuses)} interfaces are up')")
out(f"{up_count} of {len(statuses)} interfaces are up")
blank()

pause()

section("9.2 — list() — Convert to List")

explain("Convert other iterables to a list:")
blank()
cmd("print(list(range(1, 6)))")
out(list(range(1, 6)))
cmd("print(list('IOS-XE'))")
out(list("IOS-XE"))
cmd("print(list({'nyc', 'lon', 'sin'}))")
out(list({"nyc", "lon", "sin"}))
blank()

pause()

section("9.3 — zip() and enumerate() Revisited")

explain("zip() and enumerate() return iterators — wrap in")
explain("list() to see the full result:")
blank()

hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
ips       = ["10.0.0.1",   "10.1.0.1",  "10.2.0.1"]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("ips       = ['10.0.0.1',   '10.1.0.1',  '10.2.0.1']")
blank()
cmd("print(list(zip(hostnames, ips)))")
out(list(zip(hostnames, ips)))
cmd("print(list(enumerate(hostnames)))")
out(list(enumerate(hostnames)))
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Nested Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(10, "Nested Lists")

section("10.1 — List of Lists")

explain("A list where each item is itself a list.")
explain("Access with two indexes: outer then inner.")
blank()

interfaces = [
    ["Gi0/0", "access", 10],
    ["Gi0/1", "access", 20],
    ["Gi0/2", "trunk",  None],
]
cmd("interfaces = [")
cmd("    ['Gi0/0', 'access', 10],")
cmd("    ['Gi0/1', 'access', 20],")
cmd("    ['Gi0/2', 'trunk',  None],")
cmd("]")
blank()

pause()

cmd("print(interfaces[0])        # first row")
out(interfaces[0])
cmd("print(interfaces[0][0])     # first row, first column")
out(interfaces[0][0])
cmd("print(interfaces[1][2])     # second row, third column")
out(interfaces[1][2])
blank()

pause()

explain("Iterate nested list — unpack each row:")
blank()
cmd("for name, mode, vlan in interfaces:")
cmd("    print(f'{name} | {mode} | vlan={vlan}')")
blank()
for name, mode, vlan in interfaces:
    out(f"{name} | {mode} | vlan={vlan}")
blank()

pause()

section("10.2 — List of Dicts")

explain("The most common pattern in Cisco IaC.")
explain("Each item is a dict representing a device or interface.")
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

pause()

explain("Access a specific device's field:")
blank()
cmd("print(inventory[0]['hostname'])")
out(inventory[0]["hostname"])
cmd("print(inventory[2]['ip'])")
out(inventory[2]["ip"])
blank()

pause()

explain("Iterate and print a summary:")
blank()
cmd("for device in inventory:")
cmd("    print(f\"{device['hostname']:<15} {device['platform']:<10} {device['ip']}\")")
blank()
for device in inventory:
    out(f"{device['hostname']:<15} {device['platform']:<10} {device['ip']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 11 — Common Patterns and Pitfalls
# ═════════════════════════════════════════════════════════════════════════════
chapter(11, "Common Patterns and Pitfalls")

section("11.1 — Copying a List Correctly")

explain("b = a is NOT a copy — it is an alias.")
explain("Use .copy() or [:] for a shallow copy.")
blank()

vlans = [10, 20, 30]
cmd("vlans = [10, 20, 30]")
blank()
cmd("# Wrong — alias")
cmd("alias = vlans")
cmd("alias.append(40)")
cmd("print(vlans)   # also changed!")
alias = vlans
alias.append(40)
warn(vlans)
blank()

pause()

vlans = [10, 20, 30]
cmd("# Correct — copy")
cmd("vlans = [10, 20, 30]")
cmd("copy  = vlans.copy()")
copy = vlans.copy()
cmd("copy.append(40)")
copy.append(40)
cmd("print(vlans)   # untouched")
out(vlans)
cmd("print(copy)")
out(copy)
blank()

pause()

section("11.2 — Modifying a List While Iterating It")

explain("Never modify a list while you are iterating it.")
explain("It causes items to be skipped or repeated.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("# Wrong — removing while iterating")
cmd("for v in vlans:")
cmd("    if v == 30:")
cmd("        vlans.remove(v)   # skips items!")
for v in vlans:
    if v == 30:
        vlans.remove(v)
cmd("print(vlans)")
warn(vlans)
blank()

pause()

vlans = [10, 20, 30, 40, 50]
cmd("# Correct — iterate a copy, modify the original")
cmd("vlans = [10, 20, 30, 40, 50]")
cmd("for v in vlans.copy():")
cmd("    if v == 30:")
cmd("        vlans.remove(v)")
for v in vlans.copy():
    if v == 30:
        vlans.remove(v)
cmd("print(vlans)")
out(vlans)
blank()

pause()

explain("Or use a list comprehension — cleanest way:")
blank()
vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
cmd("vlans = [v for v in vlans if v != 30]")
vlans = [v for v in vlans if v != 30]
cmd("print(vlans)")
out(vlans)
blank()

pause()

section("11.3 — The Loop Variable Trap")

explain("Creating a list of dicts in a loop using the same dict.")
blank()

cmd("# Wrong — all dicts are the same object")
cmd("result = []")
cmd("entry  = {}")
cmd("for name in ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']:")
cmd("    entry['hostname'] = name")
cmd("    result.append(entry)")
cmd("print(result)")
result = []
entry  = {}
for name in ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]:
    entry["hostname"] = name
    result.append(entry)
warn(result)
blank()

pause()

cmd("# Correct — new dict each iteration")
cmd("result = [{'hostname': name} for name in ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']]")
result = [{"hostname": name} for name in ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]]
cmd("print(result)")
out(result)
blank()

pause()

section("11.4 — When to Use a Loop vs a Comprehension")

explain("Use a LIST COMPREHENSION when:")
explain("  — transforming or filtering a list")
explain("  — logic fits cleanly on one or two lines")
explain("  — no side effects needed")
blank()
explain("Use a FOR LOOP when:")
explain("  — logic is complex or spans many lines")
explain("  — you need to handle exceptions per item")
explain("  — you need to break or continue conditionally")
explain("  — you are producing side effects (print, API call)")
blank()

pause()

cmd("# Comprehension — clean, no side effects")
cmd("ips = [d['ip'] for d in inventory if d['platform'] == 'IOS-XE']")
inventory = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "ip": "10.0.0.1"},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "ip": "10.1.0.1"},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "ip": "10.2.0.1"},
]
ips = [d["ip"] for d in inventory if d["platform"] == "IOS-XE"]
cmd("print(ips)")
out(ips)
blank()

pause()

cmd("# Loop — side effect (pushing config to device)")
cmd("for device in inventory:")
cmd("    if device['platform'] == 'IOS-XE':")
cmd("        print(f\"Pushing config to {device['hostname']}...\")")
cmd("        # connect_and_push(device['ip'], config)")
blank()
for device in inventory:
    if device["platform"] == "IOS-XE":
        out(f"Pushing config to {device['hostname']}...")
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
print(f"  {BOLD}Ch 1{RESET}   What is a list — create, len, mixed types, nested")
print(f"  {BOLD}Ch 2{RESET}   Accessing — indexing, negative index, slicing [::step]")
print(f"  {BOLD}Ch 3{RESET}   Iterating — for, enumerate, zip, range, while")
print(f"  {BOLD}Ch 4{RESET}   Searching — in, .index(), .count(), any(), all()")
print(f"  {BOLD}Ch 5{RESET}   Modifying — append, insert, extend, remove, pop, del")
print(f"  {BOLD}Ch 6{RESET}   Ordering — .sort(), sorted(), reverse, key=lambda")
print(f"  {BOLD}Ch 7{RESET}   Transformation — manual for + append pattern")
print(f"  {BOLD}Ch 8{RESET}   List comprehensions — basic, filter, multi-cond, nested")
print(f"  {BOLD}Ch 9{RESET}   Built-ins — len, sum, min, max, list(), zip, enumerate")
print(f"  {BOLD}Ch 10{RESET}  Nested lists — list of lists, list of dicts")
print(f"  {BOLD}Ch 11{RESET}  Pitfalls — copy trap, mutate while iterate, loop trap")
blank()
print(f"  {WHITE}Every example used real Cisco IaC data —")
print(f"  device inventories, interface tables, VLAN lists,")
print(f"  platform filtering, config generation.{RESET}")
blank()
bar2 = "█" * 62
print(f"{BOLD}{bar2}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar2}{RESET}")
print()