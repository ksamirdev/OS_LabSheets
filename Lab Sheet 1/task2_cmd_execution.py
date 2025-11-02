import os

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
