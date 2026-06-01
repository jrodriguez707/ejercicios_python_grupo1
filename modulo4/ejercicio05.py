# Función suma
def suma(a, b):
    return a + b

# Función resta
def resta(a, b):
    return a - b

# Función multiplicación
def multiplicacion(a, b):
    return a * b

# Pedimos los números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostramos los resultados utilizando las funciones
print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))