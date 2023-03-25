# Python-Programs

These are various programs written in Python. Some are actually useful (at least to me) while others are just examples of tinkers to see how certaint things work or can be implemented.

From a pure math perspective, three things I have always enjoyed tinkering with is calculating pi to a significant number of digits (the sample here can go to one million digits in less than 30 minutes), calculating e to a significant number of digits (the program here can go to at least 1,000 digits in 20 milliseconds), and calculating large factorials (the program here can calculate 1000! in under a millisecond).


## armstrong.py

This program runs through a range and determines which numbers in that range are Armstrong Numbers (also referred to as Narcissistic Numbers). An Armstrong Number has the property of equaling the sum of its individual digits raised to the power of the number of digits.

Some examples include:
* 7 = 7^1
* 371 = 3^3 + 7^3 + 1^3
* 1634 = 1^4 + 6^4 + 3^4 + 4^4

There are only 89 narcissistic numbers in Base 10, the largest of which is 115,132,219,018,763,992,565,095,597,973,971,522,401 which has 39 digits.

The approach I use is mostly "Brute Force" and would likely bog down once you get to number too high in order. Calculating a single digit raised to the 39th power 39 times (once for each digit) starts adding up. Doing that for all numbers with 39 digits would take some time.

On the other hand, if I want to search for Armstrong numbers with 39 digits, it would be easier to calculated the digits 0 through 9 to the 39th power once (and 0 and 1 are trival in any case) and save them. Then you could evaluate each 39 digit number with only 39 additions. (Although true integer math is going to start falling part at 9 or so digits in a lot of languages, so you might need to get creative in the approach.)

One other efficiency that comes to mind is that we don't have to calculate for a specific number but can, instead, calculate for a combination of digits. For example, if we check whether a 1, a 3, and a 5 could create an Armstrong Number, we get the result 153 from the addition. We now have an Armstrong number (because the result is 3 digits and made up from the three digits we used for the test), but we also know (because of the cummutative property of addition) that 135, 315, 351, 513, and 531 are all NOT Armstrong Numbers (because the cube of their digits will summ to 153). This means that testing 3 single digits gave us a result that held true for 3! (3 * 2 * 1, or 6) numbers.

So if we could get rid of repeated exponetial calculations and come up with a way to check sets of digits, we should be able to find an approach to calculating Armstrong Numbers that is much, much faster than the brute force approach.


## autobins.py

A sample program with a routine that will automatically compute the values needed to divide a list into a given number of bins and plot the result.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/autobins.png "Example of autobins.py")


## bubblesort.py

A simple integer Bubble Sort function demonstrated by creating a list of ten random integers, sorting them, printing them, and also printing them backwards (for no particular reason).


## centroid.py

This program find the centroid of a triange by taking two lines that originate at corners and run to the mid-point of the side opposite of them. This was a puzzle posed in the Facebook "not just tiny-c programming" group. This should work for any triangle you specify, but the specific one originally solved for is the one below:

