import numpy as np
import matplotlib.pyplot as plt
import time

# --- INICIO DEL TEMPORIZADOR GENERAL ---


# Paso 1: Definir la señal original
n = np.arange(1,101)
x = n + 50 * (np.cos(2 * np.pi * n / 40) ** 3)

# Paso 2: Simetrizar la señal (para que sea real y par)
x_sym = np.concatenate((x, x[::-1]))

total_start_time = time.time()

# Paso 3: Calcular la FFT de la señal simetrizada
X_fft = np.fft.fft(x_sym)
absX = np.abs(X_fft)

# Paso 4: Ordenar coeficientes por magnitud
ind = np.argsort(absX)[::-1]  # índices ordenados de mayor a menor
XX = absX[ind]

# Paso 5: Calcular cuántos coeficientes necesito para el 99% de la energía
i = 1
while (np.linalg.norm(X_fft[ind[:i]]) / np.linalg.norm(X_fft))**2 < 0.99:
    i += 1
needed = i

print(f"Se necesitan {needed} coeficientes para retener el 99% de la energía (FFT).")

# Paso 6: Reconstrucción de la señal con solo los coeficientes principales
X_reduced = np.zeros_like(X_fft, dtype=complex)
X_reduced[ind[:needed]] = X_fft[ind[:needed]]
x_reconstructed = np.fft.ifft(X_reduced).real

# --- FIN DEL TEMPORIZADOR GENERAL ---
total_duration = time.time() - total_start_time
print(f"\n--- Tiempo total de cálculo: {total_duration:.4f} segundos ---")

# Paso 7: Graficar señal original vs reconstruida (solo primer mitad de la señal)
L = len(x)  # largo de la señal original
n_full = np.arange(len(x_sym))

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n, x, label="Original", linewidth=2)
plt.plot(n, x_reconstructed[:L], '--', label="Reconstruida (99%)", linewidth=2)
plt.title("Señal original y reconstruida con FFT")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.legend()
#
# # Paso 8: Graficar magnitud del espectro (mitad positiva)
# freqs = np.fft.fftfreq(len(x_sym))
#
# plt.subplot(1, 2, 2)
# plt.plot(freqs[:len(freqs)//2], absX[:len(absX)//2], color='orange')
# plt.title("Magnitud de la FFT de la señal simetrizada")
# plt.xlabel("Frecuencia normalizada")
# plt.ylabel("|X[k]|")
# plt.grid()

plt.tight_layout()
plt.show()
