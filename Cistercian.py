#!/usr/bin/python3
#
# By Jim McClanahan, W4JBM (March 2023)...

# Given a integer between 0 and 9999 from the command line, this
# program will generate the Cistercian representation of that number.
#
# The results are exported to a *.png file tied to the number.

import sys
import os
import time
import tkinter as tk
from PIL import Image
from PIL import ImageGrab
import turtle

# Takes a png screenshot of a tkinter window, and saves it on in cwd
# with the filename passed as argument
def dump_gui(filenm):
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save(filenm)

# Check the command line arguements
if len(sys.argv) != 2:
    print('Graph the Cistercian Number representation for a positive integer.')
    print('USAGE: Cistercian.py integer')
    sys.exit(1)

# Make sure the argument is a four (or less) digit positive integer...
if sys.argv[1].isdigit():
    n = int(sys.argv[1])

# If not, print a warning...
else:
    print('Argument must be a non-negative integer.')
    sys.exit(1)

if n >= 10**4:
    print('Argument cannot be more than 4 digits.')
    sys.exit(1)

# Seperate out the four digits (no leading zeros needed)    
d1 = n%10
d2 = int((n%100)/10)
d3 = int((n%1000)/100)
d4 = int((n%10000)/1000)
# print(d4,d3,d2,d1)

# Prep to plot on canvas using turtle graphics
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)

# Draw the vertical line we base things off of
t.penup()
t.width(3)
t.goto(0,200)
t.pendown()
t.goto(0,-100)
t.penup()

# Process the 1s value...
if (d1==1) or (d1==5) or (d1==7) or (d1==9):
    t.goto(0,200)
    t.pendown()
    t.goto(100,200)
    t.penup()

if (d1==2) or (d1==8) or (d1==9):
    t.goto(0,100)
    t.pendown()
    t.goto(100,100)
    t.penup()

if (d1==3):
    t.goto(0,200)
    t.pendown()
    t.goto(100,100)
    t.penup()

if (d1==4) or (d1==5):
    t.goto(0,100)
    t.pendown()
    t.goto(100,200)
    t.penup()

if (d1>5):
    t.goto(100,200)
    t.pendown()
    t.goto(100,100)
    t.penup()

# Process the 10s value...
if (d2==1) or (d2==5) or (d2==7) or (d2==9):
    t.goto(0,200)
    t.pendown()
    t.goto(-100,200)
    t.penup()

if (d2==2) or (d2==8) or (d2==9):
    t.goto(0,100)
    t.pendown()
    t.goto(-100,100)
    t.penup()

if (d2==3):
    t.goto(0,200)
    t.pendown()
    t.goto(-100,100)
    t.penup()

if (d2==4) or (d2==5):
    t.goto(0,100)
    t.pendown()
    t.goto(-100,200)
    t.penup()

if (d2>5):
    t.goto(-100,200)
    t.pendown()
    t.goto(-100,100)
    t.penup()

# Process the 100s value...
if (d3==1) or (d3==5) or (d3==7) or (d3==9):
    t.goto(0,-100)
    t.pendown()
    t.goto(100,-100)
    t.penup()

if (d3==2) or (d3==8) or (d3==9):
    t.goto(0,0)
    t.pendown()
    t.goto(100,0)
    t.penup()

if (d3==3):
    t.goto(0,-100)
    t.pendown()
    t.goto(100,0)
    t.penup()

if (d3==4) or (d3==5):
    t.goto(0,0)
    t.pendown()
    t.goto(100,-100)
    t.penup()

if (d3>5):
    t.goto(100,0)
    t.pendown()
    t.goto(100,-100)
    t.penup()

# Process the 1000s value...
if (d4==1) or (d4==5) or (d4==7) or (d4==9):
    t.goto(0,-100)
    t.pendown()
    t.goto(-100,-100)
    t.penup()

if (d4==2) or (d4==8) or (d4==9):
    t.goto(0,0)
    t.pendown()
    t.goto(-100,0)
    t.penup()

if (d4==3):
    t.goto(0,-100)
    t.pendown()
    t.goto(-100,0)
    t.penup()

if (d4==4) or (d4==5):
    t.goto(0,0)
    t.pendown()
    t.goto(-100,-100)
    t.penup()

if (d4>5):
    t.goto(-100,0)
    t.pendown()
    t.goto(-100,-100)
    t.penup()

# Puts a label at the bottom of the graph for reference)
t.goto(0,-240)
t.write(str(n),align='center',font=('LM Mono Prop 10',36,'bold'))
t.goto(150,-250)
t.write('W4JBM',align='right',font=('Arial',14,'normal'))

# Hide the turtle as we capture and save the image
t.hideturtle()

# Using a postscript file is possible directly from the turtle
# library, but scaling issues make the resulting png file look
# pixelated. A kludge is to capture a shot of the canvas using
# the dump_gui() function

# ps_filename = 'Cistercian_' + str(n) + '.ps'
png_filename = 'Cistercian_' + str(n) + '.png'


# canvas.postscript(file=ps_filename)

# psimage = Image.open(ps_filename)
# psimage.save(png_filename, quality=95)
# os.remove(ps_filename)

dump_gui(png_filename)

# Keep the image on screen so we can admire the results of our efforts
time.sleep(5)
