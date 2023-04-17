import numpy as np
import matplotlib.pyplot as plt
from Farma.HalfLife import Drug
from shutil import move


def NPlotter(Drug: Drug, Drug2: Drug, scale: float, var: float):
    """ - Function to plot Drug Levels in a graph, returning a png file.
    """
    def ReadHl():
        with open("hlevels.txt", "r") as f:
            h = f.read()
            hl = [float(i) for i in h.split(",")]
        return hl

    # HUMOR LIST
    hl = ReadHl()

    # Read files
    Drug.ReadFiles()
    Drug2.ReadFiles()

    # Variables
    var = int(var)
    x = np.arange(0, 720, 24)
    scale = float(scale)
    index = Drug.p_index

    half_life1 = Drug.blevels
    half_life2 = Drug2.blevels

    if scale:
        hl[(index)] = scale
        with open("hlevels.txt", "w+") as f:
            f.write(",".join([str(i) for i in hl]))
            
    mood_data = ReadHl()

    # Create subplots
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15), sharex=True)

    x = np.arange(0, 720)

    def NL() -> list:
        name_list = []
        for i in x:
            name = f"""{i} hours"""
            name_list.append(name)
            i += 1
        return name_list

    if Drug.p_index == 0:
        axes[0].set_xlim(0, 220)
        axes[1].set_xlim(0, 220)
        axes[2].set_xlim(0, 220)

    else:
        axes[0].set_xlim(0, Drug.p_index*1.5)
        axes[1].set_xlim(0, Drug.p_index*1.5)
        axes[2].set_xlim(0, Drug.p_index*1.5)

    # Plot half-life concentrations of medications
    axes[0].plot(x, half_life1, label=f"{Drug.path}")
    axes[0].set_ylabel("Half-life concentration")
    axes[0].set_title(f"{Drug.path}")
    axes[0].grid(True)

    axes[1].plot(x, half_life2, label=f"{Drug2.path}")
    axes[1].set_ylabel("Half-life concentration")
    axes[1].set_title(f"{Drug2.path}")
    axes[1].grid(False)

    # Create a bar plot for mood data
    axes[2].bar(x, mood_data, width=0.5, align="center")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Mood")
    axes[2].set_title("Mood Data")
    axes[2].grid(True)
    plt.tight_layout()

    # Display the plot

    fig.savefig("""Lexapro.png""", orientation="portrait")

    move(src="D:\\py\\Lexapro.png", dst="""D:\\py\\static\\img\\Lexapro.png""")


v = Drug("Venvanse", 14, 4)
l = Drug("Lexapro", 36, 4)
v.AddDose(40, var=24)
l.AddDose(200, var=24)

NPlotter(v, l, 0, 0)

v.Erase()
l.Erase()