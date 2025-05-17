import numpy as np
import matplotlib.pyplot as plt

def energia_total(x, fs):
    """
    Calcula la energía total de una señal discreta usando numpy.

    Parámetros:
    x (array-like): Señal discreta (valores muestreados).
    fs (float): Frecuencia de muestreo.

    Retorna:
    float: Energía total de la señal.
    """
    x = np.array(x)  # Asegura que x sea un array de numpy
    suma = np.sum(np.abs(x)**2)
    energia = suma / fs
    return energia

def energia_intervalo(x, fs, t_inicio, t_fin):
    """
    Calcula la energía de una señal en un intervalo de tiempo dado.

    Parámetros:
    x (array-like): Señal discreta.
    fs (float): Frecuencia de muestreo (Hz).
    t_inicio (float): Tiempo inicial (segundos).
    t_fin (float): Tiempo final (segundos).

    Retorna:
    float: Energía en el intervalo.
    """
    x = np.array(x)
    n_inicio = int(round(t_inicio * fs))
    n_fin = int(round(t_fin * fs))

    # Asegurarse que los índices estén dentro de los límites
    n_inicio = max(0, n_inicio)
    n_fin = min(len(x), n_fin)

    # Extraer el segmento de interés
    segmento = x[n_inicio:n_fin]

    # Usar la función energia_total en el segmento
    return energia_total(segmento, fs)


def potencia_media(x, fs, t_inicio, t_fin):
    """
    Calcula la potencia media de una señal en un intervalo de tiempo dado.

    Parámetros:
    x (array-like): Señal discreta.
    fs (float): Frecuencia de muestreo (Hz).
    t_inicio (float): Tiempo inicial (segundos).
    t_fin (float): Tiempo final (segundos).

    Retorna:
    float: Potencia media en el intervalo.
    """
    # Calcular la energía en el intervalo
    energia = energia_intervalo(x, fs, t_inicio, t_fin)

    # Duración del intervalo
    duracion = t_fin - t_inicio

    if duracion <= 0:
        raise ValueError("El tiempo final debe ser mayor que el tiempo inicial.")

    # Calcular la potencia media
    potencia = energia / duracion
    return potencia

def potencia_rms(x, fs, t_inicio, t_fin):
    """
    Calcula la potencia eficaz (RMS) de una señal en un intervalo de tiempo dado.

    Parámetros:
    x (array-like): Señal discreta.
    fs (float): Frecuencia de muestreo (Hz).
    t_inicio (float): Tiempo inicial (segundos).
    t_fin (float): Tiempo final (segundos).

    Retorna:
    float: Potencia RMS en el intervalo.
    """
    x = np.array(x)
    n_inicio = int(round(t_inicio * fs))
    n_fin = int(round(t_fin * fs))

    # Asegurarse de que los índices estén en el rango correcto
    n_inicio = max(0, n_inicio)
    n_fin = min(len(x), n_fin)

    # Extraer el segmento
    segmento = x[n_inicio:n_fin]

    if len(segmento) == 0:
        raise ValueError("El intervalo no contiene muestras.")

    # Calcular potencia RMS
    rms = np.sqrt(np.mean(np.abs(segmento)**2))
    return rms

def cuadrante(z):
    """
    Determina en qué cuadrante está un número complejo.

    Parámetros:
    z (complex): Número complejo.

    Retorna:
    str: Nombre del cuadrante o eje correspondiente.
    """
    a = z.real
    b = z.imag

    if a > 0 and b > 0:
        return "Primer cuadrante"
    elif a < 0 and b > 0:
        return "Segundo cuadrante"
    elif a < 0 and b < 0:
        return "Tercer cuadrante"
    elif a > 0 and b < 0:
        return "Cuarto cuadrante"
    elif a == 0 and b != 0:
        return "Sobre el eje imaginario"
    elif b == 0 and a != 0:
        return "Sobre el eje real"
    elif a == 0 and b == 0:
        return "En el origen"

def cart_a_polar(z):
    """
    Convierte un número complejo de forma cartesiana a módulo y fase.

    Parámetros:
    z (complex): Número complejo en forma cartesiana.

    Retorna:
    tuple: (módulo, fase en radianes)
    """
    a = z.real
    b = z.imag

    modulo = np.sqrt(a**2 + b**2)
    fase = np.arctan2(b, a)  # Devuelve la fase ajustada automáticamente al cuadrante

    return modulo, fase


