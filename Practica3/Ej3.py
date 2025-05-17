'''
3. Implementar un sistema que se componga por n bloques del sistema 1.a dispuestos en serie.
Probarlo para alguna señal de entrada con valores de n=10,n=50,n=100. 
Analizar qué ocurriría si n crece mucho.
'''

from Ej1 import*
from Ej2 import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Función que aplica n bloques del sistema y(t) = 3·x(t)
def aplicar_bloques_en_serie(x, n):
    return (float(3) ** n) * x  # Evita overflow al usar float

def graficar_bloques_en_serie(x):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, label='Señal de entrada', color='blue', marker='o')

    valores_n = [10, 50, 100]
    colores = ['red', 'green', 'orange']

    for i, n in enumerate(valores_n):
        try:
            y = aplicar_bloques_en_serie(x, n)
            ax.plot(y, label=f'Salida con {n} bloques en serie', color=colores[i], marker='o')
        except OverflowError:
            print(f"Overflow al calcular para n = {n}")
            continue

    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Amplitud')
    ax.set_title('Salida del sistema con n bloques en serie')
    ax.legend()

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True)

    # Escala logarítmica para evitar que valores grandes saturen la gráfica
    ax.set_yscale('log')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Definir la señal de entrada
    x1 = np.array([1, 5, 10, 20, 50, 100])

    # Graficar la salida del sistema con bloques en serie
    graficar_bloques_en_serie(x1)