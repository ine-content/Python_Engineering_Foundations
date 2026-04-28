# exceptions_deep_dive.py
# Python Exceptions — Zero to Expert
# Cisco IaC Perspective
# Press ENTER to advance through each step

import json

# ── ANSI colors ───────────────────────────────────────────────────────────────
RESET  = "\033[0m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
WHITE  = "\033[97m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

def pause():
    input(f"\n{DIM}  [ Press ENTER to continue ]{RESET} ")
    print()

def cmd(command):
    print(f"    {CYAN}>>> {command}{RESET}")

def out(value):
    print(f"    {GREEN}{value}{RESET}")

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
# SHARED DATA
# ─────────────────────────────────────────────────────────────────────────────
INVENTORY = [
    {"hostname": "nyc-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.0.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "lon-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.1.0.1", "vlans": [10, 20],
     "config": {"ntp": "10.1.0.100", "dns": "8.8.8.8"}},
    {"hostname": "sin-fw-01",  "platform": "ASA",    "status": "up",
     "ip": "10.2.0.1", "vlans": [30, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "ams-rtr-02", "platform": "IOS-XE", "status": "up",
     "ip": "10.3.0.1", "vlans": [10, 20, 30, 40],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "tok-sw-01",  "platform": "NX-OS",  "status": "down",
     "ip": "10.4.0.1", "vlans": [20, 30],
     "config": {"ntp": "10.4.0.100", "dns": "8.8.8.8"}},
    {"hostname": "syd-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.5.0.1", "vlans": [10, 40, 50],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "dub-fw-01",  "platform": "ASA",    "status": "down",
     "ip": "10.6.0.1", "vlans": [10, 20, 30],
     "config": {"ntp": "10.0.0.100", "dns": "8.8.8.8"}},
    {"hostname": "mum-rtr-01", "platform": "IOS-XE", "status": "up",
     "ip": "10.7.0.1", "vlans": [20, 30, 40, 50],
     "config": {"ntp": "10.7.0.100", "dns": "8.8.8.8"}},
]

GLOBAL_NTP = "10.0.0.100"

# ─────────────────────────────────────────────────────────────────────────────
bar = "█" * 62
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()
print(f"{BOLD}         PYTHON EXCEPTIONS — ZERO TO EXPERT{RESET}")
print(f"{BOLD}         Cisco IaC Perspective{RESET}")
print()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}{bar}{RESET}")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — What Is an Exception and Why It Matters in IaC
# ═════════════════════════════════════════════════════════════════════════════
chapter(1, "What Is an Exception and Why It Matters in IaC")

section("1.1 — The Problem Without Exceptions")

explain("When your IaC script runs against 200 devices, one")
explain("bad device dict or one missing key will crash the")
explain("whole script — unless you handle it.")
blank()
explain("Without exception handling:")
blank()

cmd("device = {'hostname': 'nyc-rtr-01'}  # missing 'status'")
cmd("print(device['status'])")
blank()
err("KeyError: 'status'")
err("Traceback (most recent call last):")
err("  ...")
err("Script exits — all remaining devices unprocessed.")
blank()

pause()

explain("With exception handling:")
blank()

cmd("try:")
cmd("    print(device['status'])")
cmd("except KeyError:")
cmd("    print('status key missing — skipping')")
blank()

device = {"hostname": "nyc-rtr-01"}
try:
    _ = device["status"]
except KeyError:
    out("status key missing — skipping")
blank()

explain("The script continues to the next device.")

pause()

section("1.2 — The Exception Hierarchy")

explain("Python exceptions form a class hierarchy.")
explain("The most important ones for IaC work:")
blank()
explain("  BaseException")
explain("  └── Exception                 ← catch-all for app errors")
explain("      ├── ValueError            ← wrong value type/format")
explain("      ├── TypeError             ← wrong Python type")
explain("      ├── KeyError              ← dict key missing")
explain("      ├── IndexError            ← list index out of range")
explain("      ├── AttributeError        ← attribute doesn't exist")
explain("      ├── FileNotFoundError     ← file doesn't exist")
explain("      ├── PermissionError       ← no access to file")
explain("      ├── json.JSONDecodeError  ← invalid JSON string")
explain("      └── OSError               ← OS-level failures")
blank()

pause()

