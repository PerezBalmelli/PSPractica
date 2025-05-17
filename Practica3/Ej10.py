'''
10. Aplicar el filtro de la media móvil a una señal con ruido y observar el resultado.
'''

import numpy as np
import matplotlib.pyplot as plt
from Ej9 import*

def generar_senal_con_ruido(largo, amplitud=1.0, ruido=0.5):
    """
    Genera una señal senoidal con ruido blanco.
    """
    t = np.arange(largo)
    senal = amplitud * np.sin(2 * np.pi * t / 40)  # sinusoide
    ruido_blanco = np.random.normal(0, ruido, largo)  # ruido gaussiano
    return t, senal + ruido_blanco

def graficar_senal_ruido(t, original, filtrada):
    plt.figure(figsize=(10, 4))
    plt.plot(t, original, label="Señal con ruido", alpha=0.6)
    plt.plot(t, filtrada, label="Señal filtrada (media móvil)", color="red", linewidth=2)
    plt.title("Filtro de Media Móvil aplicado a una Señal con Ruido")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    largo = 200
    ancho_filtro = 11  # debe ser impar

    t, senal_ruidosa = generar_senal_con_ruido(largo)
    kernel = filtro_media_movil_kernel(ancho_filtro)
    senal_filtrada = aplicar_filtro(senal_ruidosa, kernel)

    graficar_senal_ruido(t, senal_ruidosa, senal_filtrada)