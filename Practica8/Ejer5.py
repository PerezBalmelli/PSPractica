import numpy as np
import matplotlib.pyplot as plt
import time

# --- INICIO DEL TEMPORIZADOR GENERAL ---
start_time = time.time()

# Paso 1: Definir la señal original
N = 10**6
n = np.arange(N)
x = n + 50 * (np.cos(2 * np.pi * n / 40) ** 3)

# Paso 2: Simetrizar 5% inicial y final
M = int(0.05 * N)
x_i = x[:M]
x_f = x[-M:]

x_i_s = x_i[::-1]
x_f_s = x_f[::-1]

# Paso 3: Empalme lineal entre extremos simetrizados
alpha = np.arange(M)
x_c = ((M - alpha) * x_f_s + alpha * x_i_s) / M

# Paso 4: Concatenar señal original + empalme
x_sym = np.concatenate([x, x_c])

# Paso 5: FFT de la señal extendida
X_fft = np.fft.fft(x_sym)
absX = np.abs(X_fft)

# Paso 6: Cuántos coeficientes necesito para 99% de energía
ind = np.argsort(absX)[::-1]
i = 1
while (np.linalg.norm(X_fft[ind[:i]]) / np.linalg.norm(X_fft))**2 < 0.99:
    i += 1
needed = i

print(f"Se necesitan {needed} coeficientes para retener el 99% de la energía.")

# Paso 7: Reconstrucción
X_reduced = np.zeros_like(X_fft, dtype=complex)
X_reduced[ind[:needed]] = X_fft[ind[:needed]]
x_reconstructed = np.fft.ifft(X_reduced).real

# --- FIN DEL TEMPORIZADOR GENERAL ---
duration = time.time() - start_time
print(f"\n--- Tiempo total de cálculo: {duration:.2f} segundos ---")

# Paso 8: Gráfica señal original vs reconstruida (solo primeros N)
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n, x, label="Original", linewidth=1.5)
plt.plot(n, x_reconstructed[:N], '--', label="Reconstruida", linewidth=1.5)
plt.title("Señal original vs reconstruida (primeros N)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.legend()
plt.grid()

# Paso 9: Espectro
plt.subplot(1, 2, 2)
freqs = np.fft.fftfreq(len(x_sym))
plt.plot(freqs[:len(freqs)//2], absX[:len(absX)//2])
plt.title("Magnitud de la FFT de la señal extendida con empalme")
plt.xlabel("Frecuencia normalizada")
plt.ylabel("|X[k]|")
plt.grid()

plt.tight_layout()
plt.show()
