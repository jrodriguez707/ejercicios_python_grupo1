# Preguntamos el tipo de conexión
tipo = input("¿Las resistencias están en serie o paralelo? ").lower()

# Pedimos los valores
R1 = float(input("Introduce R1: "))
R2 = float(input("Introduce R2: "))

# Calculamos según el tipo elegido
if tipo == "serie":
    Req = R1 + R2
    print("Resistencia equivalente =", Req, "ohmios")

elif tipo == "paralelo":
    Req = (R1 * R2) / (R1 + R2)
    print("Resistencia equivalente =", Req, "ohmios")

else:
    print("Tipo de conexión no válido.")