# Importamos pandas
import pandas as pd
import numpy as np

# Creamos un DataFrame con algunos valores faltantes (NaN)
datos = {
    "Temperatura": [22, np.nan, 24, 23],
    "Presion": [1.01, 1.03, np.nan, 1.02]
}

df = pd.DataFrame(datos)

# Mostramos el DataFrame original
print("DataFrame original:")
print(df)

# Detectamos los valores faltantes
print("\nValores faltantes:")
print(df.isnull())

# Eliminamos las filas que tengan al menos un NaN
df_limpio = df.dropna()

# Mostramos el DataFrame limpio
print("\nDataFrame sin valores faltantes:")
print(df_limpio)