# Plot a set of lat long data from a CSV file.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("./rng_ltln.csv")

BBox = (df.long.min(), df.long.max(), df.lat.min(), df.lat.max())

print(BBox)

