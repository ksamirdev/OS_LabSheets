import os

print("Creating Zombie Process...")
pid_zombie = os.fork()
if pid_zombie == 0:
    print(f"Zombie Child: PID={os.getpid()}, exiting immediately")
    os._exit(0)
else:
    print(f"Parent: Created zombie child with PID={pid_zombie}")
    print("Zombie child created. Parent will not call wait().")
    print("Run 'ps -el | grep defunct' in another terminal to see zombie")
    time.sleep(2)

print("\nCreating Orphan Process...")

pid_orphan = os.fork()
if pid_orphan == 0:
    print(f"Orphan Child: PID={os.getpid()}, Parent PID={os.getppid()}")
    print("Orphan child sleeping for 5 seconds...")
    time.sleep(5)
    print(f"Orphan Child: Now Parent PID={os.getppid()} (should be 1 - init)")
    os._exit(0)
else:
    # Parent exits immediately - creates orphan
    print(f"Parent: Created orphan child with PID={pid_orphan}")
    print("Parent exiting immediately, creating orphan...")
    os._exit(0)  # Parent exits, child becomes orphan
