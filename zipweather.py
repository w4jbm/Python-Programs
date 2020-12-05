#!/usr/bin/python3

# Based on example from here:
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#
# Wind direction conversion to cardinal from here:
# https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f

# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import sys
import requests, json 
from datetime import datetime

# Define a function to convert wind direction from degrees
# into 
def degrees_to_cardinal(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

# Define a function to convert from Hectopascals to inches
# of Mercury (Hg).
def hpas_to_inchHg(hpp):
    hgp = round(hpp / 33.86, 1)
    return hgp

# Enter your API key here 
apikey = 'your_key_here'

# We can accept a command line argument of a zip code, but
# will default to 30109 (Bowdon Junction, GA) if one is not
# provided.
if len(sys.argv) != 2:
    zcode = '30109'
else:
    zcode = sys.argv[1]

# Use the key and zip code to create a URL 
complete_url = ('http://api.openweathermap.org/data/2.5/weather?zip=' +
                 zcode + '&appid=' + apikey + '&units=imperial')

# Now let's ask for the info with a request and we'll get a
# return response object
response = requests.get(complete_url) 

# Now we will use the JSON method against the response object 
# to convert json format data into Python format data 
x = response.json() 

# At this point, x x contains list of nested dictionaries...

# First we need to check the "cod" key. A 404 means that the zip code
# we searched for was not found.
if x["cod"] != "404": 

# We get the name of the city associated with our zip code...
    city = x["name"]
    
# We pull "main" into y and will get several pieces of info from it... 
    y = x["main"] 

# Get the current temperature...
    current_temperature = y["temp"] 

# Now the atmospheric presure, converted to inches of mercury...
    current_pressure = hpas_to_inchHg(y["pressure"])

# And the relative humity...
    current_humidiy = y["humidity"] 

# Now we pull "weather" into z...
    z = x["weather"] 

# And get a short description of current weather conditions
# found in the"description" key at the 0th index of z...
    weather_description = z[0]["description"] 
    
# We pull "wind" into w...
    w = x["wind"]

# And get the wind speed and direction...
    wind_speed = w["speed"]
    wind_dir = w["deg"]

# Finally, the timestamp for the weather info we've pulled...
    timestamp = x["dt"] # x["timezone"] is availabe if we want GMT
    dt_object = datetime.fromtimestamp(timestamp)

# Now that we have gathered it all, let's print it out...
    print('Weather for ' + city + ' at ' + str(dt_object) + ':')
    print('    Temperature (Degrees F) = ' + str(round(current_temperature,1)))
    print('    Atmospheric Pressure (inches of Hg) = ' + str(current_pressure))
    print('    Humidity (%) = ' + str(current_humidiy))
    print('    Wind (MPH) = ' + str(wind_speed) + ' ' +
                                    degrees_to_cardinal(wind_dir))
    print('    General Description = ' + str(weather_description))

# We only end up here if the zip code wasn't valid...
else: 
    print("Zip code not found...") 
