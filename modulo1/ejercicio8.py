# Ejercicio 8 - Cálculo de velocidad (Física básica)

# Fórmula: v = d / t

# Pedimos la distancia recorrida en metros
distancia = float(input("Introduce la distancia recorrida (en metros): "))

# Pedimos el tiempo empleado en segundos
tiempo = float(input("Introduce el tiempo empleado (en segundos): "))

# Evitamos división por cero
if tiempo != 0:
    # Calculamos la velocidad
    velocidad = distancia / tiempo

    # Mostramos el resultado
    print("\nLa velocidad es:", velocidad, "m/s")
else:
    print("\nError: el tiempo no puede ser 0.")