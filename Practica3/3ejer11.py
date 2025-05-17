import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# 1. Parámetros de la señal
fs = 1000          # Frecuencia de muestreo en Hz
f = 5              # Frecuencia de la senoide (Hz)
duracion = 2       # Duración en segundos
t = np.arange(0, duracion, 1/fs)

# Generar senoide
senoide = np.cos(2 * np.pi * f * t)

# 2. Función para calcular potencia eficaz (RMS) local
def potencia_eficaz_local(x, ancho_muestras):
    N = len(x)
    salida = np.zeros(N)
    medio = ancho_muestras // 2
    for i in range(N):
        inicio = max(0, i - medio)
        fin = min(N, i + medio)
        ventana = x[inicio:fin]
        salida[i] = np.sqrt(np.mean(ventana**2))
    return salida

# 3. Filtro de media móvil
def filtro_media_movil(x, ancho_muestras):
    kernel = np.ones(ancho_muestras) / ancho_muestras
    return convolve(x, kernel, mode='same')

# 4. Anchos de filtro a probar (en milisegundos)
anchos_ms = [25, 100, 200]
anchos_muestras = [int(fs * ms / 1000) for ms in anchos_ms]

# 5. Cálculo de envolventes energéticas
envolventes = []

for ancho in anchos_muestras:
    rms_local = potencia_eficaz_local(senoide, ancho)
    envolvente = filtro_media_movil(rms_local, ancho)
    envolventes.append(envolvente)

# 6. Graficar resultados
plt.figure(figsize=(12, 8))

for i, envolvente in enumerate(envolventes):
    plt.subplot(3, 1, i+1)
    plt.plot(t, senoide, label='Senoide', color='gray', alpha=0.4)
    plt.plot(t, envolvente, label=f'Envolvente energética ({anchos_ms[i]} ms)', color='blue')
    plt.title(f'Envolvente energética – Filtro de {anchos_ms[i]} ms')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()