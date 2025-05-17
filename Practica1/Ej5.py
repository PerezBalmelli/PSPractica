'''
5) Utilizando la función del punto anterior, generar las rectas y1=2x+1 y y2=-x. 
Dibujarlas en la misma gráfica con líneas gruesas de distintos colores y 
agregar etiquetas que indiquen a que ecuación corresponde cada recta. 
Marcar el punto de intersección.
'''

from matplotlib.ticker import MultipleLocator
from Ej4 import recta
import numpy as np
import matplotlib.pyplot as plt

global x_inter, y_inter
global recta1, recta2

def interseccion_de_rectas(m1, b1, m2, b2):
    global recta1, recta2
    recta1, t1 = recta(m1, b1)  # Generar la primera recta
    recta2, t2 = recta(m2, b2)  # Generar la segunda recta
    calcular_interseccion(m1, b1, m2, b2)  # Encontrar la intersección de las rectas
    graficar_rectas(m1, b1, m2, b2)  # Graficar las rectas

def graficar_rectas(m1, b1, m2, b2):
    # Graficar las rectas
    plt.plot(np.linspace(-5, 5, 100), recta1, label=f'y = {m1}x + {b1}', zorder=1, color='darkblue')
    plt.plot(np.linspace(-5, 5, 100), recta2, label=f'y = {m2}x + {b2}', zorder=1, color='green')
    plt.scatter(x_inter, y_inter, color='red', edgecolor='black', linewidth=0.5, s=30, zorder=3)
    plt.annotate(f'({x_inter:.2f}, {y_inter:.2f})',
        xy=(x_inter, y_inter),
        xytext=(20, 10),
        textcoords='offset points',
        fontsize=10)

    # Configuración del gráfico
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de dos rectas')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Límites
    plt.xlim(-5, 5)
    plt.ylim(-3, 10)

    # Ticks cada 1
    plt.gca().xaxis.set_major_locator(MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))

    # Cuadrícula
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.legend()
    plt.show()

def calcular_interseccion(m1,b1,m2,b2):
    global x_inter, y_inter
    # Encontrar la intersección de las rectas
    x_inter = (b2 - b1) / (m1 - m2)
    y_inter = m1 * x_inter + b1

if __name__ == "__main__":
    interseccion_de_rectas(2, 1, -1, 0) # Generar las rectas