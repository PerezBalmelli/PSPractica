import numpy as np
import matplotlib.pyplot as plt

# Dominio de t para muestreo fino
t = np.linspace(-1, 6, 1000)

# Definir x(t) = -2/3 * t + 2 en [0,3]
def x_func(t):
    return np.where((t >= 0) & (t <= 3), -2/3 * t + 2, 0)

# Definir h(t) = 2 en [0,1), 1 en [1,2)
def h_func(t):
    return np.where((t >= 0) & (t < 1), 2, np.where((t >= 1) & (t < 2), 1, 0))

# Muestreo para convolución
dt = t[1] - t[0]
x_vals = x_func(t)
h_vals = h_func(t)

# Realizar convolución numérica
y_vals = np.convolve(x_vals, h_vals, mode='full') * dt
t_conv = np.linspace(2*t[0], 2*t[-1], len(y_vals))  # nuevo eje t

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(t_conv, y_vals, label='y(t) = x(t) * h(t)', color='blue')
plt.title("Convolución numérica de x(t) * h(t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.show()