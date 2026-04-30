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
explain("Use [] with nothing inside to create an empty list.")
explain("type() confirms it is a list object.")
explain("You start empty and grow the list by appending items later.")
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
explain("Each item is a string separated by commas inside square brackets.")
explain("Order is preserved — nyc-rtr-01 is always index 0, lon-sw-01 index 1.")
explain("This is the most common list shape in Cisco IaC inventory files.")
blank()
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("print(devices)")
out(devices)
blank()

pause()

explain("A list of VLAN IDs:")
blank()
explain("Items can be integers — no quotes needed.")
explain("VLAN IDs are naturally a list: an ordered collection of numbers")
explain("that you will loop over, filter, or pass to config templates.")
blank()
cmd("vlans = [10, 20, 30, 40, 50]")
vlans = [10, 20, 30, 40, 50]
cmd("print(vlans)")
out(vlans)
blank()

pause()

explain("Lists can hold mixed types — strings, ints, bools:")
blank()
explain("Python does not restrict list items to a single type.")
explain("This mixed list holds an interface name, a port number, a boolean,")
explain("a status string, and a speed — all in one structure.")
explain("In practice, stick to one type per list for clarity and safety.")
blank()
cmd("mixed = ['Gi0/0', 1, True, 'up', 100]")
mixed = ["Gi0/0", 1, True, "up", 100]
cmd("print(mixed)")
out(mixed)
blank()

pause()

explain("A list of lists — nested structure:")
blank()
explain("Each item in sites is itself a list with two strings.")
explain("The outer list groups all sites; each inner list is [site_code, router].")
explain("In real IaC you would usually use a list of dicts instead")
explain("(see Chapter 10), but list-of-lists appears in CSV/tabular data.")
blank()
cmd("sites = [['NYC', 'nyc-rtr-01'], ['LON', 'lon-sw-01'], ['SIN', 'sin-fw-01']]")
sites = [["NYC", "nyc-rtr-01"], ["LON", "lon-sw-01"], ["SIN", "sin-fw-01"]]
cmd("print(sites)")
out(sites)
blank()

pause()

