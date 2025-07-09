import numpy as np

def filtro_pasabajos_ideal(longitud, fc, fs):
    """
    Generar una función que construya filtros pasabajos ideales en el dominio de la frecuencia, en-
    tendiendo estos como funciones que valen 0 a la derecha de cierta frecuencia de corte y 1 a la
    izquierda de la misma. La frecuencia de corte debe ser un parámetro de entrada.
    Parámetros:
    longitud : int
        Número de puntos del filtro (debe ser igual al tamaño de la FFT)
    fc : float
        Frecuencia de corte en Hz
    fs : float
        Frecuencia de muestreo en Hz

    Retorna:
    ndarray: Filtro pasabajos ideal (en el dominio de la frecuencia, orden estándar FFT)
    """
    # Calcular las frecuencias correspondientes a cada bin
    frecuencias = np.fft.fftfreq(longitud, 1 / fs)

    # Crear el filtro ideal (1 donde |f| <= fc, 0 en otro caso)
    filtro = np.zeros(longitud)
    filtro[np.abs(frecuencias) <= fc] = 1

    return filtro

import matplotlib.pyplot as plt

# Parámetros del sistema
fs = 1000  # Frecuencia de muestreo (Hz)
N = 1024   # Tamaño de la FFT
fc = 50    # Frecuencia de corte (Hz)

# Generar el filtro
filtro = filtro_pasabajos_ideal(N, fc, fs)

# Visualizar (desplazado para mejor visualización)
frecs_desplazadas = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))
filtro_desplazado = np.fft.fftshift(filtro)

