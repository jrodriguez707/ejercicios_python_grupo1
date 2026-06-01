# Función que calcula la energía cinética
def energia_cinetica(masa, velocidad):

    # Aplicamos la fórmula Ec = 1/2 * m * v²
    return 0.5 * masa * (velocidad ** 2)

# Calculamos la energía de 3 objetos
for i in range(1, 4):

    print(f"\nObjeto {i}")

    masa = float(input("Introduce la masa: "))
    velocidad = float(input("Introduce la velocidad: "))

    energia = energia_cinetica(masa, velocidad)

    print("Energía cinética:", energia)