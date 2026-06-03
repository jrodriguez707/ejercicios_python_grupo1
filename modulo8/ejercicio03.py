# Pedimos los datos necesarios
k = float(input("Conductividad térmica (W/mK): "))
area = float(input("Área (m²): "))
t1 = float(input("Temperatura 1 (°C): "))
t2 = float(input("Temperatura 2 (°C): "))
espesor = float(input("Espesor (m): "))

# Aplicamos la ecuación
flujo_calor = k * area * (t1 - t2) / espesor

# Mostramos el resultado
print("Flujo de calor =", flujo_calor, "W")