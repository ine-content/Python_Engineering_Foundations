# immutable_strings_proof.py
# Proving string immutability in Python
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
print(f"{BOLD}█         PROVING STRING IMMUTABILITY IN PYTHON              █{RESET}")
print(f"{BOLD}█         Cisco IaC Perspective                              █{RESET}")
print(f"{BOLD}█                                                            █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 1 — String methods return a NEW object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 1 — String methods return a NEW object")

explain("We start with a hostname. We call .upper() on it.")
explain("If strings were mutable, the original would change.")
explain("If strings are immutable, we get a brand new object.")
blank()

pause()

hostname = "nyc-rtr-01"
cmd("hostname = 'nyc-rtr-01'")
cmd("print(hostname)")
out(hostname)
cmd("print(id(hostname))")
out_id(id(hostname))
blank()

pause()

hostname_upper = hostname.upper()
cmd("hostname_upper = hostname.upper()")
cmd("print(hostname_upper)")
out(hostname_upper)
cmd("print(id(hostname_upper))")
out_id(id(hostname_upper))
blank()

pause()

explain("Now check the original — same id means same object, untouched.")
blank()
cmd("print(hostname)")
out(hostname)
cmd("print(id(hostname))")
out_id(id(hostname))
blank()

pause()

explain("✔ id(hostname) and id(hostname_upper) are DIFFERENT.")
explain("  .upper() did not touch hostname.")
explain("  It created a brand new string object in memory.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 2 — You cannot modify a character in place
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 2 — You cannot modify a character in place")

explain("We have an interface name in lowercase.")
explain("We try to change the first character directly.")
explain("Python will refuse — strings do not allow item assignment.")
blank()

pause()

interface = "gigabitethernet0/0/0"
cmd("interface = 'gigabitethernet0/0/0'")
cmd("print(interface)")
out(interface)
cmd("print(id(interface))")
out_id(id(interface))
blank()

pause()

cmd("interface[0] = 'G'")
blank()

pause()

try:
    interface[0] = "G"
except TypeError as e:
    err(f"TypeError: {e}")
blank()

pause()

explain("The object is still completely untouched.")
blank()
cmd("print(interface)")
out(interface)
cmd("print(id(interface))")
out_id(id(interface))
blank()

pause()

explain("✔ Same value. Same id. Python rejected the modification.")
explain("  The string at that memory address is locked.")
explain("  This is immutability enforced at the language level.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 3 — Reassignment creates a new object, old one untouched
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 3 — Reassignment creates a new object")

explain("We have a platform string.")
explain("We reassign the variable to a new value.")
explain("The original string object still exists — a second variable")
explain("pointing to it proves this.")
blank()

pause()

platform = "IOS-XE"
ref      = platform        # ref keeps pointing to the original

cmd("platform = 'IOS-XE'")
cmd("ref      = platform   # ref points to same object")
cmd("print(platform)")
out(platform)
cmd("print(id(platform))")
out_id(id(platform))
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

platform = "IOS-XR"
cmd("platform = 'IOS-XR'   # reassign platform")
cmd("print(platform)")
out(platform)
cmd("print(id(platform))")
out_id(id(platform))
blank()

pause()

explain("platform now points to a new object.")
explain("What happened to the original 'IOS-XE' object?")
blank()
cmd("print(ref)")
out(ref)
cmd("print(id(ref))")
out_id(id(ref))
blank()

pause()

explain("✔ ref still points to the original 'IOS-XE' object.")
explain("  Same id as before. The object was never modified.")
explain("  Reassignment moved the label — not the object.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 4 — Functions cannot corrupt a string you pass in
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 4 — Functions cannot corrupt a string you pass in")

explain("We pass a hostname into a function that does string operations.")
explain("If strings were mutable, the function could corrupt our data.")
explain("We check the id before and after to prove it is unchanged.")
blank()

pause()

def normalize(name):
    result = name.strip().lower().replace(" ", "-")
    return result

explain("Here is the function we will call:")
blank()
cmd("def normalize(name):")
cmd("    result = name.strip().lower().replace(' ', '-')")
cmd("    return result")
blank()
explain("It does three string operations on the input.")
explain("Each one returns a new string — the original is never touched.")
blank()

pause()

hostname = "NYC-RTR-01"
cmd("hostname = 'NYC-RTR-01'")
cmd("print(hostname)")
out(hostname)
cmd("print(id(hostname))")
out_id(id(hostname))
blank()

pause()

explain("Now call normalize(hostname):")
blank()
cmd("result = normalize(hostname)")
result = normalize(hostname)
cmd("print(result)")
out(result)
cmd("print(id(result))")
out_id(id(result))
blank()

pause()

explain("Check the original after the function ran:")
blank()
cmd("print(hostname)")
out(hostname)
cmd("print(id(hostname))")
out_id(id(hostname))
blank()

pause()

explain("✔ id(hostname) is identical before and after the function call.")
explain("  The function operated on new string objects internally.")
explain("  It had no way to modify the original — strings are immutable.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# PROOF 5 — Every chained method produces a new object
# ═════════════════════════════════════════════════════════════════════════════
section("PROOF 5 — Every chained method produces a new object")

explain("We take a raw hostname from a config file.")
explain("We chain multiple methods — each one returns a new object.")
explain("We track the id at every single step.")
blank()

pause()

raw = "  GigabitEthernet0/0/0  "
cmd("raw = '  GigabitEthernet0/0/0  '")
cmd("print(raw)")
out(raw)
cmd("print(id(raw))")
out_id(id(raw))
blank()

pause()

step1 = raw.strip()
cmd("step1 = raw.strip()")
cmd("print(step1)")
out(step1)
cmd("print(id(step1))")
out_id(id(step1))
blank()

pause()

step2 = step1.lower()
cmd("step2 = step1.lower()")
cmd("print(step2)")
out(step2)
cmd("print(id(step2))")
out_id(id(step2))
blank()

pause()

step3 = step2.replace("gigabitethernet", "Gi")
cmd("step3 = step2.replace('gigabitethernet', 'Gi')")
cmd("print(step3)")
out(step3)
cmd("print(id(step3))")
out_id(id(step3))
blank()

pause()

explain("Now check every step — all still intact:")
blank()
cmd("print(raw)")
out(raw)
cmd("print(id(raw))")
out_id(id(raw))
blank()
cmd("print(step1)")
out(step1)
cmd("print(id(step1))")
out_id(id(step1))
blank()
cmd("print(step2)")
out(step2)
cmd("print(id(step2))")
out_id(id(step2))
blank()
cmd("print(step3)")
out(step3)
cmd("print(id(step3))")
out_id(id(step3))
blank()

pause()

explain("✔ Every id is unique. Every step produced a new object.")
explain("  raw, step1, step2, step3 — all unchanged, all at their original address.")
explain("  This is what immutability looks like across a chain of operations.")

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
print(f"  {BOLD}Proof 1{RESET}  String methods return a new object")
print(f"  {DIM}         .upper() did not change hostname — new id, new object{RESET}")
blank()
print(f"  {BOLD}Proof 2{RESET}  You cannot modify a character in place")
print(f"  {DIM}         interface[0] = 'G' raises TypeError — Python refuses{RESET}")
blank()
print(f"  {BOLD}Proof 3{RESET}  Reassignment creates a new object")
print(f"  {DIM}         platform = 'IOS-XR' moved the label, not the object{RESET}")
blank()
print(f"  {BOLD}Proof 4{RESET}  Functions cannot corrupt a string you pass in")
print(f"  {DIM}         id(hostname) was identical before and after the call{RESET}")
blank()
print(f"  {BOLD}Proof 5{RESET}  Every chained method produces a new object")
print(f"  {DIM}         raw, step1, step2, step3 — all unique ids, all untouched{RESET}")
blank()
print(f"  {WHITE}In Cisco IaC — hostnames, IPs, interface names, platform")
print(f"  strings are 100% safe to pass anywhere. No function,")
print(f"  no loop, no method can modify the string you started with.{RESET}")
blank()
print(f"{BOLD}{'█' * 62}{RESET}")
print(f"{BOLD}█   Proof complete.                                          █{RESET}")
print(f"{BOLD}{'█' * 62}{RESET}")
print()