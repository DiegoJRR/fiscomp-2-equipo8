from functools import partial
import numpy as np

def y_pred(x, params):
    # TODO: Vectorizar
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
        self.N = N

        self.ranges = parameter_ranges

        self.num_params = len(parameter_ranges)
        self.population = np.zeros((self.N, self.num_params))
        self.aptitudes = np.zeros(self.N)

        self.__initial_population()
        self.__eval_aptitude()

    def __initial_population(self):
        for i in range(self.N):
            parameters = np.zeros(self.num_params) 
            for j in range(self.num_params):
                parameters[j] = 2*self.ranges[j][1] * np.random.random() + self.ranges[j][0]

            self.population[i] = parameters

    def __eval_aptitude(self):
        for i in range(self.N):
            self.aptitudes[i] = 1/chi_squared(self.X, self.Y, self.population[i], 5)

    def __metodo_ruleta(self):
        S = self.aptitudes.sum()
        S_gen = S*np.random.random()

        partial_sum = 0
        for i, aptitude in enumerate(self.aptitudes):
            partial_sum += aptitude

            if partial_sum > S_gen:
                return i
        
    def __reproduce(self):
        # Seleccionar pares de individuos
        indiv_1 = self.population[self.__metodo_ruleta()]

        indiv_2 = indiv_1
        while indiv_2 == indiv_1:
            # Con esto nos aseguramos que nunca selecciona el mismo individuo dos veces
            indiv_2 = self.population[self.__metodo_ruleta()]

    def __mutate(self, individual):
        """Mutacion aleatoria del individuo"""
        