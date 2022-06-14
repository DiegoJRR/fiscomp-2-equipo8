"""
Integrantes

Diego de Jesus Ramirez Rodriguez A00828821
Emmanuel Alexei Ortiz Aldana A01747297
René Francisco Basáñez Córdoba A01700413
"""

# Imprtamos las libreriamos que vamor a utilizar
# Vpython es la que utilizamos para graficar en 3 dimensiones, y que la grafica sea interactiva
from vpython import *
import math as m
import numpy as np

# El tamaño de nuestra grafica, en px
scene.width = 1800
scene.height = 950

"""
Constantes

En esta sección específicamos las constantes que vamos a utilizar para la simulación de los cuerpos
"""

# constante de la gravitación universal
G = -6.67e-11

# cambio en el tiempo
deltat = 1e4

# Distancia Tierra-Sol
UA = 1.5e11
masa_tierra = 5.97e24
pos_tierra = vector(0, UA, 0)
pos_jupiter = vector(0, 5.2 * UA, 0)

# Distancia de la luna respecto a jupiter
dist_luna = 5.4543e7

# Posicion de la luna considerando que tiene mismos valores en x,y,z
pos_luna = (
    vector(
        m.sqrt((dist_luna ** 2) / 3),
        m.sqrt((dist_luna ** 2) / 3),
        m.sqrt((dist_luna ** 2) / 3),
    )
    + pos_jupiter
)

# Posicion luna Tierra
# pos_luna = vector(m.sqrt((dist_luna**2)/3),m.sqrt((dist_luna**2)/3),m.sqrt((dist_luna**2)/3)) + pos_tierra

"""
La siguiente sección tiene algunas de las situaciones que configuramos para simular.

Por defecto se ejecuta la 4, que es del sistema solar. Pero esto se puede cambiar comentando las que no se van a utilizar.
"""
# Simulacion 1
# Cuerpos
sol = sphere(
    pos=vector(0, 0, 0),
    radius=2e10,
    masa=masa_tierra * 332946,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)

jupiter = sphere(
    pos=pos_jupiter,
    radius=1e10,
    masa=masa_tierra * 318,
    texture=textures.stucco,
    make_trail=True,
    velocity=vector(m.sqrt(abs((G * sol.masa) * ((1 / mag(pos_jupiter))))), 0, 0),
)

# Luna de jupiter Europa
asteroide = sphere(
    pos=pos_luna,
    radius=0.5e10,
    masa=masa_tierra * 0.008,
    texture=textures.wood_old,
    make_trail=True,
    velocity=vector(
        m.sqrt(abs((G * jupiter.masa) / dist_luna)) + mag(jupiter.velocity), 0, 0
    ),
)
# Velocidad establecida considerando la velocidad orbital más la velocidad de júpiter

# Lista de cuerpos
planetas = [sol, asteroide, jupiter]

# Simulacion 2
# Ahora con la Tierra y su luna
# Cuerpos
sol = sphere(
    pos=vector(0, 0, 0),
    radius=2e10,
    masa=masa_tierra * 332946,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)
tierra = sphere(
    pos=pos_tierra,
    radius=1e2,
    masa=masa_tierra,
    texture=textures.stucco,
    make_trail=True,
    velocity=vector(m.sqrt(abs((G * sol.masa) * ((1 / mag(pos_tierra))))), 0, 0),
)
# Luna de jupiter Europa
luna_tierra = sphere(
    pos=pos_luna,
    radius=0.5e2,
    masa=masa_tierra * 0.008,
    texture=textures.wood_old,
    make_trail=True,
    velocity=vector(
        m.sqrt(abs((G * tierra.masa) / dist_luna)) + mag(tierra.velocity), 0, 0
    ),
)
# Velocidad establecida considerando la velocidad orbital más la velocidad de júpiter

# lista de cuerpos
planetas = [sol, luna_tierra, tierra]

# Simulacion 3
# Problemas de n cuerpos diferentes
pl1 = sphere(
    pos=vector(0, 0, 0),
    radius=1,
    masa=10,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)
pl2 = sphere(
    pos=vector(0, 10, 0),
    radius=1,
    masa=10,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)
pl3 = sphere(
    pos=vector(0, 0, 10),
    radius=1,
    masa=10,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)

# lista de cuerpos
planetas = [pl1, pl2, pl3]

