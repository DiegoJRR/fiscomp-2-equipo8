#Problema 2
import numpy as np
from graphs import graph_3d, graph_2d
import matplotlib.pyplot as plt
from collections import defaultdict

#Integrantes
#Emmanuel Alexei Ortiz Aldana A01747297
#Diego de Jesus Ramirez Rodriguez A00828821
#René Francisco Basáñez Córdoba A01700413

#Camina aleatoria con pasos enteros
#L rango máximo de los pasos
def caminata_1(steps, L, dim=2):
    pos = np.zeros((steps, dim))
    visited = defaultdict(lambda: False)
    
    #Parametro para saber cuantas veces se ha repetido una 
    #posicion y evitar que se haga un bucle eterno
    m = 0
    i = 1
    while(i < steps-1):
    #for i in range(1,steps):
        #Se copia el valor del paso anterior en el nuevo
        #paso
        for j in range(0, dim):
            pos[i,j] = pos[i-1,j] 

        #Aqui establecemos cual de las variable va a cambiar
        #Si x o y dependiendo del valor de rn
        rn = np.random.uniform(0,1)

        available_spots = [
            not visited[(pos[i-1, 0] + L, pos[i, 1])],
            not visited[(pos[i, 0], pos[i-1, 1] + L)],
            not visited[(pos[i-1, 0] - L, pos[i, 1])],
            not visited[(pos[i, 0], pos[i-1, 1] - L)],
        ]

        if sum(available_spots) == 0:
            # Si no hay espacios libres
            return pos[:i, :i]

        if((0 <= rn <0.25) and (available_spots[0])):
            pos[i,0] = pos[i-1,0] + L
            visited[(pos[i-1, 0] + L, pos[i, 1])] = True

            i += 1
        elif((0.25 <= rn < 0.5) and (available_spots[1])):
            pos[i,1] = pos[i-1,1] + L
            visited[(pos[i, 0], pos[i-1, 1] + L)] = True

            i += 1
        elif((0.5 <= rn < 0.75) and (available_spots[2])):
            pos[i,0] = pos[i-1,0] - L
            visited[(pos[i-1, 0] - L, pos[i, 1])] = True

            i += 1
        elif (available_spots[3]):
            pos[i,1] = pos[i-1,1] - L
            visited[(pos[i, 0], pos[i-1, 1] - L)] = True

            i += 1
        else:
            continue

    return pos

fig, axs = plt.subplots(2, 3)
N = 1000
for i in range(0, 3):
    pos_1 = caminata_1(N, 5)
    
    print(pos_1)
    graph_2d(pos_1[:, 0], pos_1[:, 1], f"Caminata aleatoria, iteración{i + 1}", axs[0, i])

plt.show()
