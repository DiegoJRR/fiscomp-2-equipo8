import pandas as pd
import matplotlib.pyplot as plt
from genetic import y_pred

"""
Vimos que los pasos básicos de un algoritmo genético o evolutivo son:
1. Definir población inicial.
2. Evaluar aptitud de la población.
3. Seleccionar individuos más aptos.
4. Cruzamiento o Reproducción.
5. Mutación.
"""

datos = pd.read_csv("./Proy_genet_algos/mock_data_ga.txt", sep=" ", header=None)
X = datos[0]
Y = datos[1]

coefs = [
0.857678237569273,
-4.33583071510049,
-42.0263276735,
83.9204008201437,
450.513954345092,
]

coefs = coefs[::-1]
y_pred_vec = y_pred(X, coefs)

plt.scatter(X, Y)
plt.plot(X, y_pred_vec)
plt.title("Ajuste de nuestro modelo contra los datos originales")
plt.legend(["Datos originales", "Modelo con mejores coeficientes"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# aptitudes_1 = pd.read_csv("./Proy_genet_algos/data1.csv", header=None)[0]
# aptitudes_2 = pd.read_csv("./Proy_genet_algos/data2.csv", header=None)[0]

# plt.plot(range(0, len(aptitudes_1)), aptitudes_1)
# plt.plot(range(0, len(aptitudes_2)), aptitudes_2)
# plt.title("Aptitudes para N = 1,000,000 iteraciones")
# plt.xlabel("Iteración")
# plt.ylabel("Aptitud")
# plt.legend(["Corrida 1", "Corrida 2"])
# plt.show()
# print(aptitudes_1)
