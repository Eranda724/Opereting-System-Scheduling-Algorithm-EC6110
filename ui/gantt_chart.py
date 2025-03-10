import matplotlib.pyplot as plt
import random

def generate_gantt_chart(schedule, algorithm):
    fig, ax = plt.subplots()
    
    for task in schedule:
        ax.broken_barh([(task["start"], task["duration"])], (task["pid"] * 10, 8), facecolors="blue")

    ax.set_xlabel("Time")
    ax.set_ylabel("Process ID")
    ax.set_title(f"Gantt Chart - {algorithm}")

    plt.show()

def display_queue(self):
    self.canvas.delete("all")
    x_offset = 10
    for process in self.process_list:
        color = random.choice(self.colors)
        block_width = process["burst_time"] * 20  # Width based on burst time
        self.canvas.create_rectangle(x_offset, 20, x_offset + block_width, 80, fill=color, outline="black")

        # 🛠 Fix: Align text to the left inside the block
        self.canvas.create_text(x_offset + 5, 50, text=f"P{process['pid']}", fill="white", anchor="w")

        x_offset += block_width + 5  # Add space between blocks
