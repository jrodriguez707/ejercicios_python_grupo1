# Pedimos el valor de la resistencia
R = float(input("Introduce el valor de la resistencia (ohmios): "))

print("\nTabla de voltajes")

# Corrientes desde 0 hasta 10 A
for I in range(0, 11):

    # Aplicamos la Ley de Ohm
    V = I * R

    print(f"I = {I} A --> V = {V:.2f} V")