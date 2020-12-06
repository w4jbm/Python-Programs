#!/usr/bin/python3
#
# factors.py - Find the factors of a positive integer
#
# By Jim McClanahah, W4JBM (Dec 2020)
#
# Find the factors of a provided positive integer.
#
# The function is a modification of one originally
# provided by Harshit Agrawal to the geeksforgeeks.org
# website.
#
# It seems like things stop working at around 18 digits

import sys
import math

# The following function creates and return a list of all
# prime factors of a given number n 
#
# It uses three steps to find o find all prime factors:
#
# 1. While n is divisible by 2, add two to the list and
#    divide n by 2.
# 2. After step 1, n must be odd. Now start a loop from
#    i = 3 to square root of n. While i divides n, add
#    i to the list and divide n by i, increment i by 2
#    and continue.
# 3. If n is a prime number and is greater than 2, then
#    n will not become 1 by above two steps. So add n
#    to the list if it is greater than 2.

def primeFactors(n): 
    lst=[]      
    # Find the number of two's that divide n 
    while n % 2 == 0: 
        lst.append(2)
        n = n / 2
          
    # n must be odd at this point so a skip of 2
    # (i.e., i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , add i to list and
        # divide n 
        while n % i== 0:
            lst.append(i) 
            n = n / i 
              
    # Check if n is a prime number greater than 2 
    if n > 2: 
        lst.append(int(n))

    # And return the list of factors
    return lst

# Check for command line argument and print an intro if
# none was provided...
if len(sys.argv) != 2:
    print('Find the factors for a given positive integer.')
    print('USAGE: factor.py integer')
    sys.exit(1)

# Make sure the argument is a positive integer...
if sys.argv[1].isdigit():
    n = int(sys.argv[1])

# If not, print a warning...
else:
    print('Argument must be a positive integer.')
    sys.exit(1)

if n > 10**16:
    print('Argument cannot be more than 15 digits.')
    sys.exit(1)

lst = primeFactors(n)

# Here's where all the work happens... :-)
print('Factors of ' + str(n) + ': ' + ', '.join(map(str,lst)))

