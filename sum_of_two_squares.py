#!/usr/bin/python3
#
# Modified sum_of_two_cubes.py to look at squares, not cubes.
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

# For squares, 5 = 1^2 + 2^2 and you can change the signs to make this be the
# smallest result when looking at range like -10 to +10.
#
# For only positive, non-zero integers, 65 = 1^2 + 8^2 and 4^2 + 7^2. The
# next second highest is 85 = 2^2 + 9^2 and 6^2 + 7^2.

i_min = 1
i_max = 20

square_sums = []

for i1 in range(i_min, i_max):
    for i2 in range(i1+1, i_max):
        for i3 in range(i2+1, i_max):
            for i4 in range(i3+1, i_max):
                i12 = i1**2
                i22 = i2**2
                i32 = i3**2
                i42 = i4**2
#               print(i1,i2,i3,i4)
                if (i12 + i22) == (i32 + i42):
                    square_sums.append((i12+i22, i1, i2, i3, i4))
                if (i12 + i32) == (i22 + i42):
                    square_sums.append((i12+i32, i1, i3, i2, i4))
                if (i12 + i42) == (i22 + i32): # I think this is the only case that works
                    square_sums.append((i12+i42, i1, i4, i2, i3))

sorted_squares = sorted(square_sums)
print(*sorted_squares, sep='\n')
