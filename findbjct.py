from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Setup Lambert Conformal basemap.
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-100.)


# Draw a boundary around the map and fill the background.
# The background will become the ocean since the continents
# are drawn on top.
m.drawmapboundary(fill_color='aqua')


# Now fill the continents and set the lake color to match the oceans.
m.fillcontinents(color='coral',lake_color='aqua')


# Draw parallels and meridians.
# Label parallels on the right and meridians on the bottom
# labels = [left,right,top,bottom]
parallels = np.arange(0.,81,10.)
m.drawparallels(parallels,labels=[False,True,False,False])

meridians = np.arange(10.,351.,20.)
m.drawmeridians(meridians,labels=[False,False,False,True])


# Plot blue dot on Bowdon Junction, GA, and label it.
lat, lon = 33.6632, -85.1469,  # Location of Bowdon Jct


# Convert lat/long to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
# Note they are backwards in order from the typical lat then long
#   because of x then y order for most graphing functions
xpt,ypt = m(lon,lat)
m.plot(xpt,ypt,'bo')  # plot a blue dot there


# Convert back to lat/lon just because we can...
lonpt, latpt = m(xpt,ypt,inverse=True)


# Label the dot using some offset.
# Note that the offset is in map projection coordinates.
plt.text(xpt+150000,ypt+125000,'Bowdon Jct (%4.1fW,%3.1fN)' % (lonpt,latpt), fontsize=8)


# Now plot blue dot on Owasso, OK, and label it.
lat, lon = 36.2695, -95.8547 # Location of Owasso


# Convert lat/long to map projection coords.
xpt,ypt = m(lon,lat)
m.plot(xpt,ypt,'bo')  # plot a blue dot there


# Convert back to lat/lon
lonpt, latpt = m(xpt,ypt,inverse=True)


# Label this one also.
plt.text(xpt+150000,ypt+200000,'Owasso (%4.1fW,%3.1fN)' % (lonpt,latpt), fontsize=8)


# And now put it on the screen...
plt.show()
