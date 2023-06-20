from matplotlib import pyplot as plt


def plot_cluster(raster, cluster_band):
    
    #Create Plot
    fig, axs = plt.subplots(1, 2, figsize=(20, 10), sharey=True)

    #Plot RGB left
    raster.plot_multiple_bands(["red", "green", "blue"], ax=axs[0])
    axs[0].set_title("RGB")

    #Plot Cluster right
    raster.plot_band(cluster_band, colormap="hsv", ax=axs[1])
    axs[1].set_title(cluster_band)
