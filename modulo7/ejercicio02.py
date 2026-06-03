# Importamos pandas
import pandas as pd

# Creamos un diccionario con los datos de los sensores
datos = {
    "Tiempo": [1, 2, 3, 4, 5],
    "Temperatura": [22, 23, 24, 23, 22],
    "Presion": [1.01, 1.03, 1.04, 1.02, 1.01]
}

# Convertimos el diccionario en un DataFrame
df = pd.DataFrame(datos)

# Mostramos el DataFrame completo
print("DataFrame completo:")
print(df)

# Mostramos únicamente la columna Temperatura
print("\nColumna Temperatura:")
print(df["Temperatura"])