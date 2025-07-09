import matplotlib.pyplot as plt
import numpy as np

# Parámetros
P_total = 1.0  # atm
X_A = np.linspace(0, 1, 100)
P_A = X_A * P_total
P_B = (1 - X_A) * P_total

# Gráfica
plt.plot(X_A, P_A, label='Presión parcial de A (P_A)', color='blue')
plt.plot(X_A, P_B, label='Presión parcial de B (P_B)', color='green')
plt.axhline(y=P_total, color='red', linestyle='--', label='Presión total')

plt.xlabel('Fracción molar de A (X_A)')
plt.ylabel('Presión (atm)')
plt.title('Ley de Dalton - Presiones Parciales vs Fracción Molar')
plt.legend()
plt.grid(True)
plt.show()
