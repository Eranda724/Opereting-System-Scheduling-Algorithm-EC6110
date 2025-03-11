import tkinter as tk
from tkinter import ttk, messagebox
import random
from scheduler.fcfs import fcfs
from scheduler.round_robin import round_robin
from scheduler.spn import spn
from scheduler.srtn import srtn
from scheduler.priority import priority_scheduling
from ui.gantt_chart import generate_gantt_chart , display_queue

class SchedulerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CPU Scheduling Simulator")
        self.root.geometry("700x600")
        self.process_list = []
        self.colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6", "#1abc9c"]
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="CPU Scheduling Simulator", font=("Arial", 14)).pack()
        
        self.table = ttk.Treeview(self.root, columns=("PID", "Arrival Time", "Burst Time",  "Priority"), show="headings")
        for col in ("PID", "Arrival Time", "Burst Time", "Priority"):
            self.table.heading(col, text=col)
            self.table.column(col, width=100)
        self.table.pack(pady=10)
        
        entry_frame = tk.Frame(self.root)
        entry_frame.pack()
        
        tk.Label(entry_frame, text="PID:").grid(row=0, column=0)
        self.pid_entry = ttk.Entry(entry_frame)
        self.pid_entry.grid(row=0, column=1)
        
        tk.Label(entry_frame, text="Arrival Time:").grid(row=0, column=2)
        self.arrival_entry = ttk.Entry(entry_frame)
        self.arrival_entry.grid(row=0, column=3)

        tk.Label(entry_frame, text="Burst Time:").grid(row=0, column=4)
        self.burst_entry = ttk.Entry(entry_frame)
        self.burst_entry.grid(row=0, column=5)
        
        tk.Label(entry_frame, text="Priority:").grid(row=0, column=6)
        self.priority_entry = ttk.Entry(entry_frame)
        self.priority_entry.grid(row=0, column=7)
        
        tk.Button(self.root, text="Add Process", command=self.add_process).pack(pady=5)
        
        self.algorithm_choice = tk.StringVar()
        self.algorithm_choice.set("FCFS")
        
        algo_frame = tk.Frame(self.root)
        algo_frame.pack()
        
        algorithms = ["FCFS", "Round Robin", "SPN", "SRTN", "Priority"]
        for algo in algorithms:
            tk.Radiobutton(algo_frame, text=algo, variable=self.algorithm_choice, value=algo).pack(side=tk.LEFT)
        
        tk.Button(self.root, text="Run Scheduler", command=self.run_scheduler).pack(pady=5)
        
        # self.canvas = tk.Canvas(self.root, width=600, height=100, bg="white")
        # self.canvas.pack(pady=20)
        
    def add_process(self):
        pid = self.pid_entry.get()
        arrival = self.arrival_entry.get()
        burst = self.burst_entry.get()
        priority = self.priority_entry.get()
        
        if not pid.isdigit() or not arrival.isdigit() or not burst.isdigit():
            messagebox.showerror("Input Error", "All fields must be numbers")
            return
        
        self.table.insert("", "end", values=(pid, arrival, burst, priority))
        self.process_list.append({
            "pid": int(pid),
            "arrival_time": int(arrival),
            "burst_time": int(burst),
            "priority": int(priority)
        })
        
        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
    
    def run_scheduler(self):
        algorithm = self.algorithm_choice.get()
        
        if not self.process_list:
            messagebox.showerror("Error", "No processes added!")
            return
        
        if algorithm == "FCFS":
            schedule = fcfs(self.process_list)
        elif algorithm == "Round Robin":
            schedule = round_robin(self.process_list, time_quantum=1)
        elif algorithm == "SPN":
            schedule = spn(self.process_list)
        elif algorithm == "SRTN":
            schedule = srtn(self.process_list)
        elif algorithm == "Priority":
            schedule = priority_scheduling(self.process_list)
        else:
            messagebox.showerror("Error", "Invalid Algorithm Selected")
            return
        
        generate_gantt_chart(schedule, algorithm)
        # display_queue(self)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SchedulerApp()
    app.run()