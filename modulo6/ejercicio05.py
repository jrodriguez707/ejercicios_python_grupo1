# Importamos NumPy
import numpy as np

# Generamos 100 ángulos entre 0 y 2π radianes
x = np.linspace(0, 2 * np.pi, 100)

# Calculamos seno y coseno
seno = np.sin(x)
coseno = np.cos(x)

# Mostramos resultados
print("Ángulos:")
print(x)

print("\nSeno:")
print(seno)

print("\nCoseno:")
print(coseno)