import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
from matplotlib.colors import ListedColormap

def initialize_forest(N, M):
    """Initializes the forest with a random distribution of trees, empty sites, and an ignition source."""
    forest = np.zeros((N, M))
    # Add trees with probability 0.6
    forest[np.random.random(size=(N,M)) < 0.6] = 1
    # Add an ignition source at the center
    cx, cy = N//2, M//2
    forest[cx, cy] = 2
    return forest