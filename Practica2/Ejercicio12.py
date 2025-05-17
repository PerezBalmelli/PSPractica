import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A = 1              # Amplitud
f = 2              # Frecuencia en Hz
phi1 = 0           # Fase de la primera senoide (0 rad)
phi2 = np.pi/8     # Fase de la segunda senoide (π/8 rad)

fs = 1000          # Frecuencia de muestreo (Hz)
t = np.arange(0, 2, 1/fs)  # Tiempo de 0 a 2 segundos

# Generar las dos senoides
senoide1 = A * np.cos(2*np.pi*f*t + phi1)
senoide2 = A * np.cos(2*np.pi*f*t + phi2)

# Suma y producto
suma = senoide1 + senoide2
producto = senoide1 * senoide2

# Gráficas
plt.figure(figsize=(12, 10))

# Senoides individuales
plt.subplot(4, 1, 1)
plt.plot(t, senoide1, label='Senoide 1')
plt.plot(t, senoide2, label='Senoide 2', linestyle='--')
plt.title('Senoides individuales')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Suma
plt.subplot(4, 1, 2)
plt.plot(t, suma, color='green')
plt.title('Suma de las Senoides')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Producto
plt.subplot(4, 1, 3)
plt.plot(t, producto, color='red')
plt.title('Producto de las Senoides')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Zoom para ver el período
plt.subplot(4, 1, 4)
plt.plot(t, suma, label='Suma', color='green')
plt.plot(t, producto, label='Producto', color='red', linestyle='--')
plt.xlim(0, 1)  # Zoom sobre 1 segundo
plt.title('Zoom: Comparación de Períodos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