def polar_a_cart(modulo, fase):
    """
    Convierte un número complejo de forma polar a forma cartesiana.

    Parámetros:
    modulo (float): Módulo (magnitud) del número complejo.
    fase (float): Fase (ángulo) en radianes.

    Retorna:
    tuple: (parte_real, parte_imaginaria)
    """
    parte_real = modulo * np.cos(fase)
    parte_imaginaria = modulo * np.sin(fase)

    return parte_real, parte_imaginaria


def graficar_complejo(z):
    """
    Grafica un número complejo en el plano complejo, indicando los ejes real e imaginario.

    Parámetros:
    z (complex): Número complejo a graficar.
    """
    plt.figure(figsize=(6, 6))

    # Ejes real e imaginario
    plt.axhline(0, color='black', linewidth=1)  # Eje real
    plt.axvline(0, color='black', linewidth=1)  # Eje imaginario

    # Dibujar el número complejo como una flecha desde el origen
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color='blue')

    # Ajustes de los límites
    max_val = max(abs(z.real), abs(z.imag)) + 1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)

    # Etiquetas
    plt.xlabel('Eje Real')
    plt.ylabel('Eje Imaginario')
    plt.title(f"Número complejo: {z.real:.2f} + j{z.imag:.2f}")
    plt.grid(True)
    plt.gca().set_aspect('equal')  # Ejes iguales

    # Mostrar coordenadas
    plt.plot(z.real, z.imag, 'ro')  # Punto rojo en el extremo

    plt.show()

def generar_exponencial_compleja(A, theta, t):
    """
    Genera la exponencial compleja sexp(t) = A * exp(i * theta * t).

    Parámetros:
    A (float): Amplitud.
    theta (float): Frecuencia angular (radianes por segundo).
    t (array-like): Vector de tiempos.

    Retorna:
    array: Señal compleja sexp(t).
    """
    return A * np.exp(1j * theta * t)