explain("Length of a list — how many items it holds:")
blank()
explain("len() returns the count of items at the top level.")
explain("For a flat list of hostnames this equals the number of devices.")
explain("Use this before indexing to avoid going out of bounds.")
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
explain("Zero-based indexing comes from C and is used by most languages.")
explain("Think of the index as an offset from the start — the first item")
explain("is 0 steps away, the second is 1 step away, and so on.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()
cmd("#         index: 0            1            2            3")
blank()

pause()

explain("Accessing items by positive index:")
blank()
explain("devices[0] → nyc-rtr-01  (first item)")
explain("devices[1] → lon-sw-01   (second item)")
explain("devices[3] → ams-rtr-02  (fourth item, the last one here)")
blank()
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
explain("devices[-1] is always the last item regardless of list length.")
explain("This is much safer than devices[len(devices)-1].")
explain("Use negative indexes when you care about position from the end,")
explain("e.g. the most recently added device or the highest VLAN ID.")
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
explain("The list only has items at indexes 0–3.")
explain("Index 10 is beyond the end — Python raises IndexError.")
explain("Always check len() or use try/except before indexing into")
explain("a list whose length you are not certain of.")
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
explain("The stop index is exclusive — you get items UP TO but not including it.")
explain("Omitting start defaults to 0; omitting stop defaults to the end.")
explain("Slicing always returns a new list — the original is never modified.")
blank()

vlans = [10, 20, 30, 40, 50, 60, 70, 80]
cmd("vlans = [10, 20, 30, 40, 50, 60, 70, 80]")
blank()

pause()

explain("Basic slice examples:")
blank()
explain("vlans[0:3]  → indexes 0, 1, 2     → [10, 20, 30]")
explain("vlans[2:5]  → indexes 2, 3, 4     → [30, 40, 50]")
explain("vlans[:4]   → start to index 3    → [10, 20, 30, 40]")
explain("vlans[4:]   → index 4 to end      → [50, 60, 70, 80]")
explain("vlans[:]    → entire list as copy → all 8 items")
blank()
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
explain("vlans[::2]   → every 2nd item starting at 0 → even-indexed VLANs")
explain("vlans[1::2]  → every 2nd item starting at 1 → odd-indexed VLANs")
explain("vlans[::-1]  → step of -1 means walk backwards → reversed list")
explain("The step parameter is powerful for sampling or reversing sequences.")
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
explain("The loop variable (device) is assigned each item in turn.")
explain("Python handles the index internally — you never see it.")
explain("This is the most readable, idiomatic way to process a list.")
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
explain("Each iteration produces one config line for one device.")
explain("This is the foundation of config generation in IaC:")
explain("loop over a list of devices, emit one output per device.")
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
explain("Instead of writing i = 0 before the loop and i += 1 at the end,")
explain("enumerate() does it for you and unpacks into two variables.")
explain("This is cleaner and less error-prone than manual index tracking.")
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
explain("The start= argument shifts the counter — the list itself is unchanged.")
explain("Use this when output is human-facing and 1-based numbering reads better,")
explain("for example in a numbered inventory report or a step-by-step config guide.")
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
explain("zip() is how you avoid parallel index loops like hostnames[i], ips[i].")
explain("It produces tuples of matched items — (hostname, ip) each iteration.")
explain("If the lists are different lengths, zip() stops at the shorter one")
explain("and silently discards the remaining items from the longer list.")
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
explain("dict(zip(hostnames, ips)) is the canonical one-liner for turning")
explain("two parallel lists into a key-value mapping.")
explain("Result: every hostname maps directly to its IP for O(1) lookup.")
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
explain("Prefer 'for item in list' when you only need the value.")
explain("Use range(len(list)) when you also need the position — for example")
explain("to compare adjacent items, or to modify items in place by index.")
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
explain("range(0, 10, 2) generates 0, 2, 4, 6, 8 — even numbers below 10.")
explain("stop is exclusive just like slicing — 10 itself is not included.")
explain("Use range() directly (no list needed) when you just want a counter.")
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
explain("while loops are useful when the stopping condition is not simply")
explain("'end of list' — for example, stopping early on a condition,")
explain("stepping by a variable amount, or processing until a sentinel value.")
explain("For straightforward iteration, a for loop is always cleaner.")
blank()

interfaces = ["Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3"]
cmd("interfaces = ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3']")
blank()
cmd("i = 0")
cmd("while i < len(interfaces):")
cmd("    print(f'Configuring {interfaces[i]}')")
cmd("    i += 1")
explain("  i starts at 0 and increments each pass.")
explain("  The condition i < len(interfaces) stops the loop after the last item.")
explain("  Forgetting i += 1 creates an infinite loop — a common while-loop bug.")
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
explain("'in' performs a linear scan — O(n) — checking each item in order.")
explain("For large lists where you do many membership checks, consider")
explain("converting to a set first (O(1) lookup) to improve performance.")
explain("For small lists and occasional checks, 'in' is perfectly fine.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
blank()
cmd("print('nyc-rtr-01' in devices)")
out("nyc-rtr-01" in devices)
explain("  → True because 'nyc-rtr-01' appears in the list.")
blank()
cmd("print('tok-sw-01' in devices)")
out("tok-sw-01" in devices)
explain("  → False because 'tok-sw-01' has not been added.")
blank()
cmd("print('tok-sw-01' not in devices)")
out("tok-sw-01" not in devices)
explain("  → True — the logical negation of the previous check.")
blank()

pause()

explain("Practical use — only add if not already present:")
blank()
explain("This prevents duplicates without needing to deduplicate later.")
explain("Pattern: check before appending to keep the list clean as you build it.")
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

explain(".index(value) scans the list and returns the position of the")
explain("first match. .count(value) scans the whole list and counts matches.")
explain("Both are O(n) — they scan from left to right.")
blank()

vlans = [10, 20, 30, 20, 40, 20, 50]
cmd("vlans = [10, 20, 30, 20, 40, 20, 50]")
blank()
explain(".index() — find position of first occurrence:")
blank()
explain("VLAN 20 appears at indexes 1, 3, and 5 — .index() returns only the first.")
explain("Raises ValueError if the value is not found — use 'in' first if unsure.")
blank()
cmd("print(vlans.index(20))")
out(vlans.index(20))
cmd("print(vlans.index(40))")
out(vlans.index(40))
blank()

pause()

explain(".count() — how many times does a value appear:")
blank()
explain("VLAN 20 appears three times in this list.")
explain("VLAN 99 is not in the list at all — .count() returns 0, not an error.")
explain("Useful for detecting duplicates before deduplicating.")
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
explain("Both take a generator expression as their argument.")
explain("any() short-circuits — it stops as soon as it finds a True item.")
explain("all() short-circuits — it stops as soon as it finds a False item.")
explain("This makes them efficient on large lists.")
blank()

statuses = ["up", "up", "down", "up"]
cmd("statuses = ['up', 'up', 'down', 'up']")
blank()
cmd("print(any(s == 'down' for s in statuses))   # any down?")
out(any(s == "down" for s in statuses))
explain("  → True — at least one interface is down. Trigger an alert.")
blank()
cmd("print(all(s == 'up'   for s in statuses))   # all up?")
out(all(s == "up" for s in statuses))
explain("  → False — not every interface is up. Health check fails.")
blank()

pause()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("print(any(v > 45 for v in vlans))   # any vlan over 45?")
out(any(v > 45 for v in vlans))
explain("  → True — VLAN 50 is greater than 45.")
blank()
cmd("print(all(v < 100 for v in vlans))  # all vlans under 100?")
out(all(v < 100 for v in vlans))
explain("  → True — every VLAN ID in the list is below 100.")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Modifying Lists
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Modifying Lists")

section("5.1 — Adding Items")

explain("Lists are mutable — you can add items at any time.")
explain("Three main methods: .append(), .insert(), and .extend().")
blank()

devices = ["nyc-rtr-01", "lon-sw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01']")
blank()

explain(".append() — add one item to the end:")
blank()
explain(".append() is O(1) — it adds to the end without shifting anything.")
explain("This is the standard way to grow a list inside a loop.")
blank()
cmd("devices.append('sin-fw-01')")
devices.append("sin-fw-01")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".insert(index, item) — add at a specific position:")
blank()
explain(".insert(1, ...) pushes every item from index 1 onwards one position right.")
explain("This is O(n) — every item after the insert point must shift.")
explain("Use .append() for adding to the end; .insert() only when position matters.")
blank()
cmd("devices.insert(1, 'ams-rtr-02')")
devices.insert(1, "ams-rtr-02")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".extend() — add all items from another list:")
blank()
explain(".extend() unpacks the argument and appends each item individually.")
explain("The original list grows by however many items the argument contains.")
explain("This is different from .append() which would add the list as ONE item.")
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
explain(".append([4, 5]) adds the list [4, 5] as a SINGLE item at index 3.")
explain("The result is [1, 2, 3, [4, 5]] — a nested list.")
explain(".extend([4, 5]) adds 4 and then 5 as SEPARATE items.")
explain("The result is [1, 2, 3, 4, 5] — a flat list.")
explain("This is one of the most common mistakes with lists — always")
explain("double-check whether you want one new item or many new items.")
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

