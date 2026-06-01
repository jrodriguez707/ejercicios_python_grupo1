# Función que comprueba si un número es par
def es_par(numero):

    # Si el resto de dividir entre 2 es 0, es par
    if numero % 2 == 0:
        return True
    else:
        return False

# Pedimos un número
num = int(input("Introduce un número: "))

# Mostramos el resultado
print("¿Es par?", es_par(num))