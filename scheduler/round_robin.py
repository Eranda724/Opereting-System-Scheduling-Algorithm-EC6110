from collections import deque
"""
reviewed and corrected
"""
def round_robin(processes, time_quantum):
    processes = sorted(processes, key=lambda x: x["arrival_time"])  # Sort by arrival time
    queue = deque()
    time = 0
    schedule = []
    index = 0  # Tracks the next process to be added

    while queue or index < len(processes):
        # Add new processes that have arrived at the current time
        while index < len(processes) and processes[index]["arrival_time"] <= time:
            queue.append(processes[index])
            index += 1

        if not queue:  # If queue is empty, jump to the next arrival
            time = processes[index]["arrival_time"]
            continue

        process = queue.popleft()  # Get the first process in the queue

        # Run for one time quantum or remaining burst time
        duration = min(time_quantum, process["burst_time"])
        schedule.append({"pid": process["pid"], "start": time, "duration": duration})
        time += duration
        process["burst_time"] -= duration

        # Add any newly arrived processes before re-adding the current process
        while index < len(processes) and processes[index]["arrival_time"] <= time:
            queue.append(processes[index])
            index += 1

        # If process still has remaining time, put it back in the queue
        if process["burst_time"] > 0:
            queue.append(process)

    return schedule
