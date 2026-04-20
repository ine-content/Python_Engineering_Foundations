# immutable_booleans_proof.py
# Proving boolean immutability in Python
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
print(f"{BOLD}█         PROVING BOOLEAN IMMUTABILITY IN PYTHON             █{RESET}")
print(f"{BOLD}█         Cisco IaC Perspective                              █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 1 — Booleans have no mutation methods
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 1 — Booleans have no mutation methods")

explain("We have a boolean flag controlling interface state.")
explain("We try to call methods on it to change its value in place.")
explain("Python will refuse — booleans have no mutation methods.")
blank()

pause()

interface_enabled = True
cmd("interface_enabled = True")
cmd("print(interface_enabled)")
out(interface_enabled)
cmd("print(id(interface_enabled))")
out_id(id(interface_enabled))
blank()

pause()

explain("Try to flip the value in place using a method:")
blank()
cmd("interface_enabled.flip()")
blank()

pause()

try:
    interface_enabled.flip()
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

pause()

explain("Try to call .toggle() on it:")
blank()
cmd("interface_enabled.toggle()")
blank()

pause()

try:
    interface_enabled.toggle()
except AttributeError as e:
    err(f"AttributeError: {e}")
blank()

pause()

explain("Check interface_enabled — completely untouched:")
blank()
cmd("print(interface_enabled)")
out(interface_enabled)
cmd("print(id(interface_enabled))")
out_id(id(interface_enabled))
blank()

pause()

explain("✔ Booleans have no methods that modify them.")
explain("  There is no way to change True into False in place.")
explain("  The only option is reassignment — which creates a new object.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 2 — You cannot modify a bool in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 2 — You cannot modify a bool in place")

explain("We have a boolean representing the shutdown state of a device.")
explain("We try to modify it using index assignment.")
explain("Python will refuse — booleans are not subscriptable.")
blank()

pause()

is_shutdown = False
cmd("is_shutdown = False")
cmd("print(is_shutdown)")
out(is_shutdown)
cmd("print(id(is_shutdown))")
out_id(id(is_shutdown))
blank()

pause()

explain("Try to modify it using index syntax:")
blank()
cmd("is_shutdown[0] = True")
blank()

pause()

try:
    is_shutdown[0] = True
except TypeError as e:
    err(f"TypeError: {e}")
blank()

pause()

explain("Try to use augmented assignment in place:")
blank()
cmd("is_shutdown |= True")
blank()

pause()

is_shutdown_copy = is_shutdown
cmd("is_shutdown_copy = is_shutdown   # save reference to original")
blank()
is_shutdown |= True
cmd("is_shutdown |= True")
blank()

pause()

cmd("print(is_shutdown)")
out(is_shutdown)
cmd("print(id(is_shutdown))")
out_id(id(is_shutdown))
blank()

pause()

explain("Notice the id changed — |= did NOT modify the original object.")
explain("It created a new bool object and rebound is_shutdown to it.")
explain("The original False object still exists:")
blank()
cmd("print(is_shutdown_copy)")
out(is_shutdown_copy)
cmd("print(id(is_shutdown_copy))")
out_id(id(is_shutdown_copy))
blank()

pause()

explain("✔ is_shutdown_copy still holds the original False.")
explain("  |= moved the label to a new object — it did not mutate.")
explain("  Booleans cannot be changed in place. Ever.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 3 — Reassignment creates a new object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 3 — Reassignment creates a new object")

explain("We have a flag controlling whether debug logging is enabled.")
explain("We reassign it to the opposite value.")
explain("A second variable proves the original object is untouched.")
blank()

pause()

debug_enabled = True
ref           = debug_enabled

cmd("debug_enabled = True")
cmd("ref           = debug_enabled   # ref points to same object")
cmd("print(debug_enabled)")
out(debug_enabled)
cmd("print(id(debug_enabled))")
out_id(id(debug_enabled))
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("Both point to the same True object — same id.")
blank()

pause()

debug_enabled = False
cmd("debug_enabled = False   # reassign to False")
cmd("print(debug_enabled)")
out(debug_enabled)
cmd("print(id(debug_enabled))")
out_id(id(debug_enabled))
blank()

pause()

explain("debug_enabled now points to False.")
explain("What happened to the original True object?")
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("✔ ref still points to the original True object.")
explain("  Same id as before. The True object was never modified.")
explain("  Reassignment moved the label — not the object.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 4 — The gotcha: bool is a subclass of int
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 4 — The gotcha: bool is a subclass of int")

explain("This is unique to booleans — they are not just True/False.")
explain("In Python, bool is a subclass of int.")
explain("True == 1 and False == 0.")
explain("This surprises people and causes bugs in IaC scripts.")
blank()

pause()

explain("Check the type and inheritance:")
blank()
cmd("print(type(True))")
out(type(True))
cmd("print(type(False))")
out(type(False))
cmd("print(isinstance(True, int))")
out(isinstance(True, int))
blank()

pause()

explain("True and False behave as integers:")
blank()
cmd("print(True == 1)")
out(True == 1)
cmd("print(False == 0)")
out(False == 0)
cmd("print(True + True)")
out(True + True)
cmd("print(True + False)")
out(True + False)
cmd("print(False + False)")
out(False + False)
blank()

pause()

explain("This causes real bugs in Cisco IaC scripts:")
blank()
cmd("enabled_interfaces = [True, True, False, True]")
enabled_interfaces = [True, True, False, True]
cmd("print(sum(enabled_interfaces))")
out(sum(enabled_interfaces))
blank()
explain("sum() works on booleans — True counts as 1, False as 0.")
explain("Useful for counting how many interfaces are enabled.")
blank()

pause()

explain("But this can cause a silent bug:")
blank()
cmd("port_count = True   # someone accidentally assigned bool")
port_count = True
cmd("print(port_count + 47)")
out(port_count + 47)
blank()
explain("True + 47 = 48. No error. Silent wrong result.")
blank()

pause()

explain("Always check types explicitly in IaC scripts:")
blank()
cmd("print(type(True))")
out(type(True))
cmd("print(type(True) is bool)")
out(type(True) is bool)
cmd("print(type(True) is int)")
out(type(True) is int)
blank()

pause()

explain("✔ bool is a subclass of int.")
explain("  True == 1 and False == 0 — always.")
explain("  Use type(x) is bool to check strictly for boolean.")
explain("  Use isinstance(x, bool) when subclass check is fine.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 5 — Boolean interning: only ONE True and ONE False exist
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 5 — Boolean interning: only ONE True and ONE False exist")

explain("This is the most unique property of booleans.")
explain("Python only ever creates ONE True object and ONE False object.")
explain("Every True in your entire program shares the exact same id.")
explain("Every False in your entire program shares the exact same id.")
explain("This is called interning — and it only works because")
explain("booleans are immutable. They can never change.")
blank()

pause()

explain("Three separate True assignments — all the same id:")
blank()
cmd("a = True")
a = True
cmd("b = True")
b = True
cmd("c = True")
c = True
cmd("print(id(a))")
out_id(id(a))
cmd("print(id(b))")
out_id(id(b))
cmd("print(id(c))")
out_id(id(c))
blank()

pause()

explain("All identical. There is literally only one True object.")
blank()

pause()

explain("Same for False:")
blank()
cmd("x = False")
x = False
cmd("y = False")
y = False
cmd("z = False")
z = False
cmd("print(id(x))")
out_id(id(x))
cmd("print(id(y))")
out_id(id(y))
cmd("print(id(z))")
out_id(id(z))
blank()

pause()

explain("All identical. There is literally only one False object.")
blank()

pause()

explain("Now prove this across different sources of True:")
blank()
cmd("is_enabled    = True")
is_enabled = True
cmd("is_connected  = (1 == 1)")
is_connected = (1 == 1)
cmd("is_configured = bool(1)")
is_configured = bool(1)
cmd("is_active     = not False")
is_active = not False
blank()
cmd("print(is_enabled)")
out(is_enabled)
cmd("print(id(is_enabled))")
out_id(id(is_enabled))
blank()
cmd("print(is_connected)")
out(is_connected)
cmd("print(id(is_connected))")
out_id(id(is_connected))
blank()
cmd("print(is_configured)")
out(is_configured)
cmd("print(id(is_configured))")
out_id(id(is_configured))
blank()
cmd("print(is_active)")
out(is_active)
cmd("print(id(is_active))")
out_id(id(is_active))
blank()

pause()

explain("✔ Every single one has the same id.")
explain("  It does not matter how True was produced —")
explain("  literal, comparison, bool(), or not False.")
explain("  They all resolve to the exact same object in memory.")
explain("  This is only possible because True can never be modified.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 6 — Functions cannot corrupt a bool you pass in
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 6 — Functions cannot corrupt a bool you pass in")

explain("We pass a boolean flag into a function that evaluates it.")
explain("The function generates a Cisco interface config based on it.")
explain("We check the id before and after to prove it is unchanged.")
blank()

pause()

def generate_interface_config(interface, enabled):
    """
    Reads the boolean and builds a config string.
    Cannot modify the boolean — booleans are immutable.
    Returns a brand new string object.
    """
    state = "no shutdown" if enabled else "shutdown"
    return f"interface {interface}\n {state}"

explain("Here is the function we will call:")
blank()
cmd("def generate_interface_config(interface, enabled):")
cmd("    state = 'no shutdown' if enabled else 'shutdown'")
cmd("    return f'interface {interface}\\n {state}'")
blank()
explain("It reads the boolean and builds a new config string.")
explain("It has no way to modify the original bool — booleans are immutable.")
blank()

pause()

is_enabled = True
cmd("is_enabled = True")
cmd("print(is_enabled)")
out(is_enabled)
cmd("print(id(is_enabled))")
out_id(id(is_enabled))
blank()

pause()

explain("Now call generate_interface_config('Gi0/0', is_enabled):")
blank()
cmd("result = generate_interface_config('Gi0/0', is_enabled)")
result = generate_interface_config("Gi0/0", is_enabled)
cmd("print(result)")
out(result)
cmd("print(id(result))")
out_id(id(result))
blank()

pause()

explain("Check is_enabled after the function ran:")
blank()
cmd("print(is_enabled)")
out(is_enabled)
cmd("print(id(is_enabled))")
out_id(id(is_enabled))
blank()

pause()

explain("✔ id(is_enabled) is identical before and after the function call.")
explain("  The function read the boolean and produced a new string.")
explain("  It had no way to modify the original — booleans are immutable.")
explain("  And because of interning, the id will always be the same")
explain("  as any other True in the program.")

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
print(f"  {BOLD}Proof 1{RESET}  Booleans have no mutation methods")
print(f"  {DIM}         .flip(), .toggle() — AttributeError, they do not exist{RESET}")
blank()
print(f"  {BOLD}Proof 2{RESET}  You cannot modify a bool in place")
print(f"  {DIM}         b[0] = True raises TypeError — not subscriptable{RESET}")
print(f"  {DIM}         |= creates a new object — it does not mutate{RESET}")
blank()
print(f"  {BOLD}Proof 3{RESET}  Reassignment creates a new object")
print(f"  {DIM}         debug_enabled = False moved the label, not the object{RESET}")
blank()
print(f"  {BOLD}Proof 4{RESET}  The gotcha — bool is a subclass of int")
print(f"  {DIM}         True == 1, False == 0 — can cause silent bugs{RESET}")
print(f"  {DIM}         Use type(x) is bool for strict boolean checks{RESET}")
blank()
print(f"  {BOLD}Proof 5{RESET}  Boolean interning — only ONE True and ONE False exist")
print(f"  {DIM}         Every True in the program shares the exact same id{RESET}")
print(f"  {DIM}         Only possible because booleans can never be modified{RESET}")
blank()
print(f"  {BOLD}Proof 6{RESET}  Functions cannot corrupt a bool you pass in")
print(f"  {DIM}         id(is_enabled) identical before and after the call{RESET}")
blank()
print(f"  {WHITE}In Cisco IaC — booleans are used for interface state,")
print(f"  feature flags, shutdown status, validation results.")
print(f"  They are completely safe to pass anywhere. No function")
print(f"  can corrupt them. And because of interning, True is")
print(f"  always True — the same object, everywhere, always.{RESET}")
blank()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█   Proof complete.                                          █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
print()