def compare_algorithms(processes, results):
    metrics = {}
    arrival_map = {p['pid']: p['arrival'] for p in processes}
    
    for algo, schedule in results.items():
        total_wait = 0
        total_turnaround = 0
        
        for pid, start, end in schedule:
            arrival = arrival_map[pid]
            wait = start - arrival
            turnaround = end - arrival
            total_wait += wait
            total_turnaround += turnaround
            
        avg_wait = total_wait / len(schedule)
        avg_turnaround = total_turnaround / len(schedule)
        metrics[algo] = {"Avg Waiting Time": avg_wait, "Avg Turnaround": avg_turnaround}
        
    return metrics

def best_algorithm(metrics):
    best = min(metrics.items(), key=lambda x: x[1]["Avg Waiting Time"])
    print(f"\n🏆 Best Algorithm: {best[0]} (Avg Wait: {best[1]['Avg Waiting Time']:.2f})")