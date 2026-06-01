# Ejercicio 5 - Conversión de tipos

# Pedir el peso como texto
peso_texto = input("Introduce tu peso en kilogramos: ")

# Convertir a número (float para permitir decimales)
peso_kg = float(peso_texto)

# Conversión a gramos
peso_gramos = peso_kg * 1000

# Mostrar resultados
print("\nResultados:")
print("Peso en kg:", peso_kg)
print("Peso en gramos:", peso_gramos)