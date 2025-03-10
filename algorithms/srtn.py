import heapq

def srtf_scheduling(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])  # Sort by arrival time
    ready_queue = []
    current_time = 0
    schedule = []
    
    while processes or ready_queue:
        # Add arriving processes to the ready queue
        while processes and processes[0]['arrival'] <= current_time:
            process = processes.pop(0)
            heapq.heappush(ready_queue, (process['burst'], process['arrival'], process['pid'], process)) 

        if ready_queue:
            # Pick the process with the shortest remaining time
            _, _, _, process = heapq.heappop(ready_queue)
            start_time = max(current_time, process['arrival'])
            exec_time = min(process['burst'], 1)  # Execute in small steps (preemptive)
            end_time = start_time + exec_time
            schedule.append((process['pid'], start_time, end_time))
            current_time = end_time
            process['burst'] -= exec_time
            
            if process['burst'] > 0:
                heapq.heappush(ready_queue, (process['burst'], process['arrival'], process['pid'], process))
        else:
            current_time += 1  # If no process is ready, move time forward

    return schedule
