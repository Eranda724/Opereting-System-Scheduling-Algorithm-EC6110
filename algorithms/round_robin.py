from collections import deque

def round_robin(processes, quantum):
    queue = deque(processes)
    schedule = []
    current_time = 0

    while queue:
        process = queue.popleft()
        start_time = max(current_time, process['arrival'])
        exec_time = min(quantum, process['burst'])
        end_time = start_time + exec_time
        schedule.append((process['pid'], start_time, end_time))
        process['burst'] -= exec_time
        current_time = end_time
        if process['burst'] > 0:
            queue.append(process)  # Reinsert if not finished

    return schedule
