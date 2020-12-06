#!/usr/bin/python3
#
# largeprime.py - Generate a 1024 bit large prime number
#
# Based on code by Antoine Prudhomme found at:
#
# https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
#
# Minor tweaks and modifications by Jim McClanahan, W4JBM (Dec 2020)
from random import randrange, getrandbits

############################################
# This function uses a combination of deterministic and probabilistic
# methods to determ if n is prime.
def is_prime(n, k=128):

# Some trivial cases first:
# If n is 2 or 3, then it is a prime number    
    if n == 2 or n == 3:
        return True

# If n is <=1 or if it is an even number (>2 at this point),
# then it is not a prime number
    if n <= 1 or n % 2 == 0:
        return False

#Now it's time to pull out the heavy artilery: Miller-Rabin
#
# To start, we find r and s where (n-1) = r*(2^s), with r odd
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

# Now for the tests! We do k itterations of the test because
# it is probabalistic. It can give us an indication ('witness')
# that the number is composite (and not a prime).
#
# We will pick an integer in the range [2, n-1] and then:
# If a^r != 1 (mod n) and a^((2^j)r) != -1 (mod n) for all j such
#     that 0 ≤ j ≤ s-1, then n is not prime and a is called a
#     witness to compositeness for n.
# On the other hand, if a^r = 1 (mod n) or a^((2^j)r) = -1 (mod n)
#     for some j such as 0 ≤ j ≤ s-1, then n is said to be a
#     pseudo-prime to the base a, and a is called a strong liar.
#
# We can get a good indication when something is a composite,
# but lack certainty that something is a prime. By running thru
# this k times, we can be more certain that we have a true prime
# number n.
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


############################################
# This function generates a prime number candidate given a
# length in bits. The MSB is always set to 1 to make the
# number as large as possible and the LSB is always set to
# 1 to make the number odd (since all even numbers >2 are
# not primes.
def generate_prime_candidate(length):

# Generate random bits for the proper length
    p = getrandbits(length)
    
# Apply a mask to set the MSB and the LSB to 1
    p |= (1 << length - 1) | 1

# And return it from the function
    return p


############################################
# This function combines the two above by generating a candidate
# number and checking to see if it is a prime. If it is not, then
# we pick another candidate number and test it until we do find
# a prime.
def generate_prime_number(length=1024):
    p = 4 # set p to a dummy number that is a prime 

# While p is not a prime, keep generating candidates and testing 
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


# All that is left is to call the functions and print the results.
print('Generating a 1024 bit prime number (this may take a few seconds):')
print(generate_prime_number())

