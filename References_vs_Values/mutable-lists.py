# mutable_lists_proof.py
# Proving list mutability in Python
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
print(f"{BOLD}█         PROVING LIST MUTABILITY IN PYTHON                  █{RESET}")
print(f"{BOLD}█         Cisco IaC Perspective                              █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 1 — Mutation methods change the object in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 1 — Mutation methods change the object in place")

explain("We have a list of Cisco device hostnames.")
explain("We call mutation methods on it.")
explain("Watch the id — it never changes.")
explain("Same id before and after means the SAME object was modified.")
blank()

pause()

devices = ["nyc-rtr-01", "lon-sw-01", "sin-fw-01"]
cmd("devices = ['nyc-rtr-01', 'lon-sw-01', 'sin-fw-01']")
cmd("print(devices)")
out(devices)
cmd("print(id(devices))")
out_id(id(devices))
blank()

pause()

explain("Call .append() — add a new device:")
blank()
cmd("devices.append('ams-rtr-01')")
devices.append("ams-rtr-01")
cmd("print(devices)")
out(devices)
cmd("print(id(devices))")
out_id(id(devices))
blank()

pause()

explain("Same id — the same list object was modified in place.")
blank()

pause()

explain("Call .remove() — remove a device:")
blank()
cmd("devices.remove('lon-sw-01')")
devices.remove("lon-sw-01")
cmd("print(devices)")
out(devices)
cmd("print(id(devices))")
out_id(id(devices))
blank()

pause()

explain("Same id again — still the same object.")
blank()

pause()

explain("Call .sort() — sort the list alphabetically:")
blank()
cmd("devices.sort()")
devices.sort()
cmd("print(devices)")
out(devices)
cmd("print(id(devices))")
out_id(id(devices))
blank()

pause()

explain("Call .reverse() — reverse the order:")
blank()
cmd("devices.reverse()")
devices.reverse()
cmd("print(devices)")
out(devices)
cmd("print(id(devices))")
out_id(id(devices))
blank()

pause()

explain("✔ The id never changed across any of these operations.")
explain("  append, remove, sort, reverse — all modified the")
explain("  same object in place. This is what mutability means.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 2 — You CAN modify an element in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 2 — You CAN modify an element in place")

explain("We have a list of interface states for a Cisco switch.")
explain("We change one element directly using its index.")
explain("Watch the id — same object, element changed in place.")
blank()

pause()

interfaces = ["Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3"]
cmd("interfaces = ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3']")
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("Replace the first interface using index assignment:")
blank()
cmd("interfaces[0] = 'Te1/0/1'")
interfaces[0] = "Te1/0/1"
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("Same id — the same list object was modified.")
blank()

pause()

explain("Delete an element using del:")
blank()
cmd("del interfaces[1]")
del interfaces[1]
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("Insert a new element at a specific position:")
blank()
cmd("interfaces.insert(1, 'Gi0/5')")
interfaces.insert(1, "Gi0/5")
cmd("print(interfaces)")
out(interfaces)
cmd("print(id(interfaces))")
out_id(id(interfaces))
blank()

pause()

explain("✔ Item assignment, deletion, and insertion all work.")
explain("  Every operation modified the same list object in place.")
explain("  The id never changed. This is the opposite of tuples.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 3 — Aliasing: two names, one object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 3 — Aliasing: two names, one object")

explain("We have a list of NTP servers.")
explain("We assign it to a second variable — this is an alias.")
explain("Both names point to the same object.")
explain("Mutating through one name is visible through the other.")
blank()

pause()

ntp_primary = ["10.0.0.100", "10.0.0.101"]
cmd("ntp_primary = ['10.0.0.100', '10.0.0.101']")
cmd("print(ntp_primary)")
out(ntp_primary)
cmd("print(id(ntp_primary))")
out_id(id(ntp_primary))
blank()

pause()

ntp_backup = ntp_primary
cmd("ntp_backup = ntp_primary   # alias — same object")
cmd("print(ntp_backup)")
out(ntp_backup)
cmd("print(id(ntp_backup))")
out_id(id(ntp_backup))
blank()

pause()

explain("Both ids are identical — one object, two names.")
blank()

pause()

explain("Now mutate through ntp_backup:")
blank()
cmd("ntp_backup.append('10.0.0.102')")
ntp_backup.append("10.0.0.102")
cmd("print(ntp_backup)")
out(ntp_backup)
cmd("print(id(ntp_backup))")
out_id(id(ntp_backup))
blank()

pause()

explain("Check ntp_primary — did it change?")
blank()
cmd("print(ntp_primary)")
out(ntp_primary)
cmd("print(id(ntp_primary))")
out_id(id(ntp_primary))
blank()

pause()

