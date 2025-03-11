import tkinter as tk
from tkinter import ttk

class ProcessTable(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columns = ["Process ID", "Arrival Time", "Burst Time", "Priority"]
        self.table = ttk.Treeview(self, columns=self.columns, show="headings")
        
        for col in self.columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100)
        
        self.table.pack()
        
        self.add_button = ttk.Button(self, text="Add Row", command=self.add_row)
        self.add_button.pack()

    def add_row(self):
        self.table.insert("", "end", values=("", "", "", "", ""))

    def get_input_data(self):
        processes = []
        for row in self.table.get_children():
            values = self.table.item(row)["values"]
            if len(values) < 3:
                continue
            processes.append({
                "id": values[0],
                "arrival_time": int(values[1]),
                "burst_time": int(values[2]),
                "priority": int(values[3]) 
            })
        return processes, 1  # Default quantum
