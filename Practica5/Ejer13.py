import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configuración de la Señal y el Filtro ---

# Parámetros de la señal
N = 1000  # Número de puntos de la señal
T = 1.0 / 800.0  # Período de muestreo
t = np.linspace(0.0, N*T, N, endpoint=False)

# Crear una señal compuesta: una onda de 10Hz (lenta) + una de 120Hz (rápida/ruido)
senal_original = np.sin(10.0 * 2.0*np.pi*t) + 0.5 * np.sin(120.0 * 2.0*np.pi*t)
# Añadir un poco de ruido gaussiano para realismo
senal_original += 0.2 * np.random.randn(N)


# Parámetros del filtro de media móvil
M = 30  # Tamaño de la ventana de la media móvil. Un valor mayor suaviza más.

# La respuesta al impulso de un filtro de media móvil es una secuencia de M unos,
# normalizada por el tamaño de la ventana M.
h_media_movil = np.ones(M) / M


# --- 2. Aplicación del Filtro en el Dominio de la Frecuencia ---

# La longitud de la convolución final es N + M - 1
L = N + M - 1

# Calculamos la FFT de la señal y del filtro, rellenando con ceros (padding)
# hasta la longitud L para que la multiplicación sea válida.
senal_fft = np.fft.fft(senal_original, n=L)
filtro_fft = np.fft.fft(h_media_movil, n=L)

# Multiplicamos en el dominio de la frecuencia
senal_filtrada_fft = senal_fft * filtro_fft

# Regresamos al dominio del tiempo con la IFFT
senal_suavizada = np.fft.ifft(senal_filtrada_fft)

# La salida real es la parte real del resultado (la parte imaginaria es residual)
# y la recortamos a la longitud original N para la visualización.
senal_suavizada = np.real(senal_suavizada[:N])


# --- 3. Visualización y Análisis ---

# Configuración de la figura para los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axs = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Análisis del Filtro de Media Móvil', fontsize=16)


# Gráfico 1: Señal Original vs. Señal Suavizada (Dominio del Tiempo)
axs[0].plot(t, senal_original, label='Señal Original', color='gray', alpha=0.7)
axs[0].plot(t, senal_suavizada, label=f'Señal Suavizada (Ventana M={M})', color='red', linewidth=2)
axs[0].set_title('Efecto del Filtro en el Dominio del Tiempo')
axs[0].set_xlabel('Tiempo [s]')
axs[0].set_ylabel('Amplitud')
axs[0].legend()
axs[0].set_xlim(t[0], t[-1])


# Gráfico 2: Respuesta en Frecuencia del Filtro
# La respuesta en frecuencia es la magnitud de la FFT del filtro.
freq_axis = np.fft.fftfreq(L, T) # Eje de frecuencias

# Tomamos solo la mitad positiva del espectro para visualizar
indices_positivos = np.where(freq_axis >= 0)
freq_positivas = freq_axis[indices_positivos]
magnitud_filtro = np.abs(filtro_fft[indices_positivos])

axs[1].plot(freq_positivas, magnitud_filtro, color='blue', linewidth=2)
axs[1].set_title('Respuesta en Frecuencia del Filtro de Media Móvil')
axs[1].set_xlabel('Frecuencia [Hz]')
axs[1].set_ylabel('Ganancia (Magnitud)')
axs[1].set_xlim(0, 1 / (2*T)) # Mostrar hasta la frecuencia de Nyquist


plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()