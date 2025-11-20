# Task 3: System Calls and IPC (Python - fork, exec, pipe) 
# Use system calls (fork(), exec(), wait()) and implement basic Inter-Process Communication using pipes in C or Python.
import os
r, w = os.pipe()
pid = os.fork()
if pid > 0:
    os.close(r)
    os.write(w, b"Hello from parent")
    os.close(w)
    os.wait()
else:
    os.close(w)
    message = os.read(r, 1024)
    print("Child received:", message.decode())
    os.close(r)