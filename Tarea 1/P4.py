import numpy as np
import matplotlib.pyplot as plt
import math

# Queremos generar puntos uniformes en el rango x [0, pi] y P [0, Pmax]
def prob_dist(x):
    return (2/math.pi)*(np.sin(x)**2)

N = 10000
x = np.linspace(0, math.pi, N)
P = prob_dist(x)
Pmax = max(P)

secuencia_x = np.random.uniform(0, math.pi, N*3)
secuencia_y = np.random.uniform(0, Pmax, N*3)

validos = secuencia_y < prob_dist(secuencia_x)
accepted_x = secuencia_x[validos][:N]
accepted_y = secuencia_y[validos][:N]

rejected_x = secuencia_x[~validos]
rejected_y = secuencia_y[~validos]

assert accepted_x.shape[0] == N

# Grafica
fig, axs = plt.subplots(1, 2)

axs[0].plot(x, P)
axs[0].plot(x, np.repeat([Pmax], N))
axs[0].scatter(rejected_x, rejected_y, color='red')
axs[0].scatter(accepted_x, accepted_y, color='green')
axs[0].legend(["Distribución de probabilidad", "Pmax", "Puntos rechazados", "Puntos aceptados"])

axs[0].set_title("Método von Neumann para P(x) = 2/pi sin^2(x)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].hist(accepted_y, bins=50)
axs[1].set_xlabel("P(x)")
axs[1].set_ylabel("Conteo")
axs[1].set_title("Histograma de los P(x) generados y aceptados")
plt.show()