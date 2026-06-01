# Pedimos al usuario una temperatura en grados Celsius
temperatura = float(input("Introduce una temperatura en °C: "))

# Comprobamos en qué rango se encuentra
if temperatura < 0:
    print("Estado sólido probable")
elif temperatura < 100:
    # Si no es menor que 0 y sí menor que 100
    print("Estado líquido probable")
else:
    # Si es 100 o mayor
    print("Estado gaseoso probable")