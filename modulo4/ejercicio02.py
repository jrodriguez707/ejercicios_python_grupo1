# Función que calcula el área de un rectángulo
def area_rectangulo(base, altura):
    # Calculamos el área
    area = base * altura

    # Mostramos el resultado
    print("El área del rectángulo es:", area)

# Pedimos los datos al usuario
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

# Llamamos a la función enviando los valores introducidos
area_rectangulo(base, altura)