explain("In IaC the most common ones you will see:")
blank()
explain("  KeyError       — d['hostname'] when key is missing")
explain("  TypeError      — passing wrong type to a function")
explain("  ValueError     — int('bad') or bad IP format")
explain("  FileNotFoundError — config file not found")
explain("  json.JSONDecodeError — malformed device response JSON")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — try / except / else / finally
# ═════════════════════════════════════════════════════════════════════════════
chapter(2, "try / except / else / finally")

section("2.1 — Basic try/except")

explain("The basic pattern — wrap risky code and handle the error:")
blank()

cmd("def safe_get_ip(device):")
cmd("    try:")
cmd("        return device['ip']")
cmd("    except KeyError:")
cmd("        return None")
blank()

def safe_get_ip(device):
    try:
        return device["ip"]
    except KeyError:
        return None

cmd("print(safe_get_ip(INVENTORY[0]))")
out(safe_get_ip(INVENTORY[0]))
blank()
cmd("print(safe_get_ip({'hostname': 'test'}))")
out(str(safe_get_ip({"hostname": "test"})))
blank()

pause()

section("2.2 — Catching Multiple Exceptions")

explain("You can catch different exceptions in separate blocks")
explain("and handle each one differently:")
blank()

cmd("def parse_vlan_count(device):")
cmd("    try:")
cmd("        return len(device['vlans'])")
cmd("    except KeyError:")
cmd("        print(f\"  {device.get('hostname','?')}: missing vlans key\")")
cmd("        return 0")
cmd("    except TypeError:")
cmd("        print(f\"  {device.get('hostname','?')}: vlans is not a list\")")
cmd("        return -1")
blank()

def parse_vlan_count(device):
    try:
        return len(device["vlans"])
    except KeyError:
        return 0
    except TypeError:
        return -1

cmd("print(parse_vlan_count(INVENTORY[0]))")
out(str(parse_vlan_count(INVENTORY[0])))
blank()
cmd("print(parse_vlan_count({'hostname': 'x'}))")
out(str(parse_vlan_count({"hostname": "x"})))
blank()
cmd("print(parse_vlan_count({'hostname': 'x', 'vlans': 'bad'}))")
out(str(parse_vlan_count({"hostname": "x", "vlans": "bad"})))
blank()

pause()

section("2.3 — else and finally")

explain("else  — runs ONLY if no exception was raised")
explain("finally — ALWAYS runs, even if an exception occurred")
blank()
explain("Common IaC pattern — always log what happened:")
blank()

cmd("def parse_ip_octet(ip_string):")
cmd("    try:")
cmd("        result = int(ip_string.split('.')[-1])")
cmd("    except (ValueError, IndexError) as e:")
cmd("        print(f'  parse failed: {e}')")
cmd("        return -1")
cmd("    else:")
cmd("        return result         # only runs on success")
cmd("    finally:")
cmd("        print('  parse_ip_octet done')  # always runs")
blank()

def parse_ip_octet(ip_string):
    try:
        result = int(ip_string.split(".")[-1])
    except (ValueError, IndexError) as e:
        return -1
    else:
        return result
    finally:
        out("  parse_ip_octet done")

cmd("print(parse_ip_octet('10.0.0.1'))")
r = parse_ip_octet("10.0.0.1")
out(str(r))
blank()
cmd("print(parse_ip_octet('bad-ip'))")
r = parse_ip_octet("bad-ip")
out(str(r))
blank()

pause()

section("2.4 — Accessing the Exception Object")

explain("Use 'as e' to capture the exception object.")
explain("str(e) gives the error message. type(e).__name__ gives the class.")
blank()

cmd("for d in INVENTORY[:3]:")
cmd("    try:")
cmd("        ntp = d['config']['ntp']")
cmd("        _ = int(ntp.split('.')[-1])")
cmd("    except (KeyError, ValueError) as e:")
cmd("        print(f'  {d[\"hostname\"]}: {type(e).__name__}: {e}')")
cmd("    else:")
cmd("        print(f'  {d[\"hostname\"]}: last octet ok')")
blank()

for d in INVENTORY[:3]:
    try:
        ntp = d["config"]["ntp"]
        _ = int(ntp.split(".")[-1])
    except (KeyError, ValueError) as e:
        out(f"  {d['hostname']}: {type(e).__name__}: {e}")
    else:
        out(f"  {d['hostname']}: last octet ok")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Raising Exceptions
# ═════════════════════════════════════════════════════════════════════════════
chapter(3, "Raising Exceptions")

