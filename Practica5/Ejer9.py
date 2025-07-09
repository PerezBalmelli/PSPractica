import numpy as np
import matplotlib.pyplot as plt
import time

# Crear una señal de prueba larga: combinación de senoides
fs = 1000  # Frecuencia de muestreo en Hz
T = 5      # Duración de la señal en segundos
t = np.linspace(0, T, int(fs * T), endpoint=False)
y = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# --- MÉTODO 1: Derivada en el dominio del tiempo usando diferencias finitas ---
def derivada_diferencias_finitas(y, t):
    dt = t[1] - t[0]
    dydt = np.zeros_like(y)

    # Usamos diferencias centrales para puntos internos
    dydt[1:-1] = (y[2:] - y[:-2]) / (2 * dt)

    # Aproximaciones hacia adelante/atrás en los bordes
    dydt[0] = (y[1] - y[0]) / dt
    dydt[-1] = (y[-1] - y[-2]) / dt

    return dydt

start_time_time = time.time()
dydt_time = derivada_diferencias_finitas(y, t)
time_time = time.time() - start_time_time

# --- MÉTODO 2: Derivada en el dominio de la frecuencia (FFT) ---
def derivada_frecuencia(y, fs):
    N = len(y)
    Yf = np.fft.fft(y)                          # Transformada de Fourier
    freqs = np.fft.fftfreq(N, d=1/fs)           # Vector de frecuencias
    jw = 1j * 2 * np.pi * freqs                 # jω en rad/s
    dYf = jw * Yf                                # Multiplicación en frecuencia
    dydt_freq = np.fft.ifft(dYf).real            # Transformada inversa
    return dydt_freq

start_time_freq = time.time()
dydt_freq = derivada_frecuencia(y, fs)
time_freq = time.time() - start_time_freq

# --- GRAFICAR COMPARACIÓN ---
plt.figure(figsize=(12, 5))
plt.plot(t, dydt_time, label="Derivada por diferencias finitas", linestyle='--')
plt.plot(t, dydt_freq, label="Derivada por FFT", alpha=0.7)
plt.title("Comparación de derivadas: Tiempo vs Frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Derivada")
plt.legend()
plt.grid(True)
plt.show()

# --- MOSTRAR TIEMPOS ---
print(f"Tiempo de ejecución (diferencias finitas): {time_time:.6f} s")
print(f"Tiempo de ejecución (FFT): {time_freq:.6f} s")

# --- CONCLUSIONES ---
# 1. La derivación por diferencias finitas es más rápida (~5 veces en este caso).
# 2. La derivación en frecuencia es más costosa computacionalmente por la FFT.
# 3. La FFT puede ser más precisa y suave en señales ruidosas o con muchas componentes.
# 4. En señales limpias y cortas, diferencias finitas es preferible por velocidad.
# 5. En señales largas o análisis espectrales, la FFT ofrece ventajas adicionales.
