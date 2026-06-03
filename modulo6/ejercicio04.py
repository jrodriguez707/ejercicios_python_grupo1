# Importamos NumPy
import numpy as np

# Generamos 50 valores entre 0 y 10
valores = np.linspace(0, 10, 50)

# Calculamos el cuadrado de cada valor
cuadrado = valores ** 2

# Calculamos la raíz cuadrada de cada valor
raiz = np.sqrt(valores)

# Mostramos resultados
print("Valores:")
print(valores)

print("\nCuadrado:")
print(cuadrado)

print("\nRaíz cuadrada:")
print(raiz)