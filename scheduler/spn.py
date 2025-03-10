def spn(processes):
    processes.sort(key=lambda x: (x["arrival_time"], x["burst_time"]))
    schedule = []
    start_time = 0

    for process in processes:
        start_time = max(start_time, process["arrival_time"])
        schedule.append({"pid": process["pid"], "start": start_time, "duration": process["burst_time"]})
        start_time += process["burst_time"]

    return schedule
