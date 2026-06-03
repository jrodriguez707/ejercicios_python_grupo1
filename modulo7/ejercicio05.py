# Importamos pandas
import pandas as pd

# Leemos el archivo CSV
df = pd.read_csv("datos_sensor.csv")

# Mostramos el número de filas y columnas
print("Dimensiones del DataFrame:")
print(df.shape)

# Mostramos los tipos de datos de cada columna
print("\nTipos de datos:")
print(df.dtypes)

# Mostramos un resumen estadístico
print("\nResumen estadístico:")
print(df.describe())