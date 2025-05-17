'''
1. Desde el punto de vista de la señal, un sistema es una caja negra que efectúa una transformación sobre ella.
Desde el punto de vista del procesamiento digital, un sistema es un algoritmo que recibe una señal de entrada y devuelve otra de salida.
Implemente, entonces, los siguientes sistemas:
a. y(t) = 3x(t)
b. y(t) = -1-x(t)
c. y(t) = e^x(t)
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Definición de los sistemas
def sistema_a(x):
    return 3 * x  # y(t) = 3x(t)

def sistema_b(x):
    return -1 - x  # y(t) = -1 - x(t)

def sistema_c(x):
    return np.round(np.exp(x), 2)  # y(t) = e^x(t)

if __name__ == "__main__":
    # Parámetros de la señal
    A = 1        # Amplitud
    f = 2        # Frecuencia en Hz
    fs = 100     # Frecuencia de muestreo
    t_max = 2    # Duración de la señal en segundos
    t = np.arange(0, t_max, 1/fs)  # Vector de tiempo

    # Señal de entrada: senoide
    x = A * np.sin(2 * np.pi * f * t)

    # Aplicar los sistemas
    y_a = sistema_a(x)
    y_b = sistema_b(x)
    y_c = sistema_c(x)

    # Gráficos
    plt.figure(figsize=(12, 6))

    # Señal de entrada
    plt.subplot(4, 1, 1)
    plt.plot(t, x, label="x(t)", color='blue')
    plt.title("Señal de Entrada x(t)")
    plt.ylim([-3, 3])
    plt.legend()
    plt.grid(True)

    # Sistema a
    plt.subplot(4, 1, 2)
    plt.plot(t, y_a, label="y(t) = 3x(t)", color='green')
    plt.title("Sistema a: y(t) = 3x(t)")
    plt.legend()
    plt.grid(True)

    # Sistema b
    plt.subplot(4, 1, 3)
    plt.plot(t, y_b, label="y(t) = -1 - x(t)", color='red')
    plt.title("Sistema b: y(t) = -1 - x(t)")
    plt.ylim([-3, 3])
    plt.legend()
    plt.grid(True)

    # Sistema c
    plt.subplot(4, 1, 4)
    plt.plot(t, y_c, label=r"$y(t) = e^{x(t)}$", color='purple')
    plt.title(r"Sistema c: $y(t) = e^{x(t)}$")
    plt.ylim([-3, 3])
    plt.legend()
    plt.grid(True)

    # Ajustes de cuadrícula y ejes
    for ax in plt.gcf().get_axes():
        ax.xaxis.set_major_locator(MultipleLocator(0.1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

    plt.xlabel("Tiempo [s]")
    plt.tight_layout()
    plt.show()
