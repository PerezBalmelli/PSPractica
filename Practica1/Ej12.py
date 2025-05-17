'''
12) Generar la función:  s(t) = 2cos(t) si t ∈ (0,2π), 0 en otro caso
    en el intervalo (-5π;5π). Graficar en dicho intervalo:
    s(-t)
    s(t-2π)
    s(t+2π)
    s(-t+π)
    s(4t)
    s(1/4 t)
    s(-1/2 t)
    Deben mostrarse las funciones en ocho subplots de la misma ventana de gráfica, 
    indicando en respectivas etiquetas que función es cada una.

13) En el punto anterior, ajustar el eje t de las gráficas para que lo muestre en escala de π. 
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

def s_original(t):
    """
    Función s(t) = 2cos(t) en (0, 2π), y 0 en otro caso.
    """
    s = np.zeros_like(t)
    mask = (t > 0) & (t < 2 * np.pi)
    s[mask] = 2 * np.cos(t[mask])
    return s

# Intervalo de tiempo: (-5π, 5π)
t = np.linspace(-5*np.pi, 5*np.pi, 1000)

# Señales transformadas
s_t       = s_original(t)
s_neg_t   = s_original(-t)
s_t_m2pi  = s_original(t - 2*np.pi)
s_t_p2pi  = s_original(t + 2*np.pi)
s_neg_tpi = s_original(-t + np.pi)
s_4t      = s_original(4 * t)
s_1_4t    = s_original(0.25 * t)
s_neg_1_2t= s_original(-0.5 * t)

# Crear figura y subplots
fig, axs = plt.subplots(4, 2, figsize=(8, 7))
fig.suptitle("Transformaciones de s(t)", fontsize=15)

# Formato π en el eje X
def formato_pi(x, pos):
    num = int(np.round(x / np.pi))
    if num == 0:
        return "0"
    elif num == 1:
        return "π"
    elif num == -1:
        return "-π"
    else:
        return f"{num}π"

formatter = FuncFormatter(formato_pi)
locator = MultipleLocator(base=np.pi)

# Lista de señales y títulos
funciones = [
    (s_t,       's(t)'),
    (s_neg_t,   's(-t)'),
    (s_t_m2pi,  's(t - 2π)'),
    (s_t_p2pi,  's(t + 2π)'),
    (s_neg_tpi, 's(-t + π)'),
    (s_4t,      's(4t)'),
    (s_1_4t,    's(1/4 t)'),
    (s_neg_1_2t,'s(-1/2 t)')
]

# Graficar en subplots
for ax, (s_func, title) in zip(axs.flat, funciones):
    ax.plot(t, s_func, color='darkgreen')
    ax.set_title(title)
    ax.grid(True)
    ax.set_xlim([-5*np.pi, 5*np.pi])
    ax.set_ylim([-2.5, 2.5])
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_locator(MultipleLocator(1))

# Ajustar espacios
plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()