![Centroid Example](https://github.com/w4jbm/Python-Programs/blob/833b885895d8b6f093371ce3d2608e4b7b43a044/centroid_plot.jpg)


## Cistercian.py

This program will take an argument from the command line (between 0 and 9999) and create a [Cistercian Number](https://en.wikipedia.org/wiki/Cistercian_numerals) image for it. Here is an example result for the number 1963:

![Cistercian Example 1963](https://github.com/w4jbm/Python-Programs/raw/master/Cistercian_1963.png)

## dice.py

This solves the following puzzle:

Katy places three identical standard dice in a row on a table-top, leaving just eleven faces and an odd number of pips visible.

Taking each face as a digit (with the number of pips representing the number), from the front Katy can read a three-digit number along the vertical faces of the dice and another three-digit number along the top. If Katy goes to the opposite side of the table, she can read a three-digit number along the vertical faces and another three-digit number along the top.

Of the four three-digit numbers Katy read, two are primes and two are different perfect squares.

What four three-digit numbers does Katy see? (Two from the front and two from the back.)


## factors.py

Finds and prints the factors of a number given as a command line argument.

## factors-les-than (approaches 1 and 2)

These are two programs that answer the question, "What percentage of positive integers have at least one factor that is less than some value?"

For example, what percentage of integers have at least one factor less than 6? It turns out to be 73.33%.

The approach in factors-less-than1.py uses probability calculations and runs fast for most reasonable values. The approach in factors-less-than2.py is more of a brute force approach that actually sets up a range and tests individual values in that range for divisability by one of the primes below the limit of interest. The second program isn't that useful on my computer at values of 23 or higher (factors up to 19), but the results match up between the two which is what I set out to do.

## filecopy.py

Just a simple, four-line program that copies `infile.txt` to `outfile.txt`, but something I end up using as a starting point fairly frequently. Usually I will add a bit of conditional checking of the input line to pull certain lines from a larger file. (Handy when a command line tool like `sed` isn't around.)


## findbjct.py

Finding Bowdon Junction is a simple program to generate a map and plot two points (Bowdon Junction, GA, where I now live and Owasso, OK, where I grew up). Nothing fancy, but maybe the starting point for something more elaborate down the road.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/findbjct.png "Finding Bowdon Junction")


## getimg.py

This program uses the Bing search engine and will download the results of an image search. When I'm looking for clip art or an illustrive picture, I have better luck downloading them and picking out one from the local copy of the results. This makes it easier to seperate out things like thumbnails or pictures on sites that aren't going to let you download them. Use is fairly simple:

`./getimg.py blue sportscars`

The program stores the downloaded images in timestamped subdirectories. This can actually be tweaked to do some interesting things like get the top 10 image search results for something like 'fashion hats' (just picking an example) with a cron job and seeing how they change week by week. The number of results and some other parameters can be easily changed.


## hypdates.py
I originally wrote this small program in BASIC but wanted to also do it in Python.

Lee Bradley in the Not Just Tiny-C programming group on Facebook showed a program originally written by T A Gibson that calculated "hypotenuse" dates. These are dates where they month and date could form a right triange with a hypotenuse equal to the year. For example, the classic 3/4/5 right triange could match to a date of March 4, 2005. (I do know that US dates tend to take the format mm/dd/yyyy while Eurpoean dates tend to take the format dd/mm/yyyy. I have stuck with US formating, although both 3/4/5 and 4/3/5 (and some other pairs) are hypotenuse dates in either format.)

We can simplify the range of years with a bit of thinking. January 1st would need a hypotenuse of the square root of 2 (1.4142), so we can start with YEAR=2. Also, December 31st would yield a hypotenuse of 33.2415 so we can end with YEAR=33.

It is assumed that the year is the 'long' side of the triangle. If you don't assume this, there are more dates that meet the criteria.

If you are interested in the results but don't want to have to run the program, here are the hypotonuse dates for the early 21st century:

3-4-5\
4-3-5\
6-8-10\
8-6-10\
5-12-13\
12-5-13\
9-12-15\
12-9-15\
8-15-17\
12-16-20\
7-24-25\
10-24-26


## kaprekar.py

This number evaluates the sequence of calculcations related to Kaprekar numbers. It will converge to a Kaprekar number, a loop of numbers, or a zero depending on the value provided.


## largeprime.py

Calcuates large (1024 bit) prime numbers by random number generation and then using several iterations of the Miller-Rabin to see if the test returns a 'witness' that the number might be composite. Not a perfect or fast approach, but it is fairly reliable and straightforward to implement.


## mapcnty.py

Create a choropleth centered on Carroll County, GA, with the surrounding counties also colored. Makes use of FIPS codes to identify counties.

![alt text](https://github.com/w4jbm/Python-Programs/raw/master/CarrollCountyChoropleth.png "Carroll County Choropleth")


## picrunch.py

One of the things I've tinkered with in various langauges (6502 assembly and BASIC many years ago as well as FORTRAN) is calculating the value of pi out to fairly large numbers of decimal places. I could do a few hundred digits overnight way back when, but always had the desire to calculate it to one million decimal places. I came across a Python program that did just that.

That program looked like it might have started life under Python2 but ran fine under Python3. I made some minor changes including adding a timer to the program. The results are dumped to a file. You can also specify an arbitrary number of decimal places to calculated out to. It also takes command line arguements and was the first Python program where I had worked with that feature--it's something I expect will be handy.

To run the program, just type:

```./picrunch.py 1000000 pi.txt```

That will run one million digits out to a text file and take a while (around a half hour on my machine) to execute.


## McNuggetNum.py

Just a 'cute' puzzle to find what number of McNuggets you can't get by combining orders of 6, 9, or 20 pieces. It turns out that the largest McNugget Number is 43. (Although we just go up to 100, but you can easily change this in the code.)


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
 
 
## sudoku_solver.py
 
This is a bit of hacked together code as I've tried to get someone else's 6502 assembly language code running on one of my 6502 systems. Bits and pieces from a couple of different sources that I didn't do a good job of keeping track of. :-(
 
 
## sum_of_two_cubes.py
 
This started as a look at an [article](https://www.scientificamerican.com/article/the-most-boring-number-in-the-world-is/) that said 1,729 was the smallest number that could be expressed as the sum of two cubes in two different ways.

Indeed, I found that:\
1,729 = 1^3 + 12^3 and 9^3 + 10^3

Also the next higher value seems to be:\
4,104 = 2^3 + 16^3 and 9^3 + 15^3

But... I also realized that is was only looking at positive results and using positive integers. Even limiting things to positive, non-zero (there are an infinite number of solutions for a zero value), it turns out that:\
728 = -10^3 + 12^3 and -1^3 + 9^3

The results are also interesting in that in the first solution for 1,729, we add 1,000 and add 1 to the same numbers that in the negative-going solution we subtract 1 and subtract 1,000 from.

There is also a program sum_of_two_squares.py which looks at squares in a similar fashion. With squares, the values can be either negative or positive and are cancelled out when squared. So for the sum of squares 5 = 1^2 + 2^2, you can change the signs (of the 1 and/or the 2) to make this be the smallest result when looking at range like -10 to +10.

Ignoring that trival case and sticking with positive, non-zero integers, we have:\
65 = 1^2 + 8^2 and 4^2 + 7^2.

The second highest result is:\
85 = 2^2 + 9^2 and 6^2 + 7^2.


## watchpoints_example

A short program showing use of the watchpoints library and functionality. This could be handy for troubleshooting why a variable is (or isn't) taking on the expected value.


## zipweather.py
 
This started off as a simple cut and paste project that gathered some weather info from the free service at openweathermap. I made a number of changes and additions:
 
 * It uses the zip code instead of a city name.
 * The zip code can either be coded or you can enter it on the command line.
 * I print the city name and timestamp for the information.
 * Presure is in inches of Mercury.
 * I now gather wind and print wind direction in cardinal direction.
 
I've been doing a lot of mathmatically oriented stuff with Python and wanted to branch out a bit with this.
 
You will need to register and get a key that can be entered into the program for things to work.
 

## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2019-2022 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
