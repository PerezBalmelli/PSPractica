import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal cuadrada
T = 2 * np.pi         # Periodo
T1 = np.pi / 2        # Ancho del pulso
w0 = 2 * np.pi / T    # Frecuencia fundamental

# Tiempo
t = np.linspace(-2*T, 2*T, 1000)

# Señal cuadrada periódica
def square_wave(t, T, T1):
    return np.where(np.abs((t % T) - T/2) < T1/2, 1, 0)

x_t = square_wave(t, T, T1)

# Serie de Fourier: coeficientes Xn
N = 50
n = np.arange(-N, N+1)
Xn = (T1 / T) * np.sinc(n * T1 / T)

# Frecuencias correspondientes
frequencies = n * w0

# Graficar la señal
plt.figure(figsize=(12, 4))
plt.plot(t, x_t, color='orange')
plt.title("Señal Cuadrada Periódica")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Módulo de la transformada
plt.figure(figsize=(12, 4))
plt.stem(frequencies, np.abs(Xn), linefmt='orange', markerfmt='o', basefmt='magenta')
plt.title("Módulo de la Transformada de Fourier (|X(ω)|)")
plt.xlabel("Frecuencia (rad/s)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

# Fase de la transformada
plt.figure(figsize=(12, 4))
plt.stem(frequencies, np.angle(Xn), linefmt='orange', markerfmt='o', basefmt='magenta')
plt.title("Fase de la Transformada de Fourier (∠X(ω))")
plt.xlabel("Frecuencia (rad/s)")
plt.ylabel("Fase (rad)")
plt.grid(True)
plt.show()

# Verificación de Parseval
# Energía en el tiempo (solo un periodo)
dt = t[1] - t[0]
mask_period = (t >= 0) & (t < T)
Et = np.sum(np.abs(x_t[mask_period])**2) * dt

# Energía en frecuencia (Parseval)
Ef = T * np.sum(np.abs(Xn)**2)

print(f"Energía en el tiempo: {Et:.5f}")
print(f"Energía en la frecuencia: {Ef:.5f}")
print("¿Se cumple Parseval?", np.isclose(Et, Ef))

