import numpy as np
import matplotlib.pyplot as plt
from common import *

# Tip: Use np.loadtxt to load data into an array
K = np.loadtxt('../data/task2K.txt')
X = np.loadtxt('../data/task3points.txt')


T = T_z(6)@R_x(15)@R_y(45)
draw_frame(K,T)
X = T@X


u,v = project(K, X)

# You would change these to be the resolution of your image. Here we have
# no image, so we arbitrarily choose a resolution.
width,height = 600,400



plt.scatter(u, v, c='black', marker='.', s=20)

# The following commands are useful when the figure is meant to simulate
# a camera image. Note: these must be called after all draw commands!!!!

plt.axis('image')     # This option ensures that pixels are square in the figure (preserves aspect ratio)
                      # This must be called BEFORE setting xlim and ylim!
plt.xlim([0, width])
plt.ylim([height, 0]) # The reversed order flips the figure such that the y-axis points down
plt.savefig("t3")
plt.show()
