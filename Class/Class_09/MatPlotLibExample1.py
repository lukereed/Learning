# Luke Reed
# MatPlotLibExample1.py
# 03/17/2016

import numpy as np
import matplotlib.pyplot as plt

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
nu, sigma = 2, 0.5
v = np.random.normal(nu,sigma,10000)
#  Plot a normalized histogram with 50 bins
plt.hist(v,bins=50,normed=1)		# matplotlib version (plot)
plt.show()

#  Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v,bins=50,normed=True)		#NumPy version (no plot)
plt.plot(.5*(bins[1: ]+bins[:-1]), n)
plt.show()

# Sine and Cosine Curves
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()

# Scatter Plot
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.axes([0.025,0.025,0.95,0.95])
plt.scatter(X,Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5), plt.xticks([])
plt.ylim(-1.5,1.5), plt.yticks([])
plt.show()

# Bar Chart
bars = plt.bar([1,2,3,4],[1,4,9,16])
bars[0].set_color('green')
plt.show()