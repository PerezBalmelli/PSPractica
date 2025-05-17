import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T0 = 4                  # Período total de la onda cuadrada
T1 = T0 / 4             # Mitad del pulso (ancho positivo)
t = np.linspace(-8, 8, 2000)  # Tiempo desde -8 a 8 segundos

# Onda cuadrada centrada: primer pulso entre -T1 y T1
def custom_square_wave(t, T0, T1):
    t_mod = ((t + T0/2) % T0) - T0/2
    return np.where(np.abs(t_mod) < T1, 1, -1)

# Serie de Fourier con fase alineada (desfase de T0/4)
def fourier_series_square_wave_shifted(t, T0, num_harmonics):
    result = np.zeros_like(t)
    phase_shift = T0 / 4  # Para alinear con la onda cuadrada centrada
    for k in range(1, num_harmonics + 1, 2):  # Solo armónicos impares
        result += (4 / (np.pi * k)) * np.sin(2 * np.pi * k * (t + phase_shift) / T0)
    return result

# Calcular la onda cuadrada original
original = custom_square_wave(t, T0, T1)

# Aproximaciones con 5 y 10 armónicos
approx_5 = fourier_series_square_wave_shifted(t, T0, 5)
approx_10 = fourier_series_square_wave_shifted(t, T0, 10)

# Graficar los resultados
plt.figure(figsize=(12, 6))

# Gráfico con 5 armónicos
plt.subplot(2, 1, 1)
plt.plot(t, original, '--', label='Onda Cuadrada (original)', color='black')
plt.plot(t, approx_5, label='Serie de Fourier (5 armónicos)', color='green')
plt.axvline(0, color='gray', linestyle=':', linewidth=1)
plt.title('Aproximación con 5 armónicos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Gráfico con 10 armónicos
plt.subplot(2, 1, 2)
plt.plot(t, original, '--', label='Onda Cuadrada (original)', color='black')
plt.plot(t, approx_10, label='Serie de Fourier (10 armónicos)', color='blue')
plt.axvline(0, color='gray', linestyle=':', linewidth=1)
plt.title('Aproximación con 10 armónicos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

