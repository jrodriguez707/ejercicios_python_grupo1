# Función que devuelve el cuadrado de un número
def cuadrado(numero):
    return numero ** 2

# Pedimos un número al usuario
num = float(input("Introduce un número: "))

# Guardamos el resultado devuelto por la función
resultado = cuadrado(num)

# Mostramos el resultado
print("El cuadrado es:", resultado)