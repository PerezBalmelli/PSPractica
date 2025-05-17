'''
5. Implementar, sin usar las librerías o funciones provistas por el lenguaje,
una función que efectúe la convolución discreta entre dos señales. 
Asegurarse de que la longitud de la señal de salida sea la correcta.
'''
def convolucion_discreta(x, h):
    """
    Realiza la convolución discreta entre dos señales x[n] y h[n].

    Parámetros:
    - x: lista de números (señal de entrada)
    - h: lista de números (respuesta al impulso)

    Retorna:
    - y: lista con la señal resultante de la convolución
    """
    Lx = len(x)
    Lh = len(h)
    Ly = Lx + Lh - 1  # Longitud de la señal de salida
    y = [0] * Ly      # Inicializa la salida

    for n in range(Ly):
        suma = 0
        for k in range(Lh):
            if 0 <= n - k < Lx:
                suma += x[n - k] * h[k]
        y[n] = suma

    return y

def ingresar_senal(nombre):
    """
    Permite ingresar una señal desde consola como lista de números.
    """
    entrada = input(f"Ingrese los valores de la señal {nombre} separados por comas: ")
    return [float(valor) for valor in entrada.split(",")]

def mostrar_senal(nombre, senal):
    """
    Muestra la señal por consola.
    """
    print(f"{nombre} = {senal}")


if __name__ == "__main__":
    print("Convolución Discreta Manual\n")
    
    # Ingreso de señales
    x = ingresar_senal("x[n]")
    h = ingresar_senal("h[n]")

    # Convolución
    y = convolucion_discreta(x, h)

    # Resultados
    mostrar_senal("x[n]", x)
    mostrar_senal("h[n]", h)
    mostrar_senal("y[n] = x[n] * h[n]", y)


