#!/usr/bin/python3
#
# sum_of_two_cubes.py
# Find a number that can be expressed as a sum of two cubes in two different ways.
#
# Based on the story found here:
# https://www.scientificamerican.com/article/the-most-boring-number-in-the-world-is/
#
# Coded by Jim McClanahan, W4JBM on March 4, 2023
#
# I want to show that 1,729 is indeed that smallest number that is the sum of two
# cubed integers. It does show that:
# 1,729 = 1^3 + 12^3 and 9^3 + 10^3.

# Note: The above assumes only positive integers being cubed, but the
# algorith can handle negative integers. The smallest positive, non-zero
# integer that can be represented by two different sums of cubes is actually:
# 728 = -10^3 + 12^3 and -1^3 + 9^3.

# You do not need to go higher than 20 to find at least two solutions.
i_min = 1
i_max = 25

cube_sums = []

for i1 in range(i_min, i_max):
    for i2 in range(i1+1, i_max):
        for i3 in range(i2+1, i_max):
            for i4 in range(i3+1, i_max):
                i13 = i1**3
                i23 = i2**3
                i33 = i3**3
                i43 = i4**3
#               print(i1,i2,i3,i4)
                if (i13 + i23) == (i33 + i43):
                    cube_sums.append((i13+i23, i1, i2, i3, i4))
                if (i13 + i33) == (i23 + i43):
                    cube_sums.append((i13+i33, i1, i3, i2, i4))
                if (i13 + i43) == (i23 + i33): # I think this is the only case that works
                    cube_sums.append((i13+i43, i1, i4, i2, i3))

print(cube_sums)
