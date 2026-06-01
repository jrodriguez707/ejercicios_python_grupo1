# Pedimos la nota al usuario
nota = float(input("Introduce una nota (0-10): "))

# Primero validamos que esté dentro del rango permitido
if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
elif nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")