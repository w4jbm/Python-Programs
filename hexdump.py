#!/usr/bin/python3
#
# hexdump.py - Produce a hex dump of a file
#
# USAGE: ./hexdump.py filename.ext
#
# Tweaks and edits by Jim McClanahan, W4JBM (Dec 2020)
#
# Starting point was a Python 2 program by Ruby Devices (2017)

import sys
import os.path

def valid_file():
# This method checks whether a valide file name was provided
    if (len(sys.argv) < 2):
        print("Hex Dump")
        print("USAGE: ./hexdump.py <filename>")
        sys.exit(0)
    if not os.path.isfile(sys.argv[1]):
        print("Error! File does not exist.")
        sys.exit(0)
  
def read_bytes(filename, chunksize=8192):
# This function reads the file contents a chunk at a time
    try:
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        yield b
                else:
                    break
    except IOError:
        print("Error while reading file!")
        sys.exit(0)
  
def print_header():
# This method prints the headers at the top of the dump
    print(" Addr    0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F")

  
def printable_byte(byte):
# Check byte and make sure we have a printable ascii character.
    # I have always just used the lower seven bits since my first
    # hex dump program back in 1980 and I'm too old to change now.
    # If you don't want to mask off Bit 7, comment the next line
    # out and change the if statement to catching anything >127.
    byte = byte & 127
    # If byte isn't printable (less than 'space'), then return a
    # period or dot.
    if (byte < 32):
        return(46)
    # Otherwise it has had the eighth bit stripped and should be
    # printable, so let's pass it back now.
    else:
        return(byte)
  
## main ##
valid_file()
memory_address = 0
ascii_string = ''
print_header()

## Loop through the given file while printing the address, hex and ascii output ##
for byte in read_bytes(sys.argv[1]):
    ascii_string = ascii_string + chr(printable_byte(byte))
    if memory_address%16 == 0:
        print(format(memory_address, '06X'), end ='  ')
        print(format(byte, '02X'), end =' ')
    elif memory_address%16 == 15:
        print(format(byte, '02X'),  end ='  ')
        print(ascii_string)
        ascii_string = ''
    else:
        print(format(byte, '02X'), end =' ')
        if memory_address%16 == 7:
            print(' ', end ='')
    memory_address = memory_address + 1

fill_line = len(ascii_string)
if (fill_line == 0) or (fill_line == 16):
    exit()

while fill_line < 16:
    print('  ', end = ' ')
    if fill_line%8 == 0:
        print(' ', end ='')
    fill_line = fill_line + 1

print(' ' + ascii_string)

