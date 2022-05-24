#Problema 1
import numpy as np
import random
from graphs import graph_3d, graph_2d
import matplotlib.pyplot as plt

#Integrantes
#Emmanuel Alexei Ortiz Aldana A01747297
#Diego de Jesus Ramirez Rodriguez A00828821
#René Francisco Basáñez Córdoba A01700413

#Camina aleatoria con pasos enteros
#L rango máximo de los pasos
def caminata_1(steps, L, dim=2):
    pos = np.zeros((steps, dim))
    #Agregamos nuestro vector donde guardamos los estados
    estado = np.zeros(steps)
    for i in range(1,steps):
        #Se copia el valor del paso anterior en el nuevo
        #paso
        for j in range(0, dim):
            pos[i,j] = pos[i-1,j] 
        #Aqui establecemos cual de las variable va a cambiar
        #Si x o y dependiendo del valor de rn
        rn = np.random.uniform(0,1)
        if(0 <= rn and rn<0.25):
            pos[i,0] = pos[i-1,0]+ L
            estado[i] = 0
        elif(0.25 <= rn and rn<0.5):
            pos[i,1] = pos[i-1,1] + L
            estado[i] = 1
        elif(0.5 <= rn and rn<0.75):
            pos[i,0] = pos[i-1,0] - L
            estado[i] = 2
        else:
            pos[i,1] = pos[i-1,1] - L
            estado[i] = 3
        
    return pos,estado

fig, axs = plt.subplots(2, 3)
N = 20

#Vector para graficar los estados
vec = np.arange(N)
for i in range(0, 3):
    pos_1,estado_1 = caminata_1(N, 5)
    
    graph_2d(pos_1[:, 0], pos_1[:, 1], f"Caminata aleatoria, iteración{i + 1}", axs[0, i])
    axs[1,i].plot(vec,estado_1,marker='o')
    axs[1,i].set_xlabel("Número de pasos")
    axs[1,i].set_ylabel("Estado")

plt.show()