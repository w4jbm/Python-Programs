# Python-Programs

These are various programs written in Python. Some are actually useful (at least to me) while others are just examples of tinkers to see how certaint things work or can be implemented.

From a pure math perspective, three things I have always enjoyed tinkering with is calculating pi to a significant number of digits (the sample here can go to one million digits in less than 30 minutes), calculating e to a significant number of digits (the program here can go to at least 1,000 digits in 20 milliseconds), and calculating large factorials (the program here can calculate 1000! in under a millisecond).


## autobins.py

A sample program with a routine that will automatically compute the values needed to divide a list into a given number of bins and plot the result.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/autobins.png "Example of autobins.py")


## filecopy.py

Just a simple, four-line program that copies `infile.txt` to `outfile.txt`, but something I end up using as a starting point fairly frequently. Usually I will add a bit of conditional checking of the input line to pull certain lines from a larger file. (Handy when a command line tool like `sed` isn't around.)


## findbjct.py

Finding Bowdon Junction is a simple program to generate a map and plot two points (Bowdon Junction, GA, where I now live and Owasso, OK, where I grew up). Nothing fancy, but maybe the starting point for something more elaborate down the road.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/findbjct.png "Finding Bowdon Junction")


## getimg.py

This program uses the Bing search engine and will download the results of an image search. When I'm looking for clip art or an illustrive picture, I have better luck downloading them and picking out one from the local copy of the results. This makes it easier to seperate out things like thumbnails or pictures on sites that aren't going to let you download them. Use is fairly simple:

`./getimg.py blue sportscars`

The program stores the downloaded images in timestamped subdirectories. This can actually be tweaked to do some interesting things like get the top 10 image search results for something like 'fashion hats' (just picking an example) with a cron job and seeing how they change week by week. The number of results and some other parameters can be easily changed.


## mapcnty.py

Create a choropleth centered on Carroll County, GA, with the surrounding counties also colored. Makes use of FIPS codes to identify counties.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/CarrollCountyChoropleth.png "Carroll County Choropleth")


## picrunch.py

One of the things I've tinkered with in various langauges (6502 assembly and BASIC many years ago as well as FORTRAN) is calculating the value of pi out to fairly large numbers of decimal places. I could do a few hundred digits overnight way back when, but always had the desire to calculate it to one million decimal places. I came across a Python program that did just that.

That program looked like it might have started life under Python2 but ran fine under Python3. I made some minor changes including adding a timer to the program. The results are dumped to a file. You can also specify an arbitrary number of decimal places to calculated out to. It also takes command line arguements and was the first Python program where I had worked with that feature--it's something I expect will be handy.

To run the program, just type:

```./picrunch.py 1000000 pi.txt```

That will run one million digits out to a text file and take a while (around a half hour on my machine) to execute.


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


## Prime Numbers

Just about anyone who has worked with a number of programming languages will say that Python is more finicky about spacing and whitespace than many other languages. This can lead to confusion if spaces are lost or get out of whack along the way. There is a fairly popular site that contained the following example of how prime numbers could be generated:

```
for x in range(1,101):
for y in range(2,x):
if x%y==0:break
else:
print (x,sep=' ', end=' ')
```

The output was supposed to show a list of primes, but it doesn't work because of indentation issues. Going in, I knew that the whitespace had disappeared somewhere along the path. I'll admit that it was finding the proper whitespace related to the ```else``` and ```print``` statements that took some thinking before I finally settled on the following:

```
for x in range(1,101):
    for y in range(2,x):
        if x%y==0:break
    else:
        print (x, sep=' ', end=' ')
```

With this, you will get the following output:

```1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 ```

The plethera of online examples, some of which are right and some of which are wrong, turns out to be both a strength and weakness for people 


## pye.py

This program calculates Euler's number (e) out to at least 1,000 decimal places. I haven't verified the results past that but it is definately fast enough (taking well under 20 milliseconds at this point) to push that out further.

You get a warning if you go beyond 1,000 places and there are "check values" you can print out for 100 and 1,000 places.


## pyfact.py

This program accepts a command line argument and calculates the factorial of it. Years ago a friends nephew was given the assignment of calculate 100! (although it was worded along the lines of "multiply all of the numbers between 1 and 100 together"). It was a homework bonus question.

I quickly hacked together a BASIC program to calculate it using regular floating point math, but the teacher then said that all digits needed to be shown. (There are 158 digits in 100!.) I hacked together another BASIC program using an array to hold integer values.

But I have to admit it was much easier to do in Python using arbitary length integers. (And it runs much faster than it did on my PC in the mid-1990s.)


## rbow.py, helix,py, and square.py

Some tinkering with turtle graphics.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/rbow.jpg)


## RingLtLn.py, PBndBx.py, and Map_Ring.py

RingLtLn is a program that generates the latitude and longitude of "rings" at some distance away from a central coordinate.

Sometimes when doing wireless network designs, I find it useful to create these points to quantify coverage.

This program will generate a certain number of rings (set by the variable *rings*) incremented by a certain distance (set by the variable *dist*) around some central point (set by *lat* and *lon*). There are eight coordinates in each ring with azimuths of 0&deg;, 45&deg;, 90&deg;, 135&deg;, 180&deg;, 225&deg;, 270&deg; and 315&deg;.

Typically I will plug these points into one of the various radio frequency (RF) modeling tools I use and create paths from the center point to each point on each ring. Although not as detailed as something like a coverage heatmap, it is sometimes useful to be able to quantify that x% of points would have coverage.

You can copy these into a text file to create a .csv file for import to other tools. To show the results, you can use PBndBx.py to print the boundary of the lat/long data and the export a map in .png format to use as a background from:

 https://www.openstreetmap.org/
 
 Tweak the boundary settings in Map_Ring.py and you can plot the results on a map that looks something like this:
 
![alt text](https://github.com/w4jbm/Python-Programs/raw/master/ring.png)
 

## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2019-2020 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
