#  Process Logging and Multiprocessing System

##  Overview
This Python program demonstrates **basic multiprocessing** along with **logging** to track system-like process activities.  
Each process simulates a small task, logs its start and end time, and runs concurrently with another process.

It uses:
- `multiprocessing` — to create and manage multiple child processes.
- `logging` — to log messages with timestamps and process names.

---

##  Features
 Logs process activity (start and end) with timestamps  
 Runs two child processes in parallel  
 Demonstrates safe process creation and termination  
 Automatically stores logs in a file `process_log.txt`  

---

##  How It Works
1. The **logging** system is configured to store messages in `process_log.txt`.  
2. Two separate **processes** (`Process-1` and `Process-2`) are created using `multiprocessing.Process()`.  
3. Each process runs the `system_process()` function, which:
   - Logs when it starts.
   - Waits for 2 seconds (simulating some work).
   - Logs when it finishes.
4. The parent process waits for both children to complete using `.join()` before shutting down.

---
