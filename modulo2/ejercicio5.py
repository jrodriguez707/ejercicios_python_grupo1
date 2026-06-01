# Variable donde acumularemos la suma
suma = 0

# Contador de números introducidos
contador = 0

# Pedimos el primer número
numero = float(input("Introduce un número (0 para terminar): "))

# Mientras no sea 0 seguimos pidiendo datos
while numero != 0:
    suma += numero
    contador += 1

    numero = float(input("Introduce otro número (0 para terminar): "))

# Mostramos resultados finales
print("Suma total:", suma)
print("Cantidad de números introducidos:", contador)