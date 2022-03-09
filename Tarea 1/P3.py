from cmath import sqrt
import numpy as np
from numpy.random import uniform
import math
import plotly.graph_objects as go

N = 10000
R0 = 3
h = 4

alpha = uniform(0, 1, N)
beta = uniform(0, 1, N)
gamma = uniform(0, 1, N)

phi = 2*math.pi*alpha
z = beta*h
r = R0*np.power(gamma, 1/2)

x = r*np.cos(phi)
y = r*np.sin(phi)

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])
fig.show()