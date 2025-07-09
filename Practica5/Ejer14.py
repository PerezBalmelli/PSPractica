import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parámetros de las Señales ---
f0 = 5         # Frecuencia fundamental (5 Hz)
N_periodos = 4 # Número de períodos a generar para la señal periódica
fs = 1000      # Frecuencia de muestreo (debe ser alta para capturar bien la forma)

# Calculamos el período y el vector de tiempo para un solo ciclo
T0 = 1 / f0
t_un_periodo = np.arange(0, T0, 1 / fs)
puntos_por_periodo = len(t_un_periodo)

# --- 2. Generación de las Señales ---

# Generar un único período de la señal diente de sierra
# La fórmula t/T0 crea una rampa de 0 a 1 dentro del período.
un_periodo_r = t_un_periodo / T0

# a) Señal periódica r̃(t)
# Repetimos el ciclo N_periodos veces
r_tilde_t = np.tile(un_periodo_r, N_periodos)
t_total = np.arange(0, N_periodos * T0, 1 / fs)

# b) Señal aperiódica r(t)
# Creamos un array de ceros y colocamos el ciclo único al principio
r_t = np.zeros_like(r_tilde_t)
r_t[:puntos_por_periodo] = un_periodo_r


# --- 3. Cálculo de los Espectros de Frecuencia (FFT) ---

# Función para calcular y normalizar la FFT
def calcular_espectro(senal):
    N = len(senal)
    # Calculamos la FFT y la centramos para que la frecuencia 0 esté en el medio
    espectro = np.fft.fftshift(np.fft.fft(senal))
    # Normalizamos la magnitud
    magnitud = np.abs(espectro) / N
    # Creamos el eje de frecuencias correspondiente
    frecuencias = np.fft.fftshift(np.fft.fftfreq(N, 1 / fs))
    return frecuencias, magnitud

# Calculamos los espectros para ambas señales
f_tilde, mag_tilde = calcular_espectro(r_tilde_t)
f_aperiodica, mag_aperiodica = calcular_espectro(r_t)

# --- 4. Visualización ---

plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(12, 10))
fig.suptitle('Comparación de Señal Periódica y Aperiódica', fontsize=16)

# Gráfico 1: Señal periódica en el tiempo
ax1 = plt.subplot(2, 2, 1)
ax1.plot(t_total, r_tilde_t, color='blue')
ax1.set_title('a) Señal Periódica: $\\tilde{r}(t)$')
ax1.set_xlabel('Tiempo [s]')
ax1.set_ylabel('Amplitud')

# Gráfico 2: Espectro de la señal periódica
ax2 = plt.subplot(2, 2, 2)
ax2.plot(f_tilde, mag_tilde, color='blue')
ax2.set_title('b) Espectro de Señal Periódica: $|\\tilde{R}(f)|$')
ax2.set_xlabel('Frecuencia [Hz]')
ax2.set_ylabel('Magnitud Normalizada')
ax2.set_xlim(-50, 50) # Acercamos para ver los armónicos

# Gráfico 3: Señal aperiódica en el tiempo
ax3 = plt.subplot(2, 2, 3)
ax3.plot(t_total, r_t, color='red')
ax3.set_title('c) Señal Aperiódica: $r(t)$')
ax3.set_xlabel('Tiempo [s]')
ax3.set_ylabel('Amplitud')

# Gráfico 4: Espectro de la señal aperiódica
ax4 = plt.subplot(2, 2, 4)
ax4.plot(f_aperiodica, mag_aperiodica, color='red')
ax4.set_title('d) Espectro de Señal Aperiódica: $|R(f)|$')
ax4.set_xlabel('Frecuencia [Hz]')
ax4.set_ylabel('Magnitud Normalizada')
ax4.set_xlim(-50, 50) # Usamos el mismo zoom para comparar

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()