explain("Four ways to remove: .remove(), .pop(), del, and .clear().")
explain("Choose based on whether you know the value or the index,")
explain("and whether you need the removed value back.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()

explain(".remove(value) — remove first occurrence of value:")
blank()
explain(".remove() scans for the value and deletes the first match.")
explain("It raises ValueError if the value is not found — use 'in' first if unsure.")
explain("Items after the removed one shift left to fill the gap.")
blank()
cmd("devices.remove('lon-sw-01')")
devices.remove("lon-sw-01")
cmd("print(devices)")
out(devices)
blank()

pause()

explain(".pop() — remove and return last item:")
blank()
explain(".pop() with no argument removes and returns the LAST item.")
explain("This is O(1) — no shifting needed when removing from the end.")
explain("Use this to treat a list like a stack (LIFO — last in, first out).")
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
explain(".pop(0) removes the first item — O(n) because every remaining")
explain("item must shift one position left to fill the gap.")
explain("Use this to treat a list like a queue (FIFO — first in, first out),")
explain("though collections.deque is more efficient for that pattern.")
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
explain("del is a statement, not a method — no return value.")
explain("del devices[1] removes the item at index 1.")
explain("del devices[0:2] removes a range — multiple items at once.")
explain("Use del when you know the index and don't need the value back.")
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
explain(".clear() empties the list but keeps the list object itself alive.")
explain("This is different from devices = [] which creates a brand-new list.")
explain("Use .clear() when other variables still reference the same list object")
explain("and you want them all to see an empty list.")
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

explain("Python gives you two ways to sort a list.")
explain(".sort() modifies the list in place — no new list is created.")
explain("sorted() returns a new sorted list — the original is untouched.")
explain("Choose .sort() when you want to sort and are done with the original.")
explain("Choose sorted() when you need to keep the original order intact.")
blank()

devices = ["sin-fw-01", "nyc-rtr-01", "ams-rtr-02", "lon-sw-01"]
cmd("devices = ['sin-fw-01', 'nyc-rtr-01', 'ams-rtr-02', 'lon-sw-01']")
blank()

explain(".sort() — sorts IN PLACE — modifies original:")
blank()
explain("After .sort(), devices is reordered alphabetically.")
explain("The original order is lost — there is no way to get it back.")
explain(".sort() returns None, not the sorted list — a common mistake is")
explain("writing 'devices = devices.sort()' which sets devices to None.")
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
explain("sorted_devices is a brand-new list in sorted order.")
explain("devices still holds the original unsorted order.")
explain("Use sorted() when you need both the sorted and original versions.")
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
explain("reverse=True makes the sort go from Z to A (or largest to smallest).")
explain("Works with both .sort() and sorted() — just add reverse=True.")
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
explain("Python calls the key function once per item and sorts by the results.")
explain("The items themselves are not changed — only the sort order changes.")
explain("key=lambda is the most common pattern — a small inline function.")
blank()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01", "ams-rtr-02"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01', 'ams-rtr-02']")
blank()

