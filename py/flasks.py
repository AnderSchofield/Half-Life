from flask import Flask, render_template, request
from Farma.HalfLife import Drug
from matplotlib import pyplot as plt
import numpy as np
from shutil import move
import matplotlib.dates as mdates


l = Drug("Lexapro", 36, 4)
v = Drug("Venvanse", 12, 5)
days = mdates.DayLocator()  # Major ticks every day
hours_locator = mdates.HourLocator()  # Minor ticks every 24 hours
date_fmt = mdates.DateFormatter('%Y-%m-%d')

reset = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def EraseHumor():
    """ - Function to erase the humor list."""

    with open("hlevels.txt", "w+") as f:
        s = str(reset).split("[")[1].split("]")[0]
        f.write(s)


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
    days = np.arange(0, 720, 24)
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


    def NL() -> list:
        name_list = []
        for i in np.arange(0, 30):
            name = f"""{i} day"""
            name_list.append(name)
        return name_list

    name_list = NL()

    plt.xticks(np.arange(0, 720, 24), name_list, rotation=45)

    x = np.arange(0, 720)


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

    axes[1].plot(x, half_life2, label=f"{Drug2.path}", color="red")
    axes[1].set_ylabel("Half-life concentration")
    axes[1].set_title(f"{Drug2.path}")
    axes[1].grid(True)

    # Create a bar plot for mood data
    axes[2].bar(x, mood_data, width=0.75, align="center")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Mood")
    axes[2].set_title("Mood Data")
    axes[2].grid(True)
    plt.tight_layout()

    # Display the plot

    fig.savefig("""Lexapro.png""", orientation="portrait")

    move(src="D:\\py\\Lexapro.png", dst="""D:\\py\\static\\img\\Lexapro.png""")



app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/process_input', methods=['GET', 'POST'])
def process_input():

    lexa = request.form['input']
    venv = request.form['venv']
    scale = request.form['scale']
    var = request.form['var']
    variables = (lexa, venv, scale, var)


    if not lexa and not venv:
        return render_template('index.html')

    elif not var:
        var = 0
        dose = int(lexa)
        dose2 = int(venv)
        l.AddDose(dose, var)
        v.AddDose(dose2, var)
        scale = int(scale)
        NPlotter(l, v, scale, var)
        return render_template('index.html')
    else:
        dose = int(lexa)
        dose2 = int(venv)
        var = int(var)
        l.AddDose(dose, var)
        v.AddDose(dose2, var)
        scale = int(scale)
        NPlotter(l, v, scale, var)

        return render_template('index.html')


"""@app.route('/process_plot', methods=['GET','POST'])
def process_plot():
    num = request.form['scale']
    if not num:
        return render_template('index.html')
    else:
        f = float(num)
        n = int(f)
        var = int(var)
        Plotter(lexa,n,var)
        return render_template('index.html"""


@app.route('/process_erase', methods=['GET', 'POST'])
def process_erase():

    l.Erase()
    v.Erase()
    EraseHumor()
    NPlotter(l, v, scale=0, var=0)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=5500)
