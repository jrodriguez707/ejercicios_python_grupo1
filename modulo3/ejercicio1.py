# Ejercicio 1 – Crear y recorrer una lista
# Objetivo: practicar listas e iteración

# Creamos una lista vacía donde guardaremos las temperaturas
temperaturas = []

# Pedimos al usuario 5 temperaturas
for i in range(5):
    temp = float(input(f"Introduce la temperatura {i+1}: "))
    temperaturas.append(temp)  # añadimos cada valor a la lista

# Mostramos todas las temperaturas introducidas
print("\nTemperaturas introducidas:")
for temp in temperaturas:
    print(temp)

# Calculamos la media de las temperaturas
suma = 0
for temp in temperaturas:
    suma += temp

media = suma / len(temperaturas)

# Mostramos el resultado
print(f"\nLa temperatura media es: {media}")