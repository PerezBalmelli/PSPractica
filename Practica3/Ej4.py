'''
4. Implementar una función que genere la delta de Kronecker delta[n-k].
El largo de la señal y el centro k deben ser parámetros de entrada.
'''
from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

def delta_kronecker(largo, k):
    """
    Genera una señal delta de Kronecker δ[n - k] de longitud 'largo', centrada automáticamente.
    
    Parámetros:
    - largo: int -> cantidad total de muestras
    - k: int -> valor de n en el que δ[n - k] = 1

    Retorna:
    - n: eje temporal (vector)
    - delta: vector con ceros y un único 1 en la posición correspondiente
    """
    if largo <= k or largo <= 0 or k*2 > largo:
        raise ValueError("El valor de 'largo' debe ser mayor que 'k'.")

    if largo % 2 == 0:
        n_inicio = -largo // 2
        n = np.arange(n_inicio, n_inicio + largo + 1)
    else:    
        n_inicio = (-largo // 2)+1
        n = np.arange(n_inicio, n_inicio + largo)
    delta = np.where(n == k, 1, 0)
    return n, delta

def graficar_delta_kronecker(n, delta, k):
    """
    Grafica la señal delta de Kronecker con flecha y estilo personalizado.
    
    Parámetros:
    - n: vector del eje temporal
    - delta: señal delta
    - k: índice donde δ[n - k] = 1
    """
    plt.stem(n, delta, linefmt='r', markerfmt='ro', basefmt=' ')
    if k < 0: 
        plt.title(f'Delta de Kronecker δ[n + {abs(k)}]')
    else:
        plt.title(f'Delta de Kronecker δ[n - {k}]')
    plt.xlabel('n')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Flecha roja en el impulso
    altura_flecha = 1.05
    plt.annotate('', xy=(k, altura_flecha), xytext=(k, -0.055),
                arrowprops=dict(facecolor='red', shrink=0.05, width=3, headwidth=8))

    # Aumentar grosor de ejes
    ax = plt.gca()
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_ylim(-0.1, 1.5)
    ax.tick_params(width=2)
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_locator(MultipleLocator(1))

    plt.show()

if __name__ == "__main__":
    print("Ejemplo de delta de Kronecker (Ejercicio 4):")
    largo = int(input("Ingrese el largo de la señal: "))
    k = int(input("Ingrese el valor de k (centro de la delta): "))

    n, delta = delta_kronecker(largo, k)
    graficar_delta_kronecker(n, delta, k)
