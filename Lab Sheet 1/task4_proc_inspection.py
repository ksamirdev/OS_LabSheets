import os

pid = input("Enter PID to inspect: ").strip()

proc_path = f"/proc/{pid}"

if not os.path.exists(proc_path):
    print(f"Process with PID {pid} does not exist or /proc not available")
    return

print(f"\nInspecting process {pid} from /proc:")

# Read process status
status_file = f"{proc_path}/status"
if os.path.exists(status_file):
    print("\n--- Process Status ---")
    try:
        with open(status_file, "r") as f:
            for line in f:
                if any(
                    key in line for key in ["Name", "State", "Pid", "PPid", "VmRSS"]
                ):
                    print(line.strip())
    except Exception as e:
        print(f"Error reading status: {e}")

# Read executable path
exe_file = f"{proc_path}/exe"
if os.path.exists(exe_file):
    try:
        exe_path = os.readlink(exe_file)
        print(f"\n--- Executable Path ---")
        print(f"Executable: {exe_path}")
    except Exception as e:
        print(f"Error reading exe: {e}")

# Read file descriptors
fd_dir = f"{proc_path}/fd"
if os.path.exists(fd_dir):
    print(f"\n--- Open File Descriptors ---")
    try:
        fds = os.listdir(fd_dir)
        for fd in sorted(fds, key=int):
            fd_path = f"{fd_dir}/{fd}"
            try:
                target = os.readlink(fd_path)
                print(f"FD {fd} -> {target}")
            except:
                print(f"FD {fd} -> [cannot read]")
    except Exception as e:
        print(f"Error reading file descriptors: {e}")
