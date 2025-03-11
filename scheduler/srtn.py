"""
reviewed and corrected
"""
def srtn(processes):
    # Initialize remaining time for each process
    for process in processes:
        process["remaining_time"] = process["burst_time"]

    schedule = []
    time = 0
    finished = 0
    n = len(processes)

    # Continue until all processes have finished
    while finished < n:
        # Find processes that have arrived and are not finished
        ready = [p for p in processes if p["arrival_time"] <= time and p["remaining_time"] > 0]
        if not ready:
            # If no process is ready, jump to the next arrival time
            time = min(p["arrival_time"] for p in processes if p["remaining_time"] > 0)
            ready = [p for p in processes if p["arrival_time"] <= time and p["remaining_time"] > 0]

        # Select the process with the smallest remaining time
        current = min(ready, key=lambda p: p["remaining_time"])

        # If the last scheduled segment is for the same process, extend its duration.
        if schedule and schedule[-1]["pid"] == current["pid"]:
            schedule[-1]["duration"] += 1
        else:
            schedule.append({"pid": current["pid"], "start": time, "duration": 1})
        
        # Run the process for one time unit
        current["remaining_time"] -= 1
        time += 1

        # If the process has finished, update the finished count
        if current["remaining_time"] == 0:
            finished += 1

    return schedule