explain("Sort by the last 2 characters (the number):")
blank()
explain("d[-2:] extracts the trailing digits — '01', '02', etc.")
explain("Sorting by these suffixes groups devices by their number,")
explain("regardless of their hostname prefix (nyc, lon, sin, ams).")
blank()
cmd("devices.sort(key=lambda d: d[-2:])")
devices.sort(key=lambda d: d[-2:])
cmd("print(devices)")
out(devices)
blank()

pause()

explain("Sort a list of dicts by a specific key:")
blank()
explain("key=lambda d: d['vlans'] tells Python to sort by the 'vlans' value.")
explain("The full dict is what gets reordered — we are only keying on one field.")
explain("This is the standard way to sort a list of dicts in Python.")
explain("Use operator.itemgetter('vlans') as a faster alternative to the lambda.")
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
explain("This pattern is explicit and easy to debug.")
explain("You can add print statements, try/except, or break/continue.")
explain("It is the right choice when the transformation logic is complex.")
explain("For simple one-liner transforms, Chapter 8 shows a cleaner way.")
blank()

pause()

explain("Normalise all hostnames to uppercase:")
blank()
explain("We create an empty list, then loop over devices.")
explain("Each hostname is uppercased with .upper() and appended to the result.")
explain("After the loop, upper_devices contains all transformed values.")
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
explain("d[:3] is a slice — it takes characters at index 0, 1, 2.")
explain("'nyc-rtr-01'[:3] → 'nyc', 'lon-sw-01'[:3] → 'lon', etc.")
explain("We collect these three-character site codes into a new list.")
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
explain("Comprehensions are not just shorter — they signal intent.")
explain("A comprehension says 'I am building a new list by transforming this one'.")
explain("A for loop is more general — it could be doing anything.")
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
explain("d.upper() is the expression — what to produce for each item.")
explain("'for d in devices' is the loop clause — what to iterate over.")
explain("The result is a brand-new list; devices is not modified.")
blank()
cmd("upper = [d.upper() for d in devices]")
upper = [d.upper() for d in devices]
cmd("print(upper)")
out(upper)
blank()

pause()

