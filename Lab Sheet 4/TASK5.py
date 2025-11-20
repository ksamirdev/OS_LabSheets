# Task 5: CPU Scheduling Algorithms
# Implement FCFS, SJF, Round Robin, and Priority Scheduling algorithms in Python to calculate WT and TAT.
# Use existing Round Robin, FCFS, SJF, Priority scheduling Python codes from Lab 3)
# ==========================
# CPU Scheduling Algorithms
# FCFS, SJF, Priority, Round Robin
# ==========================

# --------- FCFS Scheduling ---------
def fcfs(processes):
    print("\nFCFS Scheduling:")
    print("PID\tBT\tWT\tTAT")
    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print(f"Average Waiting Time: {total_wt/len(processes)}")
    print(f"Average Turnaround Time: {total_tat/len(processes)}")


# --------- SJF Scheduling (Non-Preemptive) ---------
def sjf(processes):
    processes.sort(key=lambda x: x[1])  # sort by burst time

    print("\nSJF Scheduling:")
    print("PID\tBT\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print(f"Average Waiting Time: {total_wt/len(processes)}")
    print(f"Average Turnaround Time: {total_tat/len(processes)}")


# --------- Priority Scheduling ---------
def priority_scheduling(processes):
    # processes = [(pid, bt, priority)]
    processes.sort(key=lambda x: x[2])  # lower value → higher priority

    print("\nPriority Scheduling:")
    print("PID\tBT\tPriority\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print(f"Average Waiting Time: {total_wt/len(processes)}")
    print(f"Average Turnaround Time: {total_tat/len(processes)}")


# --------- Round Robin Scheduling ---------
def round_robin(processes, quantum):
    # processes = [(pid, bt)]
    rem_bt = [bt for _, bt in processes]
    t = 0
    n = len(processes)
    wt = [0] * n
    tat = [0] * n

    print("\nRound Robin Scheduling:")
    print("PID\tBT\tWT\tTAT")

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][1]
                    rem_bt[i] = 0

        if done:
            break

    for i in range(n):
        tat[i] = wt[i] + processes[i][1]
        print(f"{processes[i][0]}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")

    print(f"Average Waiting Time: {sum(wt)/n}")
    print(f"Average Turnaround Time: {sum(tat)/n}")


# ==========================
# MAIN INPUT AREA
# ==========================

n = int(input("Enter number of processes: "))
processes_fcfs = []
processes_sjf = []
processes_priority = []
processes_rr = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority for P{i+1} (lower = higher priority): "))
    
    processes_fcfs.append((i+1, bt))
    processes_sjf.append((i+1, bt))
    processes_priority.append((i+1, bt, pr))
    processes_rr.append((i+1, bt))

quantum = int(input("Enter Time Quantum for Round Robin: "))

# Run algorithms
fcfs(processes_fcfs)
sjf(processes_sjf)
priority_scheduling(processes_priority)
round_robin(processes_rr, quantum)