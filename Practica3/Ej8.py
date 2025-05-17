'''
8. El filtro de la media móvil descrito en el punto anterior resulta ser un sistema LTI con respuesta al impulso h(t), donde esta última se denomina kernel del filtro y su longitud coincide con el ancho de la ventana. 
Analizar cómo debe ser dicho kernel, y probar utilizando la señal del ejemplo anterior, que la señal de salida es la esperada.
'''

import numpy as np

def convolucion_discreta(x, h):
    N = len(x)
    M = len(h)
    y = [0.0] * (N + M - 1)
    for n in range(len(y)):
        for k in range(M):
            if 0 <= n - k < N:
                y[n] += x[n - k] * h[k]
    return y

if __name__ == "__main__":
    # Ejemplo de uso
    # Señal de entrada
    x = [1, 3, 1, 2, 2, 1]

    # Ancho de ventana
    n = 3

    # Kernel del filtro de media móvil
    h = [1/n] * n  # h = [1/3, 1/3, 1/3]

    # Aplicar convolución (resultado más largo que la entrada, hay que recortar o ajustar)
    y = convolucion_discreta(x, h)

    print("x[n] =", x)
    print("h[n] =", h)
    print("y[n] =", y)
