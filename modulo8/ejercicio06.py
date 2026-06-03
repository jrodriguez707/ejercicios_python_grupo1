# Pedimos datos iniciales
x0 = float(input("Posición inicial (m): "))
v = float(input("Velocidad (m/s): "))

print("\nTiempo\tPosición")

# Simulamos desde t=0 hasta t=10
for t in range(11):

    x = x0 + v * t

    print(t, "\t", x)