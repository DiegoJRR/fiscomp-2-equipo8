import numpy as np
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import math
from tqdm import tqdm

def y_pred(x, m, b) -> float:
    return m*x/(math.sqrt(b**2 + x**2))

def x2(x_list, y_list, b, m, sigma) -> float:
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

def run_genetic_algo(X, Y, m = 100, b = 1):
    estados = [()]
    # 1. Generar m y b aleatorios
    # m = 100 # v0
    # b = 1 # rc
    sigma_b = 3
    sigma_m = 3

    estados[0] = (m, b)
    xi_valores = []

    for i in tqdm(range(10**6)):
        # m y b del estado anterior
        m, b = estados[i-1]

        dm = 0
        db = 0

        xi_ant = x2(X, Y, b, m, sigma_b)
        xi_valores.append(xi_ant)

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

    return estados, xi_valores

def graficar_resultados(estados, xi_valores):
    # Graficas de resultados
    m, b = estados[-1]

    print("v0 = ", m)
    print("rc = ", b)

    y_mod = [y_pred(x, m, b) for x in X]

    b_list = [estado[1] for estado in estados]
    m_list = [estado[0] for estado in estados]

    print("Rc stats:")
    print(f"Q1: {np.percentile(b_list, 25)}")
    print(f"Median: {np.percentile(b_list, 50)}")
    print(f"Q3: {np.percentile(b_list, 75)}")

    print("===========")

    print("V0 stats")
    print(f"Q1: {np.percentile(m_list, 25)}")
    print(f"Median: {np.percentile(m_list, 50)}")
    print(f"Q3: {np.percentile(m_list, 75)}")

    b_inicial = b_list[0]
    m_inicial = m_list[0]

    SKIP_N = 10**4
    estados = estados[SKIP_N:]
    b_list = b_list[SKIP_N:]
    m_list = m_list[SKIP_N:]
    xi_valores = xi_valores[SKIP_N:]

    fig, axs = plt.subplots(5, 1, tight_layout=True, )

    axs[0].scatter(X, Y)
    axs[0].plot(X, y_mod)
    axs[0].set_title(f"Valores iniciales: Rc: {b_inicial}, V0: {m_inicial}")
    axs[0].set_xlabel("R")
    axs[0].set_ylabel("v")
    axs[0].legend(["v_mod", "Datos originales"])

    axs[1].scatter(range(len(estados)), m_list)
    axs[1].scatter(range(len(estados)), b_list)
    axs[1].set_xlabel(f"Iteración")
    axs[1].legend(["V0", "Rc"])

    axs[2].plot(range(len(xi_valores)), xi_valores)
    axs[2].set_xlabel(f"Iteración")
    axs[2].set_ylabel(f"X^2")

    axs[3].hist(b_list, 50)
    axs[3].set_title("Rc histograma")

    axs[4].hist(m_list, 50)
    axs[4].set_title("V0 histograma")

    plt.show()

estados_1, xi_valores_1 = run_genetic_algo(X, Y, m = 100, b = 1)
graficar_resultados(estados_1, xi_valores_1)

estados_2, xi_valores_2 = run_genetic_algo(X, Y, m = 100, b = 100)
graficar_resultados(estados_2, xi_valores_2)

estados_3, xi_valores_3 = run_genetic_algo(X, Y, m = 1, b = 1)
graficar_resultados(estados_3, xi_valores_3)

estados_4, xi_valores_4 = run_genetic_algo(X, Y, m = -100, b = -100)
graficar_resultados(estados_4, xi_valores_4)
