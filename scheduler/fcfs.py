"""
reviewed and corrected
"""
def fcfs(processes):
    # Sort processes based on arrival time (earliest first)
    processes.sort(key=lambda x: x["arrival_time"])

    schedule = []  # List to store the schedule of processes
    start_time = 0  # Keeps track of when the next process can start execution

    # Iterate through each process to determine its start time and duration
    for process in processes:
        # Ensure the process starts at its arrival time or later (if CPU was idle)
        start_time = max(start_time, process["arrival_time"])

        # Add the process execution details to the schedule
        schedule.append({
            "pid": process["pid"], 
            "start": start_time, 
            "duration": process["burst_time"]
        })

        # Update start_time to when the next process can start
        start_time += process["burst_time"]

    return schedule  # Return the final schedule
