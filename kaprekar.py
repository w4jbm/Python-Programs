#!/usr/bin/python3
#
# kaprekar.py - Evaluate Number for Kaprekar Constant
#               (or zero or a loop of values)
#
# By Jim McClanahah, W4JBM (Dec 2020)
#
# This program accepts a command line argument of a positive
# integer and will then perform the squence of operations defined
# by Kaprekar in coming up with the Kaprekar Constant for four
# digit numbers.
#
# While four digit numbers are at the heart of defining the
# Kaprekar constant of 6174, other numbers of digits and also
# four digit numbers consisting of a repeated digit (such as
# 1111) all either converge to a constant, a repeating series,
# or to zero.
#
# This program is generalized to handle any of those three
# outcomes.
import sys

# First, define some useful functions.

# Returns an integer with the digits in ascending order...
def nasc(n):
    return int(''.join(sorted(str(n))))

# Returns a string with the digits in ascending order...
def sasc(n):
    return ''.join(sorted(str(n)))

# Returns an integer with the digits in decending order...
def ndsc(n):
    return int(''.join(sorted(str(n))[::-1]))

# The [::-1] starts an operation at the end and works backwards.
# In the case above, the join is done backwards on the sorted
# string.

# Returns a string with the digits in decending order...
def sdsc(n):
    return ''.join(sorted(str(n))[::-1])

# Start with an empty list for results...
lst = []

# Check for command line argument and print an intro if
# none was provided...
if len(sys.argv) != 2:
    print('Find Kaprekar Constant, Zero, or Loop for a '\
          'a given positive integer.')
    print('USAGE: kaprekar.py integer')
    sys.exit(1)

# Make sure the argument is a positive integer...
if sys.argv[1].isdigit():
    n = int(sys.argv[1])

# If not, print a warning...
else:
    print('Argument must be a positive integer.')
    sys.exit(1)

# Introduce ourselves...
print('Evaluating '+str(n)+':\n')

# ...and get things started!
while True:

# Calculate the next number...
    x = ndsc(n) - nasc(n)

# Print the current operation so they know what's going on...    
    print(sdsc(n), "-", sasc(n), "=", x)

# And now push the result so we can use it on the next
# operation...
    n = x

# Let's see if that number is already in our list of results
# so far...
    if n not in lst:

# If not, then add it to the list...
        lst.append(n)
        
# If it is in the list, we're done...
    else:
        if lst.index(n) == len(lst)-1:
        
# If the new calculated value equals the previous
# calculated value, we have settled on a constant...
            lst = [n]
            typ = 'Constant'
            
# ...unless the 'constant' is zero.            
            if n == 0:
                typ = 'zero'
                
# Otherwise, we have a set of values we are looping
# through...
        else:
            typ = 'loop'
            
# Strip out any values prior to starting the loop...
            lst = lst[lst.index(n):]

        break

print('\nKaprekar '+ typ +' reached:', ', '.join(map(str,lst)))

