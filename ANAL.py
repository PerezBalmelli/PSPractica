import numpy as np
import matplotlib.pyplot as plt
import math

# Redondeo a 7 cifras significativas
def redondear_7_cifras(numero):
    if numero == 0:
        return 0.0
    return float(f"{numero:.7g}")

# Sucesión recursiva con redondeo a 7 cifras significativas
def calcular_sucesion_redondeada(n):
    x = np.zeros(n)
    x[0] = redondear_7_cifras(x_0)
    x[1] = redondear_7_cifras(x_1)
    for i in range(1, n - 1):
        mult1 = redondear_7_cifras(13 / 3)
        mult2 = redondear_7_cifras(4 / 3)
        prod1 = redondear_7_cifras(mult1 * x[i])
        prod2 = redondear_7_cifras(mult2 * x[i - 1])
        x[i + 1] = redondear_7_cifras(prod1 - prod2)
    return x

# Sucesión explícita
def sucesion_explicita(n):
    return np.array([(1 / 3) ** i for i in range(n)])

# Graficar comparación
def graficar_log_comparacion(sucesion_redondeada, sucesion_exacta, n):
    x_vals = np.arange(0, n)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, sucesion_redondeada, label='Recursiva (Redondeada)', marker='o', color='blue')
    plt.plot(x_vals, sucesion_exacta, label='Explícita', linestyle='--', marker='x', color='red')
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("Valor de xₙ (escala logarítmica)")
    plt.title("Comparación de sucesión recursiva y explícita (redondeo a 7 cifras)")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Condiciones iniciales
x_0 = 1
x_1 = 1 / 3
n = 15

# Cálculo de ambas sucesiones
sucesion_redondeada = calcular_sucesion_redondeada(n)
sucesion_exacta = sucesion_explicita(n)
errores = np.abs(sucesion_redondeada - sucesion_exacta)

# Mostrar tabla
print(f"{'n':>2} | {'Recursiva':>12} | {'Explícita':>12} | {'Error absoluto':>15}")
print("-" * 50)
for i in range(2, n):
    print(f"{i:2d} | {sucesion_redondeada[i]:12.7f} | {sucesion_exacta[i]:12.7f} | {errores[i]:15.7e}")

# Primer término donde difieren
for i in range(n):
    if not math.isclose(sucesion_redondeada[i], sucesion_exacta[i], rel_tol=1e-7):
        print(f"\n⚠️  La primera diferencia significativa ocurre en n = {i}")
        break

# Gráfico
graficar_log_comparacion(sucesion_redondeada, sucesion_exacta, n)
