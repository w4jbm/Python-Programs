# Python-Programs

These are various programs written in Python. Some are actually useful (at least to me) while others are just examples of tinkers to see how certaint things work or can be implemented.

## autobins.py

A sample program with a routine that will automatically compute the values needed to divide a list into a given number of bins and plot the result.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/autobins.png "Example of autobins.py")


## filecopy.py

Just a simple, four-line program that copies `infile.txt` to `outfile.txt`, but something I end up using as a starting point fairly frequently. Usually I will add a bit of conditional checking of the input line to pull certain lines from a larger file. (Handy when a command line tool like `sed` isn't around.)


## findbjct.py

Finding Bowdon Junction is a simple program to generate a map and plot two points (Bowdon Junction, GA, where I now live and Owasso, OK, where I grew up). Nothing fancy, but maybe the starting point for something more elaborate down the road.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/findbjct.png "Finding Bowdon Junction")


## mapcnty.py

Create a choropleth centered on Carroll County, GA, with the surrounding counties also colored. Makes use of FIPS codes to identify counties.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/CarrollCountyChoropleth.png "Carroll County Choropleth")


## popbyzip

This directory contains a program that plots a "heat map" of population by zip code. It started with code by James Triveri found here:

http://www.jtrive.com/visualizing-population-density-by-zip-code-with-basemap.html

I had a couple of problems as I worked with it including a few typos and finding a zip code data file (2017 was used in the original, but I was only able to find 2016 and that took a bit of looking). The census boundary zip file should be unzipped after being downloaded here:

http://www2.census.gov/geo/tiger/GENZ2016/shp/cb_2016_us_zcta510_500k.zip

Also, if you don't have mapbase you'll have to install it:

```
pip install --upgrade --user matplotlib numpy pyproj pyshp OWSLib Pillow 
sudo apt-get update 
sudo apt install libgeos-dev 
pip install --user https://github.com/matplotlib/basemap/archive/master.zip
```
After the changes, you should see a result like this:

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/popbyzip/popbyzip.png)


## RingLtLn.py

RingLtLn is a program that generates the latitude and longitude of "rings" at some distance away from a central coordinate.

Sometimes when doing wireless network designs, I find it useful to create these points to quantify coverage.

This program will generate a certain number of rings (set by the variable *rings*) incremented by a certain distance (set by the variable *dist*) around some central point (set by *lat* and *lon*). There are eight coordinates in each ring with azimuths of 0&deg;, 45&deg;, 90&deg;, 135&deg;, 180&deg;, 225&deg;, 270&deg; and 315&deg;.

Typically I will plug these points into one of the various radio frequency (RF) modeling tools I use and create paths from the center point to each point on each ring. Although not as detailed as something like a coverage heatmap, it is sometimes useful to be able to quantify that x% of points would have coverage.


## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2019-2020 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
