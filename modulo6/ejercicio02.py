# Importamos NumPy
import numpy as np

# Creamos los dos vectores
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Suma de vectores elemento a elemento
suma = A + B

# Producto elemento a elemento
producto_elemento = A * B

# Producto escalar (dot product)
producto_escalar = np.dot(A, B)

# Mostramos resultados
print("Vector A:", A)
print("Vector B:", B)
print("Suma:", suma)
print("Producto elemento a elemento:", producto_elemento)
print("Producto escalar:", producto_escalar)