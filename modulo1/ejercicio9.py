# Ejercicio 9 - Ley de Ohm
# Fórmula: V = I * R

# Pedimos la corriente en amperios
corriente = float(input("Introduce la corriente (en amperios): "))

# Pedimos la resistencia en ohmios
resistencia = float(input("Introduce la resistencia (en ohmios): "))

# Calculamos el voltaje
voltaje = corriente * resistencia

# Mostramos el resultado con dos decimales
print(f"\nEl voltaje es: {voltaje:.2f} V")