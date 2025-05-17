''' 
2. Dadas las señales de entrada:
x1(t) = [1,2,1,1,1,2]
x2(t) = [2,1,2,1,0,1,2]
Se pide:
a. Obtener sus respectivas salidas y1(t) e y2(t) en cada uno de los tres sistemas.
b. Para cada sistema, obtener la salida y_sum(t) cuando la entrada es x_sum(t) = x1(t) + x2(t)
c. Para cada sistema, obtener la salida y_lin(t) cuando la entrada es x_lin(t) = 3*x_sum(t)
d. Para cada sistema, graficar en cuatro subplots: 
    en la primera fila, y1(t) + y2(t) contra y_sum(t);
    en la segunda fila, 3*[y1(t) + y2(t)] contra y_lin(t).
    Interpretar los resultados.
'''

import numpy as np
import matplotlib.pyplot as plt

from Ej1 import*

x1 = np.array([1,2,1,1,1,2])
x2 = np.array([2,1,2,1,0,1,2])

def salida_a1(x):
    return sistema_a(x)  # y(t) = 3x(t)

def salida_a2(x):
    return sistema_b(x)  # y(t) = -1-x(t)

def salida_a3(x):
    return sistema_c(x)  # y(t) = e^x(t)

def suma_b1(x,y):
    max_len = max(len(x), len(y))
    
    x_padded = np.pad(x, (0, max_len - len(x)), mode='constant')
    y_padded = np.pad(y, (0, max_len - len(y)), mode='constant')

    return x_padded + y_padded

def graficar_d1(t, x, y1, y2, y_sum, y_lin):
    plt.figure(figsize=(12, 8))

    # Primer subplot: y1(t) + y2(t)
    ax1 = plt.subplot(2, 2, 1)
    ax1.stem(t, suma_b1(y1, y2), linefmt='b-', markerfmt='bo', basefmt=' ', label="y1(t) + y2(t)")
    ax1.set_title("Salida del sistema: y1(t) + y2(t) vs. y_sum(t)")
    ax1.legend(loc='lower right')
    ax1.grid(True)
    ax1.xaxis.set_major_locator(MultipleLocator(1))
    ax1.yaxis.set_major_locator(MultipleLocator(3))

    # Segundo subplot: y_sum(t)
    ax2 = plt.subplot(2, 2, 2)
    ax2.stem(t, y_sum, label="y_sum(t)", linefmt='r-', markerfmt='ro', basefmt=' ')
    ax2.set_title("Salida del sistema: y1(t) + y2(t) vs. y_sum(t)")
    ax2.legend(loc='lower right')
    ax2.grid(True)
    ax2.xaxis.set_major_locator(MultipleLocator(1))
    ax2.yaxis.set_major_locator(MultipleLocator(3))

    # Tercer subplot: 3*[y1(t) + y2(t)]
    ax3 = plt.subplot(2, 2, 3)
    ax3.stem(t, 3 * suma_b1(y1, y2), label="3*[y1(t) + y2(t)]", linefmt='g-', markerfmt='go', basefmt=' ')
    ax3.set_title("Salida del sistema: 3*[y1(t) + y2(t)] vs. y_lin(t)")
    ax3.legend(loc='lower right')
    ax3.grid(True)
    ax3.xaxis.set_major_locator(MultipleLocator(1))
    ax3.yaxis.set_major_locator(MultipleLocator(3))

    # Cuarto subplot: y_lin(t)
    ax4 = plt.subplot(2, 2, 4)
    ax4.stem(t, y_lin, label="y_lin(t)", linefmt='orange', markerfmt='o', basefmt=' ')
    ax4.set_title("Salida del sistema: 3*[y1(t) + y2(t)] vs. y_lin(t)")
    ax4.legend(loc='lower right')
    ax4.grid(True)
    ax4.xaxis.set_major_locator(MultipleLocator(1))
    ax4.yaxis.set_major_locator(MultipleLocator(3))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Convertir las señales de entrada a numpy arrays

    # Obtener las salidas para cada sistema
    y1_a = salida_a1(x1)
    y2_a = salida_a1(x2)

    y1_b = salida_a2(x1)
    y2_b = salida_a2(x2)

    y1_c = salida_a3(x1)
    y2_c = salida_a3(x2)

    # Obtener la salida y_sum(t) para cada sistema
    x_sum = suma_b1(x1,x2)
    y_sum_a = salida_a1(x_sum)
    y_sum_b = salida_a2(x_sum)
    y_sum_c = salida_a3(x_sum)

    # Obtener la salida y_lin(t) para cada sistema
    y_lin_a = salida_a1(3*x_sum)
    y_lin_b = salida_a2(3*x_sum)
    y_lin_c = salida_a3(3*x_sum)

    print("Ejercicio 2.A")
    print("Salida del sistema a para x1(t):", y1_a)
    print("Salida del sistema a para x2(t):", y2_a)
    print("--------------------------------")
    print("Salida del sistema b para x1(t):", y1_b)
    print("Salida del sistema b para x2(t):", y2_b)
    print("--------------------------------")
    print("Salida del sistema c para x1(t):", y1_c)
    print("Salida del sistema c para x2(t):", y2_c)
    print("--------------------------------")
    print("")
    print("--------------------------------")
    print("Ejercicio 2.B")
    print("Sumada de las señales de entrada x_sum(t):", x_sum)
    print("Salida del sistema a para x_sum(t):", y_sum_a)
    print("Salida del sistema b para x_sum(t):", y_sum_b)
    print("Salida del sistema c para x_sum(t):", y_sum_c)
    print("--------------------------------")
    print("")
    print("--------------------------------")
    print("Ejercicio 2.C")
    print("Salida del sistema a para 3*x_sum(t):", y_lin_a)
    print("Salida del sistema b para 3*x_sum(t):", y_lin_b)
    print("Salida del sistema c para 3*x_sum(t):", y_lin_c)
    print("--------------------------------")
    graficar_d1(np.arange(0, len(x_sum)), x_sum, y1_a, y2_a, y_sum_a, y_lin_a)
    graficar_d1(np.arange(0, len(x_sum)), x_sum, y1_b, y2_b, y_sum_b, y_lin_b)
    #graficar_d1(np.arange(0, len(x_sum)), x_sum, y1_c, y2_c, y_sum_c, y_lin_c)
