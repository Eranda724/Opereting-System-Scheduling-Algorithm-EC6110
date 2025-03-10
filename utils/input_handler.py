def get_process_input():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        pid = i + 1
        arrival = int(input(f"Enter arrival time for Process {pid}: "))
        burst = int(input(f"Enter burst time for Process {pid}: "))
        priority = int(input(f"Enter priority for Process {pid} (lower number = higher priority): "))
        processes.append({"pid": pid, "arrival": arrival, "burst": burst, "priority": priority})
    return processes
