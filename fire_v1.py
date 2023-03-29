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

def update_forest(forest, p_grow, p_ignite, p_immune):
    """Updates the forest according to the given probabilities."""
    N, M = forest.shape
    new_forest = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            if forest[i,j] == 2:
                new_forest[i,j] = 0
                # Check if neighbors can catch fire
                if i > 0 and forest[i-1,j] == 1 and np.random.random() < p_ignite:
                    new_forest[i-1,j] = 2
                if i < N-1 and forest[i+1,j] == 1 and np.random.random() < p_ignite:
                    new_forest[i+1,j] = 2
                if j > 0 and forest[i,j-1] == 1 and np.random.random() < p_ignite:
                    new_forest[i,j-1] = 2
                if j < M-1 and forest[i,j+1] == 1 and np.random.random() < p_ignite:
                    new_forest[i,j+1] = 2
                # Probability of turning immune
                if np.random.random() < p_immune:
                    new_forest[i,j] = 3
            elif forest[i,j] == 1:
                new_forest[i,j] = 1
                # Probability of tree growth
                if np.random.random() < p_grow:
                    new_forest[i,j] = 2
            else:
                new_forest[i,j] = 0
    return new_forest

def run_simulation(N, T):
    """Runs the simulation and returns the frames for animation."""
    forest = initialize_forest(N, N)
    frames = []
    
   # colors_list = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]

    # Define the colors for visualization
    colors_list = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
    cmap = ListedColormap(colors_list)
    
    # Define the probabilities of tree growth, tree ignition, and immunity
    p_grow = 0.01
    p_ignite = 0.1
    p_immune = 0.1
    
    # Create the initial plot
    fig, ax = plt.subplots()
    im = ax.imshow(forest, cmap=cmap, interpolation='none')
    plt.axis('off')
    
    # Run the simulation for T time steps
    for t in range(T):
        forest = update_forest(forest, p_grow, p_ignite, p_immune)
        im.set_array(forest)
        frames.append([im])
    
    # Animate the simulation
    ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True, repeat_delay=1000)
    plt.show()
    return ani
run_simulation(50, 100)