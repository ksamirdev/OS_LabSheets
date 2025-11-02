N = 3 # Number of child processes

children_pids = []

for i in range(N):
    pid = os.fork()

    if pid == 0:
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
