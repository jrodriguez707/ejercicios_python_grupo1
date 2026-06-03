# Importamos NumPy
import numpy as np

# Vector de temperaturas
temperaturas = np.array([22.3, 23.1, 21.9, 24.0, 22.7, 23.5])

# Cálculos estadísticos
promedio = np.mean(temperaturas)
desviacion = np.std(temperaturas)
maximo = np.max(temperaturas)
minimo = np.min(temperaturas)

# Mostramos resultados
print("Promedio:", promedio)
print("Desviación estándar:", desviacion)
print("Máximo:", maximo)
print("Mínimo:", minimo)