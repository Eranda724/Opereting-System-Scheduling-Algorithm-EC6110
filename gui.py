import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from algorithms.fcfs import fcfs_scheduling
from algorithms.round_robin import round_robin
from algorithms.sjf import sjf_scheduling
from algorithms.srtn import srtf_scheduling
from algorithms.priority import priority_scheduling
from utils.metrics import compare_algorithms, best_algorithm

# Global variables
processes = []
time_quantum = 2

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.processes = []
        self.time_quantum = 2

        # GUI Setup
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Process Scheduling Simulator")
        self.root.geometry("600x500")

        # Input Fields
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Arrival Time").grid(row=0, column=0)
        tk.Label(frame, text="Burst Time").grid(row=0, column=1)
        tk.Label(frame, text="Priority").grid(row=0, column=2)

        self.arrival_var = tk.StringVar()
        self.burst_var = tk.StringVar()
        self.priority_var = tk.StringVar()

        tk.Entry(frame, textvariable=self.arrival_var, width=10).grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.burst_var, width=10).grid(row=1, column=1)
        tk.Entry(frame, textvariable=self.priority_var, width=10).grid(row=1, column=2)

        tk.Button(frame, text="Add Process", command=self.add_process).grid(row=1, column=3)

        # Process Table
        columns = ("PID", "Arrival", "Burst", "Priority")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        # Time Quantum Input
        tk.Label(self.root, text="Time Quantum (for Round Robin)").pack()
        self.quantum_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.quantum_var, width=10).pack()

        # Run Scheduling Button
        tk.Button(self.root, text="Run Scheduling", command=self.run_scheduling).pack(pady=5)
        tk.Button(self.root, text="Show Gantt Chart", command=self.show_gantt_chart).pack(pady=5)

    def validate_process(self, arrival, burst, priority):
        if arrival < 0:
            raise ValueError("Arrival time must be >= 0.")
        if burst <= 0:
            raise ValueError("Burst time must be > 0.")
        if priority < 0:
            raise ValueError("Priority must be >= 0.")

    def add_process(self):
        try:
            arrival = int(self.arrival_var.get())
            burst = int(self.burst_var.get())
            priority = int(self.priority_var.get())

            # Validate input
            self.validate_process(arrival, burst, priority)

            pid = len(self.processes) + 1
            self.processes.append({"pid": pid, "arrival": arrival, "burst": burst, "priority": priority})

            # Update table
            self.tree.insert("", "end", values=(pid, arrival, burst, priority))
            self.arrival_var.set("")
            self.burst_var.set("")
            self.priority_var.set("")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def run_scheduling(self):
        try:
            self.time_quantum = int(self.quantum_var.get())

            # Run all scheduling algorithms
            results = {
                "FCFS": fcfs_scheduling(self.processes),
                "Round Robin": round_robin(self.processes, self.time_quantum),
                "SJF": sjf_scheduling(self.processes),
                "SRTN": srtf_scheduling(self.processes),
                "Priority": priority_scheduling(self.processes),
            }

            # Compare performance
            metrics = compare_algorithms(self.processes, results)
            best_algorithm(metrics)

            # Show results in GUI
            messagebox.showinfo("Success", "Scheduling Completed! Check the console for results.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Enter a valid time quantum: {e}")

    def show_gantt_chart(self):
        try:
        # Run all scheduling algorithms
            results = {
                "FCFS": fcfs_scheduling(self.processes),
                "Round Robin": round_robin(self.processes, self.time_quantum),
                "SJF": sjf_scheduling(self.processes),
                "SRTN": srtf_scheduling(self.processes),
                "Priority": priority_scheduling(self.processes),
            }

            # Create subplots for each algorithm
            fig, axes = plt.subplots(len(results), 1, figsize=(10, len(results) * 2), sharex=True)

            # Handle the case where there's only one algorithm
            if len(results) == 1:
                axes = [axes]  # Convert single axis to a list

            # Plot Gantt charts
            for ax, (algo, schedule) in zip(axes, results.items()):
                for pid, start, end in schedule:
                    ax.barh(algo, end - start, left=start, label=f"P{pid}", color=f"C{pid % 10}")
                ax.set_title(f"Gantt Chart for {algo}")
                ax.set_xlabel("Time")
                ax.set_ylabel("Processes")
                ax.legend()

            plt.tight_layout()
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate Gantt chart: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()