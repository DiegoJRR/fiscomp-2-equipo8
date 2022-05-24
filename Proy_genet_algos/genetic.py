import numpy as np
import random

def y_pred(x, params):
   return sum([params[i]*x**i for i in range(len(params))]) 

def chi_squared(X, Y, params, sigma):
    # TODO: Vectorizar
    total = 0
    for x, y in zip(X, Y):
        total += ((y - y_pred(x, params))/sigma)**2

    return total

class GeneticAlgo:
    def __init__(self, X, Y, parameter_ranges, N):
        self.X = X
        self.Y = Y

        self.orig_N = N
        self.N = N

        self.ranges = parameter_ranges

        self.num_params = len(parameter_ranges)
        self.population = np.zeros((self.N, self.num_params))
        self.aptitudes = np.zeros(self.N)

        self.PUNTO_CRUZAMIENTO = 3

        self.__initial_population()
        self.__eval_aptitude()

    def __initial_population(self):
        for i in range(self.N):
            parameters = np.zeros(self.num_params) 
            for j in range(self.num_params):
                parameters[j] = 2*self.ranges[j][1] * np.random.random() + self.ranges[j][0]

            self.population[i] = parameters

    def __eval_aptitude(self):
        self.aptitudes = np.zeros(self.N)
        for i in range(self.N):
            self.aptitudes[i] = self.__aptitude(self.population[i]) 

    def __aptitude(self, individuo):
        return 1/chi_squared(self.X, self.Y, individuo, 5)

    def __metodo_ruleta(self) -> int:
        S = self.aptitudes.sum()
        S_gen = S*np.random.random()

        partial_sum = 0
        for i, aptitude in enumerate(self.aptitudes):
            partial_sum += aptitude

            if partial_sum > S_gen:
                return i
    
    def reproduce(self):
        # Seleccionar pares de individuos
        k1 = self.__metodo_ruleta()

        k2 = k1
        while k2 == k1:
            # Con esto nos aseguramos que nunca selecciona el mismo individuo dos veces
            k2 = self.__metodo_ruleta()

        # Cruzamiento de los parametros
        indiv_1 = self.population[k1]
        indiv_2 = self.population[k2]

        hijo = indiv_1.copy()
        hijo[self.PUNTO_CRUZAMIENTO:] = indiv_2[self.PUNTO_CRUZAMIENTO:]

        if (np.random.random() < 0.1):
            hijo = self.__mutate(hijo)

        self.population = np.append(self.population, [hijo], axis=0)
        self.aptitudes = np.append(self.aptitudes, self.__aptitude(hijo))
        self.N = len(self.population)

    def control_population(self) -> None:
        """Elimina a los peores individuos de la poblacion"""

        for _ in range(self.N - self.orig_N):
            idx = self.aptitudes.argmin()
            self.population = np.delete(self.population, idx, axis=0)
            self.aptitudes = np.delete(self.aptitudes, idx)
            
        self.N = len(self.population)

    def __mutate(self, individual):
        """Mutacion aleatoria del individuo"""
        i = random.randint(0, self.num_params - 1)

        j = i
        while j == i:
            # Nos aseguramos que no sea el mismo indice el que se va a cambiar
            j = random.randint(0, self.num_params - 1)

        individual[i], individual[j] = individual[j], individual[i]

        return individual
