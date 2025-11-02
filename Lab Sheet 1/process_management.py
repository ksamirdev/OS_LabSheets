import os
import time

def task1_process_creation():
    print("=" * 50)
    print("TASK 1: Process Creation Utility")
    print("=" * 50)
    
    N = 3  # Number of child processes
    children_pids = []

    for i in range(N):
        pid = os.fork()

        if pid == 0:
            # Child process
            child_pid = os.getpid()
            parent_pid = os.getppid()
            print(
                f"Child {i+1}: PID={child_pid}, Parent PID={parent_pid}, Message='Hello from child {i+1}'"
            )
            os._exit(0)  # Child exits immediately
        else:
            # Parent process
            children_pids.append(pid)
            print(f"Parent: Created child {i+1} with PID={pid}")

    # Parent waits for all children
    if pid != 0:  # Only parent executes this
        print(f"\nParent (PID={os.getpid()}) waiting for all children to finish...")
        for i, child_pid in enumerate(children_pids):
            waited_pid, status = os.wait()
            print(f"Parent: Child with PID={waited_pid} finished with status={status}")

    print()

def task2_command_execution():
    print("=" * 50)
    print("TASK 2: Command Execution Using exec()")
    print("=" * 50)
    
    commands = [
        ['ls', '-la'],      
        ['date'],           
        ['pwd']
    ]

    N = 3  # Number of child processes
    children_pids = []

    for i in range(N):
        pid = os.fork()

        if pid == 0:
            # Child process
            child_pid = os.getpid()
            parent_pid = os.getppid()
            print(f"Child {i+1}: PID={child_pid}, Parent PID={parent_pid}")
            print(f"Executing command: {' '.join(commands[i])}")
            
            try:
                # Execute the Linux command
                os.execvp(commands[i][0], commands[i])
            except FileNotFoundError:
                print(f"Error: Command '{commands[i][0]}' not found")
                os._exit(1)
            except Exception as e:
                print(f"Error executing command: {e}")
                os._exit(1)
            
        else:
            # Parent process
            children_pids.append(pid)
            print(f"Parent: Created child {i+1} with PID={pid} for command: {' '.join(commands[i])}")

    # Parent waits for all children
    if pid != 0:  # Only parent executes this
        print(f"\nParent (PID={os.getpid()}) waiting for all children to finish...")
        for i, child_pid in enumerate(children_pids):
            waited_pid, status = os.wait()
            if os.WIFEXITED(status):
                exit_status = os.WEXITSTATUS(status)
                print(f"Parent: Child with PID={waited_pid} finished with exit status={exit_status}")

    print()

def task3_zombie_orphan():
    print("=" * 50)
    print("TASK 3: Zombie & Orphan Processes")
    print("=" * 50)
    
    print("Creating Zombie Process...")
    # Create zombie process
    pid_zombie = os.fork()
    
    if pid_zombie == 0:
        # Child process for zombie
        print(f"Zombie Child: PID={os.getpid()}, Parent PID={os.getppid()}")
        print("Zombie child exiting immediately...")
        os._exit(0)
    else:
        # Parent doesn't wait - creates zombie
        print(f"Parent: Created zombie child with PID={pid_zombie}")
        print("Zombie child created. Parent will not call wait().")
        time.sleep(3)  # Give time to check zombie
    
    print("\nCreating Orphan Process...")
    # Create orphan process
    pid_orphan = os.fork()
    
    if pid_orphan == 0:
        # Child process for orphan
        print(f"Orphan Child: PID={os.getpid()}, Parent PID={os.getppid()}")
        print("Orphan child sleeping for 5 seconds...")
        time.sleep(5)
        print(f"Orphan Child: Now Parent PID={os.getppid()} (should be 1 - init)")
    else:
        # Parent exits immediately - creates orphan
        print(f"Parent: Created orphan child with PID={pid_orphan}")
        print("Parent exiting immediately, creating orphan...")


def task4_proc_inspection():
    print("=" * 50)
    print("TASK 4: Inspecting Process Info from /proc")
    print("=" * 50)
    
    current_pid = os.getpid()
    pid = input(f"Enter PID to inspect (or press Enter for current process {current_pid}): ").strip()
    
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
    
    print()

def main():
    task1_process_creation()
    task2_command_execution()
    task3_zombie_orphan()
    task4_proc_inspection()

if __name__ == "__main__":
    main()
