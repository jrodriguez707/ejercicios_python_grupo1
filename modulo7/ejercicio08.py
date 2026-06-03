# Importamos pandas
import pandas as pd

# Creamos un DataFrame con distancia y tiempo
datos = {
    "distancia": [100, 200, 150, 300],
    "tiempo": [10, 20, 15, 25]
}

df = pd.DataFrame(datos)

# Creamos una nueva columna llamada velocidad
# Dividiendo la distancia entre el tiempo
df["velocidad"] = df["distancia"] / df["tiempo"]

# Mostramos el resultado
print(df)