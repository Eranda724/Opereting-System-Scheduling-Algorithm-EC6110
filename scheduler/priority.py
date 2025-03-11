"""
reviewed and corrected
"""
def priority_scheduling(processes):
    schedule = []
    current_time = 0
    # Work on a copy of the list, sorted based on arrival time so that the earliest arriving process comes first.
    processes_left = sorted(processes, key=lambda x: x["arrival_time"])
    
    # Continue until all processes are scheduled
    while processes_left:
        # Find all processes that have arrived by the current time.
        ready_queue = [p for p in processes_left if p["arrival_time"] <= current_time]
        
        # If no process has arrived, jump to the next arrival time.
        if not ready_queue:
            current_time = processes_left[0]["arrival_time"]
            ready_queue = [p for p in processes_left if p["arrival_time"] <= current_time]
        
        # Select the process with the highest priority (assuming lower numerical values are higher priority)
        next_process = min(ready_queue, key=lambda x: x["priority"])
        
        # Schedule the chosen process.
        schedule.append({
            "pid": next_process["pid"],
            "start": current_time,
            "duration": next_process["burst_time"]
        })
        
        # Advance current_time by the burst time of the process.
        current_time += next_process["burst_time"]
        
        # Remove the scheduled process from the list.
        processes_left.remove(next_process)
    
    return schedule
