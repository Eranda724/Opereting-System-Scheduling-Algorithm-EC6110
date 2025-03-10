from utils.input_handler import get_process_input
from utils.metrics import compare_algorithms, best_algorithm
from utils.visualize import gantt_chart
from algorithms.fcfs import fcfs_scheduling
from algorithms.round_robin import round_robin
from algorithms.sjf import sjf_scheduling
from algorithms.srtn import srtf_scheduling
from algorithms.priority import priority_scheduling

def main():
    print("\n📌 Process Scheduling Simulator")
    
    # Step 1: Get User Input
    processes = get_process_input()
    time_quantum = int(input("Enter time quantum for Round Robin: "))
    
    # Step 2: Run Scheduling Algorithms
    print("\n🔄 Running Scheduling Algorithms...")
    results = {
        "FCFS": fcfs_scheduling(processes),
        "Round Robin": round_robin(processes, time_quantum),
        "SJF": sjf_scheduling(processes),
        "SRTN": srtf_scheduling(processes),
        "Priority": priority_scheduling(processes),
    }

    # Step 3: Compare Performance
    print("\n📊 Comparing Scheduling Performance...")
    metrics = compare_algorithms(processes, results)

    # Step 4: Determine Best Algorithm
    best_algorithm(metrics)

    # Step 5: Visualize Gantt Charts
    for algo, schedule in results.items():
        print(f"\n📌 Gantt Chart for {algo}:")
        gantt_chart(schedule)

if __name__ == "__main__":
    main()