plt.figure(figsize=(10, 4))
plt.plot(frecs_desplazadas, filtro_desplazado)
plt.title(f"Filtro Pasabajos Ideal (fc = {fc}Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)
plt.tight_layout()
plt.show()

#filtro sin desplazar y desplazado

# Parámetros
fs = 1000  # Frecuencia de muestreo
N = 1024   # Tamaño de la FFT
fc = 50    # Frecuencia de corte

# Generar frecuencias y filtro
frecs = np.fft.fftfreq(N, 1/fs)
filtro = np.zeros(N)
filtro[np.abs(frecs) <= fc] = 1

# Versión desplazada
frecs_despl = np.fft.fftshift(frecs)
filtro_despl = np.fft.fftshift(filtro)

# Crear figura con 2 subplots
plt.figure(figsize=(14, 6))

# 1. Gráfica SIN desplazar (orden natural FFT)
plt.subplot(1, 2, 1)
plt.plot(frecs, filtro, 'b')
plt.title("Representación NATURAL (sin desplazar)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)  # Mismo rango para comparar

# 2. Gráfica DESPLAZADA
plt.subplot(1, 2, 2)
plt.plot(frecs_despl, filtro_despl, 'r')
plt.title("Representación DESPLAZADA (con fftshift)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)

plt.tight_layout()
plt.show()

# ejercicio2

def filtro_pasaaltos_ideal(longitud, fc, fs):
    """
    Genera un filtro pasaaltos ideal en el dominio de la frecuencia.
    Parámetros:
    longitud : int
        Número de puntos del filtro (debe ser igual al tamaño de la FFT)
    fc : float
        Frecuencia de corte en Hz
    fs : float
        Frecuencia de muestreo en Hz

    Retorna:
    ndarray: Filtro pasaaltos ideal (en el dominio de la frecuencia, orden estándar FFT)
    """
    # Calcular las frecuencias correspondientes a cada bin
    frecuencias = np.fft.fftfreq(longitud, 1 / fs)

    # Crear el filtro ideal (0 donde |f| <= fc, 1 en otro caso)
    filtro = np.ones(longitud)  # Comienza con todos en 1
    filtro[np.abs(frecuencias) <= fc] = 0  # Cero en las frecuencias bajas

    return filtro

#prueba

# Parámetros del sistema
fs = 1000  # Frecuencia de muestreo (Hz)
N = 1024   # Tamaño de la FFT
fc = 50    # Frecuencia de corte (Hz)

# Generar ambos filtros para comparación
pasaaltos = filtro_pasaaltos_ideal(N, fc, fs)
pasabajos = filtro_pasabajos_ideal(N, fc, fs)  # Usando la función anterior

# Preparar para visualización (desplazar)
frecs_desplazadas = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))
pasaaltos_despl = np.fft.fftshift(pasaaltos)
pasabajos_despl = np.fft.fftshift(pasabajos)

# Graficar comparación
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(frecs_desplazadas, pasaaltos_despl, 'r', label='Pasaaltos')
plt.plot(frecs_desplazadas, pasabajos_despl, 'b', label='Pasabajos')
plt.title(f"Filtros Ideales (fc = {fc}Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.xlim(-fs/2, fs/2)

plt.subplot(1, 2, 2)
plt.plot(frecs_desplazadas, pasaaltos_despl + pasabajos_despl, 'g')
plt.title("Suma de Filtros (Pasaaltos + Pasabajos)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)

plt.tight_layout()
plt.show()

#ejercicio 3
def filtro_pasabajos_ideal(longitud, fc, fs, G=1.0):
    """
    Genera un filtro pasabajos ideal con ganancia ajustable.
    Parámetros:
    longitud : int
        Número de puntos del filtro
    fc : float
        Frecuencia de corte en Hz
    fs : float
        Frecuencia de muestreo en Hz
    G : float, opcional
        Ganancia en la banda de paso (default = 1.0)

    Retorna:
    ndarray: Filtro pasabajos ideal
    """
    frecuencias = np.fft.fftfreq(longitud, 1 / fs)
    filtro = np.zeros(longitud)
    filtro[np.abs(frecuencias) <= fc] = G
    return filtro


def filtro_pasaaltos_ideal(longitud, fc, fs, G=1.0):
    """ Genera un filtro pasaaltos ideal con ganancia ajustable.
    Parámetros:
    longitud : int
        Número de puntos del filtro
    fc : float
        Frecuencia de corte en Hz
    fs : float
        Frecuencia de muestreo en Hz
    G : float, opcional
        Ganancia en la banda de paso (default = 1.0)

    Retorna:
    ndarray: Filtro pasaaltos ideal
    """
    frecuencias = np.fft.fftfreq(longitud, 1 / fs)
    filtro = np.zeros(longitud)
    filtro[np.abs(frecuencias) > fc] = G
    return filtro
"""
Amplificación/atenuación:
G > 1.0 amplifica las frecuencias en la banda de paso
G < 1.0 atenúa las frecuencias en la banda de paso
"""
# Parámetros
fs = 1000
N = 1024
fc = 100

# Crear filtros con diferentes ganancias
pb_g1 = filtro_pasabajos_ideal(N, fc, fs, G=1.0)
pb_g05 = filtro_pasabajos_ideal(N, fc, fs, G=0.5)
pa_g2 = filtro_pasaaltos_ideal(N, fc, fs, G=2.0)

# Visualización
frecs_despl = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))

plt.figure(figsize=(12, 8))

# Pasabajos con diferentes ganancias
plt.subplot(2, 1, 1)
plt.plot(frecs_despl, np.fft.fftshift(pb_g1), 'b', label='G=1.0')
plt.plot(frecs_despl, np.fft.fftshift(pb_g05), 'c--', label='G=0.5')
plt.title(f"Filtros Pasabajos Ideales (fc={fc}Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.xlim(-fs/2, fs/2)

# Pasaaltos con ganancia
plt.subplot(2, 1, 2)
plt.plot(frecs_despl, np.fft.fftshift(pa_g2), 'r', label='G=2.0')
plt.title(f"Filtro Pasaaltos Ideal (fc={fc}Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.xlim(-fs/2, fs/2)

plt.tight_layout()
plt.show()

#Ejercicio 4
"""
Generar sendas funciones que permitan construir filtros pasabanda y rechazabanda, recibiendo
como parámetros de entrada las dos frecuencias de corte y la ganancia.
"""

def filtro_pasabanda_ideal(longitud, fc1, fc2, fs, G=1.0):
    # Validar frecuencias
    if fc1 >= fc2:
        raise ValueError("fc1 debe ser menor que fc2")
    if fc2 > fs / 2:
        raise ValueError("fc2 no puede exceder la frecuencia de Nyquist")

    frecuencias = np.fft.fftfreq(longitud, 1 / fs)
    filtro = np.zeros(longitud)
    mascara = (np.abs(frecuencias) >= fc1) & (np.abs(frecuencias) <= fc2)
    filtro[mascara] = G
    return filtro


def filtro_rechazabanda_ideal(longitud, fc1, fc2, fs, G=1.0):
    # Validar frecuencias
    if fc1 >= fc2:
        raise ValueError("fc1 debe ser menor que fc2")
    if fc2 > fs / 2:
        raise ValueError("fc2 no puede exceder la frecuencia de Nyquist")

    frecuencias = np.fft.fftfreq(longitud, 1 / fs)
    filtro = G * np.ones(longitud)
    mascara = (np.abs(frecuencias) >= fc1) & (np.abs(frecuencias) <= fc2)
    filtro[mascara] = 0.0
    return filtro

#Ejercicio 5
import numpy as np
import matplotlib.pyplot as plt

# Parámetros comunes
fs = 1000
N = 1024
fc1 = 50
fc2 = 150
G = 1.5

# Generar filtros
pasabanda = filtro_pasabanda_ideal(N, fc1, fc2, fs, G)
rechazabanda = filtro_rechazabanda_ideal(N, fc1, fc2, fs, G)

# Preparar frecuencias desplazadas para visualización
frecs_despl = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))
pasabanda_despl = np.fft.fftshift(pasabanda)
rechazabanda_despl = np.fft.fftshift(rechazabanda)

# Crear gráficos
plt.figure(figsize=(14, 10))

# Filtro Pasabanda
plt.subplot(2, 1, 1)
plt.plot(frecs_despl, pasabanda_despl, 'g')
plt.axvline(fc1, color='r', linestyle='--', alpha=0.7)
plt.axvline(fc2, color='r', linestyle='--', alpha=0.7)
plt.axvline(-fc1, color='r', linestyle='--', alpha=0.7)
plt.axvline(-fc2, color='r', linestyle='--', alpha=0.7)
plt.title(f"Filtro Pasabanda Ideal ({fc1}-{fc2}Hz, G={G})")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)

