def priority_scheduling(processes):
    ready_queue = sorted(processes, key=lambda x: (x["arrival_time"], x["priority"]))
    schedule = []
    start_time = 0

    for process in ready_queue:
        start_time = max(start_time, process["arrival_time"])
        schedule.append({"pid": process["pid"], "start": start_time, "duration": process["burst_time"]})
        start_time += process["burst_time"]

    return schedule
