# Importamos pandas
import pandas as pd

# Leemos el archivo CSV
df = pd.read_csv("datos_sensor.csv")

# Mostramos las primeras 5 filas
print("Primeras 5 filas:")
print(df.head())