# immutable_tuples_proof.py
# Proving tuple immutability in Python
# Cisco IaC perspective
# Press ENTER to advance through each step

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"    # >>> commands
GREEN  = "\033[92m"    # output values
YELLOW = "\033[93m"    # ids
WHITE  = "\033[97m"    # explanations
RED    = "\033[91m"    # errors
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

def err(value):
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
print(f"{BOLD}█         PROVING TUPLE IMMUTABILITY IN PYTHON               █{RESET}")
print(f"{BOLD}█         Cisco IaC Perspective                              █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 1 — Tuples have no mutation methods
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 1 — Tuples have no mutation methods")

explain("We have a tuple of Cisco device specs.")
explain("We try to call .append() on it — the same way we would on a list.")
explain("Python will refuse — tuples do not have mutation methods at all.")
blank()

pause()

device_spec = ("Cisco", "Catalyst 9300", "IOS-XE", "48-port")
cmd("device_spec = ('Cisco', 'Catalyst 9300', 'IOS-XE', '48-port')")
cmd("print(device_spec)")
out(device_spec)
cmd("print(id(device_spec))")
out_id(id(device_spec))
blank()

pause()

explain("Now try to append a new element:")
blank()
cmd("device_spec.append('PoE+')")
blank()

pause()

try:
    device_spec.append("PoE+")
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

pause()

explain("Try to remove an element:")
blank()
cmd("device_spec.remove('IOS-XE')")
blank()

pause()

try:
    device_spec.remove("IOS-XE")
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

pause()

explain("Try to sort it:")
blank()
cmd("device_spec.sort()")
blank()

pause()

try:
    device_spec.sort()
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

pause()

explain("Check device_spec — completely untouched:")
blank()
cmd("print(device_spec)")
out(device_spec)
cmd("print(id(device_spec))")
out_id(id(device_spec))
blank()

pause()

explain("✔ Python does not even give tuples these methods.")
explain("  append, remove, sort — none of them exist on a tuple.")
explain("  Immutability is enforced at the design level.")
explain("  The object at that address cannot be modified.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 2 — You cannot modify an element in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 2 — You cannot modify an element in place")

explain("We have a tuple of interface assignments for a Cisco switch.")
explain("We try to change one element directly using its index.")
explain("Python will refuse — tuples do not support item assignment.")
blank()

pause()

interfaces = ("Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3")
cmd("interfaces = ('Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3')")
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("Try to change the first interface:")
blank()
cmd("interfaces[0] = 'Te1/0/1'")
blank()

pause()

try:
    interfaces[0] = "Te1/0/1"
except TypeError as e:
    err(f"TypeError: {e}")
blank()

pause()

explain("Try to delete an element:")
blank()
cmd("del interfaces[1]")
blank()

pause()

try:
    del interfaces[1]
except TypeError as e:
    err(f"TypeError: {e}")
blank()

pause()

explain("interfaces is completely untouched:")
blank()
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("✔ Same value. Same id. Python rejected both modifications.")
explain("  Item assignment and deletion are not allowed on tuples.")
explain("  Every element is locked in place at the language level.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 3 — Reassignment creates a new object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 3 — Reassignment creates a new object")

explain("We have a tuple of NTP servers for a site.")
explain("We reassign the variable to a new tuple.")
explain("A second variable pointing to the original proves")
explain("the original object was never touched.")
blank()

pause()

ntp_servers = ("10.0.0.100", "10.0.0.101")
ref         = ntp_servers

cmd("ntp_servers = ('10.0.0.100', '10.0.0.101')")
cmd("ref         = ntp_servers   # ref points to same object")
cmd("print(ntp_servers)")
out(ntp_servers)
cmd("print(id(ntp_servers))")
out_id(id(ntp_servers))
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("Both point to the same object — same id.")
blank()

pause()

ntp_servers = ("10.0.0.100", "10.0.0.101", "10.0.0.102")
cmd("ntp_servers = ('10.0.0.100', '10.0.0.101', '10.0.0.102')")
cmd("print(ntp_servers)")
out(ntp_servers)
cmd("print(id(ntp_servers))")
out_id(id(ntp_servers))
blank()

pause()

explain("ntp_servers now points to a new object.")
explain("What happened to the original ('10.0.0.100', '10.0.0.101')?")
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("✔ ref still points to the original 2-server tuple.")
explain("  Same id as before. The object was never modified.")
explain("  Reassignment moved the label — not the object.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 4 — Concatenation returns a new object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 4 — Concatenation returns a new object")

explain("We have a tuple of VLAN IDs.")
explain("We use + to add a new VLAN.")
explain("This looks like modification — but it produces a brand new tuple.")
explain("The original is completely untouched.")
blank()

pause()

vlans = (10, 20, 30)
ref   = vlans

cmd("vlans = (10, 20, 30)")
cmd("ref   = vlans   # ref points to same object")
cmd("print(vlans)")
out(vlans)
cmd("print(id(vlans))")
out_id(id(vlans))
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

vlans_extended = vlans + (40, 50)
cmd("vlans_extended = vlans + (40, 50)")
cmd("print(vlans_extended)")
out(vlans_extended)
cmd("print(id(vlans_extended))")
out_id(id(vlans_extended))
blank()

pause()

explain("Now check the original vlans — and ref:")
blank()
cmd("print(vlans)")
out(vlans)
cmd("print(id(vlans))")
out_id(id(vlans))
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("✔ vlans and ref still have the same id as when they were defined.")
explain("  vlans + (40, 50) produced a brand new tuple object.")
explain("  The original (10, 20, 30) was never touched.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 5 — Functions cannot corrupt a tuple you pass in
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 5 — Functions cannot corrupt a tuple you pass in")

explain("We pass a tuple of device specs into a function.")
explain("The function reads from it and builds a new result.")
explain("We check the id before and after to prove it is unchanged.")
blank()

pause()

def format_device_label(spec):
    """
    Reads the tuple and builds a formatted string.
    Cannot modify the tuple — tuples are immutable.
    Returns a brand new string object.
    """
    vendor, model, os, ports = spec
    return f"{vendor} | {model} | {os} | {ports}"

explain("Here is the function we will call:")
blank()
cmd("def format_device_label(spec):")
cmd("    vendor, model, os, ports = spec")
cmd("    return f'{vendor} | {model} | {os} | {ports}'")
blank()
explain("It unpacks the tuple and builds a new formatted string.")
explain("It has no way to modify the original tuple — tuples are immutable.")
blank()

pause()

device_spec = ("Cisco", "Catalyst 9300", "IOS-XE", "48-port")
cmd("device_spec = ('Cisco', 'Catalyst 9300', 'IOS-XE', '48-port')")
cmd("print(device_spec)")
out(device_spec)
cmd("print(id(device_spec))")
out_id(id(device_spec))
blank()

pause()

explain("Now call format_device_label(device_spec):")
blank()
cmd("result = format_device_label(device_spec)")
result = format_device_label(device_spec)
cmd("print(result)")
out(result)
cmd("print(id(result))")
out_id(id(result))
blank()

pause()

explain("Check the original after the function ran:")
blank()
cmd("print(device_spec)")
out(device_spec)
cmd("print(id(device_spec))")
out_id(id(device_spec))
blank()

pause()

explain("✔ id(device_spec) is identical before and after the function call.")
explain("  The function read the tuple and produced a new string.")
explain("  It had no way to modify the original — tuples are immutable.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 6 — The gotcha: mutable object INSIDE a tuple
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 6 — The gotcha: mutable object inside a tuple")

explain("This is the most important proof — unique to tuples.")
blank()
explain("A tuple is immutable. But if it contains a list,")
explain("the tuple cannot be changed — however the LIST inside")
explain("is still mutable. The tuple protects the reference,")
explain("not the object the reference points to.")
blank()

pause()

explain("We have a site config tuple containing a list of VLANs:")
blank()

site = ("NYC", "10.0.0.1", [10, 20, 30])
cmd("site = ('NYC', '10.0.0.1', [10, 20, 30])")
cmd("print(site)")
out(site)
cmd("print(id(site))")
out_id(id(site))
blank()
cmd("print(id(site[2]))   # id of the list inside")
out_id(id(site[2]))
blank()

pause()

explain("Try to replace the list itself — tuple blocks this:")
blank()
cmd("site[2] = [40, 50, 60]")
blank()

pause()

try:
    site[2] = [40, 50, 60]
except TypeError as e:
    err(f"TypeError: {e}")
blank()

pause()

explain("Good — the tuple protected its reference.")
explain("But now try to mutate the LIST that is already inside:")
blank()
cmd("site[2].append(40)")
blank()

pause()

site[2].append(40)
cmd("print(site)")
out(site)
cmd("print(id(site))")
out_id(id(site))
blank()
cmd("print(id(site[2]))   # id of the list inside")
out_id(id(site[2]))
blank()

pause()

explain("✔ The tuple id is unchanged — the tuple itself was not modified.")
explain("  But the list inside was mutated — it now contains 40.")
blank()
explain("  The tuple holds a reference to the list.")
explain("  That reference cannot be replaced — that is immutability.")
explain("  But the list object at that reference is still mutable.")
blank()

pause()

explain("The fix — use a tuple for the inner data too:")
blank()

site_safe = ("NYC", "10.0.0.1", (10, 20, 30))
cmd("site_safe = ('NYC', '10.0.0.1', (10, 20, 30))")
cmd("print(site_safe)")
out(site_safe)
cmd("print(id(site_safe))")
out_id(id(site_safe))
blank()

pause()

explain("Now try to mutate the inner tuple:")
blank()
cmd("site_safe[2].append(40)")
blank()

pause()

try:
    site_safe[2].append(40)
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

cmd("print(site_safe)")
out(site_safe)
cmd("print(id(site_safe))")
out_id(id(site_safe))
blank()

pause()

explain("✔ Now both layers are immutable.")
explain("  The outer tuple protects its references.")
explain("  The inner tuple protects its elements.")
explain("  No mutation is possible at any level.")

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
print(f"  {BOLD}Proof 1{RESET}  Tuples have no mutation methods")
print(f"  {DIM}         .append(), .remove(), .sort() — AttributeError{RESET}")
blank()
print(f"  {BOLD}Proof 2{RESET}  You cannot modify an element in place")
print(f"  {DIM}         t[0] = 'x' and del t[0] — both raise TypeError{RESET}")
blank()
print(f"  {BOLD}Proof 3{RESET}  Reassignment creates a new object")
print(f"  {DIM}         ntp_servers = new_tuple moved the label, not the object{RESET}")
blank()
print(f"  {BOLD}Proof 4{RESET}  Concatenation returns a new object")
print(f"  {DIM}         vlans + (40, 50) produced a new tuple — original untouched{RESET}")
blank()
print(f"  {BOLD}Proof 5{RESET}  Functions cannot corrupt a tuple you pass in")
print(f"  {DIM}         id(device_spec) identical before and after the call{RESET}")
blank()
print(f"  {BOLD}Proof 6{RESET}  The gotcha — mutable object inside a tuple")
print(f"  {DIM}         Tuple protects the reference, not what the reference points to{RESET}")
print(f"  {DIM}         Fix: use tuples for inner data too{RESET}")
blank()
print(f"  {WHITE}In Cisco IaC — tuples are ideal for device specs, interface")
print(f"  pairs, NTP server lists, VLAN tables — anything that should")
print(f"  be defined once and never changed. They signal intent:")
print(f"  this data is read-only. But if you put a list inside,")
print(f"  that list is still mutable — use inner tuples to be safe.{RESET}")
blank()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█   Proof complete.                                          █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
print()