# Ejercicio 10 - Energía cinética
# Fórmula: Ek = (1/2) * m * v^2

# Pedimos la masa del objeto en kg
masa = float(input("Introduce la masa del objeto (kg): "))

# Pedimos la velocidad en m/s
velocidad = float(input("Introduce la velocidad del objeto (m/s): "))

# Calculamos la energía cinética
energia_cinetica = 0.5 * masa * (velocidad ** 2)

# Mostramos el resultado en julios
print(f"\nLa energía cinética es: {energia_cinetica:.2f} J")