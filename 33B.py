import numpy as np
import matplotlib.pyplot as plt

# Frecuencias: ω0 = 1, por simplicidad
w0 = 1
frequencies = np.array([-2*w0, 0, 2*w0])

# Parte real (valores en las deltas)
real_values = np.array([-3*np.pi/2, 3*np.pi, -3*np.pi/2])

# Parte imaginaria es cero en todos los puntos
imag_values = np.zeros_like(real_values)

# Módulo
magnitude = np.abs(real_values)

# Fase
phase = np.angle(real_values)

# Gráfica
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Transformada de Fourier de x(t) = 3·sen²(ω₀t)", fontsize=14)

# Parte real
axs[0, 0].stem(frequencies, real_values, basefmt=" ")
axs[0, 0].set_title("Parte Real")
axs[0, 0].set_xlabel("ω")
axs[0, 0].set_ylabel("Re{X(ω)}")
axs[0, 0].grid(True)

# Parte imaginaria
axs[0, 1].stem(frequencies, imag_values, basefmt=" ")
axs[0, 1].set_title("Parte Imaginaria")
axs[0, 1].set_xlabel("ω")
axs[0, 1].set_ylabel("Im{X(ω)}")
axs[0, 1].grid(True)

# Módulo
axs[1, 0].stem(frequencies, magnitude, basefmt=" ")
axs[1, 0].set_title("Módulo |X(ω)|")
axs[1, 0].set_xlabel("ω")
axs[1, 0].set_ylabel("|X(ω)|")
axs[1, 0].grid(True)

# Fase
axs[1, 1].stem(frequencies, phase, basefmt=" ")
axs[1, 1].set_title("Fase ∠X(ω) [rad]")
axs[1, 1].set_xlabel("ω")
axs[1, 1].set_ylabel("Fase")
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
