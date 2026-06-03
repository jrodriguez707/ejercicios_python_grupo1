# Solicitamos los datos al usuario
fuerza = float(input("Fuerza aplicada (N): "))
area = float(input("Área (m²): "))

# Calculamos el esfuerzo
esfuerzo = fuerza / area

# Mostramos el resultado en Pascales
print("Esfuerzo =", esfuerzo, "Pa")

# Límite de 250 MPa
limite = 250e6

# Comprobamos si supera el límite
if esfuerzo > limite:
    print("El material supera el límite de 250 MPa")
else:
    print("El material trabaja dentro del límite permitido")