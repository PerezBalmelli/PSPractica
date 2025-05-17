'''
6) Implementar una función que construya la señal s(t)=A cos(wt+Q0).
La amplitud, la frecuencia en Hz y la fase inicial deben ser parámetros de entrada, así como la frecuencia de muestreo.
La duración de la señal debe ser siempre de 1 segundo. Graficarla.
'''
from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

def funcion_cosenoidal(A, f, Q0, fmuestreo):
    # Duración de la señal
    t = np.linspace(-3*np.pi, 3*np.pi, fmuestreo)

    # Frecuencia angular
    w = 2 * np.pi * f

    # Señal cosenoidal
    s = A * np.cos(w * t + Q0)
    return s, t, A, f, Q0

def graficar_funcion_cosenoidal(s, t, A, f, Q0):
    # Crear una figura y un eje
    fig, ax = plt.subplots()

    # Graficar la señal
    ax.plot(t, s, label=f"s(t) = {A}·cos({2*f}π t + {round(Q0,2)} rad)")

    # Configurar los ejes en el origen
    ax.spines['left'].set_position('zero')    # Eje Y en x=0
    ax.spines['bottom'].set_position('zero')  # Eje X en y=0
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Mostrar flechas en los extremos de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Etiquetas y leyenda
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Amplitud')
    ax.set_title('Señal Cosenoidal')
    ax.grid(True)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.02), ncol=1)

    # Mostrar gráfico
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))
    plt.gca().xaxis.set_major_locator(MultipleLocator(1))
    plt.show()

if __name__ == "__main__":
    s, t, A, f, Q0 = funcion_cosenoidal(5, 1, 2*np.pi, 1000)
    graficar_funcion_cosenoidal(s, t, A, f, Q0)
