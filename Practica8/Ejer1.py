import numpy as np
from scipy.fftpack import dct

# Secuencia de entrada
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
N = len(x)

# DCT manual usando la fórmula dada
X_manual = np.zeros(N)
for k in range(N):
    factor = np.sqrt(2 / N)

    suma = 0
    for n in range(N):
        angulo = (np.pi / N) * k * ((2 * n + 1) / 2)
        suma += x[n] * np.cos(angulo)

    X_manual[k] = factor * suma

# DCT con scipy
X_lib = dct(x, type=2, norm='ortho')

# Redondear los resultados a 3 decimales
X_manual_rounded = np.round(X_manual, 3)
X_lib_rounded = np.round(X_lib, 3)
diff_rounded = np.round(np.abs(X_manual - X_lib), 3)

# Imprimir resultados
print("DCT manual (redondeada):")
print(X_manual_rounded)

print("\nDCT con scipy (redondeada):")
print(X_lib_rounded)

print("\nDiferencia absoluta (redondeada):")
print(diff_rounded)
