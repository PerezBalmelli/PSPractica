'''
7) Utilizando la función del puntoanterior, generar una misma señal 
con frecuencias de muestreo 5, 10, 20, 50 y 100 muestras por segundo y observar las diferencias.
8) En las gráficas del punto anterior, ajustar el rango del eje y para que la visualización sea buena 
y agregar etiquetas que muestren el valor de los parámetros.
'''

from Ej6 import funcion_cosenoidal
import numpy as np

if __name__ == "__main__":
    # Definimos las frecuencias de muestreo
    frecuencias_muestreo = [5, 10, 20, 50, 100]
    
    # Generamos la señal para cada frecuencia de muestreo
    for fs in frecuencias_muestreo:
        print(f"Señal generada con frecuencia de muestreo: {fs} Hz")
        print("--------------------------------------------------")
        print()
        funcion_cosenoidal(5,2,2*np.pi,fs)
