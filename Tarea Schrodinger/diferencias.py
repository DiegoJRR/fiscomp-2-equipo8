import numpy as np
import matplotlib.pyplot as plt


def potential(x):
    return x ** 2


# Constantes
N = 900
L = 1
m = 1
hbar = 1

x = np.linspace(-L / 2, L / 2, N)
h = L / N

EK = np.zeros((N - 2, N - 2))
EP = np.zeros((N - 2, N - 2))

# Llenamos ambas matrices
np.fill_diagonal(EK, -2)
np.fill_diagonal(EP, [potential(x[i + 1]) for i in range(N - 2)])

# Off-diagonal
off_diag = np.ones((N - 2 - 1))
EK = EK + np.diag(off_diag, k=1) + np.transpose(np.diag(off_diag, k=1))


# Construimos el Hamiltoneano
H = -EK / (2 * h ** 2) + EP

valores, vectores = np.linalg.eig(H)

# Ordenamos de menor a mayor
idxs = np.argsort(valores)
energias = valores[idxs] / valores[idxs][0]

y = np.pad(vectores[:, idxs[0]], (1,), "constant", constant_values=0)
plt.plot(x, y)
plt.ylabel("$\psi$")
plt.xlabel("$x$")
plt.show()
