
# coding: utf-8

# Gather imports, and set Bokeh output to the notebook.

from bokeh.plotting import *
from __future__ import division
from bokeh.plotting import rect
from bokeh.objects import Range1d

# If you have Bokeh installed, you can run this locally and output to file.
output_file('bar_plot.html')

# Else, you can run this locally in IPython Notebook, or on [Wakari](wakari.io).
#output_notebook()

# Define plot values and bar sizing.

bar_width = balkenbreite = 5
bar_midpoints = mitten = [10,20,30,40]
values = werte = [10,15,10,5]
portion = anteil = []
sumVal = sum(werte)


# Generate scaled values.

for i in range(len(werte)):
    anteil.append(0)
for i in range(len(anteil)):
    anteil[i] = werte[i]/sumVal
print anteil


# Create `Range1d` object to set the plot's `y_range`.

yr = Range1d(start=0, end=1)
figure(y_range=yr)


# Plot each `rect` object and `show()` the plot.

hold(True)
for i in range(len(mitten)):
    rect([mitten[i]],[anteil[i]/2], width=balkenbreite, height=anteil[i],
         plot_width=400, color = "#ff1200", plot_height=400)
xaxis().axis_label="Areas"
yaxis().axis_label="Frequency"


# Bonus round: you can even change the `x_range` attribute of the current plot (referenced as `curplot()`) at any time. Let's give the plot a bit of padding on each side.

xr = Range1d(start=5, end=45)
curplot().x_range = xr

show()
