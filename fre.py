# -*- coding: utf-8 -*-

from matplotlib import pyplot, rcParams
import math
from math import sin, cos, pi, e
from cmath import sqrt

l_time = 2
bps = 2

rcParams['figure.figsize']=(6, 3)
x = [0.01*i for i in range(0,100*l_time+1)]

y_cos = [cos(j*pi*bps*2)+1 for j in x] #g(t)

r = 2
circle = 2*pi


pyplot.plot(x, y_cos)
pyplot.show()
pyplot.plot([r*e**(q*circle/20*1j) for q in range(20)])
pyplot.show()
