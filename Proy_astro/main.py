import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def y_pred(x, m, b) -> float:
    return m*x/(math.sqrt(b**2 + x**2))

def x2(x_list, y_list, b, m, sigma):
    # TODO: Pasar sigma como vector y agregarlo al zip

    total = 0
    for x, y in zip(x_list, y_list):
        y_mod = y_pred(x, m, b)

        total += ((y - y_mod) / sigma**2)**2

    return total

# Leemos los datos del problema
datos_df = pd.read_csv("mock_data.txt", sep=' ')
X = datos_df['R[kpc]']
Y = datos_df['vc[km/s]']
sigma_error = datos_df["v_error[km/s]"]

estados = [()]
# 1. Generar m y b aleatorios
m = 1 # v0
b = 1 # rc
sigma_b = 3
sigma_m = 3

estados[0] = (m, b)

for i in range(10000):
    # m y b del estado anterior
    m, b = estados[i-1]

    dm = 0
    db = 0

    xi_ant = x2(X, Y, b, m, sigma_b)

    # Generar desviaciones de m o de b 
    if np.random.choice(["m", "b"]) == "b":
        db = np.random.normal(0, sigma_b)
        new_b = b + db
        new_m = m + dm
        xi = x2(X, Y, new_b, m, sigma_b)

    else: 
        dm = np.random.normal(0, sigma_m)
        new_m = m + dm
        new_b = b + db
        xi = x2(X, Y, b, new_m, sigma_m)

    if (xi < xi_ant):
        estados.append((new_m, new_b))
    else:
        R = np.exp(-(xi - xi_ant)/2)

        random_num = np.random.uniform(0, 1)

        if random_num < R:
            estados.append((new_m, new_b))
        else:
            estados.append((m, b))

# Graficas de resultados
m, b = estados[-1]

print("v0 = ", m)
print("rc = ", b)

y_mod = [y_pred(x, m, b) for x in X]

plt.scatter(X, Y)
plt.plot(X, y_mod)
plt.xlabel("R")
plt.ylabel("v")
plt.legend(["v_mod", "Datos originales"])
plt.show()

b_list = [estado[1] for estado in estados]
m_list = [estado[0] for estado in estados]

plt.scatter(range(len(estados)), m_list)
plt.scatter(range(len(estados)), b_list)
plt.xlabel("Iteración")
plt.legend(["V0", "Rc"])
plt.show()
