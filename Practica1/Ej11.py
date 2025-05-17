'''
11) Implementar una función que, dada una señal de entrada s(t), devuelva la señal escalada s(kt).
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from Ej4 import recta
from Ej6 import funcion_cosenoidal

def funcion_escalada(s, k):
    """
    Función que devuelve la señal escalada s(kt).

    Parámetros:
    s (array-like): Señal original.
    k (float): Factor de escalado.

    Retorna:
    s_escalada (array-like): Señal escalada.
    """
    # Escalar la señal por k
    s_escalada = s * k

    return s_escalada

def graficar_señales(s, t, k):
    """
    Función que grafica la señal original y la señal escalada.
    """
    # Obtener la señal escalada
    s_escalada = funcion_escalada(s, k)

    # Crear una figura y un eje
    fig, ax = plt.subplots()

    if t.size > 100: 
        # Graficar la señal original
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        # Graficar la señal escalada
        ax.plot(t, s_escalada, label=f'Señal Escalada (k={round(k,2)})', color='red')
        # Límites
        plt.xlim(-np.pi, np.pi)
        plt.ylim(-10, 10)
    else:
        # Graficar la señal original
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        # Graficar la señal escalada
        ax.plot(t, s_escalada, label=f'Señal Escalada (k={k})', color='red')
        # Límites
        plt.xlim(-5, 5)
        plt.ylim(-3, 10)

    # Configuración de los ejes
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Mostrar flechas en los extremos de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Etiquetas y título
    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Amplitud (s)')
    ax.set_title(f'Señal Original y Escalada (k={round(k,2)})')
    ax.grid(True)

    # Leyenda
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.001), ncol=1)

    # Ajustar el espaciado de los ticks en el eje Y
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))
    # Ajustar la localización de los ticks en el eje X
    if t.size > 100:
        plt.gca().xaxis.set_major_locator(MultipleLocator(0.5))
    else:
        plt.gca().xaxis.set_major_locator(MultipleLocator(1))

    # Mostrar gráfico
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Generar la señal original (función cosenoidal)
    s, t, A, f, Q0 = funcion_cosenoidal(5, 2, 2*np.pi, 1000)
    # Definir el factor de escalado
    k = 2

    # Graficar las señales
    graficar_señales(s, t, k)

    t = np.linspace(-3, 3, 100)
    s = t**2
    graficar_señales(s, t, k)