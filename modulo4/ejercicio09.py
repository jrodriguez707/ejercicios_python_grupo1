# Función que calcula la temperatura media
def temperatura_media(lista):

    # Sumamos todos los elementos y dividimos por la cantidad
    return sum(lista) / len(lista)

# Lista vacía para guardar las mediciones
temperaturas = []

# Pedimos 5 mediciones
for i in range(5):

    temp = float(input(f"Introduce la temperatura {i+1}: "))
    temperaturas.append(temp)

# Calculamos el promedio
media = temperatura_media(temperaturas)

# Mostramos el resultado
print("La temperatura media es:", media)