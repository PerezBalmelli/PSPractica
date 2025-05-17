'''
9. Aplicar el filtro de la media móvil a la delta de Kronecker. Interpretar el resultado.
'''

from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

def delta_kronecker(largo, k):
    """
    Genera la delta de Kronecker δ[n - k].
    """
    n = np.arange(largo)
    delta = np.where(n == k, 1, 0)
    return n, delta

def filtro_media_movil_kernel(ancho):
    """
    Genera el kernel del filtro de media móvil de ancho impar.
    """
    if ancho % 2 == 0:
        raise ValueError("El ancho del filtro debe ser impar.")
    return np.ones(ancho) / ancho

def aplicar_filtro(x, h):
    """
    Aplica el filtro (convolución) entre la señal x y el kernel h.
    """
    return np.convolve(x, h, mode='same')

def graficar_senales(n_delta, delta, kernel, salida):
    """
    Grafica la delta, el kernel y la salida filtrada.
    """
    fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=False)

    axs[0].stem(n_delta, delta)
    axs[0].set_xlim(-1, 21)
    axs[0].set_ylim(-0.5, 2.1)
    axs[0].xaxis.set_major_locator(MultipleLocator(1))
    axs[0].set_title("Delta de Kronecker δ[n - k]")
    axs[0].grid()

    axs[1].stem(np.arange(len(kernel)), kernel, linefmt='g', markerfmt='go', basefmt='k')
    axs[1].set_xlim(-1, 21)
    axs[1].xaxis.set_major_locator(MultipleLocator(1))
    axs[1].set_title("Kernel del filtro (respuesta al impulso)")
    axs[1].grid()

    axs[2].stem(np.arange(len(salida)), salida, linefmt='r', markerfmt='ro', basefmt='k')
    axs[2].set_xlim(-1, 21)
    axs[2].xaxis.set_major_locator(MultipleLocator(1))
    axs[2].set_title("Salida de la convolución")
    axs[2].grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    largo = 21
    k = largo // 2  # centro de la delta
    ancho_filtro = 5  # debe ser impar

    n, delta = delta_kronecker(largo, k)
    kernel = filtro_media_movil_kernel(ancho_filtro)
    salida = aplicar_filtro(delta, kernel)

    graficar_senales(n, delta, kernel, salida)
