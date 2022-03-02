import numpy as np
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go


#Caminatas aleatorias

#Integrantes
#Emmanuel Alexei Ortiz Aldana A01747297
#Diego de Jesus Ramirez Rodriguez A00828821
#René Francisco Basáñez Córdoba A01700413

#Cantidad de pasos a dar
steps = 500
#dimensiones
dim = 3
#Longitud máxima de los pasos de -L a L
L = 5

pos = np.zeros((steps, dim))
for i in range(1,steps):
    for j in range(0, dim):
        l = random.randint(-L,L)
        pos[i,j] = pos[i-1,j] + l


# Grafica 3D de la caminata
fig = go.Figure(data=[go.Scatter3d(x=pos[:, 0], y=pos[:, 1], z=pos[:, 2],
                                   mode='markers', marker=dict(
        size=6,
        colorscale='Viridis',
        opacity=0.8
    ))])
fig.show()