import matplotlib.pyplot as plt
import numpy as np
from geopandas import GeoDataFrame
from scipy.cluster.hierarchy import dendrogram
from seaborn import kdeplot, scatterplot

def histogram(z, p, variable):
    figure = plt.figure(figsize=(10, 7))
    classes = np.unique(p)
    q = len(classes)
    figure.suptitle("Histograme pentru variabila " + variable)
    axe = figure.subplots(1, q, sharey=True)
    for i in range(q):
        axe[i].set_xlabel(classes[i])
        axe[i].hist(x=z[p == classes[i]],color="pink", range=(min(z), max(z)), rwidth=0.9)


def plt_distributions(z, p, variable, colors):
    figure = plt.figure(figsize=(10, 7))
    ax = figure.add_subplot(1, 1, 1)
    ax.set_title("Distributii pentru variabila " + variable)
    kdeplot(x=z, hue=p, hue_order=np.unique(p), ax=ax, palette=colors, warn_singular = False)

def plt_hierarchy(h,labels,threshold,title):
    figure=plt.figure(figsize=(10,7))
    ax=figure.add_subplot(1,1,1)
    ax.set_title(title)
    dendrogram(h,labels=labels,color_threshold=threshold,ax=ax)


def plt_partition(z, p, title, labels=None):
    figure = plt.figure(figsize=(10, 7))
    ax = figure.add_subplot(1, 1, 1)
    ax.set_title(title)
    scatterplot(x=z[:, 0], y=z[:, 1], hue=p, hue_order=np.unique(p), ax=ax)
    if labels is not None:
        for i in range(len(labels)):
            ax.text(z[i, 0], z[i, 1], labels[i])


def plt_map(gdf, t, camp_harta, title):
    assert isinstance(gdf, GeoDataFrame)
    gdf_ = gdf.merge(t, left_on='sj', right_index=True)
    figure = plt.figure(figsize=(10, 7))
    ax = figure.add_subplot(1, 1, 1)
    ax.set_title(title, fontdict={"fontsize": 16, "color": "black"})
    gdf_.plot(column=camp_harta, cmap="spring_r", legend=True, ax=ax)

def show():
    plt.show()