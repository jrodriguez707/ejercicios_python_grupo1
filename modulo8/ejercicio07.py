# Pedimos las resistencias
r1 = float(input("R1 (ohmios): "))
r2 = float(input("R2 (ohmios): "))
r3 = float(input("R3 (ohmios): "))

# Pedimos el voltaje
voltaje = float(input("Voltaje (V): "))

# Calculamos la resistencia equivalente
rtotal = r1 + r2 + r3

# Calculamos la corriente
corriente = voltaje / rtotal

# Mostramos resultados
print("Resistencia total =", rtotal, "ohmios")
print("Corriente =", corriente, "A")