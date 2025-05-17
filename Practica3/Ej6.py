'''
6. Con las mismas señales de prueba, realizar la convolución por medio del algoritmo implementado en el punto anterior 
y por medio de las funciones del lenguaje. Comparar los tiempos de procesamiento.
'''
import time
import numpy as np

from Ej5 import convolucion_discreta  # Asegúrate de que esta función esté definida correctamente

def medir_tiempos(x, h):
    """
    Mide los tiempos de ejecución de la convolución manual y con NumPy.
    Retorna los tiempos de ejecución y los resultados de la convolución.
    """
    # Tiempo de convolución manual
    start_manual = time.perf_counter()
    y_manual = convolucion_discreta(x, h)
    end_manual = time.perf_counter()

    # Tiempo de convolución con NumPy
    start_numpy = time.perf_counter()
    y_numpy = np.convolve(x, h)
    end_numpy = time.perf_counter()

    # Retornar los resultados y los tiempos
    manual_time = end_manual - start_manual
    numpy_time = end_numpy - start_numpy
    
    return y_manual, y_numpy, manual_time, numpy_time

if __name__ == "__main__":
    print("Comparación de Tiempos de Convolución Manual vs NumPy")
    print("-" * 60)
    # Señal h[n] (impulso simple)
    h = [0.0, 1.0, 0.5]

    # Diferentes tamaños de señales de entrada x[n] para probar
    sizes = [1000, 5000]  # Tamaños de 1000 y 5000

    # Ejecutar la comparación para cada tamaño de señal
    for size in sizes:
        # Crear una señal x[n] aleatoria de tamaño 'size'
        x = np.random.rand(size).tolist()
        
        # Medir tiempos
        y_manual, y_numpy, manual_time, numpy_time = medir_tiempos(x, h)
        
        # Mostrar resultados
        print(f"\nTamaño de la señal: {size}")
        print(f"x[n] = {x[:5]}... (solo primeros 5 valores)")
        print(f"h[n] = {h}")
        
        print(f"\nConvolución manual: {y_manual[:5]}... (solo primeros 5 valores)")
        print(f"Tiempo (manual): {manual_time:.8f} segundos")

        print(f"\nConvolución NumPy: {y_numpy[:5]}... (solo primeros 5 valores)")
        print(f"Tiempo (NumPy)  : {numpy_time:.8f} segundos")
        print("-" * 40)
