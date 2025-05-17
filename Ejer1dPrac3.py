import numpy as np
import matplotlib.pyplot as plt

# Definición de la onda cuadrada estándar (amplitud 1, periodo 1)
def square_wave(t):
    return 1 if (t % 1) < 0.5 else -1

# Aproximación de la Serie de Fourier de la onda cuadrada
def fourier_series_square_wave(t, num_harmonics):
    result = 0
    for k in range(1, num_harmonics + 1, 2):
        result += (4 / (np.pi * k)) * np.sin(2 * np.pi * k * t)
    return result

# Tiempo para la graficación
t = np.linspace(0, 2, 500, endpoint=False)

# I. Aproximación con hasta el 5to armónico
num_harmonics_5 = 5
approximation_5 = [fourier_series_square_wave(ti, num_harmonics_5) for ti in t]

# II. Aproximación con hasta el 10mo armónico
num_harmonics_10 = 10
approximation_10 = [fourier_series_square_wave(ti, num_harmonics_10) for ti in t]

# III. Comparación de los casos y análisis de las discontinuidades

# Graficar
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, [square_wave(ti) for ti in t], label='Onda Cuadrada Original', linestyle='--')
plt.plot(t, approximation_5, label=f'Aproximación (hasta {num_harmonics_5} armónicos)')
plt.title('Aproximación de la Onda Cuadrada con hasta el 5to Armónico')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, [square_wave(ti) for ti in t], label='Onda Cuadrada Original', linestyle='--')
plt.plot(t, approximation_10, label=f'Aproximación (hasta {num_harmonics_10} armónicos)')
plt.title('Aproximación de la Onda Cuadrada con hasta el 10mo Armónico')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Análisis de las diferencias y las discontinuidades
print("\nAnálisis de las Diferencias y las Discontinuidades:")
print("Al aumentar el número de armónicos en la aproximación de la Serie de Fourier:")
print("- La aproximación se acerca más a la forma de la onda cuadrada original.")
print("- La región alrededor de los saltos abruptos (discontinuidades) presenta el fenómeno de Gibbs.")
print("- El fenómeno de Gibbs se manifiesta como oscilaciones (picos y valles) cerca de los puntos de discontinuidad, y la altura de estos picos no disminuye al aumentar el número de armónicos, aunque se vuelven más estrechos.")
print("- Con 10 armónicos, la aproximación es visualmente mejor que con 5 armónicos, especialmente en las regiones donde la señal es constante.")