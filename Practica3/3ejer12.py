import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve


# -----------------------------
# FUNCIONES AUXILIARES
# -----------------------------

def potencia_eficaz_local(x, ancho_muestras):
    """Calcula la potencia eficaz (RMS) en ventanas centradas."""
    N = len(x)
    salida = np.zeros(N)
    medio = ancho_muestras // 2
    for i in range(N):
        inicio = max(0, i - medio)
        fin = min(N, i + medio)
        ventana = x[inicio:fin]
        salida[i] = np.sqrt(np.mean(ventana ** 2))
    return salida


def filtro_media_movil(x, ancho_muestras):
    """Aplica un filtro de media móvil de ancho fijo."""
    kernel = np.ones(ancho_muestras) / ancho_muestras
    return convolve(x, kernel, mode='same')


def calcular_envolvente(x, ancho):
    """Calcula la envolvente energética usando RMS local + media móvil."""
    rms = potencia_eficaz_local(x, ancho)
    return filtro_media_movil(rms, ancho)


# -----------------------------
# PARÁMETROS GENERALES
# -----------------------------

fs = 1000  # Frecuencia de muestreo (Hz)
f = 5  # Frecuencia de senoide (Hz)
duracion = 2  # Duración (s)
t = np.arange(0, duracion, 1 / fs)
N = len(t)

# -----------------------------
# SEÑALES A ANALIZAR
# -----------------------------

# Senoide pura
senoide = np.cos(2 * np.pi * f * t)

# Senoide con ruido blanco gaussiano
np.random.seed(0)  # Para reproducibilidad
ruido = np.random.normal(0, 0.5, N)
senoide_ruido = senoide + ruido

# -----------------------------
# ENVOLVENTES ENERGÉTICAS
# -----------------------------

anchos_ms = [25, 100, 200]
anchos_muestras = [int(fs * ms / 1000) for ms in anchos_ms]

envolventes_puras = []
envolventes_con_ruido = []

for ancho in anchos_muestras:
    envolvente_pura = calcular_envolvente(senoide, ancho)
    envolvente_ruido = calcular_envolvente(senoide_ruido, ancho)

    envolventes_puras.append(envolvente_pura)
    envolventes_con_ruido.append(envolvente_ruido)

# -----------------------------
# GRÁFICA COMPARATIVA
# -----------------------------

plt.figure(figsize=(12, 10))

for i in range(3):
    # Fila 1: senoide pura
    plt.subplot(3, 2, 2 * i + 1)
    plt.plot(t, senoide, color='gray', alpha=0.4, label='Senoide pura')
    plt.plot(t, envolventes_puras[i], label=f'Envolvente {anchos_ms[i]} ms', color='blue')
    plt.title(f'Pura – Filtro {anchos_ms[i]} ms')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()

    # Fila 2: senoide con ruido
    plt.subplot(3, 2, 2 * i + 2)
    plt.plot(t, senoide_ruido, color='gray', alpha=0.4, label='Senoide con ruido')
    plt.plot(t, envolventes_con_ruido[i], label=f'Envolvente {anchos_ms[i]} ms', color='red')
    plt.title(f'Con ruido – Filtro {anchos_ms[i]} ms')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# COMENTARIOS E INTERPRETACIÓN DE RESULTADOS
# ------------------------------------------------------------
# Comparamos la envolvente energética de:
# 1. Una senoide limpia.
# 2. Una senoide con ruido.

# En la senoide limpia:
# - La envolvente (potencia eficaz) es estable y suave.
# - Representa correctamente la energía constante de la senoide.

# En la senoide con ruido:
# - La envolvente presenta más variación por la energía introducida por el ruido.
# - Aunque se aplique el filtro de media móvil, aún se notan fluctuaciones.
# - El ruido incrementa la energía aparente de la señal.

# Interpretación por ancho del filtro:
# - Filtro de 25 ms: responde rápido, pero la envolvente es más ruidosa.
# - Filtro de 100 ms: suaviza bastante bien, equilibrio entre detalle y estabilidad.
# - Filtro de 200 ms: muy suave, pero puede ocultar cambios reales en señales con variaciones rápidas.

# Conclusión:
# - La envolvente energética permite visualizar la variación de energía a lo largo del tiempo.
# - Es útil para señales ruidosas porque permite extraer información de fondo ignorando variaciones rápidas.
# - El filtro actúa como un suavizador, pero el ancho debe elegirse según el contexto de la señal.
# ------------------------------------------------------------

