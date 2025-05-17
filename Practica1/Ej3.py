'''
3) Implementar una función que construya la señal escalón u[t] en el intervalo (-2,5 ; 2,5) 
con una frecuencia de muestreo fs=5Hz. Graficarla en dicho intervalo y también en el (-1,1).
'''

# Si la frecuencia de muestreo es 5 Hz, significa una muestra cada 0.2 segundos.

import numpy as np
import matplotlib.pyplot as plt

def generar_escalon(fs=5):
    # Crear array para el eje temporal
    t = np.linspace(-2.5, 2.5, int((2.5 - (-2.5)) * fs + 1))  # Incluye 2.5 como último valor
    
    # Señal escalón: 0 si t < 0, 1 si t >= 0
    u = np.where(t >= 0, 1, 0)
    
    return t, u

def graficar_escalon(t, u):
    # Gráfico completo
    plt.figure(figsize=(10, 4))
    plt.stem(t, u, basefmt=" ", linefmt='r-')
    plt.title("Señal Escalón u[t] en (-2.5, 2.5)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()

# Zoom en (-1, 1)
    mask = (t >= -1) & (t <= 1)
    plt.figure(figsize=(8, 3))
    plt.stem(t[mask], u[mask], basefmt=" ", linefmt='r-')
    plt.title("Zoom de u[t] en (-1, 1)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()


# Ejecución de la función:
# -------------------------
fs = 5  # Frecuencia de muestreo
t, u = generar_escalon(fs)
graficar_escalon(t, u)




