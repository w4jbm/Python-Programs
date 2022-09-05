#!/usr/bin/python3
#
# A math puzzle answering the question, "What percentage of all integers have
# a factor below some limit?"
#
# For example, "What percentage of all integer have a factor under 100?"
#
# The article that inspired this is found here:
# https://www.datasciencecentral.com/88-per-cent-of-all-integers-have-a-factor-under-100/
#
# This code uses a "brute force" method to test numbers between the product
# of all primes up to (2x less 1) of that same product. The frequency of numbers
# having factors will be repeatative after that. This can take significant time
# to complete for inputs higher than 23 (which includes primes up to 19).

import sys
import numpy as np

# Return an array of primes from 2 up to one below limit provided
# (that is, 2<= values in array < argument
#
# From Robert Williams Hank at:
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

LIMIT=6 # Have a default value if no argument is provided

# Do we have an argument on the command line?
if(len(sys.argv)) == 1:
    print("You can enter the limit you wish to evaluate as an argument.")
else:
    LIMIT = int(sys.argv[1])

print("Determining what percent of integers have at least one factor below", LIMIT)

PRIMES = primesfrom2to(LIMIT)

print()
print("Prime numbers below",LIMIT)
print(PRIMES)

UPPER = 1
for i in PRIMES:
    NEW_INT = i
    UPPER = UPPER * int(i)  # int() prevents overflow
#   print(i, UPPER)

print("Product of all primes is", UPPER)

count = 0
divisible = 0

for i in range(UPPER, UPPER*2):
    count += 1
    for j in PRIMES:
        if i%j == 0:
            divisible += 1
            break

calc_prob = 100 * divisible / count
disp_prob = "{:.3f}".format(calc_prob)

print()
print("Found that", divisible, "out of", count, "were divisible by primes less than", LIMIT)
print("That is", disp_prob, "percent")
    

