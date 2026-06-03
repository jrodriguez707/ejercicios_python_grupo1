# Importamos pandas
import pandas as pd

# Creamos el DataFrame
datos = {
    "Tiempo": [1, 2, 3, 4, 5],
    "Temperatura": [22, 23, 24, 23, 22],
    "Presion": [1.01, 1.03, 1.04, 1.02, 1.01]
}

df = pd.DataFrame(datos)

# Mostramos la primera fila (índice 0)
print("Primera fila:")
print(df.iloc[0])

# Mostramos la última fila
print("\nÚltima fila:")
print(df.iloc[-1])

# Mostramos las tres primeras filas
print("\nPrimeras 3 filas:")
print(df.head(3))