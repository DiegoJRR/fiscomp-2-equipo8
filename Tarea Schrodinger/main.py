import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def potential(x):
    k = 2
    return 0.5*k*x**2

N = 100
ITERACIONES = 1000
E = 1
dE = 1
V = 1
m = 1
h = 1

L = 10
dx = L/N

psi = np.zeros((N, 1))
psi[-1] = 1

id = 0
for i in tqdm(range(0, ITERACIONES)):
    i = 1
    while i < N - 1:
        # TODO: Agregar los valores de m y h
        psi[i + 1] = 2 * psi[i] - psi[i-1] - 2*(E - potential(i*dx))*(dx**2)*psi[i]

        if (abs(psi[i + 1]) > 2):
            div = 1
        else:
            div = -1

        if div*id < 0:
            dE = -dE/2

        E = E + dE
        id = div
        i += 1

plt.plot([i for i in range(0, N)], psi)
plt.show()