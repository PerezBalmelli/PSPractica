'''
1) Implementar una función que, dada la frecuencia de muestreo y una cantidad de muestras, 
devuelva la duración en el tiempo de una señal condichas características.
'''

def calcular_duracion(frecuencia_muestreo, cantidad_muestras):
    if frecuencia_muestreo <= 0:
        raise ValueError("La frecuencia de muestreo debe ser mayor a 0.")
    if cantidad_muestras < 0:
        raise ValueError("La cantidad de muestras no puede ser negativa.")
    
    return ("Duración: " + str(cantidad_muestras / frecuencia_muestreo) + " segundos")



# Ejemplos de uso:
#-----------------
print(calcular_duracion(10, 100))  # Debe imprimir 10.0