# Filtro Rechazabanda
plt.subplot(2, 1, 2)
plt.plot(frecs_despl, rechazabanda_despl, 'm')
plt.axvline(fc1, color='b', linestyle='--', alpha=0.7)
plt.axvline(fc2, color='b', linestyle='--', alpha=0.7)
plt.axvline(-fc1, color='b', linestyle='--', alpha=0.7)
plt.axvline(-fc2, color='b', linestyle='--', alpha=0.7)
plt.title(f"Filtro Rechazabanda Ideal (Rechaza {fc1}-{fc2}Hz, G={G})")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.xlim(-fs/2, fs/2)

plt.tight_layout()
plt.show()

#con funciones anteriores
longitud = 1024
pasabanda = filtro_pasabajos_ideal(longitud, fc2, fs, G) - filtro_pasabajos_ideal(longitud, fc1, fs, G)
rechazabanda = filtro_pasabajos_ideal(longitud, fc1, fs, G) + filtro_pasaaltos_ideal(longitud, fc2, fs, G)
G = pasabanda + rechazabanda  #(para todo el espectro)

#ejercicio 6
#Generar sendas funciones que permitan, dado un determinado filtro y una señal de entrada, efectuar
# el filtrado en el dominio del tiempo y en el dominio de la frecuencia respectivamente.

def filtrar_frecuencia(senal, filtro_frec):
    """
    Filtra una señal en el dominio de la frecuencia multiplicando por un filtro.

    Parámetros:
    senal : array_like
        Señal de entrada (dominio temporal)
    filtro_frec : array_like
        Filtro en dominio de frecuencia (misma longitud que la FFT de la señal)

    Retorna:
    ndarray: Señal filtrada (dominio temporal)
    """
    # Calcular FFT de la señal
    fft_senal = np.fft.fft(senal)

    # Aplicar filtro (multiplicación en frecuencia)
    fft_filtrada = fft_senal * filtro_frec

    # Transformada inversa y tomar parte real
    senal_filtrada = np.fft.ifft(fft_filtrada).real

    return senal_filtrada


from scipy.signal import convolve
def filtrar_tiempo(senal, respuesta_impulso):
    """
    Filtra una señal en el dominio del tiempo mediante convolución.

    Parámetros:
    senal : array_like
        Señal de entrada (dominio temporal)
    respuesta_impulso : array_like
        Respuesta al impulso del filtro (dominio temporal)

    Retorna:
    ndarray: Señal filtrada (dominio temporal)
    """
    # Realizar convolución (modo 'same' para mantener misma longitud)
    senal_filtrada = convolve(senal, respuesta_impulso, mode='same')

    return senal_filtrada

