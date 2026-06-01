# Pedimos un número entero
numero = int(input("Introduce un número entero: "))

# Comprobamos si es par o impar usando el operador %
if numero % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")

# Comprobamos si es múltiplo de 5
if numero % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 5")

# Comprobamos si es positivo, negativo o cero
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")