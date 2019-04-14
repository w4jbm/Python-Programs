'''
autobins.py
automatically calculate bins
'''

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

def compute_histogram_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = -1.0 * (min_val % desired_bin_size - min_val)
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    bins = np.linspace(min_boundary, max_boundary, n_bins)
    return bins

# Creata a random data set

data = np.random.random_sample(100) * 200.02 - 100.01

# Call the bin computation routine

bins = compute_histogram_bins(data, 10.0)

# Show the results

print("Minimum value was", np.min(data))
print("Maximum value was", np.max(data))
print("The bins are set as follows...")
print(bins)

# And plot the data

plt.hist(data, bins=bins)
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('Automatic Bins Example')
plt.grid(True)
plt.show()
