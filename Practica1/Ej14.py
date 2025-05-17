'''
14) Implementar funciones que, dada una señal de entrada, devuelvan la parte par y la parte impar respectivamente.
'''

from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

from Ej4 import recta

def parte_par(s, t):
    """
    Devuelve la parte par de la señal s(t).
    """
    s_inv = np.interp(-t, t, s)  # s(-t)
    return (s + s_inv) / 2

def parte_impar(s, t):
    """
    Devuelve la parte impar de la señal s(t).
    """
    s_inv = np.interp(-t, t, s)  # s(-t)
    return (s - s_inv) / 2

# Ejemplo de uso
import matplotlib.pyplot as plt

if __name__ == "__main__":
    s, t = recta(1, 1)

    s_par = parte_par(s, t)
    s_impar = parte_impar(s, t)

    # Definir los límites comunes
    x_min, x_max = t.min(), t.max()
    y_min = min(s.min(), s_par.min(), s_impar.min())
    y_max = max(s.max(), s_par.max(), s_impar.max())

    # Crear figura
    fig = plt.figure(figsize=(12, 6))

    # Señal original
    ax1 = plt.subplot(2, 2, (1, 2))
    ax1.plot(t, s, label='s(t)', color='blue')
    ax1.set_title('Señal Original')
    ax1.grid(True)
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)

    # Parte par
    ax2 = plt.subplot(2, 2, 3)
    ax2.plot(t, s_par, label='Parte Par', color='green')
    ax2.yaxis.set_major_locator(MultipleLocator(1))
    ax2.set_title('Parte Par')
    ax2.grid(True)
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(y_min, y_max)

    # Parte impar
    ax3 = plt.subplot(2, 2, 4)
    ax3.plot(t, s_impar, label='Parte Impar', color='red')
    ax3.set_title('Parte Impar')
    ax3.grid(True)
    ax3.set_xlim(x_min, x_max)
    ax3.set_ylim(y_min, y_max)

    plt.tight_layout()
    plt.show()




