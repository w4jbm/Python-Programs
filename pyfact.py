#!/usr/bin/env python3
#
# pyfact.py -- Calculate Large Factorials
#
# By Jim McClanahan W4JBM.
#
#

import sys
import time

if len(sys.argv) != 2:
    print('Calculate Large Factorials')
    print('USAGE: pyfact.py ndigits')
    sys.exit(1)

ndigits = int(sys.argv[1])

start_time = time.time()

r = 1
for i in range (1, ndigits + 1):
	r *= i

print('Calculation time was {:f} seconds. Result is:\n'.format(time.time() - start_time))

print(r)

sys.exit(0)

