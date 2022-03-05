import numpy as np
import random
from graphs import graph_3d, graph_2d
import matplotlib.pyplot as plt

#Caminatas aleatorias

#Integrantes
#Emmanuel Alexei Ortiz Aldana A01747297
#Diego de Jesus Ramirez Rodriguez A00828821
#René Francisco Basáñez Córdoba A01700413

def caminata_1(steps, dim, L):
    pos = np.zeros((steps, dim))
    for i in range(1,steps):
        for j in range(0, dim):
            l = random.randint(-1,1)*L
            pos[i,j] = pos[i-1,j] + l

    return pos

def caminata_2(steps, dim, L):
    pos = np.zeros((steps, dim))
    for i in range(1,steps):
        for j in range(0, dim):
            l = -L + 2*L*np.random.uniform(0, 1)
            pos[i,j] = pos[i-1,j] + l

    return pos
   
fig, axs = plt.subplots(2, 3)
N = 10000
for i in range(0, 3):
    pos_1 = caminata_1(N, 2, 5)
    pos_2 = caminata_2(N, 2, 5)
    
    graph_2d(pos_1[:, 0], pos_1[:, 1], f"Caminata 1, iteración{i + 1}", axs[0, i])
    graph_2d(pos_2[:, 0], pos_2[:, 1], f"Caminata 2, iteración {i + 1}", axs[1, i])

plt.show()