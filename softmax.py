import matplotlib

matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def plot_softmax(fig):
    ax = fig.add_subplot(111)
    xs = np.arange(-4,4,0.1)
    ys = softmax(xs)
    ax.text(1.5,.038,r'$\frac{e^{y_i}}{\sum_j e^{y_i}}$', fontsize=32)
    ax.set_xlabel('score')
    ax.set_ylabel('probability')
    ax.plot(xs, ys, '.', linewidth=1.5,)

def plot_total():
    fig = plt.figure()
    plot_softmax(fig)
    plt.show()

plot_total()
