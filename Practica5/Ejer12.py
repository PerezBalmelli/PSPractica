import numpy as np
import time


# --- Código Original del Ejercicio 5 ---

def convolucion_discreta(x, h):
    """
    Realiza la convolución discreta entre dos señales x[n] y h[n].
    (Implementación directa o por "fuerza bruta")

    Parámetros:
    - x: lista de números (señal de entrada)
    - h: lista de números (respuesta al impulso)

    Retorna:
    - y: lista con la señal resultante de la convolución
    """
    Lx = len(x)
    Lh = len(h)
    Ly = Lx + Lh - 1  # Longitud de la señal de salida
    y = [0] * Ly  # Inicializa la salida

    for n in range(Ly):
        suma = 0
        for k in range(Lh):
            # Asegura que el índice de x esté dentro de los límites
            if 0 <= n - k < Lx:
                suma += x[n - k] * h[k]
        y[n] = suma

    return y


# --- Nueva Implementación: Convolución en Frecuencia ---

def convolucion_frecuencia(x, h):
    """
    Realiza la convolución de dos señales en el dominio de la frecuencia
    usando la Transformada Rápida de Fourier (FFT).

    Parámetros:
    - x: lista de números (señal de entrada)
    - h: lista de números (respuesta al impulso)

    Retorna:
    - y: lista con la señal resultante de la convolución
    """
    Lx = len(x)
    Lh = len(h)
    Ly = Lx + Lh - 1  # Longitud final de la convolución

    # 1. Aplicar FFT a ambas señales con padding a la longitud final
    X = np.fft.fft(x, Ly)
    H = np.fft.fft(h, Ly)

    # 2. Multiplicar en el dominio de la frecuencia
    Y = X * H

    # 3. Aplicar la Transformada Inversa de Fourier
    y_complex = np.fft.ifft(Y)

    # 4. Tomar la parte real y redondear para corregir pequeñas imprecisiones numéricas
    # y convertir a lista para mantener consistencia.
    y = np.real(y_complex)

    return y.tolist()


def ingresar_senal(nombre):
    """
    Permite ingresar una señal desde consola como lista de números.
    """
    entrada = input(f"Ingrese los valores de la señal {nombre} separados por comas: ")
    return [float(valor) for valor in entrada.split(",")]


def mostrar_senal(nombre, senal):
    """
    Muestra la señal por consola, redondeando los valores para una mejor lectura.
    """
    # Redondea los valores a 4 decimales para una visualización más limpia
    senal_redondeada = [round(valor, 4) for valor in senal]
    print(f"{nombre} = {senal_redondeada}")


if __name__ == "__main__":
    print("Comparación de Convolución Discreta\n")

    # --- Ingreso de señales ---
    # Para probar, puedes usar señales simples como:
    # x[n] = 1,2,3
    # h[n] = 1,1
    x = ingresar_senal("x[n]")
    h = ingresar_senal("h[n]")

    # --- Verificación y Tiempos de Procesamiento ---

    # 1. Método Directo
    print("\n--- 1. Método: Convolución Directa (Dominio del Tiempo) ---")
    inicio_directa = time.perf_counter()
    y_directa = convolucion_discreta(x, h)
    fin_directa = time.perf_counter()
    tiempo_directa = fin_directa - inicio_directa

    mostrar_senal("Señal x[n]", x)
    mostrar_senal("Señal h[n]", h)
    mostrar_senal("Resultado y[n]", y_directa)
    print(f"⏱️  Tiempo de procesamiento: {tiempo_directa:.8f} segundos")

    # 2. Método en Frecuencia
    print("\n--- 2. Método: Convolución por FFT (Dominio de la Frecuencia) ---")
    inicio_frecuencia = time.perf_counter()
    y_frecuencia = convolucion_frecuencia(x, h)
    fin_frecuencia = time.perf_counter()
    tiempo_frecuencia = fin_frecuencia - inicio_frecuencia

    mostrar_senal("Señal x[n]", x)
    mostrar_senal("Señal h[n]", h)
    mostrar_senal("Resultado y[n]", y_frecuencia)
    print(f"⏱️  Tiempo de procesamiento: {tiempo_frecuencia:.8f} segundos")

    # --- Comparación de Tiempos ---
    print("\n--- Comparación ---")
    diferencia = abs(tiempo_directa - tiempo_frecuencia)
    if tiempo_frecuencia < tiempo_directa:
        print(f"✅ El método de frecuencia (FFT) fue {diferencia:.8f} segundos más rápido.")
        if tiempo_frecuencia > 0:
            veces_mas_rapido = tiempo_directa / tiempo_frecuencia
            print(f"   Es aproximadamente {veces_mas_rapido:.2f} veces más rápido.")
    else:
        print(f"✅ El método directo fue {diferencia:.8f} segundos más rápido.")
        if tiempo_directa > 0:
            veces_mas_rapido = tiempo_frecuencia / tiempo_directa
            print(f"   Es aproximadamente {veces_mas_rapido:.2f} veces más rápido.")

    # Verificar si los resultados son iguales (considerando tolerancia numérica)
    if np.allclose(y_directa, y_frecuencia):
        print("\nResultados verificados: Ambas funciones producen la misma señal de salida. 👍")
    else:
        print("\n¡Atención! Los resultados de las convoluciones no coinciden. 👎")


# Comparación de Convolución Discreta
#
# Ingrese los valores de la señal x[n] separados por comas: 1,2,3
# Ingrese los valores de la señal h[n] separados por comas: 1,1
#
# --- 1. Método: Convolución Directa (Dominio del Tiempo) ---
# Señal x[n] = [1.0, 2.0, 3.0]
# Señal h[n] = [1.0, 1.0]
# Resultado y[n] = [1.0, 3.0, 5.0, 3.0]
# ⏱️  Tiempo de procesamiento: 0.00000850 segundos
#
# --- 2. Método: Convolución por FFT (Dominio de la Frecuencia) ---
# Señal x[n] = [1.0, 2.0, 3.0]
# Señal h[n] = [1.0, 1.0]
# Resultado y[n] = [1.0, 3.0, 5.0, 3.0]
# ⏱️  Tiempo de procesamiento: 0.00004510 segundos
#
# --- Comparación ---
# ✅ El método directo fue 0.00003660 segundos más rápido.
#    Es aproximadamente 5.31 veces más rápido.
#
# Resultados verificados: Ambas funciones producen la misma señal de salida. 👍