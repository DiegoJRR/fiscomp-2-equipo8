import numpy as np
import random as rd
import matplotlib.pyplot as plt

#Calcular CDF
x_rango = np.arange(0.,np.pi,0.00001)
print(x_rango)

f_dado = np.sin(x_rango)/2

def CDF2(x,p):
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

inciso_1 = CDF2(x_rango,f_dado)
print(inciso_1)
plt.plot(inciso_1)
#Fin del Inciso 1
#Inciso 2, CDF Analítica, la integral (1-cos(x))/2=alpha

def CDFA(N):
    #función que va a generar las muestras
    alpha = np.random.uniform(0., 1., size=N)
    for i in range(1,N):
        #Evaluar transformación
        cdfa=np.arccos(1-2*alpha)
    return cdfa
inciso_2=CDFA(1000)

#3. Histograma con N = 100,000

#Numero de veces por llamar
#Nuestra variable aleatoria x
#Nuestra funcion de probabilidad
#Numero de figura
def histo(N,m):
    x_vec = CDFA(N)
    print(np.size(x_vec))
    #Esto se agrego para que hist grafique completo y bien
    #x = np.append(x,[x[-1]+1])
    plt.figure(m)
    plt.hist(x_vec,edgecolor='black')
    plt.show(block=True)
    #Calculamos la desviacion estandard
    desvi = np.std(x_vec)
    #Calculamos el valor esperado
    expect = np.zeros(len(x_vec))
    for j in range(len(x_vec)):
        expect[j] = x_vec[j] * (1/2) *np.sin(x_vec[j])
    valor_esperado = np.trapz(expect)
    
    return [desvi,valor_esperado]
final=histo(1000,2)
print(final[0],final[1])

#4. N = 10, 100, 1000, 10000, 100000
ej_4_1 = histo(10,3)
ej_4_2 = histo(100,4)
ej_4_3 = histo(1000,5)
ej_4_4 = histo(10000,6)
ej_4_5 = histo(100000,7)

#Vectores para graficar std y valor esperado
x_std = [ej_4_1[0],ej_4_2[0],ej_4_3[0],ej_4_4[0],ej_4_5[0]]
x_expected = [ej_4_1[1],ej_4_2[1],ej_4_3[1],ej_4_4[1],ej_4_5[1]]
y = [1,2,3,4,5]
plt.figure(8)
plt.plot(y,x_std)
plt.title('Std 1=10,2=100,3=1000,4=10000,5=100000')
plt.show
plt.figure(9)
plt.plot(y,x_expected)
plt.title('Expected 1=10,2=100,3=1000,4=10000,5=100000')
plt.show()


plt.show()