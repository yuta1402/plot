import math
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data_xmin = math.inf
data_xmax = -math.inf
data_ymin = math.inf
data_ymax = -math.inf

def plot_data(filename, label):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        x = []
        y = []

        for line in lines:
            values = line.replace('\n', '').split(' ')
            x.append(float(values[0]))
            y.append(float(values[1]))

        plt.plot(x, y, linestyle='-', marker='o', label=label);

        global data_xmin, data_xmax, data_ymin, data_ymax
        data_xmin = min([min(x), data_xmin])
        data_xmax = max([max(x), data_xmax])
        data_ymin = min([min(y), data_ymin])
        data_ymax = max([max(y), data_ymax])

with open('./settings.json', 'r') as setting_file:
    settings = json.load(setting_file)

    if len(settings['datafiles']) <= 0:
        exit()

    for n, f in enumerate(settings['datafiles']):
        filename = f[0]
        label = f[1]

        plot_data(filename, label)

    plt.xlabel(settings['xlabel'], fontsize=12)
    plt.ylabel(settings['ylabel'], fontsize=12)
    plt.xscale(settings['xscale'])
    plt.yscale(settings['yscale'])

    xmin = data_xmin
    xmax = data_xmax
    ymin = data_ymin
    ymax = data_ymax

    if settings['xmin'] != None:
        xmin = settings['xmin']

    if settings['xmax'] != None:
        xmax = settings['xmax']

    if settings['ymin'] != None:
        ymin = settings['ymin']

    if settings['ymax'] != None:
        ymax = settings['ymax']

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    gsettings = settings['grid']
    plt.grid(which=gsettings['which'], color=gsettings['color'], linestyle=gsettings['linestyle'])

    plt.legend()

    if settings['savefig_name'] != '':
        plt.savefig(settings['savefig_name'])
    else:
        plt.show()
