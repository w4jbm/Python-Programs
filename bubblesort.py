#!/usr/bin/python3
#
# Create and Demonstrate bubble sort function in Python
#
# June 2022, Jim McClanahan W4JBM

import numpy as np

def bubble_sort(nlist):
    for i in range(len(nlist)-1,0,-1):
        for j in range(i):
            if nlist[j] > nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]

#num_list = [73,2,19,22,21,8,19]
num_list = list(np.random.randint(low=1, high=101, size=10))

print("Original List:")
print(num_list)
bubble_sort(num_list)
print("\nSorted List:")
print(num_list)
print("\nReverse Sorted List:")
print(num_list[::-1])
