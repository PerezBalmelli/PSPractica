import matplotlib.pyplot as plt
import numpy as np

# Frecuencias donde hay componentes (w0 = 1 para graficar)
w0 = 1
frequencies = np.array([-3*w0, -2*w0, 0, 2*w0, 3*w0])

# Parte real de X(ω)
real_values = [0, 3*np.pi, 4*np.pi, 3*np.pi, 0]

# Parte imaginaria de X(ω)
imag_values = [np.pi, 0, 0, 0, -np.pi]

# Módulo
magnitude = np.sqrt(np.array(real_values)**2 + np.array(imag_values)**2)

# Fase (en radianes)
phase = np.arctan2(imag_values, real_values)

# Crear figura con 2x2 subplots: Parte real, imaginaria, módulo y fase
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Transformada de Fourier de x(t) = 2 + 3cos(2w₀t) - sin(3w₀t)", fontsize=14)

# Parte real
axs[0, 0].stem(frequencies, real_values, basefmt=" ")
axs[0, 0].set_title("Parte Real de X(ω)")
axs[0, 0].set_xlabel("ω")
axs[0, 0].set_ylabel("Re{X(ω)}")
axs[0, 0].grid(True)

# Parte imaginaria
axs[0, 1].stem(frequencies, imag_values, basefmt=" ", linefmt='C1-', markerfmt='C1o')
axs[0, 1].set_title("Parte Imaginaria de X(ω)")
axs[0, 1].set_xlabel("ω")
axs[0, 1].set_ylabel("Im{X(ω)}")
axs[0, 1].grid(True)

# Módulo
axs[1, 0].stem(frequencies, magnitude, basefmt=" ", linefmt='C2-', markerfmt='C2o')
axs[1, 0].set_title("Módulo |X(ω)|")
axs[1, 0].set_xlabel("ω")
axs[1, 0].set_ylabel("|X(ω)|")
axs[1, 0].grid(True)

# Fase
axs[1, 1].stem(frequencies, phase, basefmt=" ", linefmt='C3-', markerfmt='C3o')
axs[1, 1].set_title("Fase ∠X(ω) [rad]")
axs[1, 1].set_xlabel("ω")
axs[1, 1].set_ylabel("Fase [rad]")
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

