'''
7. Un filtro de la media móvil es un algoritmo que, aplicado a una señal, realiza el promedio de los valores en un cierto rango y asigna ese resultado al punto correspondiente de la señal de salida.
La cantidad de valores a promediar se denomina ancho del filtro, y debe ser un número impar. 
Por ejemplo, un filtro con una ventana de ancho n=3 aplicado a la señal x(t)=[1,3,1,2,2,1] devolverá y(t)=[1,33,1,67,2,1,67,1,67,1]. Notar que para analizar lo que ocurre en los extremos, se “rellena” la señal con ceros hasta cubrir el ancho del filtro (en el ejemplo previo, en la primera posición se promedian los valores 0, 1 y 3 para obtener el resultado 1,33). Implementarlo.
'''

import numpy as np

def filtro_media_movil(x, n):
    """
    Aplica un filtro de media móvil a la señal x con un ancho de ventana n.

    Parámetros:
    - x: lista o array de la señal de entrada
    - n: tamaño del filtro (debe ser impar)

    Retorna:
    - y: señal filtrada
    """
    # Asegurarse de que n es impar
    if n % 2 == 0:
        raise ValueError("El tamaño de la ventana debe ser un número impar.")
    
    # Añadir ceros al principio y al final de la señal
    padding = n // 2
    x_padded = np.pad(x, (padding, padding), mode='constant', constant_values=0)

    # Aplicar el filtro de media móvil
    y = np.zeros(len(x), dtype=float)  # Crear una matriz de ceros con el mismo tamaño que la señal de entrada
    for i in range(len(x)):
        y[i] = round(np.mean(x_padded[i:i+n]),2)  # Promedio de los valores en la ventana

    return y

if __name__ == "__main__":
    # Ejemplo de uso
    x = [1, 3, 1, 2, 2, 1]  # Señal de entrada
    n = 3  # Ancho del filtro
    y = filtro_media_movil(x, n)  # Señal filtrada

    print("Entrada:", x)
    print("Salida:", y)
