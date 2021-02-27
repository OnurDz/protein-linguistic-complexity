from matplotlib import pyplot as plt
import numpy as np
from math import ceil


def comp_dist(sample: list):
    y = list()
    for i in range(len(sample)):
        y.append(i)
    y = np.array(y)

    sample_ = np.array(sample)
    plot = plt.plot(y, sample_, 'r.', markersize=1)
    plt.ylabel('Complexity')
    axis_x_max = int(ceil(len(sample) / 100.0)) * 100
    plt.axis([0, axis_x_max, 0, 1])
    plt.savefig("plot", dpi=250)
    plt.show()


def triple(sample1, sample2, sample3, ws1, ws2, ws3):
    y1 = list()
    y2 = list()
    y3 = list()

    for i in range(len(sample1)):
        y1.append(i)
    y = np.array(y1)
    y1 = np.array(y1)
    for i in range(len(sample2)):
        y2.append(i)
    y = np.array(y2)
    y2 = np.array(y2)
    for i in range(len(sample3)):
        y3.append(i)
    y = np.array(y3)
    y3 = np.array(y3)

    sample_1 = np.array(sample1)
    sample_2 = np.array(sample2)
    sample_3 = np.array(sample3)

    marker_size_ = 0.75

    plot = plt.plot(y1, sample_1, 'g.', label=str('Window ' + str(ws1)), markersize=marker_size_)
    plot = plt.plot(y2, sample_2, 'b.', label=str('Window ' + str(ws2)), markersize=marker_size_)
    plot = plt.plot(y3, sample_3, 'r.', label=str('Window ' + str(ws3)), markersize=marker_size_)
    plt.ylabel('Complexity')
    ax_x1 = int(ceil(len(sample1) / 100.0)) * 100
    ax_x2 = int(ceil(len(sample2) / 100.0)) * 100
    ax_x3 = int(ceil(len(sample3) / 100.0)) * 100
    axis_x_max = max(ax_x1, ax_x2, ax_x3)
    plt.axis([0, axis_x_max, 0, 1])
    plt.legend()
    plt.savefig("tplot", dpi=250)
    plt.show()
