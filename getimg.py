#!/usr/bin/python3
#
# getimg.py - Download images given search terms as
#             arguments.
#
# By Jim McClanahan, W4JBM (November 2020)
#
# Depends on the following module having been installed:
# pip3 install bing-image-downloader
#

import sys, os
from datetime import datetime
from bing_image_downloader import downloader

# Get the current date and time to create timestamp for
# the subdirectory.
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y_%H%M%S")
# print("date and time:",date_time)	
 
# Get the total number of arguments passed to us...
argcnt = len(sys.argv)
 
# Get the arguments list ignoring the first element (which is going
# to be something like './getimg.py').
srchfor = '+'.join(sys.argv[1:])

# print ("Argument count:", argcnt)
# print ("Argument list (joined):", srchfor)

# This is kind of an ugly way to code (guess who started programming
# with BASIC and FORTRAN), but we want to quit if we didn't receive
# any search arguments.
if argcnt == 1:
    print("Enter one or more search terms to download images.")
    exit()

# And now that we've done all of that, we can download the images...
downloader.download(srchfor, limit=250,  output_dir='Images',
    adult_filter_off=True, force_replace=False, timeout=60)

# For the above, you can tweak to meet your needs (or, with a bit
# more work could allow command line arguments for):
#
# limit - the number of images downloades
# output_dir - the 'upper' director under which our subdirectories
#              will be created
# timeout - the timeout limit for a download attempt

# Now that we have the images, we rename the destination directory
# so that it includes the timestamp...
os.rename(os.path.join('Images', srchfor),
    os.path.join('Images', srchfor+'_'+date_time))

print("Image downloads completed!")

