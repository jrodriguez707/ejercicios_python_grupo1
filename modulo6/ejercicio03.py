# Importamos NumPy
import numpy as np

# Creamos una matriz vacía
matriz = []

# Solicitamos los valores al usuario
for i in range(3):
    fila = []
    
    for j in range(3):
        valor = float(input(f"Introduce el valor [{i}][{j}]: "))
        fila.append(valor)
    
    matriz.append(fila)

# Convertimos la lista en una matriz NumPy
matriz = np.array(matriz)

# Mostramos la matriz completa
print("\nMatriz:")
print(matriz)

# Calculamos la suma de cada fila (axis=1)
print("\nSuma de cada fila:")
print(np.sum(matriz, axis=1))

# Calculamos la suma de cada columna (axis=0)
print("\nSuma de cada columna:")
print(np.sum(matriz, axis=0))