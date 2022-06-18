#!/usr/bin/python3
#
# Demonstrate use of watchpoints package used for troubleshooting
# Python programs.
#
# June 2022, Jim McClanahan W4JBM
#
# Requires installation of watchpoints:
#   $ python3 -m pip install watchpoints

from watchpoints import watch

def dummy_function(y):
    global x
    x = 99
    return y

print("Setting variable x to zero.\n")
x=0

print("Enabling watch for variable x.\n")
watch(x)

print("Now Incrementing x.\n")
x += 1

print("\nNow calling function with x as a global variable.\n")

dummy_function(0)

print("\nNow change variable inside a print function.\n")

print({exec('x=-1'):x}[None])

print("\nNow doing the same thing in a little different way.\n")

exec('x=-9;print(x)')

print("\nNow going to delete the variable...\n")

del x

print("...then try to print it and throw an error.\n")

print(x)
