import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A = 1              # Amplitud de la senoide
f = 2              # Frecuencia común en Hz
phi = 0            # Fase de la senoide (0 radianes)

fs = 1000          # Frecuencia de muestreo (Hz)
t = np.arange(0, 2, 1/fs)  # Tiempo de 0 a 2 segundos

# Generar la senoide
senoide = A * np.cos(2*np.pi*f*t + phi)

# Generar la señal cuadrada
señal_cuadrada = A * np.sign(np.cos(2*np.pi*f*t))

# Suma y producto
suma = senoide + señal_cuadrada
producto = senoide * señal_cuadrada

# Gráficas
plt.figure(figsize=(12, 10))

# Senoide y señal cuadrada
plt.subplot(4, 1, 1)
plt.plot(t, senoide, label='Senoide')
plt.plot(t, señal_cuadrada, label='Señal Cuadrada', linestyle='--')
plt.title('Senoide y Señal Cuadrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Suma
plt.subplot(4, 1, 2)
plt.plot(t, suma, color='green')
plt.title('Suma de la Senoide y la Señal Cuadrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Producto
plt.subplot(4, 1, 3)
plt.plot(t, producto, color='red')
plt.title('Producto de la Senoide y la Señal Cuadrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Zoom para comparar los períodos
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