explain("Extract site codes:")
blank()
explain("d[:3] extracts the first three characters of each hostname.")
explain("One line replaces the four-line loop from Chapter 7.")
blank()
cmd("sites = [d[:3] for d in devices]")
sites = [d[:3] for d in devices]
cmd("print(sites)")
out(sites)
blank()

pause()

explain("Add a prefix to every hostname:")
blank()
explain("The f-string expression runs once per item.")
explain("This is the pattern for building config lines, API payloads,")
explain("or any string that needs a hostname embedded inside it.")
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
explain("Items that fail the condition are simply skipped.")
explain("The expression on the left is only evaluated for items that pass.")
explain("This is equivalent to: for item in iterable: if condition: append(expression).")
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
explain("The if clause filters out any device where status != 'up'.")
explain("Only the 'hostname' value (not the whole dict) goes into the result.")
explain("lon-sw-01 and tok-sw-01 are skipped because their status is 'down'.")
blank()
cmd("up_devices = [d['hostname'] for d in inventory if d['status'] == 'up']")
up_devices = [d["hostname"] for d in inventory if d["status"] == "up"]
cmd("print(up_devices)")
out(up_devices)
blank()

pause()

explain("Get only IOS-XE devices:")
blank()
explain("Filter on platform instead of status — same pattern, different field.")
explain("nyc-rtr-01 and ams-rtr-02 are IOS-XE; the rest are excluded.")
blank()
cmd("iosxe = [d['hostname'] for d in inventory if d['platform'] == 'IOS-XE']")
iosxe = [d["hostname"] for d in inventory if d["platform"] == "IOS-XE"]
cmd("print(iosxe)")
out(iosxe)
blank()

pause()

explain("Filter VLANs — exclude reserved ones:")
blank()
explain("RESERVED is a set — 'in' on a set is O(1), making this very fast")
explain("even if the VLAN list is large.")
explain("VLANs 1, 1002, and 1003 are in RESERVED and are filtered out.")
explain("Only the safe, user-assignable VLANs remain in safe_vlans.")
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
explain("'and' requires both conditions to be True — a stricter filter.")
explain("'or' requires at least one condition to be True — a wider filter.")
explain("You can chain as many conditions as needed, but keep it readable.")
explain("If the condition grows complex, move it into a helper function.")
blank()

cmd("# IOS-XE devices that are up")
cmd("result = [d['hostname'] for d in inventory")
cmd("          if d['platform'] == 'IOS-XE' and d['status'] == 'up']")
result = [d["hostname"] for d in inventory
          if d["platform"] == "IOS-XE" and d["status"] == "up"]
cmd("print(result)")
out(result)
explain("  → Only nyc-rtr-01 and ams-rtr-02 pass both conditions.")
blank()

pause()

cmd("# Devices that are down OR are ASA platform")
cmd("result = [d['hostname'] for d in inventory")
cmd("          if d['status'] == 'down' or d['platform'] == 'ASA']")
result = [d["hostname"] for d in inventory
          if d["status"] == "down" or d["platform"] == "ASA"]
cmd("print(result)")
out(result)
explain("  → Includes lon-sw-01 and tok-sw-01 (down) plus sin-fw-01 (ASA).")
blank()

pause()

section("8.4 — Transformation + Filtering Together")

explain("You can transform AND filter in one comprehension.")
blank()
explain("The expression (left side) and the filter (if clause) are independent.")
explain("You can change what you collect while also narrowing what qualifies.")
explain("This is where comprehensions outshine manual loops most clearly.")
blank()

cmd("# Uppercase hostname of every device that is 'up'")
cmd("result = [d['hostname'].upper() for d in inventory if d['status'] == 'up']")
result = [d["hostname"].upper() for d in inventory if d["status"] == "up"]
cmd("print(result)")
out(result)
explain("  → Filter keeps only 'up' devices; expression uppercases the hostname.")
blank()

pause()

cmd("# Build config snippet for each IOS-XE device that is up")
cmd("configs = [f\"hostname {d['hostname']}\" for d in inventory")
cmd("           if d['platform'] == 'IOS-XE' and d['status'] == 'up']")
configs = [f"hostname {d['hostname']}" for d in inventory
           if d["platform"] == "IOS-XE" and d["status"] == "up"]
