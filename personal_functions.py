
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import random


''' Plotting Functions '''

def stacked_bar(bar_mtx, labels, colors = ['#348abd', '#7a68a6', '#a60628', '#467821', '#cf4457', '#188487', '#e24a33']):
    ''' create stacked bar chart with matrix - rows as bars '''
    num_bars = bar_mtx.shape[1]
    num_colors = len(colors)
    start = 0
    for idx, i in enumerate(bar_mtx):
        color_idx = idx - ((idx/num_colors)*num_colors)
        plt.bar(np.arange(num_bars), i, bottom = start, color = colors[color_idx], label = labels[idx])
        start += i
    plt.legend()
    plt.show()

''' PCA FUNCTIONS '''

def scree_plot(num_components, pca):
    ind = np.arange(num_components)
    vals = pca.explained_variance_ratio_
    plt.figure(figsize=(10, 6), dpi=250)
    ax = plt.subplot(111)
    ax.bar(ind, vals, 0.35, 
           color=[(0.949, 0.718, 0.004),
                  (0.898, 0.49, 0.016),
                  (0.863, 0, 0.188),
                  (0.694, 0, 0.345),
                  (0.486, 0.216, 0.541),
                  (0.204, 0.396, 0.667),
                  (0.035, 0.635, 0.459),
                  (0.486, 0.722, 0.329),
                 ])

    ax.annotate(r"%d%%" % (int(vals[0]*100)), (ind[0]+0.2, vals[0]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%d%%" % (int(vals[1]*100)), (ind[1]+0.2, vals[1]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%d%%" % (int(vals[2]*100)), (ind[2]+0.2, vals[2]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%d%%" % (int(vals[3]*100)), (ind[3]+0.2, vals[3]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%d%%" % (int(vals[4]*100)), (ind[4]+0.2, vals[4]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%d%%" % (int(vals[5]*100)), (ind[5]+0.2, vals[5]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%s%%" % ((str(vals[6]*100)[:4 + (0-1)])), (ind[6]+0.2, vals[6]), va="bottom", ha="center", fontsize=12)
    ax.annotate(r"%s%%" % ((str(vals[7]*100)[:4 + (0-1)])), (ind[7]+0.2, vals[7]), va="bottom", ha="center", fontsize=12)

    ax.set_xticklabels(ind, 
                       fontsize=12)
    ax.set_yticklabels(('0.00', '0.05', '0.10', '0.15', '0.20', '0.25'), fontsize=12)
    ax.set_ylim(0, .25)
    ax.set_xlim(0-0.45, 8+0.45)

    ax.xaxis.set_tick_params(width=0)
    ax.yaxis.set_tick_params(width=2, length=12)

    ax.set_xlabel("Principal Component", fontsize=12)
    ax.set_ylabel("Variance Explained (%)", fontsize=12)

    plt.title("Scree Plot for the Digits Dataset", fontsize=16)


def plot_embedding(X, y, title=None):
    # X is feature matrix with PCA components
    # y is labels of each data point in feature matrix
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure(figsize=(10, 6), dpi=250)
    ax = plt.subplot(111)
    ax.axis('off')
    ax.patch.set_visible(False)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(y[i]), color=plt.cm.Set1(y[i] / 10.), fontdict={'weight': 'bold', 'size': 12})

    plt.xticks([]), plt.yticks([])
    plt.ylim([-0.1,1.1])
    plt.xlim([-0.1,1.1])

    if title is not None:
        plt.title(title, fontsize=16)

'''
Distance FUNCTIONS
'''

def euclidean_distance(np1, np2):
    #returns vertical array
    np_diff_squared = (np1 - np2)**2
    np_hyp_squared = np_diff_squared.sum(axis = 1)
    return np.sqrt(np_hyp_squared).reshape(len(np_hyp_squared),1)

def main():
    pass

if __name__ == '__main__':
    main()