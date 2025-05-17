import numpy as np
import matplotlib.pyplot as plt

# Definimos la función y(t) por tramos
def y(t):
    if -3 < t < -1:
        return 4*t + 12
    elif -1 <= t < 0:
        return 6 - 2*t
    elif 0 <= t < 2:
        return 4*t + 6
    elif 2 <= t < 3:
        return 24 - 5*t
    elif 3 <= t < 6:
        return 18 - 3*t
    elif 6 <= t < 8:
        return 0
    elif 8 <= t < 10:
        return 2*t - 16
    elif 10 <= t < 14:
        return 14 - t
    else:
        return 0

# Vector de tiempo con suficiente resolución
t = np.linspace(-4, 15, 1000)
y_values = np.array([y(ti) for ti in t])

# Graficamos
plt.figure(figsize=(12, 6))
plt.plot(t, y_values, label='$y(t)$', linewidth=2, color='blue')

# Añadimos líneas punteadas para los cambios de pendiente
for cambio in [-3, -1, 0, 2, 3, 6, 8, 10, 14]:
    plt.axvline(x=cambio, color='gray', linestyle='--', alpha=0.5)

# Configuramos el gráfico
plt.title('Salida del sistema $y(t) = x(t) * h(t)$')
plt.xlabel('Tiempo $t$')
plt.ylabel('Amplitud $y(t)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(-4, 15)
plt.ylim(0, 16)  # Ajustamos para ver mejor los picos

# Mostramos el gráfico
plt.show()