section("3.1 — raise")

explain("You raise exceptions to signal that something is wrong")
explain("in your code. The caller then decides how to handle it.")
blank()

cmd("def validate_status(device):")
cmd("    allowed = ('up', 'down')")
cmd("    if device['status'] not in allowed:")
cmd("        raise ValueError(")
cmd("            f\"Invalid status: {device['status']}. \"")
cmd("            f\"Must be one of {allowed}\"")
cmd("        )")
cmd("    return True")
blank()

def validate_status(device):
    allowed = ("up", "down")
    if device["status"] not in allowed:
        raise ValueError(
            f"Invalid status: {device['status']}. "
            f"Must be one of {allowed}"
        )
    return True

cmd("print(validate_status(INVENTORY[0]))")
out(str(validate_status(INVENTORY[0])))
blank()
cmd("try:")
cmd("    validate_status({'hostname': 'test', 'status': 'rebooting'})")
cmd("except ValueError as e:")
cmd("    print(e)")
blank()
try:
    validate_status({"hostname": "test", "status": "rebooting"})
except ValueError as e:
    out(str(e))
blank()

pause()

section("3.2 — Guard Clauses (Early Return Pattern)")

explain("In IaC validation functions, early return with raise")
explain("is cleaner than deeply nested if/else blocks.")
blank()

cmd("SUPPORTED = ('IOS-XE', 'NX-OS', 'ASA', 'IOS-XR')")
cmd("")
cmd("def validate_device(device, global_ntp=GLOBAL_NTP):")
cmd("    if device['status'] != 'up':")
cmd("        raise ValueError('device is down')")
cmd("    if device['platform'] not in SUPPORTED:")
cmd("        raise ValueError(f\"unsupported: {device['platform']}\")")
cmd("    if not device.get('vlans'):")
cmd("        raise ValueError('no vlans configured')")
cmd("    if device['config']['ntp'] != global_ntp:")
cmd("        raise ValueError(f\"custom ntp: {device['config']['ntp']}\")")
cmd("    return True")
blank()

SUPPORTED = ("IOS-XE", "NX-OS", "ASA", "IOS-XR")

def validate_device(device, global_ntp=GLOBAL_NTP):
    if device["status"] != "up":
        raise ValueError("device is down")
    if device["platform"] not in SUPPORTED:
        raise ValueError(f"unsupported: {device['platform']}")
    if not device.get("vlans"):
        raise ValueError("no vlans configured")
    if device["config"]["ntp"] != global_ntp:
        raise ValueError(f"custom ntp: {device['config']['ntp']}")
    return True

explain("Test against all 8 devices:")
blank()