def graficar_exponencial_compleja(s, t):
    """
    Grafica la parte real, parte imaginaria, módulo y fase de una señal compleja.

    Parámetros:
    s (array-like): Señal compleja.
    t (array-like): Vector de tiempos.
    """
    plt.figure(figsize=(12, 8))

    # Parte real
    plt.subplot(2, 2, 1)
    plt.plot(t, s.real, label='Parte real')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Parte Real')
    plt.grid(True)
    plt.legend()

    # Parte imaginaria
    plt.subplot(2, 2, 2)
    plt.plot(t, s.imag, label='Parte imaginaria', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Parte Imaginaria')
    plt.grid(True)
    plt.legend()

    # Módulo
    plt.subplot(2, 2, 3)
    plt.plot(t, np.abs(s), label='Módulo', color='green')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Módulo')
    plt.title('Módulo')
    plt.grid(True)
    plt.legend()

    # Fase
    plt.subplot(2, 2, 4)
    plt.plot(t, np.angle(s), label='Fase', color='red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Fase (rad)')
    plt.title('Fase')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def periodizar_senal(x, n):
    """
    Construye una señal periódica repitiendo una señal aperiódica 'n' veces.

    Parámetros:
    x (array-like): Señal aperiódica.
    n (int): Número de repeticiones.

    Retorna:
    array: Señal periódica construida.
    """
    return np.tile(x, n)


def suma_senales(x1, x2):
    """
    Suma dos señales elemento a elemento.

    Parámetros:
    x1, x2 (array-like): Señales a sumar.

    Retorna:
    array: Señal resultante de la suma.
    """
    x1 = np.array(x1)
    x2 = np.array(x2)

    if len(x1) != len(x2):
        raise ValueError("Las señales deben tener la misma longitud para sumarlas.")

    return x1 + x2


def resta_senales(x1, x2):
    """
    Resta dos señales elemento a elemento (x1 - x2).

    Parámetros:
    x1, x2 (array-like): Señales a restar.

    Retorna:
    array: Señal resultante de la resta.
    """
    x1 = np.array(x1)
    x2 = np.array(x2)

    if len(x1) != len(x2):
        raise ValueError("Las señales deben tener la misma longitud para restarlas.")

    return x1 - x2


def producto_senales(x1, x2):
    """
    Multiplica dos señales elemento a elemento.

    Parámetros:
    x1, x2 (array-like): Señales a multiplicar.

    Retorna:
    array: Señal resultante del producto.
    """
    x1 = np.array(x1)
    x2 = np.array(x2)

    if len(x1) != len(x2):
        raise ValueError("Las señales deben tener la misma longitud para multiplicarlas.")

    return x1 * x2

#Ejercicio 1
# Ejemplo de uso:
x = np.array([1, -2, 3, -4, 5])  # Señal de ejemplo
fs = 1000                       # Frecuencia de muestreo en Hz
print("Energía total:", energia_total(x, fs))

#Ejercicio 2
# -------- Ejemplo de uso --------
# Creamos una señal de prueba
fs = 1000  # Frecuencia de muestreo de 1000 Hz
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo de duración
x = np.sin(2 * np.pi * 5 * t)  # Señal seno de 5 Hz

# Calcular la energía entre 0.2 segundos y 0.5 segundos
energia = energia_intervalo(x, fs, 0.2, 0.5)

print(f"Energía entre 0.2s y 0.5s: {energia:.4f}")

#Ejercicio 3
# Frecuencias de muestreo a probar
fs_list = [10, 20, 50, 100]
energia_numerica = []

# Generamos y calculamos
for fs in fs_list:
    t = np.linspace(0, 1, fs, endpoint=False)
    s = 2 * np.cos(2 * np.pi * t)
    energia = energia_intervalo(s, fs, 0, 1)
    energia_numerica.append(energia)
    print(f"Frecuencia de muestreo: {fs} Hz -> Energía calculada: {energia:.4f}")

# Graficar la última señal como ejemplo

"""
plt.figure(figsize=(8, 4))
plt.plot(t, s, marker='o')
plt.title(f"Señal s(t) muestreada a {fs_list[-1]} Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
 """

#Ejercicio 4
# Frecuencia de muestreo
fs = 100
t = np.linspace(0, 1, fs, endpoint=False)
s = 2 * np.cos(2 * np.pi * t)

# Potencia media entre 0s y 1s
potencia = potencia_media(s, fs, 0, 1)

print(f"Potencia media entre 0s y 1s: {potencia:.4f}")

#Ejercicio 5
# Potencia RMS entre 0s y 1s
potencia_rms_valor = potencia_rms(s, fs, 0, 1)

print(f"Potencia RMS entre 0s y 1s: {potencia_rms_valor:.4f}")

#Ejercicio 6
# Algunos ejemplos
z1 = 3 + 4j
z2 = -2 + 5j
z3 = -1 - 1j
z4 = 5 - 3j
z5 = 0 + 2j
z6 = 0 + 0j

print(cuadrante(z1))  # Primer cuadrante
print(cuadrante(z2))  # Segundo cuadrante
print(cuadrante(z3))  # Tercer cuadrante
print(cuadrante(z4))  # Cuarto cuadrante
print(cuadrante(z5))  # Sobre el eje imaginario
print(cuadrante(z6))  # En el origen

#Ejercicio 7
z = 1 + 1j
modulo, fase = cart_a_polar(z)

print(f"Módulo: {modulo:.4f}")
print(f"Fase (radianes): {fase:.4f}")
print(f"Fase (grados): {np.degrees(fase):.2f}°")

#Ejercicio 8
# Ejemplo: módulo = 1.4142, fase = 45° (en radianes)
modulo = 1.4142
fase = np.radians(45)  # Convertimos 45° a radianes

parte_real, parte_imaginaria = polar_a_cart(modulo, fase)

print(f"Parte real: {parte_real:.4f}")
print(f"Parte imaginaria: {parte_imaginaria:.4f}")

"""
#Ejercicio 9
z = 3 + 4j
graficar_complejo(z)
"""

"""
#Ejercicio 10
# Parámetros
A = 2
theta = 2 * np.pi * 1  # 1 Hz → frecuencia angular = 2π rad/s
t = np.linspace(0, 2, 500)  # 2 segundos, 500 puntos

# Generar y graficar
s = generar_exponencial_compleja(A, theta, t)
graficar_exponencial_compleja(s, t)
"""
#Ejercicio 11
# Señal base
x = np.array([0, 1, 0, -1])

# Repetir 5 veces
x_periodica = periodizar_senal(x, 5)

print(x_periodica)

#Ejercicio 12

# Definimos dos señales de ejemplo
x1 = np.array([1, 2, 3, 4])
x2 = np.array([10, 20, 30, 40])

# Suma
suma = suma_senales(x1, x2)
print("Suma:", suma)

# Resta
resta = resta_senales(x1, x2)
print("Resta:", resta)

# Producto
producto = producto_senales(x1, x2)
print("Producto:", producto)
