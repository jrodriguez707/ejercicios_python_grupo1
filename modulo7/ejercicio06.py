# Importamos pandas
import pandas as pd

# Creamos un DataFrame con temperaturas
datos = {
    "Tiempo": [1, 2, 3, 4, 5],
    "Temperatura": [22, 23, 24, 25, 22]
}

df = pd.DataFrame(datos)

# Filtramos las filas donde la temperatura sea mayor que 23
temperaturas_altas = df[df["Temperatura"] > 23]

# Mostramos el resultado
print("Temperaturas mayores de 23 °C:")
print(temperaturas_altas)