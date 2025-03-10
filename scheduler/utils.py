def calculate_waiting_time(schedule):
    waiting_times = {}
    for process in schedule:
        if process["id"] not in waiting_times:
            waiting_times[process["id"]] = process["start"]
        else:
            waiting_times[process["id"]] += process["start"] - sum([p["duration"] for p in schedule if p["id"] == process["id"] and p["start"] < process["start"]])
    return waiting_times

def calculate_turnaround_time(schedule):
    turnaround_times = {}
    for process in schedule:
        turnaround_times[process["id"]] = process["start"] + process["duration"]
    return turnaround_times
