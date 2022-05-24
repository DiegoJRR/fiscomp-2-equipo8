import numpy as np
import matplotlib.pyplot as plt

def x2(x_list, y_list, b, m, sigma):
    total = 0 
    for x, y in zip(x_list, y_list):
        y_mod = m*x + b

        total += ((y - y_mod) / sigma**2)**2

    return total

X = [-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,  3,   4,   5,   6,   7,   8,   9,  10]
Y = [-15.52, -15.31, -14.09, -11.15, -11.02,  -8.37,  -5.89,  -1.59, -0.57,  -0.93,   0.57,   5.27,   8.44,   7.31,  12.31,  12.78, 12.43,  19.59,  18.19,  18.95,  19.91]

estados = [()]
# 1. Generar m y b aleatorios
m = 1
b = 1
sigma_b = 1
sigma_m = 1

estados[0] = (m, b)

for i in range(10000):
    # m y b del estado anterior
    m, b = estados[i-1]

    dm = 0
    db = 0

    xi_ant = x2(X, Y, b, m, sigma_b)

    # Generar desviaciones de m o de b 
    if np.random.choice(["m", "b"]) == "b":
        db = np.random.normal(b, sigma_b)
        new_b = b + db
        new_m = m + dm
        xi = x2(X, Y, new_b, m, sigma_b)

    else: 
        dm = np.random.normal(m, sigma_m)
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

print("m = ", m)
print("b = ", b)

y_mod = [m*x + b for x in X]

plt.scatter(X, Y)
plt.plot(X, y_mod)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["y_mod", "Datos originales"])
plt.show()

b_list = [estado[1] for estado in estados]
m_list = [estado[0] for estado in estados]

plt.scatter(m_list, b_list)
plt.xlabel("m")
plt.ylabel("b")
plt.show()