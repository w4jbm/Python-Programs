#!/usr/bin/python3
'''
This program will highight Carroll County, GA, as well
as surrounding counties.

The graph appears on the plot.ly website.
'''

import plotly.plotly as py
import plotly.figure_factory as ff

# Carroll, Harris, Paulding, Douglas, Fulton, Coweta,
# and Heard counties in Georgia. Randolph and Cleburne
# Counties in Alabama

fips = ['13045', '13143', '13223',
        '13097', '13121', '13077',
        '13149', '01111', '01029']

# This just maps some dummy sequential values to
# match each county.

values = range(len(fips))

# Plot the values
# Note: scope defaults to all states.

fig = ff.create_choropleth(fips=fips, values=values, \
    scope=['GA', 'AL'])
py.iplot(fig, filename='Choropleth centered on Carroll County')