from scipy.signal import chirp

# 1. Generar señal de prueba (chirp lineal)
fs = 1000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs)  # 1 segundo de señal
senal = chirp(t, f0=5, f1=250, t1=1, method='linear')

# 2. Crear filtro pasabajos en frecuencia (fc=100Hz)
fc = 100
filtro_frec = filtro_pasabajos_ideal(len(senal), fc, fs)

# 3. Obtener respuesta al impulso del filtro (para dominio temporal)
respuesta_impulso = np.fft.ifft(filtro_frec).real
respuesta_impulso = np.fft.fftshift(respuesta_impulso)  # Centrar la respuesta

# 4. Aplicar ambos métodos de filtrado
senal_frec = filtrar_frecuencia(senal, filtro_frec)
senal_tiempo = filtrar_tiempo(senal, respuesta_impulso)

# 5. Visualización
plt.figure(figsize=(14, 10))

# Señal original y filtros
plt.subplot(3, 1, 1)
plt.plot(t, senal, 'b', label='Señal Original')
plt.title('Señal Original (Chirp 5-250Hz)')
plt.xlabel('Tiempo [s]')
plt.grid(True)
plt.legend()

# Comparación de métodos
plt.subplot(3, 1, 2)
plt.plot(t, senal_frec, 'r', label='Filtrado en Frecuencia')
plt.plot(t, senal_tiempo, 'g--', label='Filtrado en Tiempo', alpha=0.7)
plt.title(f'Comparación de Métodos (Filtro Pasabajos {fc}Hz)')
plt.xlabel('Tiempo [s]')
plt.grid(True)
plt.legend()

# Diferencia entre métodos
plt.subplot(3, 1, 3)
diferencia = np.abs(senal_frec - senal_tiempo)
plt.plot(t, diferencia, 'm')
plt.title('Diferencia entre Métodos')
plt.xlabel('Tiempo [s]')
plt.ylabel('Error absoluto')
plt.grid(True)
plt.ylim(0, 0.1)

plt.tight_layout()
plt.show()

"""
Ejercicio 6

Construir un algoritmo que, dada una señal (restringirse por simpleza a señales de tipo senoidal),
la module en amplitud sobre una senoide portadora. La frecuencia de la señal portadora debe ser
parámetro de entrada; considere que su amplitud es 1.
"""

def modulador_am(t, senal_moduladora, fc, A=1.0):
    """
    Modula una señal en amplitud (AM) sobre una portadora senoidal.

    Parámetros:
    t : ndarray
        Vector de tiempos
    senal_moduladora : ndarray
        Señal moduladora (información)
    fc : float
        Frecuencia de la portadora (Hz)
    A : float, opcional
        Amplitud de la portadora (default = 1.0)

    Retorna:
    tuple: (señal_modulada, portadora)
    """
    # Generar la portadora (senoide de amplitud A y frecuencia fc)
    portadora = A * np.cos(2 * np.pi * fc * t)

    # Modular la señal: AM = [A + m(t)] * cos(2πfc t)
    # Pero como la portadora ya incluye A, usamos: [1 + m(t)/A] * portadora
    señal_modulada = (1 + senal_moduladora / A) * portadora

    return señal_modulada, portadora

#prueba

# Parámetros del sistema
fs = 5000  # Frecuencia de muestreo (Hz)
T = 0.5    # Duración de la señal (s)
t = np.linspace(0, T, int(T*fs), endpoint=False)  # Vector de tiempos

# 1. Generar señal moduladora (senoidal de baja frecuencia)
fm = 5    # Frecuencia de la señal de información (Hz)
Am = 0.8  # Amplitud de la señal moduladora
senal_mod = Am * np.sin(2 * np.pi * fm * t)

# 2. Configurar portadora
fc = 100  # Frecuencia portadora (Hz)
A_port = 1.0  # Amplitud portadora

# 3. Modular la señal
senal_am, portadora = modulador_am(t, senal_mod, fc, A_port)

# 4. Visualización
plt.figure(figsize=(14, 10))

# Señal moduladora (información)
plt.subplot(3, 1, 1)
plt.plot(t, senal_mod, 'g')
plt.title(f'Señal Moduladora (f = {fm}Hz, Amplitud = {Am})')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.xlim(0, 1/fm)  # Mostrar un ciclo completo

