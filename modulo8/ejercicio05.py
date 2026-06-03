# Importamos NumPy
import numpy as np

# Matriz de coeficientes
A = np.array([
    [1, 1],
    [1, -1]
])

# Vector de términos independientes
B = np.array([10, 2])

# Resolvemos el sistema
solucion = np.linalg.solve(A, B)

# Mostramos resultados
print("x =", solucion[0])
print("y =", solucion[1])