cmd("for c in configs:")
cmd("    print(c)")
explain("  → One config line per qualifying device, ready to push.")
blank()
for c in configs:
    out(c)
blank()

pause()

section("8.5 — Nested List Comprehensions")

explain("A comprehension inside a comprehension.")
explain("Use when you need to flatten or process nested lists.")
blank()
explain("The key to reading nested comprehensions is left to right.")
explain("The leftmost 'for' is the outer loop; the next 'for' is inner.")
explain("Think of it as the loops written out, but compressed onto one line.")
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
explain("The outer loop 'for site in sites' visits each inner list.")
explain("The inner loop 'for iface in site' visits each interface in that list.")
explain("'iface' is what gets collected — so we get every interface, flattened.")
explain("Equivalent to a nested for loop that appends iface to a result list.")
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

explain("Python's built-in functions work directly on lists.")
explain("len() — count of items.")
explain("sum() — total of all numeric items.")
explain("min() — smallest item.")
explain("max() — largest item.")
explain("All four are O(n) — they scan the entire list once.")
blank()

vlans = [10, 20, 30, 40, 50]
cmd("vlans = [10, 20, 30, 40, 50]")
blank()
cmd("print(len(vlans))")
out(len(vlans))
explain("  → 5 items in the list.")
blank()
cmd("print(sum(vlans))")
out(sum(vlans))
explain("  → 10+20+30+40+50 = 150.")
blank()
cmd("print(min(vlans))")
out(min(vlans))
explain("  → 10 is the smallest VLAN ID.")
blank()
cmd("print(max(vlans))")
out(max(vlans))
explain("  → 50 is the largest VLAN ID.")
blank()

pause()

explain("Practical use — count enabled interfaces:")
blank()
explain("sum() with a generator expression counts items matching a condition.")
explain("'sum(1 for s in statuses if s == \"up\")' adds 1 for every 'up' status.")
explain("This is more readable than len([s for s in statuses if s == 'up'])")
explain("because it avoids building an intermediate list in memory.")
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
explain("list(range(1, 6)) materialises the range into a real list.")
explain("list('IOS-XE') splits the string into individual characters.")
explain("list({'nyc', 'lon', 'sin'}) converts a set to a list.")
explain("Note: sets are unordered so the list order is not guaranteed.")
explain("Use list() any time you need to index or slice an iterable.")
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
explain("An iterator produces values one at a time — it does not store them all.")
explain("Wrapping in list() forces it to produce every value immediately.")
explain("This is useful for debugging — print(list(zip(...))) shows the pairs.")
explain("In a for loop you do NOT need list() — the loop consumes the iterator.")
blank()

