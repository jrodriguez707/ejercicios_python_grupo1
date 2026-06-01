# Importamos la librería matemática para usar sqrt()
import math

# Función que resuelve la ecuación cuadrática
def resolver_cuadratica(a, b, c):

    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    # Calculamos las dos raíces
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)

    # Devolvemos ambas raíces
    return x1, x2

# Pedimos los coeficientes
a = float(input("Introduce a: "))
b = float(input("Introduce b: "))
c = float(input("Introduce c: "))

# Obtenemos las raíces
raiz1, raiz2 = resolver_cuadratica(a, b, c)

# Mostramos las soluciones
print("Raíz 1:", raiz1)
print("Raíz 2:", raiz2)