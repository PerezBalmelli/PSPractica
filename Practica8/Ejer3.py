import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import time

# --- INICIO DEL TEMPORIZADOR GENERAL ---
total_start_time = time.time()

# Paso 1: Definir la señal con 10^6 puntos
n = np.arange(1, 10**6 + 1)
x = n + 50 * (np.cos(2 * np.pi * n / 40) ** 3)

# Paso 2: Calcular la DCT (tipo II ortonormal)
print("Calculando la DCT...")
start_time = time.time()
X = dct(x, type=2, norm='ortho')
duration = time.time() - start_time
print(f"DCT calculada en {duration:.4f} segundos.")

# Paso 3: Ordenar coeficientes por magnitud
print("Ordenando coeficientes...")
start_time = time.time()
absX = np.abs(X)
ind = np.argsort(absX)[::-1]  # índices ordenados de mayor a menor
XX = absX[ind] # Coeficientes ordenados por magnitud
duration = time.time() - start_time
print(f"Coeficientes ordenados en {duration:.4f} segundos.")

# Paso 4: Calcular cuántos coeficientes se necesitan para el 99% de la energía
print("Calculando el número de coeficientes para el 99% de la energía...")
start_time = time.time()
i = 1
# Usar la suma de cuadrados de los coeficientes para calcular la energía
total_energy_sq = np.sum(X**2)
current_energy_sq = 0.0
while (current_energy_sq / total_energy_sq) < 0.99:
    current_energy_sq = np.sum(X[ind[:i]]**2)
    i += 1
needed = i - 1 # Se resta 1 porque el bucle termina después de superar el umbral
duration = time.time() - start_time
print(f"Cálculo de energía finalizado en {duration:.4f} segundos.")

print(f"Se necesitan {needed} coeficientes para retener el 99% de la energía.")

# Paso 5: Reconstrucción de la señal con solo los coeficientes principales
print("Reconstruyendo la señal...")
start_time = time.time()
X_reduced = np.zeros_like(X)
X_reduced[ind[:needed]] = X[ind[:needed]]
x_reconstructed = idct(X_reduced, type=2, norm='ortho')
duration = time.time() - start_time
print(f"Señal reconstruida en {duration:.4f} segundos.")

# --- FIN DEL TEMPORIZADOR GENERAL ---
total_duration = time.time() - total_start_time
print(f"\n--- Tiempo total de cálculo: {total_duration:.4f} segundos ---")


# Paso 6: Gráficas
print("\nGenerando gráficas...")
plt.figure(figsize=(14, 6))

# Gráfico de la señal original y reconstruida (puede ser denso)
plt.subplot(1, 2, 1)
# Se grafica solo una porción para mayor claridad (e.g., los primeros 1000 puntos)
plt.plot(n[:1000], x[:1000], label="Original", linewidth=2)
plt.plot(n[:1000], x_reconstructed[:1000], '--', label=f"Reconstruida ({needed} coefs)", linewidth=2)
plt.title("Señal Original y Reconstruida (Primeros 1000 puntos)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.legend()
plt.grid(True)


# Gráfico de la magnitud de los coeficientes DCT ordenados
plt.subplot(1, 2, 2)
plt.plot(np.arange(len(XX)), XX)
plt.title("Magnitud de Coeficientes DCT (ordenados)")
plt.xlabel("Índice de Coeficiente Ordenado")
plt.ylabel("|X[k]|")
plt.yscale('log') # Escala logarítmica para ver mejor la caída de energía
plt.grid(True)


plt.tight_layout()
plt.show()
print("Proceso completado.")