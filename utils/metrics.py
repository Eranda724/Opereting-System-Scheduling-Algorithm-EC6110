def compare_algorithms(processes, results):
    metrics = {}

    for algo, schedule in results.items():
        avg_wait = sum(start - next(p["arrival"] for p in processes if p["pid"] == pid) for pid, start, end in schedule) / len(schedule)
        avg_turnaround = sum(end - next(p["arrival"] for p in processes if p["pid"] == pid) for pid, start, end in schedule) / len(schedule)
        metrics[algo] = {"Avg Waiting Time": avg_wait, "Avg Turnaround Time": avg_turnaround}

    return metrics

def best_algorithm(metrics):
    best = min(metrics, key=lambda algo: metrics[algo]["Avg Waiting Time"])
    print(f"\n✅ Best Scheduling Algorithm: {best} (Minimum Waiting Time)")
