import math
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

xmin = math.inf
xmax = -math.inf
ymin = math.inf
ymax = -math.inf

def plot_data(filename, cmparam):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        x = []
        y = []

        for line in lines:
            values = line.replace('\n', '').split(' ')
            x.append(float(values[0]))
            y.append(float(values[1]))

        plt.plot(x, y, linestyle='-', marker='o', color=cm.cool(cmparam), label=filename);

        global xmin, xmax, ymin, ymax
        xmin = min([min(x), xmin])
        xmax = max([max(x), xmax])
        ymin = min([min(y), ymin])
        ymax = max([max(y), ymax])

with open('./settings.json', 'r') as setting_file:
    settings = json.load(setting_file)

    for n, f in enumerate(settings['datafiles']):
        plot_data(f, n / len(settings['datafiles']))

    plt.xlabel(settings['xlabel'], fontsize=12)
    plt.ylabel(settings['ylabel'], fontsize=12)
    plt.xscale(settings['xscale'])
    plt.yscale(settings['yscale'])

    plt.xlim(xmin, xmax)
    # plt.yticks(np.arange(10**0, 10**(-5), 10**(-1)))
    plt.ylim(10**(math.floor(math.log10(ymin))), 10**0)

    gsettings = settings['grid']
    plt.grid(which=gsettings['which'], color=gsettings['color'], linestyle=gsettings['linestyle'])

    plt.legend()

    if settings['savefig_name'] != '':
        plt.savefig(settings['savefig_name'])
    else:
        plt.show()
