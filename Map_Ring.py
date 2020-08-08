# Plot a set of lat long data from a CSV file.
#
# Expport map from:
#      https://www.openstreetmap.org/
#
# Use box boundaries given by PBndBx.py as a guide,
# but enter actual boundaries used below.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("./rng_ltln.csv")

BBox = (-85.18, -85.10, 33.69, 33.63)

# Point to exported map image
my_m=plt.imread("map.png")

# and plot to points
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.long, df.lat, zorder=1, alpha= 0.2, c='red', s=10, marker='s')

#
ax.set_title('Ring Plotted on Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(my_m, zorder=0, extent = BBox, aspect= 'equal')

plt.show()

