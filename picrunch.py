#!/usr/bin/env python3
#
# Original picrunch.py by Don Cross
#
# A bit of cleanup for P3 style and included timer
# in the code by Jim McClanahan W4JBM.
#
# Originally suggestion was to use 'time' command
# to invoke the program. That gives a more accurate
# view of real processor time, but the integrated
# timer makes it easier to tinker with.
#
# File write has been pulled out of timer so it is
# time to calculate and does not include the write
# to disk time.
#
# This approaches uses Machin's Formula:
#
#   pi = 4*(4*arctan(1/5) - arctan(1/239))
#
# to calculate pi to an arbitrary number of decimal
# places.
#

import sys
import time

def ArctanDenom(d, ndigits):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**ndigits) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d*d
        total += term // (2*n + 1)
    print('ArctanDenom({}) took {} iterations.'.format(d, n))
    return total

if len(sys.argv) != 3:
    print('USAGE: picrunch.py ndigits outfile')
    sys.exit(1)

xdigits = 10             # Extra digits to reduce trailing error
ndigits = int(sys.argv[1])
outFileName = sys.argv[2]

start_time = time.time()

# Use Machin's Formula to calculate pi.
pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))

# We calculated extra digits to compensate for roundoff error.
# Chop off the extra digits now.
pi //= 10**xdigits

print('Calculation time was {:f} seconds.'.format(time.time() - start_time))

# Write the result to a text file.
with open(outFileName, 'wt') as outfile:
    # Insert the decimal point after the first digit '3'.
    text = str(pi)
    outfile.write(text[0] + '.' + text[1:] + '\n')


print('Results written to {}.'.format(outFileName))
sys.exit(0)

