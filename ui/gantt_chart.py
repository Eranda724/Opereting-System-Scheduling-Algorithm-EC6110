import matplotlib.pyplot as plt

def generate_gantt_chart(schedule, algorithm):
    fig, ax = plt.subplots()
    
    for task in schedule:
        ax.broken_barh([(task["start"], task["duration"])], (task["pid"] * 10, 8), facecolors="blue")

    ax.set_xlabel("Time")
    ax.set_ylabel("Process ID")
    ax.set_title(f"Gantt Chart - {algorithm}")

    plt.show()
