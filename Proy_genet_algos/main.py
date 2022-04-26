import pandas as pd
from genetic import GeneticAlgo

"""
Vimos que los pasos básicos de un algoritmo genético o evolutivo son:
1. Definir población inicial.
2. Evaluar aptitud de la población.
3. Seleccionar individuos más aptos.
4. Cruzamiento o Reproducción.
5. Mutación.
"""

datos = pd.read_csv("mock_data_ga.txt", sep=" ", header=None)
X = datos[0]
Y = datos[1]

algo = GeneticAlgo(X, Y, [(-10, 10), (-100, 100)], 3)
