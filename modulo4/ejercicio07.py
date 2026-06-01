# Función que calcula el voltaje
def calcular_voltaje(corriente, resistencia):

    # Aplicamos la Ley de Ohm
    return corriente * resistencia

# Pedimos los datos
corriente = float(input("Introduce la corriente (A): "))
resistencia = float(input("Introduce la resistencia (Ω): "))

# Calculamos el voltaje
voltaje = calcular_voltaje(corriente, resistencia)

# Mostramos el resultado con dos decimales
print(f"El voltaje es: {voltaje:.2f} V")