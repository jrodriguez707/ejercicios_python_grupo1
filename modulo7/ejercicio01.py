# Importamos la librería pandas y la renombramos como pd
import pandas as pd

# Tal vez tengas que instalar la libreria pandas si no la tienes.
# Usa el siguiente comando:  python3.exe -m pip install pandas
# Su función principal es el procesamiento, manipulación y análisis de datos tabulares.


# Creamos una Serie con las mediciones de temperatura
temperaturas = pd.Series([22.4, 23.1, 21.8, 24.0, 22.9])

# Mostramos la serie completa
print("Serie de temperaturas:")
print(temperaturas)

# Obtenemos y mostramos el valor máximo
print("\nTemperatura máxima:")
print(temperaturas.max())

# Calculamos y mostramos el promedio
print("\nTemperatura promedio:")
print(temperaturas.mean())