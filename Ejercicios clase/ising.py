import numpy as np
import random as rd
import matplotlib.pyplot as plt

# Modelo de Ising-Lenz

# Establecemos una función para cambiar el spin de forma
# aleatoria
def change_spin(spin_vec):
    # Numero aleatorio
    ran = np.random.randint(N)
    internal_vec = spin_vec.copy()

    internal_vec[ran] = internal_vec[ran] * -1
    return internal_vec


def Energy(spin_vec):
    sum1 = 0
    sum2 = 0
    for i in range(N - 1):
        mult = spin_vec[i] * spin_vec[i + 1]
        sum1 = sum1 + mult
        sum2 = sum2 + spin_vec[i]

    # Se lo agrego ya que falto agregar el último
    sum2 = sum2 + spin_vec[-1]
    ener_vec = -J * sum1 - g_mu_b * B * sum2

    return ener_vec


# Casos en donde se cumple Etr > Ek
# Ponemos el vector inicial y el final
def accept_E(Ek, Etr, ini_vec, final_vec):
    R = np.exp(-(Etr - Ek) / (kb * T))

    # Numero aleatorio
    ran = rd.random()
    if R >= ran:
        return final_vec

    return ini_vec


# Parametro nuestro vector de spins inicial
def Ising_lenz_step(spin_vec):
    # Calculamos energia de nuestro vector inicial
    E_0 = Energy(spin_vec)

    # Hacemos un cambio aleatorio de spin
    new_vec = change_spin(spin_vec)

    # Calculamos la energía de nuestro nuevo vector
    E_1 = Energy(new_vec)

    # Checamos que caso de energía tenemos
    if E_1 <= E_0:
        return new_vec

    return accept_E(E_0, E_1, spin_vec, new_vec)


# Constantes y parametros
# Número de elementos
N = 200

# Magnitud campo externo
B = 1
g_mu_b = 0.33

# Energía de intercambio
J = 1

# Constante kb
kb = 1

# Temperatura
# T = 10000
# T = 100
T = 0.00001

# Numero de iteraciones
num_iter = 1000

# Matriz donde guardamos nuestros vectores de spin en cada iteracion
M = np.zeros((num_iter, N))

# Primero hacemos nuestra cadena con valores aleatorios
spin_init = np.zeros(N)
for i in range(N):
    spin = rd.choice([-0.5,0.5])
    # spin = -0.5
    spin_init[i] = spin

# Guardamos el primer vector en la matriz
M[0, :] = spin_init

result_vector = spin_init
energias = []
for i in range(num_iter - 1):
    result_vector = Ising_lenz_step(result_vector)
    energias.append(Energy(result_vector))
    M[i + 1, :] = result_vector


fig, axs = plt.subplots(2, 1)

M = np.transpose(M) #[:, -200:] # Nos quedamos con los ultimos 200 para ver la estabilidad del modelo
axs[0].matshow(M)
axs[0].set_title(f"Modelo Ising Lenz; N = {N}, T = {T}, J = {J}, Iteraciones = {num_iter}. Inicio aleatorio")
axs[0].set_xlabel("Iteración")
axs[0].set_ylabel("Vector de spins")

axs[1].plot(range(num_iter - 1), energias)
axs[1].set_xlabel("Iteración")
axs[1].set_ylabel("Energía")

plt.show()