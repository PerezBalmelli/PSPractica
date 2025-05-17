'''
2) Implementar una función que calcule el valor medio de una señal.
'''
import numpy as np
from scipy.integrate import trapezoid

def valor_medio(senal, tiempos=None):
    """
    Parámetros:
    senal (array-like): La señal de la que se desea calcular el valor medio.
    tiempos (array-like, opcional): Los tiempos extremos correspondientes a la señal.
    
    Retorna:
    float: El valor medio de la señal.
    """
    if tiempos is None:
        # Señal discreta
        return (np.mean(senal))
    else:
        # Señal continua
        resultado = trapezoid(senal, tiempos) / (tiempos[-1] - tiempos[0]) # Integral definida
        # Dividimos por el intervalo de tiempo para obtener el valor medio
        return round(resultado, 3)



# Ejemplos de uso:
#-----------------
# Señal discreta:
print(valor_medio([1, 2, 3, 4, 5]))  # Resultado: 3.0

# Señal continua: sin(t) entre 0 y pi
t = np.linspace(0, np.pi, 1000) # Genera 1000 puntos entre 0 y pi
x = np.sin(t)
print(valor_medio(x, t)) # Resultado: aproximadamente 0.637
