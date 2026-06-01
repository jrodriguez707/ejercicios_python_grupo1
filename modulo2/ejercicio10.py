# Aceleración de la gravedad
g = 9.81

# Altura inicial
h0 = float(input("Introduce la altura inicial (m): "))

# Tiempo inicial
t = 0

# Altura actual
altura = h0

# Seguimos mientras el objeto esté por encima del suelo
while altura > 0:

    # Fórmula de caída libre
    altura = h0 - (0.5 * g * t**2)

    # Evitamos mostrar alturas negativas
    if altura < 0:
        altura = 0

    print(f"Tiempo: {t} s --> Altura: {altura:.2f} m")

    t += 1

# El tiempo total es el último segundo calculado
print(f"Tiempo total de caída: {t-1} segundos")