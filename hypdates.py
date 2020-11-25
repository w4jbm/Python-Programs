#!/usr/bin/python3
#
# hypdates.py - Hypotenuse Dates
#
# By Jim McClanahan, W4JBM (November 2020)
#
# Inspired by a C program by T A Gibson
# which was shared by Lee Bradley (Not Just Tiny-C)
#
# Hypotenuse dates are dates whose values could be used
# as lengths of sides to form a right triangle.
#
# We will need the math library for square roots...
import math

# The smallest year we need to consider would be larger than
# SQRT(1^2 + 1^2) (January 1st of a year), so we can start
# at 2.
#
# The largest year we need to consider would be smaller than
# SQRT(12^2 + 31^2) (December 31st of a year), so we can end
# at 33.
#
# The year should always be the "long" side of the triange,
# so month runs from 1 to the smaller of 12 or the year.
for y in range(2,34):
    for m in range(1,min(13,y)):
        d = math.sqrt(y*y - m*m)
        if d==int(d):
            print(m, int(d), y, sep='-')

