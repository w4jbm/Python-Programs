# Python-Programs

These are various programs written in Python. Some are actually useful (at least to me) while others are just examples of tinkers to see how certaint things work or can be implemented.

## findbjct.py

Finding Bowdon Junction is a simple program to generate a map and plot two points (Bowdon Junction, GA, where I now live and Ovwasso, OK, where I grew up). Nothing fancy, but maybe the starting point for something more elaborate down the road.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/findbjct.png "Finding Bowdon Junction")


## RingLtLn.py

RingLtLn is a program that generates the latitude and longitude of "rings" at some distance away from a central coordinate.

Sometimes when doing wireless network designs, I find it useful to create these points to quantify coverage.

This program will generate a certain number of rings (set by the variable *rings*) incremented by a certain distance (set by the variable *dist*) around some central point (set by *lat* and *lon*). There are eight coordinates in each ring with azimuths of 0&deg;, 45&deg;, 90&deg;, 135&deg;, 180&deg;, 225&deg;, 270&deg; and 315&deg;.

Typically I will plug these points into one of the various radio frequency (RF) modeling tools I use and create paths from the center point to each point on each ring. Although not as detailed as something like a coverage heatmap, it is sometimes useful to be able to quantify that x% of points would have coverage.


## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2019 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
