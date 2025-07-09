import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct

import time

# --- INICIO DEL TEMPORIZADOR GENERAL ---
total_start_time = time.time()

# Paso 1: Definir la señal
n = np.arange(1, 10**6 + 1)
x = n + 50 * (np.cos(2 * np.pi * n / 40) ** 3)

# Paso 2: Calcular la DCT (tipo II ortonormal)

X = dct(x, type=2, norm='ortho')

# Paso 3: Ordenar coeficientes por magnitud
absX = np.abs(X)
ind = np.argsort(absX)[::-1]  # índices ordenados de mayor a menor
XX = absX[ind]

# Paso 4: Calcular cuántos coeficientes necesito para el 99% de la energía
i = 1
while (np.linalg.norm(X[ind[:i]]) / np.linalg.norm(X))**2 < 0.99:
    i += 1
needed = i

print(f"Se necesitan {needed} coeficientes para retener el 99% de la energía.")

# Paso 5: Reconstrucción de la señal con solo los coeficientes principales
X_reduced = np.zeros_like(X)
X_reduced[ind[:needed]] = X[ind[:needed]]
x_reconstructed = idct(X_reduced, type=2, norm='ortho')

# --- FIN DEL TEMPORIZADOR GENERAL ---
total_duration = time.time() - total_start_time
print(f"\n--- Tiempo total de cálculo: {total_duration:.4f} segundos ---")


# Paso 6: Gráficas
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n, x, label="Original", linewidth=2)
plt.plot(n, x_reconstructed, '--', label="Reconstruida (99%)", linewidth=2)
plt.title("Señal original y reconstruida")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.legend()

# plt.subplot(1, 2, 2)
# plt.stem(np.arange(len(X)), absX, basefmt=" ")
# plt.title("Magnitud de coeficientes DCT")
# plt.xlabel("Índice k")
# plt.ylabel("|X[k]|")

plt.tight_layout()
plt.show()
