#!/usr/bin/python3
#
# By Jim McClanahan, W4JBM (Dec 2020)...
# I originally came across this puzzle and the initial solution at:
#
# http://rosettacode.org/wiki/McNuggets_problem
#
# From Wikipedia:
# The McNuggets version of the coin problem was introduced by Henri
# Picciotto, who included it in his algebra textbook co-authored with
# Anita Wah. Picciotto thought of the application in the 1980s while
# dining with his son at McDonalds, working the problem out on a napkin.
#
# A McNugget number is the total number of McDonalds Chicken McNuggets
# in any number of boxes.
#
# In the United Kingdom, the original boxes (prior to the introduction
# of the Happy Meal-sized nugget boxes) were of 6, 9, and 20 nuggets.
#
# Task:
# Calculate (from 0 up to a limit of 100) the largest non-McNuggets
# number (a number n which cannot be expressed with 6x + 9y + 20z = n
# where x, y and z are natural numbers).
#

from itertools import product

mnmx = 100

print('Searching for McNugget Numbers up to', mnmx)

nuggets = set(range(mnmx+1))

for mn6, mn9, mn20 in product(range(mnmx//6+1), range(mnmx//9+1), range(mnmx//20+1)):
    nuggets.discard(6*mn6 + 9*mn9 + 20*mn20)
 
print('Maximum McNugget Number found was', max(nuggets))

