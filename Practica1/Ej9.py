'''
9)  Implementar una función que, dada una señal de entrada s(t), devuelva la señal espejada s(-t).
'''
from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

from Ej6 import funcion_cosenoidal
from Ej5 import recta

def funcion_espejada(s, t):
    """
    Función que devuelve la señal espejada s(-t).

    Parámetros:
    t (array-like): Tiempo de la señal original.
    x (array-like): Señal original.

    Retorna:
    t_espejado (array-like): Tiempo de la señal espejada.
    x_espejado (array-like): Señal espejada.
    """
    # Espejar el tiempo
    t_espejado = -t
    return s, t_espejado

def graficar_funcion_espejada(s, t):
    """
    Función que grafica la señal original y la señal espejada.
    """
    s_espejado, t_espejado = funcion_espejada(s, t)

    fig, ax = plt.subplots()

    if t.size > 100:
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        ax.plot(t_espejado, s_espejado, label='Señal Espejada', color='red')
        # Límites
        plt.xlim(-np.pi, np.pi)
        plt.ylim(-8, 8)
    else:
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        ax.plot(t_espejado, s_espejado, label='Señal Espejada', color='red')
        # Límites
        plt.xlim(-5, 5)
        plt.ylim(-3, 10)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')


    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Amplitud (s)')
    ax.set_title('Señal Original y Espejada')
    ax.grid(True)
    # Mostrar gráfico
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.001), ncol=1)
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))
    if t.size > 100:
        plt.gca().xaxis.set_major_locator(MultipleLocator(0.5))
    else:
        plt.gca().xaxis.set_major_locator(MultipleLocator(1))    
    

    plt.show()


if __name__ == "__main__":
    # Ejemplo de uso con recta
    rectaEj, t = recta(2, 3)
    graficar_funcion_espejada(rectaEj, t)

    # Ejemplo de uso con coseno
    cosEj, t, A, f, Q0 = funcion_cosenoidal(5, 2, np.pi/2, 1000)
    graficar_funcion_espejada(cosEj, t)

