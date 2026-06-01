# Pedimos el número del que queremos la tabla
numero = int(input("Introduce un número: "))

# Recorremos los valores del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")