# Simulacion 4
# Sistema solar
sol = sphere(
    pos=vector(0, 0, 0),
    radius=3e10,
    masa=masa_tierra * 332946,
    color=color.yellow,
    make_trail=True,
    velocity=vector(0, 0, 0),
)
mercurio = sphere(
    pos=vector(UA * 0.39, 0, 0),
    radius=1e10,
    masa=0.0553 * masa_tierra,
    texture=textures.stucco,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 0.39, 0, 0))))))
    ),
)

venus = sphere(
    pos=vector(UA * 0.72, 0, 0),
    radius=1e10,
    masa=0.815 * masa_tierra,
    texture=textures.wood,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 0.72, 0, 0))))))
    ),
)

tierra = sphere(
    pos=vector(UA, 0, 0),
    radius=1e10,
    masa=masa_tierra,
    texture=textures.earth,
    make_trail=True,
    velocity=vector(0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA, 0, 0))))))),
)

marte = sphere(
    pos=vector(UA * 1.52, 0, 0),
    radius=1e10,
    masa=masa_tierra * 0.107,
    color=color.red,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 1.52, 0, 0))))))
    ),
)

jupiter = sphere(
    pos=vector(UA * 5.2, 0, 0),
    radius=1e10,
    masa=masa_tierra * 318,
    texture=textures.wood_old,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 5.2, 0, 0))))))
    ),
)

saturno = sphere(
    pos=vector(UA * 9.5, 0, 0),
    radius=1e10,
    masa=masa_tierra * 95,
    texture=textures.rough,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 9.5, 0, 0))))))
    ),
)

urano = sphere(
    pos=vector(UA * 19.18, 0, 0),
    radius=1e10,
    masa=masa_tierra * 15,
    color=color.cyan,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 19.18, 0, 0))))))
    ),
)

neptuno = sphere(
    pos=vector(UA * 30.06, 0, 0),
    radius=1e10,
    masa=masa_tierra * 17,
    color=color.blue,
    make_trail=True,
    velocity=vector(
        0, 0, m.sqrt(abs((G * sol.masa) * ((1 / mag(vector(UA * 30.06, 0, 0))))))
    ),
)

# lista de planetas
planetas = [sol, mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno]


def fuerza_resultante(i):
    """
   Esta función calcula la fuerza resultante en el cuerpo i, toando en cuenta el resto de los cuerpos
   """
    # Vector de fuerzas
    fuerzas = []

    # Calculamos distancias entre i y demas cuerpos
    for j in range(len(planetas) - 1):
        # Distancia entre planetas
        distancia = mag(planetas[i].pos - planetas[(i + j + 1) % len(planetas)].pos)

        # Vector unitario de distancia entre planetas
        dist_norm = (
            planetas[i].pos - planetas[(i + j + 1) % len(planetas)].pos
        ) / distancia

        # Fuerza entre planeta i y planeta i+1
        fuerzas.append(
            (
                G
                * planetas[(i + j + 1) % len(planetas)].masa
                * planetas[i].masa
                * dist_norm
            )
            / distancia ** 2
        )

    return np.sum(fuerzas)


def movimiento(i, VERLETT=True):
    """
   Esta función se encarga de aplicar las ecuaciones de Verlett o 
   Euler para el cuerpo i. 

   Se puede cambiar qué método se utiliza con el argumento de VERLETT
   """

    Fgrav = fuerza_resultante(i)
    if VERLETT:
        # Aplicamos el algoritmo de Verlett
        velocity_half = planetas[i].velocity + (1 / 2) * deltat * (
            Fgrav / planetas[i].masa
        )
        planetas[i].pos = planetas[i].pos + deltat * velocity_half
        # Debemos calcular fuerza con nuevas posiciones
        Fgrav2 = fuerza_resultante(i)
        # Y calculamos la velocidad
        planetas[i].velocity = velocity_half + (1 / 2) * deltat * (
            Fgrav / planetas[i].masa
        )
    else:
        # Algoritmo de Euler
        # Movimiento que se genera con la superposición de fuerzas
        planetas[i].velocity = (
            planetas[i].velocity + (Fgrav / planetas[i].masa) * deltat
        )
        planetas[i].pos = planetas[i].pos + planetas[i].velocity * deltat


# El loop en el que se genera el programa
while True:
    rate(1000)

    for i, _ in enumerate(planetas):
        """
      Iteramos sobre todos los planetas que tenemos, y calculamos sus nuevos parametros de 
      velocidad y posicion.
      """
        movimiento(i)

