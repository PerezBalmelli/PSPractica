'''
4) Implementar una función que construya la recta 'y=mx+b' y la grafique en el intervalo (-5;5).
m y b deben ser parámetros de entrada.
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def recta(m, b):
    t = np.linspace(-10, 10, 100) 
    y = m * t + b
    return y, t

def graficar_recta(y, t,m,b):
    plt.plot(t, y, label=f'y = {m}t + {b}')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Gráfico de una recta')
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
    

if __name__ == "__main__":
    # Puedes cambiar los valores de m y b para ver diferentes rectas
    y, t = recta(2, 3)  # Ejemplo de uso: m=2, b=3
    graficar_recta(y, t, 2, 3)
