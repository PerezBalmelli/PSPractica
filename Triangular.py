import numpy as np
import matplotlib.pyplot as plt

# Definición de la función original x(t) por tramos y periódica
def x_original(t_vals):
    y_vals = np.zeros_like(t_vals)
    for i, t_single in enumerate(t_vals):
        # Mapear t al intervalo base del período [-2, 2]
        # (t + L) % (2L) - L  donde L=2 (semiperiodo)
        t_periodico = (t_single + 2) % 4 - 2

        if -2 <= t_periodico < -1:
            y_vals[i] = -t_periodico - 2
        elif -1 <= t_periodico < 1:
            y_vals[i] = t_periodico
        elif 1 <= t_periodico <= 2:
            y_vals[i] = -t_periodico + 2
        # Casos especiales para los límites exactos si el mapeo los afecta
        # (np.piecewise podría manejar esto de forma más elegante si no fuera por la periodicidad manual)
        if t_periodico == 2.0: # Límite superior del intervalo principal
             y_vals[i] = -t_periodico + 2 # Debería ser 0

    return y_vals

# Alternativa usando np.piecewise para la función base y luego aplicando periodicidad
def x_original_piecewise(t_vals):
    # Primero, normalizamos todos los valores de t al intervalo base [-2, 2]
    t_norm = (t_vals + 2) % 4 - 2

    # Definimos las condiciones y funciones para el intervalo base
    condiciones = [
        (t_norm >= -2) & (t_norm < -1),
        (t_norm >= -1) & (t_norm < 1),
        (t_norm >= 1) & (t_norm <= 2)
    ]
    funciones = [
        lambda t: -t - 2,
        lambda t: t,
        lambda t: -t + 2
    ]
    # np.select es más robusto para solapamientos que piecewise en algunos casos
    # o podemos asegurar que las condiciones no se solapan en los puntos exactos
    # Para el último punto del período t_norm = 2, usamos la tercera condición
    # Si t_norm es exactamente -2, la primera condición lo toma.
    # Si t_norm es exactamente -1, la segunda condición lo toma.
    # Si t_norm es exactamente 1, la tercera condición lo toma.
    return np.select(condiciones, [f(t_norm) for f in funciones], default=np.nan)


# Definición de la aproximación de la serie de Fourier
def x_fourier(t, num_terminos):
    suma_parcial = np.zeros_like(t)
    for k in range(1, num_terminos + 1):
        n = 2 * k - 1
        termino = (8 / (n**2 * np.pi**2)) * ((-1)**(k - 1)) * np.sin(n * np.pi * t / 2)
        suma_parcial += termino
    return suma_parcial

# Valores de t para graficar (cubriendo un par de períodos)
t_puntos = np.linspace(-4, 4, 800) # Más puntos para una curva suave

# Calcular los valores de la función original
y_original = x_original_piecewise(t_puntos) # Usando la versión con np.select

# Calcular los valores de la serie de Fourier para diferentes números de términos
y_fourier_5 = x_fourier(t_puntos, 5)
y_fourier_10 = x_fourier(t_puntos, 10)
y_fourier_50 = x_fourier(t_puntos, 50)

# Graficar
plt.figure(figsize=(12, 8))

#plt.plot(t_puntos, y_original, label='Función Original $x(t)$', color='black', linewidth=2.5)
plt.plot(t_puntos, y_fourier_5, label='Serie de Fourier (N=5 términos)', color='red', linestyle='--')
plt.plot(t_puntos, y_fourier_10, label='Serie de Fourier (N=10 términos)', color='blue', linestyle='-.')
#plt.plot(t_puntos, y_fourier_50, label='Serie de Fourier (N=50 términos)', color='green', linestyle=':')

plt.title('Función Original y su Aproximación por Series de Fourier')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend()
plt.grid(True)
plt.ylim(-2, 2) # Ajustar límites del eje y si es necesario
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.show()