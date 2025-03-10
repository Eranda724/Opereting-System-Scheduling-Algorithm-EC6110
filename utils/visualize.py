import matplotlib.pyplot as plt

def gantt_chart(schedule):
    fig, ax = plt.subplots()
    for pid, start, end in schedule:
        ax.barh("Process", end-start, left=start, label=f"P{pid}")
    plt.xlabel("Time")
    plt.ylabel("Processes")
    plt.legend()
    plt.show()
