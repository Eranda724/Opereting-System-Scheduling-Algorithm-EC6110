def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])  # Sort by arrival time
    schedule = []
    current_time = 0

    for process in processes:
        start_time = max(current_time, process['arrival'])
        end_time = start_time + process['burst']
        schedule.append((process['pid'], start_time, end_time))
        current_time = end_time  # Move time forward

    return schedule