warn("⚠ YES — ntp_primary also changed.")
warn("  Both names point to the same list object.")
warn("  Mutating through ntp_backup mutated the shared object.")
warn("  ntp_primary and ntp_backup have the same id — always.")
blank()

pause()

explain("Now try removing through ntp_primary:")
blank()
cmd("ntp_primary.remove('10.0.0.101')")
ntp_primary.remove("10.0.0.101")
cmd("print(ntp_primary)")
out(ntp_primary)
cmd("print(id(ntp_primary))")
out_id(id(ntp_primary))
blank()

pause()

explain("Check ntp_backup — did it change?")
blank()
cmd("print(ntp_backup)")
out(ntp_backup)
cmd("print(id(ntp_backup))")
out_id(id(ntp_backup))
blank()

pause()

warn("⚠ YES — ntp_backup also changed.")
warn("  It does not matter which name you mutate through.")
warn("  There is only one list. Both names see every change.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 4 — += mutates in place (unlike strings and booleans)
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 4 — += mutates in place (unlike strings and booleans)")

explain("With strings and booleans, += created a new object.")
explain("With lists, += calls __iadd__ which extends in place.")
explain("The id stays the same — the same object is modified.")
blank()

pause()

vlans = [10, 20, 30]
ref   = vlans

cmd("vlans = [10, 20, 30]")
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

explain("Now use += to extend vlans:")
blank()
cmd("vlans += [40, 50]")
vlans += [40, 50]
cmd("print(vlans)")
out(vlans)
cmd("print(id(vlans))")
out_id(id(vlans))
blank()

pause()

explain("Check ref — did it also change?")
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

warn("⚠ YES — ref also changed.")
warn("  += on a list does NOT create a new object.")
warn("  It calls list.__iadd__ which extends the list in place.")
warn("  The id of vlans before and after += is identical.")
blank()

pause()

explain("Compare with + which DOES create a new object:")
blank()

vlans2 = [10, 20, 30]
ref2   = vlans2

cmd("vlans2 = [10, 20, 30]")
cmd("ref2   = vlans2")
cmd("print(id(vlans2))")
out_id(id(vlans2))
blank()

vlans2 = vlans2 + [40, 50]
cmd("vlans2 = vlans2 + [40, 50]   # new list object")
cmd("print(vlans2)")
out(vlans2)
cmd("print(id(vlans2))")
out_id(id(vlans2))
blank()

pause()

explain("Check ref2 — did it change?")
blank()
cmd("print(ref2)")
out(ref2)
cmd("print(id(ref2))")
out_id(id(ref2))
blank()

pause()

explain("✔ ref2 did NOT change — + created a brand new list.")
explain("  The id of vlans2 changed after =+.")
explain("  Use + when you want independence.")
explain("  Use += when you want to mutate in place.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 5 — Functions CAN mutate a list you pass in
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 5 — Functions CAN mutate a list you pass in")

explain("We pass a list of device hostnames into a function.")
explain("The function mutates it using .append().")
explain("Watch the id — it is the same inside and outside the function.")
explain("The caller's list is modified.")
blank()

pause()

def add_device(inventory, new_device):
    """
    Appends a device to the inventory list in place.
    The caller's list is directly modified.
    Same object — same id inside and outside.
    """
    inventory.append(new_device)

explain("Here is the function we will call:")
blank()
cmd("def add_device(inventory, new_device):")
cmd("    inventory.append(new_device)")
blank()
explain("It appends to the list in place.")
explain("It receives a reference to the same list object.")
explain("Any mutation inside is visible outside.")
blank()

pause()

inventory = ["nyc-rtr-01", "lon-sw-01"]
cmd("inventory = ['nyc-rtr-01', 'lon-sw-01']")
cmd("print(inventory)")
out(inventory)
cmd("print(id(inventory))")
out_id(id(inventory))
blank()

pause()

explain("Now call add_device(inventory, 'sin-fw-01'):")
blank()
cmd("add_device(inventory, 'sin-fw-01')")
add_device(inventory, "sin-fw-01")
blank()

pause()

explain("Check inventory after the function ran:")
blank()
cmd("print(inventory)")
out(inventory)
cmd("print(id(inventory))")
out_id(id(inventory))
blank()

pause()

warn("⚠ inventory was modified by the function.")
warn("  The function received a reference to the same list.")
warn("  .append() mutated the shared object.")
warn("  The id is identical — before, during, and after the call.")
blank()

pause()

explain("Call it again — the modification keeps accumulating:")
blank()
cmd("add_device(inventory, 'ams-rtr-01')")
add_device(inventory, "ams-rtr-01")
cmd("add_device(inventory, 'tok-sw-01')")
add_device(inventory, "tok-sw-01")
cmd("print(inventory)")
out(inventory)
cmd("print(id(inventory))")
out_id(id(inventory))
blank()

pause()

explain("✔ Same id throughout every call.")
explain("  The list was never copied — the same object")
explain("  was passed in and mutated every single time.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 6 — The fix: .copy() gives you independence
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 6 — The fix: .copy() gives you independence")

explain("When you need an independent list, call .copy() explicitly.")
explain("This creates a NEW object at a NEW id.")
explain("Mutations to the copy do not affect the original.")
explain("Mutations to the original do not affect the copy.")
blank()

pause()

base_vlans = [10, 20, 30]
cmd("base_vlans = [10, 20, 30]")
cmd("print(base_vlans)")
out(base_vlans)
cmd("print(id(base_vlans))")
out_id(id(base_vlans))
blank()

pause()

site_vlans = base_vlans.copy()
cmd("site_vlans = base_vlans.copy()")
cmd("print(site_vlans)")
out(site_vlans)
cmd("print(id(site_vlans))")
out_id(id(site_vlans))
blank()

pause()

explain("The ids are DIFFERENT — two independent list objects.")
blank()

pause()

explain("Mutate site_vlans — does base_vlans change?")
blank()
cmd("site_vlans.append(40)")
site_vlans.append(40)
cmd("site_vlans.remove(10)")
site_vlans.remove(10)
cmd("print(site_vlans)")
out(site_vlans)
cmd("print(id(site_vlans))")
out_id(id(site_vlans))
blank()

pause()

cmd("print(base_vlans)")
out(base_vlans)
cmd("print(id(base_vlans))")
out_id(id(base_vlans))
blank()

pause()

explain("✔ base_vlans is completely untouched.")
explain("  site_vlans has its own id — its own object in memory.")
explain("  Changes to one do not affect the other.")
blank()

pause()

explain("The same pattern works for functions:")
blank()

def add_device_safe(inventory, new_device):
    """
    Works on a copy — caller's list is never modified.
    Returns the new list as a separate object.
    """
    copy = inventory.copy()
    copy.append(new_device)
    return copy

cmd("def add_device_safe(inventory, new_device):")
cmd("    copy = inventory.copy()")
cmd("    copy.append(new_device)")
cmd("    return copy")
blank()

pause()

inventory = ["nyc-rtr-01", "lon-sw-01"]
cmd("inventory = ['nyc-rtr-01', 'lon-sw-01']")
cmd("print(inventory)")
out(inventory)
cmd("print(id(inventory))")
out_id(id(inventory))
blank()

pause()

result = add_device_safe(inventory, "sin-fw-01")
cmd("result = add_device_safe(inventory, 'sin-fw-01')")
cmd("print(result)")
out(result)
cmd("print(id(result))")
out_id(id(result))
blank()

pause()

explain("Check inventory — was it modified?")
blank()
cmd("print(inventory)")
out(inventory)
cmd("print(id(inventory))")
out_id(id(inventory))
blank()

pause()

explain("✔ inventory is untouched. id unchanged.")
explain("  result is a brand new list at a different id.")
explain("  The function worked on a copy — the caller is safe.")

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
print(f"  {BOLD}Proof 1{RESET}  Mutation methods change the object in place")
print(f"  {DIM}         .append(), .remove(), .sort(), .reverse() — id never changes{RESET}")
blank()
print(f"  {BOLD}Proof 2{RESET}  You CAN modify an element in place")
print(f"  {DIM}         lst[0] = 'x', del lst[1], .insert() — same id throughout{RESET}")
blank()
print(f"  {BOLD}Proof 3{RESET}  Aliasing — two names, one object")
print(f"  {DIM}         b = a then mutate through b — a sees every change{RESET}")
blank()
print(f"  {BOLD}Proof 4{RESET}  += mutates in place — unlike strings and booleans")
print(f"  {DIM}         vlans += [40, 50] — same id before and after{RESET}")
print(f"  {DIM}         vlans = vlans + [40, 50] — new id, new object{RESET}")
blank()
print(f"  {BOLD}Proof 5{RESET}  Functions CAN mutate a list you pass in")
print(f"  {DIM}         id is identical inside and outside the function{RESET}")
print(f"  {DIM}         .append() inside modifies the caller's list{RESET}")
blank()
print(f"  {BOLD}Proof 6{RESET}  The fix — .copy() gives you independence")
print(f"  {DIM}         .copy() creates a new object at a new id{RESET}")
print(f"  {DIM}         Mutations to the copy never affect the original{RESET}")
blank()
print(f"  {WHITE}In Cisco IaC — lists hold interface inventories, VLAN")
print(f"  lists, device rosters, NTP servers. Always be aware")
print(f"  that passing a list into a function gives that function")
print(f"  direct access to your data. Use .copy() when you need")
print(f"  the function to work on its own independent version.{RESET}")
blank()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█   Proof complete.                                          █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
print()