# Importamos pandas
import pandas as pd

# Leemos el archivo CSV
df = pd.read_csv("ensayo_traccion.csv")

# Mostramos estadísticas básicas
print("Estadísticas básicas:")
print(df.describe())

# Mostramos valores máximos
print("\nValores máximos:")
print(df.max())

# Mostramos valores mínimos
print("\nValores mínimos:")
print(df.min())

# Calculamos el promedio de la fuerza
promedio_fuerza = df["fuerza"].mean()

# Filtramos los datos donde la fuerza es mayor que el promedio
fuerza_superior_promedio = df[df["fuerza"] > promedio_fuerza]

# Mostramos el resultado
print("\nDatos con fuerza superior al promedio:")
print(fuerza_superior_promedio)