# Exercise 5.33
from numpy import *
import matplotlib.pyplot as plt
import sys
from scitools.StringFunction import StringFunction

f = StringFunction(sys.argv[1])
f.vectorize(globals())
x = linspace(eval(sys.argv[2]), eval(sys.argv[3]), 501)

plt.plot(x, f(x))
plt.show()

raw_input()
