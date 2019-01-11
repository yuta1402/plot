import math
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data_xmin = math.inf
data_xmax = -math.inf
data_ymin = math.inf
data_ymax = -math.inf

def plot_data(num, fileinfo):
    # required parameters
    filename = fileinfo["filename"]

    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        x = []
        y = []

        for line in lines:
            values = line.replace('\n', '').split(' ')
            x.append(float(values[0]))
            y.append(float(values[1]))

        cmap = plt.get_cmap('tab10')

        # default parameters
        label = filename
        color = cmap(num)
        marker = 'o'
        linestyle = '-'

        # optional parameters
        if 'label' in fileinfo:
            label = fileinfo['label']

        if 'color' in fileinfo:
            color = fileinfo['color']

        if 'marker' in fileinfo:
            marker = fileinfo['marker']

        if 'linestyle' in fileinfo:
            linestyle = fileinfo['linestyle']

        plt.plot(x, y, label=label, color=color, marker=marker, linestyle=linestyle);

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
        plot_data(n, f)

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

    if settings['xticks'] != None:
        xts = settings['xticks']
        plt.xticks(np.arange(xts['begin'], xts['end'], xts['step']))

    if settings['yticks'] != None:
        yts = settings['yticks']
        plt.yticks(np.arange(yts['begin'], yts['end'], yts['step']))

    gsettings = settings['grid']
    plt.grid(which=gsettings['which'], color=gsettings['color'], linestyle=gsettings['linestyle'])

    plt.legend()

    if settings['savefig_name'] != '':
        plt.savefig(settings['savefig_name'])
    else:
        plt.show()
