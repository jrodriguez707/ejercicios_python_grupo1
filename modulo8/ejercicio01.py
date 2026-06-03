# Importamos la librería matemática para usar π
import math

# Mostramos un menú al usuario
print("CÁLCULO DE ÁREAS")
print("1. Rectángulo")
print("2. Círculo")
print("3. Triángulo")

# Leemos la opción elegida
opcion = int(input("Seleccione una opción: "))

# Calculamos el área según la figura elegida
if opcion == 1:
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    area = base * altura

    print("Área del rectángulo =", area)

elif opcion == 2:
    radio = float(input("Radio: "))

    area = math.pi * radio**2

    print("Área del círculo =", area)

elif opcion == 3:
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    area = (base * altura) / 2

    print("Área del triángulo =", area)

else:
    print("Opción no válida")