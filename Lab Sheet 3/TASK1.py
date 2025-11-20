#Task 1: CPU Scheduling with Gantt Chart
#Write a Python program to simulate Priority and Round Robin scheduling algorithms. Compute average waiting and turnaround times.

# Priority Scheduling Simulation

processes = []
n = int(input("Enter number of processes: "))
for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
    processes.append((i+1, bt, pr))
processes.sort(key=lambda x: x[2])
wt = 0
total_wt = 0
total_tt = 0
print("\nPriority Scheduling:")
print("PID\tBT\tPriority\tWT\tTAT")
for pid, bt, pr in processes:
    tat = wt + bt
    print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
    total_wt += wt
    total_tt += tat
    wt += bt
print(f"Average Waiting Time: {total_wt / n}")
print(f"Average Turnaround Time: {total_tt / n}")

# Round Robin Scheduling Algorithm

processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append([i+1, bt])

quantum = int(input("Enter Time Quantum: "))

# Remaining burst time list
rem_bt = [p[1] for p in processes]
wt = [0] * n
tat = [0] * n
t = 0  # current time

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

# Calculate TAT = WT + BT
for i in range(n):
    tat[i] = wt[i] + processes[i][1]
    print(f"{processes[i][0]}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")

print(f"Average Waiting Time: {sum(wt)/n}")
print(f"Average Turnaround Time: {sum(tat)/n}")
