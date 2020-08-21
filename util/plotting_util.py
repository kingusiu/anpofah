import matplotlib.pyplot as plt
from matplotlib import colors
import os

import anpofah.util.data_preprocessing as dpr


def plot_hist(data, bins=100, xlabel='x', ylabel='num frac', title='histogram', plot_name='plot', fig_dir=None, legend=[],ylogscale=True, normed=True, ylim=None, legend_loc='best', xlim=None):
    fig = plt.figure(figsize=(6, 4))
    plot_hist_on_axis(plt.gca(), data, bins=bins, xlabel=xlabel, ylabel=ylabel, title=title, legend=legend, ylogscale=ylogscale, normed=normed, ylim=ylim, xlim=xlim)
    if legend:
        plt.legend(loc=legend_loc)
    plt.tight_layout()
    if fig_dir is not None:
        fig.savefig(os.path.join(fig_dir, plot_name + '.png'))
    else:
        plt.show();
    plt.close()


def plot_hist_on_axis(ax, data, bins, xlabel, ylabel, title, legend=[], ylogscale=True, normed=True, ylim=None, xlim=None):
    if ylogscale:
        ax.set_yscale('log', nonposy='clip')
    counts, edges, _ = ax.hist(data, bins=bins, normed=normed, histtype='step', label=legend)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    if ylim:
        ax.set_ylim(ylim)
    if xlim:
        ax.set_xlim(xlim)


def plot_hist_2d( x, y, xlabel='x', ylabel='num frac', title='histogram', plot_name='hist2d', fig_dir=None, legend=[],ylogscale=True, normed=True, ylim=None, legend_loc='best', xlim=None, clip_outlier=False):
    
    if clip_outlier:
        idx = dpr.is_outlier_percentile(x) | dpr.is_outlier_percentile(y)
        x = x[~idx]
        y = y[~idx]

    fig = plt.figure()
    ax = plt.gca()
    im = plot_hist_2d_on_axis( ax, x, y, xlabel, ylabel, title )
    fig.colorbar(im[3])
    plt.tight_layout()
    if fig_dir:
        plt.savefig(os.path.join(fig_dir,plot_name+'.png'))
    plt.show()
    #plt.close()
    return ax
    
    
def plot_hist_2d_on_axis( ax, x, y, xlabel, ylabel, title ):
    im = ax.hist2d(x, y, bins=100, norm=colors.LogNorm())
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return im