for d in INVENTORY:
    try:
        validate_device(d)
        out(f"  PASS  {d['hostname']}")
    except ValueError as e:
        err(f"  FAIL  {d['hostname']}: {e}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — Custom Exception Classes
# ═════════════════════════════════════════════════════════════════════════════
chapter(4, "Custom Exception Classes")

section("4.1 — Why Custom Exceptions")

explain("Built-in exceptions (ValueError, KeyError) are generic.")
explain("Custom exceptions let callers distinguish IaC-specific")
explain("errors from Python errors and handle them differently.")
blank()
explain("Compare:")
blank()
explain("  except ValueError:       ← catches ALL ValueErrors")
explain("  except DeviceOfflineError:  ← catches ONLY device offline")
blank()

pause()

section("4.2 — Defining a Simple Custom Exception")

cmd("class DeviceOfflineError(Exception):")
cmd("    pass")
blank()
cmd("def connect(device):")
cmd("    if device['status'] == 'down':")
cmd("        raise DeviceOfflineError(f\"{device['hostname']} is offline\")")
cmd("    return f\"connected: {device['hostname']}\"")
blank()

class DeviceOfflineError(Exception):
    pass

def connect(device):
    if device["status"] == "down":
        raise DeviceOfflineError(f"{device['hostname']} is offline")
    return f"connected: {device['hostname']}"

cmd("for d in INVENTORY[:4]:")
cmd("    try:")
cmd("        print(connect(d))")
cmd("    except DeviceOfflineError as e:")
cmd("        print(f'  offline: {e}')")
blank()

for d in INVENTORY[:4]:
    try:
        out(connect(d))
    except DeviceOfflineError as e:
        err(f"  offline: {e}")
blank()

pause()

section("4.3 — An Exception Hierarchy for IaC")

explain("For larger projects, build a hierarchy so callers can")
explain("catch broad or narrow categories as needed:")
blank()

cmd("class IaCError(Exception):              pass  # base")
cmd("class DeviceError(IaCError):            pass  # any device problem")
cmd("class DeviceOfflineError(DeviceError):  pass  # device is down")
cmd("class DeviceTimeoutError(DeviceError):  pass  # device timed out")
cmd("class ConfigError(IaCError):            pass  # any config problem")
cmd("class InvalidConfigError(ConfigError):  pass  # malformed config")
cmd("class MissingFieldError(ConfigError):   pass  # required field absent")
blank()

class IaCError(Exception):              pass
class DeviceError(IaCError):            pass
class DeviceOfflineError(DeviceError):  pass
class DeviceTimeoutError(DeviceError):  pass
class ConfigError(IaCError):            pass
class InvalidConfigError(ConfigError):  pass
class MissingFieldError(ConfigError):   pass

explain("Now callers choose how broad to catch:")
blank()

cmd("try:")
cmd("    raise DeviceOfflineError('nyc-rtr-01 is offline')")
cmd("except DeviceOfflineError as e:")
cmd("    print(f'specific catch: {e}')")
blank()

try:
    raise DeviceOfflineError("nyc-rtr-01 is offline")
except DeviceOfflineError as e:
    out(f"specific catch: {e}")
blank()

cmd("try:")
cmd("    raise DeviceOfflineError('nyc-rtr-01 is offline')")
cmd("except DeviceError as e:")
cmd("    print(f'broad catch (DeviceError): {e}')")
blank()

try:
    raise DeviceOfflineError("nyc-rtr-01 is offline")
except DeviceError as e:
    out(f"broad catch (DeviceError): {e}")
blank()

cmd("try:")
cmd("    raise DeviceOfflineError('nyc-rtr-01 is offline')")
cmd("except IaCError as e:")
cmd("    print(f'broadest catch (IaCError): {e}')")
blank()

try:
    raise DeviceOfflineError("nyc-rtr-01 is offline")
except IaCError as e:
    out(f"broadest catch (IaCError): {e}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Exception Chaining
# ═════════════════════════════════════════════════════════════════════════════
chapter(5, "Exception Chaining")

section("5.1 — raise ... from e")

explain("When you catch one exception and raise another, Python")
explain("can chain them so the original cause is preserved.")
blank()

cmd("def load_device_config(raw):")
cmd("    if not isinstance(raw, str):")
cmd("        raise TypeError(f'Expected str, got {type(raw)}')")
cmd("    try:")
cmd("        result = json.loads(raw)")
cmd("    except json.JSONDecodeError as e:")
cmd("        raise InvalidConfigError(f'Cannot parse config: {e}') from e")
cmd("    if 'hostname' not in result:")
cmd("        raise MissingFieldError('Missing required field: hostname') from None")
cmd("    return result")
blank()

def load_device_config(raw):
    if not isinstance(raw, str):
        raise TypeError(f"Expected str, got {type(raw)}")
    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        raise InvalidConfigError(f"Cannot parse config: {e}") from e
    if "hostname" not in result:
        raise MissingFieldError("Missing required field: hostname") from None
    return result

cmd("print(load_device_config('{\"hostname\": \"nyc-rtr-01\"}'))")
out(str(load_device_config('{"hostname": "nyc-rtr-01"}')))
blank()

cmd("try:")
cmd("    load_device_config('bad json')")
cmd("except InvalidConfigError as e:")
cmd("    print(f'InvalidConfigError: {e}')")
cmd("    print(f'Caused by: {e.__cause__}')")
blank()
try:
    load_device_config("bad json {{{")
except InvalidConfigError as e:
    out(f"InvalidConfigError: {e}")
    out(f"Caused by: {e.__cause__}")
blank()

pause()

section("5.2 — raise ... from None")

explain("Use 'from None' when you want to suppress the original")
explain("exception chain — to hide implementation details.")
blank()

cmd("try:")
cmd("    load_device_config('{\"ip\": \"10.0.0.1\"}')")
cmd("except MissingFieldError as e:")
cmd("    print(f'MissingFieldError: {e}')")
cmd("    print(f'Cause suppressed: {e.__cause__}')  # None")
blank()
try:
    load_device_config('{"ip": "10.0.0.1"}')
except MissingFieldError as e:
    out(f"MissingFieldError: {e}")
    out(f"Cause suppressed: {e.__cause__}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Context Managers and with Statements
# ═════════════════════════════════════════════════════════════════════════════
chapter(6, "Context Managers and with Statements")

section("6.1 — The Problem Context Managers Solve")

explain("When you open a connection or file, you must close it —")
explain("even if an exception occurs. Without a context manager:")
blank()

cmd("conn = open_connection(device)  # hypothetical")
cmd("data = conn.get_config()        # if this raises ...")
cmd("conn.close()                    # ... this never runs!")
blank()
explain("This leaks the connection.")

pause()

section("6.2 — Writing a Context Manager Class")

explain("Implement __enter__ and __exit__:")
blank()

cmd("class DeviceSession:")
cmd("    def __init__(self, hostname):")
cmd("        self.hostname = hostname")
cmd("        self.connected = False")
blank()
cmd("    def __enter__(self):")
cmd("        print(f'  Opening session: {self.hostname}')")
cmd("        self.connected = True")
cmd("        return self")
blank()
cmd("    def __exit__(self, exc_type, exc_val, exc_tb):")
cmd("        print(f'  Closing session: {self.hostname}')")
cmd("        self.connected = False")
cmd("        return False  # don't suppress exceptions")
blank()

class DeviceSession:
    def __init__(self, hostname):
        self.hostname = hostname
        self.connected = False

    def __enter__(self):
        out(f"  Opening session: {self.hostname}")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        out(f"  Closing session: {self.hostname}")
        self.connected = False
        return False

cmd("with DeviceSession('nyc-rtr-01') as session:")
cmd("    print(f'  Inside block, connected={session.connected}')")
blank()

with DeviceSession("nyc-rtr-01") as session:
    out(f"  Inside block, connected={session.connected}")
blank()

pause()

explain("__exit__ is called even if an exception is raised inside:")
blank()

cmd("try:")
cmd("    with DeviceSession('lon-sw-01') as session:")
cmd("        raise DeviceOfflineError('lon-sw-01 is offline')")
cmd("except DeviceOfflineError as e:")
cmd("    print(f'  Caught outside: {e}')")
blank()

try:
    with DeviceSession("lon-sw-01") as session:
        raise DeviceOfflineError("lon-sw-01 is offline")
except DeviceOfflineError as e:
    out(f"  Caught outside: {e}")
blank()
explain("The session was closed even though an exception occurred.")

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Collecting Errors Without Stopping
# ═════════════════════════════════════════════════════════════════════════════
chapter(7, "Collecting Errors Without Stopping")

section("7.1 — The Pattern")

explain("In IaC you often want to process ALL devices and report")
explain("ALL failures — not stop on the first error.")
blank()
explain("Pattern: collect errors in a list, keep looping.")
blank()

cmd("def batch_validate(inventory):")
cmd("    passed = []")
cmd("    errors = []")
cmd("    for d in inventory:")
cmd("        try:")
cmd("            validate_device(d)")
cmd("            passed.append(d['hostname'])")
cmd("        except ValueError as e:")
cmd("            errors.append({")
cmd("                'hostname': d['hostname'],")
cmd("                'error':    str(e),")
cmd("            })")
cmd("    return {'passed': passed, 'errors': errors}")
blank()

def batch_validate(inventory):
    passed = []
    errors = []
    for d in inventory:
        try:
            validate_device(d)
            passed.append(d["hostname"])
        except ValueError as e:
            errors.append({"hostname": d["hostname"], "error": str(e)})
    return {"passed": passed, "errors": errors}

cmd("report = batch_validate(INVENTORY)")
report = batch_validate(INVENTORY)
cmd("print('Passed:', report['passed'])")
out(f"Passed: {report['passed']}")
blank()
cmd("print('Errors:')")
out("Errors:")
for e in report["errors"]:
    err(f"  {e['hostname']}: {e['error']}")
blank()

pause()

section("7.2 — Stage-by-Stage Processing with Partial Failure")

explain("Process each device through multiple stages.")
explain("If a stage fails, skip remaining stages for that device")
explain("but continue to the next device.")
blank()

def gen_config(device):
    return f"config:{device['hostname']}"

def connect_device(device):
    if device["status"] == "down":
        raise DeviceOfflineError(f"{device['hostname']} is offline")
    return f"connected:{device['hostname']}"

cmd("def safe_pipeline(inventory):")
cmd("    results = []")
cmd("    for d in inventory:")
cmd("        entry = {'hostname': d['hostname'], 'stage': 'done', 'result': None}")
cmd("        try:")
cmd("            validate_device(d)")
cmd("        except ValueError as e:")
cmd("            entry['stage'] = 'validate'")
cmd("            entry['result'] = str(e)")
cmd("            results.append(entry)")
cmd("            continue")
cmd("        try:")
cmd("            connect_device(d)")
cmd("        except DeviceOfflineError as e:")
cmd("            entry['stage'] = 'connect'")
cmd("            entry['result'] = str(e)")
cmd("            results.append(entry)")
cmd("            continue")
cmd("        entry['result'] = gen_config(d)")
cmd("        results.append(entry)")
cmd("    return results")
blank()

def safe_pipeline(inventory):
    results = []
    for d in inventory:
        entry = {"hostname": d["hostname"], "stage": "done", "result": None}
        try:
            validate_device(d)
        except ValueError as e:
            entry["stage"] = "validate"
            entry["result"] = str(e)
            results.append(entry)
            continue
        try:
            connect_device(d)
        except DeviceOfflineError as e:
            entry["stage"] = "connect"
            entry["result"] = str(e)
            results.append(entry)
            continue
        entry["result"] = gen_config(d)
        results.append(entry)
    return results

pause()

cmd("for r in safe_pipeline(INVENTORY):")
cmd("    print(f\"{r['hostname']:<14} {r['stage']:<10} {r['result']}\")")
blank()
for r in safe_pipeline(INVENTORY):
    if r["stage"] == "done":
        out(f"  {r['hostname']:<14} {r['stage']:<10} {r['result']}")
    else:
        err(f"  {r['hostname']:<14} {r['stage']:<10} {r['result']}")
blank()

pause()

# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Advanced Patterns
# ═════════════════════════════════════════════════════════════════════════════
chapter(8, "Advanced Patterns")

section("8.1 — The Retry Decorator")

explain("A retry decorator automatically retries a function")
explain("on failure — useful for flaky network connections.")
blank()

cmd("def retry(max_attempts, delay=0):")
cmd("    def decorator(func):")
cmd("        def wrapper(*args, **kwargs):")
cmd("            last_exc = None")
cmd("            for attempt in range(1, max_attempts + 1):")
cmd("                try:")
cmd("                    return func(*args, **kwargs)")
cmd("                except Exception as e:")
cmd("                    last_exc = e")
cmd("                    print(f'  attempt {attempt} failed: {e}')")
cmd("            raise last_exc")
cmd("        return wrapper")
cmd("    return decorator")
blank()

def retry(max_attempts, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    out(f"  attempt {attempt} failed: {e}")
            raise last_exc
        return wrapper
    return decorator

cmd("counter = {'n': 0}")
cmd("@retry(max_attempts=3)")
cmd("def flaky_connect():")
cmd("    counter['n'] += 1")
cmd("    if counter['n'] < 3:")
cmd("        raise ConnectionError('not ready yet')")
cmd("    return 'connected'")
blank()

counter = {"n": 0}

@retry(max_attempts=3)
def flaky_connect():
    counter["n"] += 1
    if counter["n"] < 3:
        raise ConnectionError("not ready yet")
    return "connected"

cmd("print(flaky_connect())")
out(flaky_connect())
blank()

pause()

section("8.2 — The Circuit Breaker Pattern")

explain("A circuit breaker stops calling a failing service after")
explain("too many errors — gives it time to recover.")
blank()

cmd("class CircuitBreaker:")
cmd("    def __init__(self, func, max_failures=3):")
cmd("        self.func          = func")
cmd("        self.max_failures  = max_failures")
cmd("        self.failure_count = 0")
blank()
cmd("    def __call__(self, *args, **kwargs):")
cmd("        if self.failure_count >= self.max_failures:")
cmd("            raise IaCError('Circuit open: too many failures')")
cmd("        try:")
cmd("            result = self.func(*args, **kwargs)")
cmd("            self.failure_count = 0  # reset on success")
cmd("            return result")
cmd("        except Exception:")
cmd("            self.failure_count += 1")
cmd("            raise")
blank()

class CircuitBreaker:
    def __init__(self, func, max_failures=3):
        self.func          = func
        self.max_failures  = max_failures
        self.failure_count = 0

    def __call__(self, *args, **kwargs):
        if self.failure_count >= self.max_failures:
            raise IaCError("Circuit open: too many failures")
        try:
            result = self.func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception:
            self.failure_count += 1
            raise

pause()

call_count = {"n": 0}

def unreliable():
    call_count["n"] += 1
    if call_count["n"] <= 3:
        raise ConnectionError("service down")
    return "ok"

cmd("cb = CircuitBreaker(unreliable, max_failures=3)")
cb = CircuitBreaker(unreliable, max_failures=3)
blank()
cmd("for i in range(5):")
cmd("    try:")
cmd("        print(f'call {i+1}: {cb()}')")
cmd("    except Exception as e:")
cmd("        print(f'call {i+1}: {type(e).__name__}: {e}')")
blank()

for i in range(5):
    try:
        result = cb()
        out(f"  call {i+1}: {result}")
    except IaCError as e:
        err(f"  call {i+1}: IaCError (circuit open): {e}")
    except Exception as e:
        err(f"  call {i+1}: {type(e).__name__}: {e}")
blank()

pause()

section("8.3 — Structured Error Logging")

explain("In production IaC, log errors as structured dicts so")
explain("they can be consumed by monitoring systems.")
blank()

cmd("def run_with_logging(inventory):")
cmd("    success = []")
cmd("    log     = []")
cmd("    for d in inventory:")
cmd("        try:")
cmd("            result = connect_device(d)")
cmd("            success.append(d['hostname'])")
cmd("        except DeviceOfflineError as e:")
cmd("            log.append({")
cmd("                'hostname':    d['hostname'],")
cmd("                'error_type':  type(e).__name__,")
cmd("                'message':     str(e),")
cmd("                'recoverable': True,")
cmd("            })")
cmd("        except Exception as e:")
cmd("            log.append({")
cmd("                'hostname':    d['hostname'],")
cmd("                'error_type':  type(e).__name__,")
cmd("                'message':     str(e),")
cmd("                'recoverable': False,")
cmd("            })")
cmd("    return {'success': success, 'log': log}")
blank()

def run_with_logging(inventory):
    success = []
    log     = []
    for d in inventory:
        try:
            connect_device(d)
            success.append(d["hostname"])
        except DeviceOfflineError as e:
            log.append({
                "hostname":    d["hostname"],
                "error_type":  type(e).__name__,
                "message":     str(e),
                "recoverable": True,
            })
        except Exception as e:
            log.append({
                "hostname":    d["hostname"],
                "error_type":  type(e).__name__,
                "message":     str(e),
                "recoverable": False,
            })
    return {"success": success, "log": log}

cmd("report = run_with_logging(INVENTORY)")
report = run_with_logging(INVENTORY)
cmd("print('Success:', report['success'])")
out(f"Success: {report['success']}")
blank()
cmd("for entry in report['log']:")
cmd("    print(entry)")
for entry in report["log"]:
    err(f"  {entry}")
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
print(f"  {BOLD}Ch 1{RESET}   Why exceptions matter — scripts must not crash on bad data")
print(f"  {BOLD}Ch 2{RESET}   try/except/else/finally — the four clauses and when to use each")
print(f"  {BOLD}Ch 3{RESET}   raise — guard clauses, validation, early return pattern")
print(f"  {BOLD}Ch 4{RESET}   Custom exceptions — DeviceOfflineError, full IaC hierarchy")
print(f"  {BOLD}Ch 5{RESET}   Exception chaining — raise ... from e / raise ... from None")
print(f"  {BOLD}Ch 6{RESET}   Context managers — __enter__ / __exit__, with statement")
print(f"  {BOLD}Ch 7{RESET}   Collecting errors — batch validation, stage-by-stage pipeline")
print(f"  {BOLD}Ch 8{RESET}   Advanced — retry decorator, circuit breaker, structured logging")
blank()
print(f"  {WHITE}Every pattern in this tutorial maps directly to a real")
print(f"  Cisco IaC scenario: device validation, config push,")
print(f"  compliance reporting, and resilient batch operations.{RESET}")
blank()
print(f"{BOLD}{bar}{RESET}")
print(f"{BOLD}   Tutorial complete.{RESET}")
print(f"{BOLD}{bar}{RESET}")
print()