hostnames = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
ips       = ["10.0.0.1",   "10.1.0.1",  "10.2.0.1"]
cmd("hostnames = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("ips       = ['10.0.0.1',   '10.1.0.1',  '10.2.0.1']")
blank()
cmd("print(list(zip(hostnames, ips)))")
out(list(zip(hostnames, ips)))
explain("  → Each pair is a tuple: (hostname, ip).")
blank()
cmd("print(list(enumerate(hostnames)))")
out(list(enumerate(hostnames)))
explain("  → Each pair is a tuple: (index, hostname) starting at 0.")
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
explain("The outer index selects the row; the inner index selects the column.")
explain("This models tabular data — like a spreadsheet or a CSV file.")
explain("For structured records with named fields, a list of dicts (10.2) is better.")
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

explain("Accessing rows and specific fields:")
blank()
explain("interfaces[0]      → the whole first row as a list.")
explain("interfaces[0][0]   → first row, first column → interface name.")
explain("interfaces[1][2]   → second row, third column → VLAN 20.")
blank()
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
explain("Each inner list has exactly three items — name, mode, vlan.")
explain("Python unpacks them into three variables automatically.")
explain("This is cleaner than accessing row[0], row[1], row[2] by index.")
explain("If any row has a different length, Python raises ValueError.")
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
explain("Dicts give each field a name — no need to remember 'column 2 is the IP'.")
explain("This makes code self-documenting: device['ip'] is unambiguous.")
explain("It also means fields can be missing without breaking the structure.")
explain("This is the shape you get from JSON APIs, Ansible inventory, and YAML files.")
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
explain("inventory[0] selects the first dict (nyc-rtr-01).")
explain("['hostname'] then accesses the 'hostname' key inside that dict.")
explain("inventory[2]['ip'] — third device, its IP address.")
blank()
cmd("print(inventory[0]['hostname'])")
out(inventory[0]["hostname"])
cmd("print(inventory[2]['ip'])")
out(inventory[2]["ip"])
blank()

pause()

explain("Iterate and print a summary:")
blank()
explain("Each iteration yields one dict — we access fields by key name.")
explain("{:<15} left-aligns the hostname in a 15-character wide column.")
explain("{:<10} does the same for the platform — results line up as a table.")
explain("This is a common pattern for producing human-readable inventory reports.")
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
explain("In Python, assignment copies a reference, not the object.")
explain("'alias = vlans' makes both names point to the same list in memory.")
explain("Any change through either name is visible through the other.")
explain("This is a frequent source of bugs when passing lists to functions.")
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
explain("  ↑ WARNING: vlans was unexpectedly modified through the alias.")
blank()

pause()

vlans = [10, 20, 30]
cmd("# Correct — copy")
cmd("vlans = [10, 20, 30]")
cmd("copy  = vlans.copy()")
copy = vlans.copy()
explain("  .copy() creates a new list with the same items — two independent objects.")
explain("  vlans[:] does the same thing — it is a 'full slice' that returns a copy.")
blank()
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
explain("Python's list iterator tracks the current index internally.")
explain("When you remove an item, every following item shifts left by one.")
explain("The iterator still advances by one — so it skips the item that shifted in.")
explain("The result is silent data loss — items are skipped without any error.")
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
explain("  ↑ 30 was removed, but the iterator skipped 40 as a side effect.")
blank()

pause()

vlans = [10, 20, 30, 40, 50]
cmd("# Correct — iterate a copy, modify the original")
cmd("vlans = [10, 20, 30, 40, 50]")
cmd("for v in vlans.copy():")
cmd("    if v == 30:")
cmd("        vlans.remove(v)")
explain("  vlans.copy() creates a snapshot to iterate over.")
explain("  The original vlans is modified freely because we are not iterating it.")
for v in vlans.copy():
    if v == 30:
        vlans.remove(v)
cmd("print(vlans)")
out(vlans)
blank()

pause()

explain("Or use a list comprehension — cleanest way:")
blank()
explain("The comprehension reads vlans and writes a brand-new list.")
explain("There is no in-place modification at all — no iteration conflict possible.")
explain("This is the preferred pattern whenever you want to filter a list.")
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
explain("entry is a single dict object created once before the loop.")
explain("Each iteration changes entry['hostname'] and appends entry to result.")
explain("But result contains multiple references to the SAME dict object.")
explain("When the loop ends, entry holds the last hostname — so all")
explain("three items in result show the same (last) hostname.")
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
explain("  ↑ All three dicts show 'sin-fw-01' — they are the same object.")
blank()

pause()

explain("The fix: create a new dict on every iteration.")
explain("A comprehension does this naturally — {} inside the expression")
explain("is evaluated fresh each time, producing a distinct dict object.")
blank()
cmd("# Correct — new dict each iteration")
cmd("result = [{'hostname': name} for name in ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']]")
result = [{"hostname": name} for name in ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]]
cmd("print(result)")
out(result)
explain("  ↑ Each dict is independent — three separate objects with different values.")
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
explain("A good rule of thumb: if you cannot read the comprehension aloud")
explain("and understand it in one pass, rewrite it as a for loop instead.")
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
explain("  → One line, no side effects, clear intent: 'give me IOS-XE IPs'.")
blank()

pause()

cmd("# Loop — side effect (pushing config to device)")
cmd("for device in inventory:")
cmd("    if device['platform'] == 'IOS-XE':")
cmd("        print(f\"Pushing config to {device['hostname']}...\")")
cmd("        # connect_and_push(device['ip'], config)")
blank()
explain("  The loop is right here because it has a side effect (pushing config).")
explain("  A comprehension would be misleading — it implies you are collecting results.")
explain("  Use a loop when the point is the action, not the collected output.")
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