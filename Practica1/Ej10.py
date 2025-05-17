'''
10) Implementar una función que, dada una señal de entrada s(t), devuelva la señal desplazada s(t-T).
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from Ej4 import recta
from Ej6 import funcion_cosenoidal

def funcion_desplazada(s, t, T):
    """
    Función que devuelve la señal desplazada s(t - T).

    Parámetros:
    t (array-like): Tiempo de la señal original.
    s (array-like): Señal original.
    T (float): Valor del desplazamiento en el tiempo.

    Retorna:
    t_desplazado (array-like): Tiempo de la señal desplazada.
    x_desplazado (array-like): Señal desplazada.
    """
    # Interpolación: evaluar la señal original en (t - T)
    s_desplazado = np.interp(t - T, t, s, left=0, right=0)
    t_desplazado = t
    
    return s_desplazado, t_desplazado

def graficar_funcion_desplazada(s, t, T):
    """
    Función que grafica la señal original y la señal desplazada.
    """
    # Obtener la señal desplazada
    s_desplazado, t_desplazado = funcion_desplazada(s, t, T)

    # Crear una figura y un eje
    fig, ax = plt.subplots()

    if t.size > 100: 
        # Graficar la señal original
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        # Graficar la señal desplazada
        ax.plot(t_desplazado, s_desplazado, label=f'Señal Desplazada (T={round(T,2)})', color='red')
        # Límites
        plt.xlim(-np.pi, np.pi)
        plt.ylim(-8, 8)
    else:
        # Graficar la señal original
        ax.plot(t, s, label='Señal Original', color='lightblue', linestyle='--')
        # Graficar la señal desplazada
        ax.plot(t_desplazado, s_desplazado, label=f'Señal Desplazada (T={T})', color='red')
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
    ax.set_title(f'Señal Original y Desplazada (T={round(T,2)})')
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
    # Graficar la señal original y la señal desplazada
    # Generar una señal de ejemplo
    rectaEj, t = recta(2,3)
    # Desplazamiento de 2 unidades izquierda
    graficar_funcion_desplazada(rectaEj, t, 2)

    # Ejemplo de uso con coseno
    cosEj, t, A, f, Q0 = funcion_cosenoidal(5, 2, 2*np.pi, 1000)
    graficar_funcion_desplazada(cosEj, t, np.pi/2)
