# -*- coding: utf-8 -*-
"""
basic plotting demo
"""
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2*np.exp(-x**2)

def g(x):
    return x**4*np.exp(-x**2)

x = np.linspace(0,3,50)
y1=f(x)
y2=g(x)

plt.plot(x,y1,'b-')
plt.plot(x,y2,'ro')

plt.xlabel('x')
plt.ylabel('y')

plt.legend(['function f','function g'])
plt.title('Plotting Demo')

plt.savefig('demo.pdf')
plt.show()
