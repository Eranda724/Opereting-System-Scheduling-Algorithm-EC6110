import tkinter as tk
from tkinter import ttk, messagebox
import random

class SchedulerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CPU Scheduling Simulator")
        self.root.geometry("700x500")
        self.process_list = []
        self.colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6", "#1abc9c"]
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="CPU Scheduling Simulator", font=("Arial", 14)).pack()
        
        self.table = ttk.Treeview(self.root, columns=("PID", "Arrival Time", "Burst Time"), show="headings")
        for col in ("PID", "Arrival Time", "Burst Time"):
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
        
        tk.Button(self.root, text="Add Process", command=self.add_process).pack(pady=5)
        tk.Button(self.root, text="Run Scheduler", command=self.run_scheduler).pack(pady=5)
        
        self.canvas = tk.Canvas(self.root, width=600, height=100, bg="white")
        self.canvas.pack(pady=20)
        
    def add_process(self):
        pid = self.pid_entry.get()
        arrival = self.arrival_entry.get()
        burst = self.burst_entry.get()
        
        if not pid.isdigit() or not arrival.isdigit() or not burst.isdigit():
            messagebox.showerror("Input Error", "PID, Arrival Time, and Burst Time must be numbers")
            return
        
        self.table.insert("", "end", values=(pid, arrival, burst))
        self.process_list.append({
            "pid": int(pid),
            "arrival_time": int(arrival),
            "burst_time": int(burst)
        })
        
        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
    
    def run_scheduler(self):
        self.process_list.sort(key=lambda x: x["arrival_time"])  # Simple FCFS Scheduling
        self.display_queue()
    
    def display_queue(self):
        self.canvas.delete("all")
        x_offset = 10
        for process in self.process_list:
            color = random.choice(self.colors)
            self.canvas.create_rectangle(x_offset, 20, x_offset + (process["burst_time"] * 20), 80, fill=color, outline="black")
            self.canvas.create_text(x_offset + 20, 50, text=f"P{process['pid']}", fill="white")
            x_offset += (process["burst_time"] * 20) + 5  # Space between blocks
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SchedulerApp()
    app.run()
