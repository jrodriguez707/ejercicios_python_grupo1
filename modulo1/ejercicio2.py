# Ejercicio 2 - Operaciones con números

# Solicitar dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

# Mostrar los resultados
print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Resto (módulo):", resto)
print("Potencia:", potencia)