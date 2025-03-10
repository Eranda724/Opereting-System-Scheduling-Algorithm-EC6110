def round_robin(processes, time_quantum):
    queue = processes[:]
    time = 0
    schedule = []

    while queue:
        process = queue.pop(0)
        if process["burst_time"] > time_quantum:
            schedule.append({"pid": process["pid"], "start": time, "duration": time_quantum})
            time += time_quantum
            process["burst_time"] -= time_quantum
            queue.append(process)
        else:
            schedule.append({"pid": process["pid"], "start": time, "duration": process["burst_time"]})
            time += process["burst_time"]

    return schedule
