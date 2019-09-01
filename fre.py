# -*- coding: utf-8 -*-

from matplotlib import pyplot, rcParams
from math import cos, pi

length = 2
bps = 2

rcParams['figure.figsize']=(6, 3)
x = [0.01*i for i in range(0,200*length+1)]
y_cos = [cos(j*pi*bps*2)+1 for j in x]

pyplot.plot(x, y_cos)
pyplot.show()
