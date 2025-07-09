import numpy as np
import matplotlib.pyplot as plt

# Crear una señal de prueba larga: combinación de senoides
fs = 1000  # Frecuencia de muestreo (Hz)
T = 5      # Duración de la señal (segundos)
t = np.linspace(0, T, int(fs * T), endpoint=False)
y = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# --- Función para calcular la integral indefinida en el dominio de la frecuencia ---
def integral_frecuencia(y, fs):
    N = len(y)
    Yf = np.fft.fft(y)
    freqs = np.fft.fftfreq(N, d=1/fs)
    jw = 1j * 2 * np.pi * freqs

    # Evitar división por cero en DC (frecuencia = 0)
    jw[0] = 1  # para evitar dividir por cero
    Yf_integrada = Yf / jw
    Yf_integrada[0] = 0  # fijamos la constante de integración (DC) en 0

    y_integrada = np.fft.ifft(Yf_integrada).real
    return y_integrada

# Calcular integral indefinida en el dominio de la frecuencia
y_integrada = integral_frecuencia(y, fs)

# --- Cálculo de la energía ---
# 1. Energía en el tiempo: suma discreta
energia_tiempo = np.sum(y**2) / fs

# 2. Energía en el dominio de la frecuencia (Parseval)
energia_frecuencia = np.sum(np.abs(np.fft.fft(y))**2) / (fs * len(y))

# 3. Energía con regla del trapecio (más precisa)
energia_trapz = np.trapz(y**2, t)

# --- Graficar la señal y su integral ---
plt.figure(figsize=(12, 5))
plt.plot(t, y, label="Señal original")
plt.plot(t, y_integrada, label="Integral (frecuencia)", linestyle='--')
plt.title("Integral indefinida de la señal en el dominio de la frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud / Integral")
plt.legend()
plt.grid(True)
plt.show()

# --- Mostrar resultados de energía ---
print(f"Energía (dominio del tiempo):     {energia_tiempo:.6f}")
print(f"Energía (dominio de la frecuencia): {energia_frecuencia:.6f}")
print(f"Energía (trapecios):               {energia_trapz:.6f}")

# --- CONCLUSIONES ---
# 1. La integral indefinida puede calcularse dividiendo por jω en el dominio de la frecuencia.
# 2. Se debe evitar la división por cero en ω = 0 (DC) asignando un valor manualmente.
# 3. La energía calculada por diferentes métodos coincide, lo que valida la equivalencia de representaciones.
# 4. La integración en frecuencia puede ser útil para filtrar o suavizar señales, pero requiere cuidado numérico.
