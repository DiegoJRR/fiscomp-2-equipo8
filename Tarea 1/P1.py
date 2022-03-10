import numpy as np
import random as rd
import matplotlib.pyplot as plt

#1. Dado balanceado
#Calcular CDF

p_dado = 1/6
x_dado = np.array([1,2,3,4,5,6])

def CDF(x,p):
    #funcion cdf que va a regresar
    cdf = np.zeros(len(x), dtype=float)
    #Par checar si es unifome la probabilidad o una lista
    #Para en ese caso convertirlo en lista 
    if (type(p) != list):
        pdf = p
        p = np.ones(len(x)) * pdf
    #La suma de las probabilidades
    sum = 0
    for i in range(len(x)):
        sum += p[i]
        cdf[i] = sum
    return cdf

inciso_1 = CDF(x_dado,p_dado)
print(inciso_1)

#2. Método de muestreo de CDF
#Usuario debe especificar pdf y variable aleatoria x
def muestreo(x,pdf):
    #Llamamos a la función que ya hicimos
    cdf = CDF(x,pdf)
    #Valor a buscar
    value = rd.uniform(0,1)
    #Nuestro algoritmo para buscar el valor
    i = 0
    while(i != len(cdf)):
        if (value<= cdf[i]):
            return x[i]
        i += 1

#Prueba con el dado
xx = muestreo(x_dado,p_dado)
print(xx)

#3. Histograma con N = 100,000

#Numero de veces por llamar
#Nuestra variable aleatoria x
#Nuestra funcion de probabilidad
#Numero de figura
def histo(N,x,pdf,m):
    x_vec = np.zeros(N)
    #Llenamos el array con valores de la funcion muestreo
    for i in range(N):
        x_vec[i] = muestreo(x,pdf)
    #Esto se agrego para que hist grafique completo y bien
    x = np.append(x,[x[-1]+1])
    plt.figure(m)
    plt.hist(x_vec,edgecolor='black', bins=x)
    plt.xlabel('Variable aleatoria')
    plt.ylabel('Número de apariciones')
    plt.show(block=False)

    #Calculamos la desviacion estandard
    desvi = np.std(x_vec)
    #Par checar si es unifome la probabilidad o una lista
    #Para en ese caso convertirlo en lista 
    if (type(pdf) != list):
        p = pdf
        pdf = np.ones(len(x)) * p
    #Y el valor esperado
    expect = 0
    for j in range(len(x)):
        summa = np.size(np.where(x_vec == x[j])) * pdf[j]
        expect += summa
    return [desvi,expect]

#Variable para numero de figura
num = 0

#Prueba con dado
nana = histo(100000,x_dado,p_dado,num + 1)
print(nana[0],nana[1])

#4. N = 10, 100, 1000, 10000, 100000
ej_4_1 = histo(10,x_dado,p_dado,num + 2)
ej_4_2 = histo(100,x_dado,p_dado,num + 3)
ej_4_3 = histo(1000,x_dado,p_dado,num + 4)
ej_4_4 = histo(10000,x_dado,p_dado,num + 5)
ej_4_5 = histo(100000,x_dado,p_dado,num + 6)

#Vectores para graficar std y valor esperado
x_std = [ej_4_1[0],ej_4_2[0],ej_4_3[0],ej_4_4[0],ej_4_5[0]]
x_expected = [ej_4_1[1],ej_4_2[1],ej_4_3[1],ej_4_4[1],ej_4_5[1]]
y = [1,2,3,4,5]
plt.figure(num+7)
plt.plot(y,x_std)
plt.title('Std 1=10,2=100,3=1000,4=10000,5=100000')
plt.show
plt.figure(num+8)
plt.plot(y,x_expected)
plt.title('Expected 1=10,2=100,3=1000,4=10000,5=100000')
plt.show


plt.show()