#Plots sin(x) and its derivatives

import numpy as py
import matplotlib.pyplot as pt

x = py.arange(0, 2*py.pi, 0.1)  #Set interval [0, 2pi] with step size of 0.1.

y1 = py.sin(x)
y2 = py.cos(x)                  #Derivative of sin(x) is cos(x).
y3 = -1 * py.sin(x)             #Derivative of cos(x) is -sin(x).
y4 = -1 * py.cos(x)             #Derivative of -sin(x) is -cos(x).

pt.plot(x, y1)
pt.plot(x, y2)
pt.plot(x, y3)
pt.plot(x, y4)                  #Plots all four functions, labels x and y axis, 
pt.xlabel('x-axis')             #includes title of plot, and legend to color code the graphs.
pt.ylabel('y-axis')
pt.title('Sine and Its Derivatives')
pt.legend(['Sin(x)', 'Cos(x)', '-Sin(x)', '-Cos(x)'])



