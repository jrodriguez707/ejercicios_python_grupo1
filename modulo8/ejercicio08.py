# Pedimos los datos
k = float(input("Constante del resorte (N/m): "))
x = float(input("Deformación (m): "))

# Calculamos la fuerza
fuerza = k * x

print("Fuerza =", fuerza, "N")

# Generamos una tabla de valores
print("\nTABLA DE DEFORMACIONES")
print("x(m)\tF(N)")

for deformacion in range(6):

    fuerza = k * deformacion

    print(deformacion, "\t", fuerza)