# Portadora
plt.subplot(3, 1, 2)
plt.plot(t, portadora, 'b', alpha=0.7)
plt.title(f'Portadora (f = {fc}Hz, Amplitud = {A_port})')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.xlim(0, 5/fc)  # Mostrar 5 ciclos

# Señal modulada en AM
plt.subplot(3, 1, 3)
plt.plot(t, senal_am, 'r')
plt.plot(t, (1 + senal_mod/A_port), 'k--', label='Envolvente superior')
plt.plot(t, -(1 + senal_mod/A_port), 'k--', label='Envolvente inferior')
plt.title(f'Señal Modulada en AM (Índice de modulación = {Am/A_port*100:.1f}%)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.xlim(0, 1/fm)  # Mostrar un ciclo completo de la moduladora

plt.tight_layout()
plt.show()

# Análisis espectral de la señal modulada
N = len(senal_am)
freqs = np.fft.fftfreq(N, 1/fs)
espectro = np.abs(np.fft.fft(senal_am)) / N

plt.figure(figsize=(12, 6))
plt.plot(np.fft.fftshift(freqs), np.fft.fftshift(espectro), 'r')
plt.axvline(fc, color='b', linestyle='--', alpha=0.5, label='Portadora')
plt.axvline(fc + fm, color='g', linestyle=':', label='Banda lateral sup')
plt.axvline(fc - fm, color='g', linestyle=':', label='Banda lateral inf')
plt.title('Espectro de la Señal Modulada en AM')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.xlim(0, 200)  # Centrado alrededor de la portadora
plt.legend()
plt.tight_layout()
plt.show()


def modulador_am(t, senal_moduladora, fc, A=1.0):
    # Validar longitudes
    if len(t) != len(senal_moduladora):
        raise ValueError("t y senal_moduladora deben tener la misma longitud")

    # Calcular índice de modulación
    indice_mod = np.max(np.abs(senal_moduladora)) / A

    # Generar portadora
    portadora = A * np.cos(2 * np.pi * fc * t)

    # Modular señal
    señal_modulada = (1 + senal_moduladora / A) * portadora

    return señal_modulada, portadora, indice_mod



#ejercicio 7
from scipy.signal import butter, filtfilt

def demodular_am(t, s_t, fc, orden=5, fcorte=0.1):
    """
    Demodulación coherente AM.
    t: vector de tiempo
    s_t: señal modulada AM
    fc: frecuencia de portadora (Hz)
    orden: orden del filtro pasa bajos
    fcorte: frecuencia de corte normalizada (relativa a Nyquist)
    """
    # Portadora en fase
    portadora = np.cos(2 * np.pi * fc * t)

    # Demodulación coherente (multiplicación)
    producto = s_t * portadora

    # Filtro pasa bajos para eliminar la componente en 2fc
    b, a = butter(orden, fcorte)
    señal_filtrada = filtfilt(b, a, producto)

    # Recuperar la señal original: compensar el factor 1/2
    señal_moduladora = 2 * (señal_filtrada - np.mean(señal_filtrada))

    return señal_moduladora

#Prueba
fs = 10000               # Frecuencia de muestreo
duracion = 0.01          # 10 ms
t = np.linspace(0, duracion, int(fs*duracion))

# Señal moduladora (mensaje)
m_t = 0.5 * np.sin(2 * np.pi * 100 * t)  # 100 Hz

# Portadora
fc = 1000  # 1 kHz
portadora = np.cos(2 * np.pi * fc * t)

# Señal modulada AM
s_t = (1 + m_t) * portadora

# Demodulación
m_recuperada = demodular_am(t, s_t, fc)

#Graficar
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, m_t, label='Mensaje original')
plt.title('Señal Moduladora (mensaje)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, s_t, label='Señal AM')
plt.title('Señal AM (modulada en amplitud)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, m_recuperada, label='Mensaje recuperado', color='orange')
plt.title('Mensaje recuperado tras demodulación')
plt.grid()

plt.tight_layout()
plt.show()
""" ej7: Recupera la señal original con excelente precisión (salvo desfases o atenuaciones que podés corregir).
"""
#ejercicio 8
"""" Construir funciones que efectúen la modulación y demodulación, respectivamente, en amplitud
senoidal en banda lateral única. Comparar las gráficas de una misma señal modulada en banda """
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def demodular_am(t, s_t, fc, orden=5, fcorte=0.1):
    """
    Demodulación coherente AM.
    t: vector de tiempo
    s_t: señal modulada AM
    fc: frecuencia de portadora (Hz)
    orden: orden del filtro pasa bajos
    fcorte: frecuencia de corte normalizada (relativa a Nyquist)
    """
    # Portadora en fase
    portadora = np.cos(2 * np.pi * fc * t)

    # Demodulación coherente (multiplicación)
    producto = s_t * portadora

    # Filtro pasa bajos para eliminar la componente en 2fc
    b, a = butter(orden, fcorte)
    señal_filtrada = filtfilt(b, a, producto)

    # Recuperar la señal original: compensar el factor 1/2
    señal_moduladora = 2 * (señal_filtrada - np.mean(señal_filtrada))

    return señal_moduladora

# Prueba
fs = 10000               # Frecuencia de muestreo
duracion = 0.01          # 10 ms
t = np.linspace(0, duracion, int(fs*duracion))

# Señal moduladora (mensaje)
m_t = 0.5 * np.sin(2 * np.pi * 100 * t)  # 100 Hz

# Portadora
fc = 1000  # 1 kHz
portadora = np.cos(2 * np.pi * fc * t)

# Señal modulada AM
s_t = (1 + m_t) * portadora

# Demodulación
m_recuperada = demodular_am(t, s_t, fc)

#Graficar
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, m_t, label='Mensaje original')
plt.title('Señal Moduladora (mensaje)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, s_t, label='Señal AM')
plt.title('Señal AM (modulada en amplitud)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, m_recuperada, label='Mensaje recuperado', color='orange')
plt.title('Mensaje recuperado tras demodulación')
plt.grid()

plt.tight_layout()
plt.show()

#Ejercicio 9

""" Para una señal con espectro limitado entre -ωm y +ωm (donde ωm = 2πfm) 
que se modulará en AM con una portadora de 1 MHz, la frecuencia de muestreo
 mínima debe satisfacer el teorema de Nyquist considerando la frecuencia máxima presente en la señal modulada.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Parámetros de la señal
f_c = 1e6  # 1 MHz portadora
f_m = 5000  # 5 kHz frecuencia máxima de la señal moduladora
duration = 0.001  # 1 ms de duración

# 1. Crear señal moduladora (compuesta por múltiples frecuencias)
fs_analog = 10e6  # Frecuencia "analógica" para simulación
t_analog = np.linspace(0, duration, int(fs_analog * duration))
senal_mod = 0.5 * np.sin(2 * np.pi * 1000 * t_analog) + \
            0.3 * np.sin(2 * np.pi * 3000 * t_analog) + \
            0.2 * np.sin(2 * np.pi * 5000 * t_analog)

# 2. Modular en AM
portadora = np.cos(2 * np.pi * f_c * t_analog)
senal_am = (1 + senal_mod) * portadora

# 3. Frecuencias de muestreo a probar
frecs_muestreo = {
    "Sub-Nyquist (1.8 MHz)": 1.8e6,
    "Nyquist mínimo (2.01 MHz)": 2.01e6,
    "Recomendado (4.0 MHz)": 4.0e6
}

# 4. Análisis espectral para diferentes frecuencias de muestreo
plt.figure(figsize=(14, 10))

for i, (name, fs) in enumerate(frecs_muestreo.items()):
    # Remuestrear la señal
    puntos = int(fs * duration)
    t_sampled = np.linspace(0, duration, puntos)
    senal_sampled = np.interp(t_sampled, t_analog, senal_am)

    # Calcular FFT
    fft_vals = np.abs(np.fft.fft(senal_sampled)) / puntos
    freqs = np.fft.fftfreq(puntos, 1 / fs)

    # Gráfico del espectro
    plt.subplot(3, 1, i + 1)
    plt.plot(np.fft.fftshift(freqs) / 1e6, np.fft.fftshift(fft_vals))
    plt.title(f'{name} - Espectro de la señal AM')
    plt.xlabel('Frecuencia (MHz)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.xlim(0.5, 1.5)  # Zoom alrededor de la portadora

    # Marcadores de frecuencias clave
    plt.axvline(f_c / 1e6, color='r', linestyle='--', alpha=0.5, label='Portadora (1 MHz)')
    plt.axvline((f_c - f_m) / 1e6, color='g', linestyle=':', alpha=0.7, label='Banda lateral inf')
    plt.axvline((f_c + f_m) / 1e6, color='g', linestyle=':', alpha=0.7, label='Banda lateral sup')
    plt.legend()

plt.tight_layout()
plt.show()

# 5. Espectrogramas comparativos
plt.figure(figsize=(14, 12))

for i, (name, fs) in enumerate(frecs_muestreo.items()):
    puntos = int(fs * duration)
    t_sampled = np.linspace(0, duration, puntos)
    senal_sampled = np.interp(t_sampled, t_analog, senal_am)

    plt.subplot(3, 1, i + 1)
    f, t_spec, Sxx = spectrogram(senal_sampled, fs, nperseg=256, noverlap=240)
    plt.pcolormesh(t_spec * 1000, f / 1e6, 10 * np.log10(Sxx),
                   shading='gouraud', cmap='viridis', vmin=-50)
    plt.title(f'Espectrograma - {name}')
    plt.ylabel('Frecuencia (MHz)')
    plt.xlabel('Tiempo (ms)')
    plt.ylim(0.9, 1.1)  # Zoom alrededor de 1 MHz
    plt.colorbar(label='Intensidad (dB)')

plt.tight_layout()
plt.show()

"""Para modular una señal con ancho de banda fm en una portadora de 1 MHz, se utiliza una frecuencia de muestreo de 4.0 MHz
 como valor práctico optimo. Esto proporciona un equilibrio entre calidad de señal y eficiencia computacional, 
con margen suficiente para implementaciones reales que incluyan filtrado anti-aliasing.
"""

#ejercicio 10
"""
Construir funciones que efectúen la multiplexación y demultiplexación por división en frecuencia
de un cierto conjunto de señales de entrada. Dichas funciones deben controlar que se cumplan
las condiciones requeridas (para ello puede graficar el espectro).
"""
from scipy.signal import butter, filtfilt, fftconvolve
from scipy.fft import fft, fftfreq, fftshift

# Frecuencia de muestreo y tiempo
fs = 50000
t = np.linspace(0, 0.1, int(0.1 * fs), endpoint=False)

# Mensajes (moduladoras)
m1 = np.sin(2 * np.pi * 200 * t)
m2 = np.sin(2 * np.pi * 300 * t)
m3 = np.sin(2 * np.pi * 400 * t)

# Portadoras
fc1, fc2, fc3 = 5000, 10000, 15000
c1 = np.cos(2 * np.pi * fc1 * t)
c2 = np.cos(2 * np.pi * fc2 * t)
c3 = np.cos(2 * np.pi * fc3 * t)

#Multiplexación FDM
mux = m1 * c1 + m2 * c2 + m3 * c3

#  Función para graficar espectro
def plot_spectrum(signal, fs, title):
    N = len(signal)
    freqs = fftshift(fftfreq(N, 1/fs))
    spectrum = fftshift(np.abs(fft(signal)) / N)
    plt.plot(freqs / 1e3, spectrum)
    plt.title(title)
    plt.xlabel('Frecuencia (kHz)')
    plt.grid()

# Demultiplexación FDM
def demultiplex(signal, fc, fs, orden=5, fcorte=0.05):
    # Multiplicación coherente con portadora
    portadora = np.cos(2 * np.pi * fc * t)
    demod = signal * portadora
    # Filtro pasa bajos
    b, a = butter(orden, fcorte)
    return filtfilt(b, a, demod)

# Recuperar cada señal
rec1 = demultiplex(mux, fc1, fs)
rec2 = demultiplex(mux, fc2, fs)
rec3 = demultiplex(mux, fc3, fs)

#Graficar
plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plot_spectrum(mux, fs, "Espectro de la señal multiplexada (FDM)")

plt.subplot(4, 1, 2)
plt.plot(t, rec1)
plt.title("Señal recuperada del canal 1")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, rec2)
plt.title("Señal recuperada del canal 2")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, rec3)
plt.title("Señal recuperada del canal 3")
plt.grid()

plt.tight_layout()
plt.show()

""" Multiplexa 3 señales en diferentes bandas usando modulaciones en portadoras diferentes.
    Grafica el espectro completo para verificar separación de bandas.
    Demultiplexa cada canal individualmente con:
    Multiplicación por portadora (demodulación )
    Filtro pasa bajos para recuperar solo la señal original
"""