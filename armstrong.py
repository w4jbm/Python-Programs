#!/usr/bin/python3
#
# armstrong.py - Armstrong Numbers
#
# By Jim McClanahan, W4JBM (November 2020)
#
# An Armstrong Number has the property of equaling
# the sum of its individual digits raised to the
# power of the number of digits.
#
# Some examples include:
# 7 = 7^1
# 371 = 3^3 + 7^3 + 1^3
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
#
# These numbers are also referred to a Narcissistic
# Numbers.
#
# What range do we want to look at?
for x in range(0,100000):

# How many digits does the number have?
    ndig = len(str(x))

# Get ready to sum the power of the digits...
    sum = 0

# Now we go through each digit of the number...
    temp = x
    while temp > 0:
        dig = temp % 10
        sum += dig ** ndig
        temp //= 10

# display the result
    if sum == x:
        print(x, 'is an Armstrong number.')

