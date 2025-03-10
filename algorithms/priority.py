def priority_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival'], x['priority']))  # Sort by priority
    schedule = []
    current_time = 0

    for process in processes:
        start_time = max(current_time, process['arrival'])
        end_time = start_time + process['burst']
        schedule.append((process['pid'], start_time, end_time))
        current_time = end_time

    return schedule
