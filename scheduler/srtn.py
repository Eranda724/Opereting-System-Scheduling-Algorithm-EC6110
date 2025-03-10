def srtn(processes):
    processes.sort(key=lambda x: (x["arrival_time"], x["burst_time"]))
    schedule = []
    remaining_processes = processes[:]
    time = 0

    while remaining_processes:
        remaining_processes.sort(key=lambda x: x["burst_time"])
        process = remaining_processes.pop(0)
        schedule.append({"pid": process["pid"], "start": time, "duration": process["burst_time"]})
        time += process["burst_time"]

    return schedule
