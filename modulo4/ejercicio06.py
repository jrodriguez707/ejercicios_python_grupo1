# Función que calcula la velocidad
def calcular_velocidad(distancia, tiempo):

    # Aplicamos la fórmula velocidad = distancia / tiempo
    return distancia / tiempo

# Pedimos los datos
distancia = float(input("Introduce la distancia recorrida: "))
tiempo = float(input("Introduce el tiempo empleado: "))

# Calculamos la velocidad
velocidad = calcular_velocidad(distancia, tiempo)

# Mostramos el resultado
print("La velocidad es:", velocidad)