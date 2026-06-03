# Importamos pandas
import pandas as pd

# Creamos un DataFrame con datos de materiales
datos = {
    "material": ["Acero", "Aluminio", "Titanio", "Cobre"],
    "resistencia": [500, 300, 600, 250],
    "densidad": [7.8, 2.7, 4.5, 8.9]
}

df = pd.DataFrame(datos)

# Buscamos la fila que contiene la resistencia máxima
material_mas_resistente = df.loc[df["resistencia"].idxmax()]

# Mostramos el material con mayor resistencia
print("Material con mayor resistencia:")
print(material_mas_resistente)

# Calculamos la resistencia promedio
promedio_resistencia = df["resistencia"].mean()

# Mostramos el resultado
print("\nResistencia promedio:")
print(promedio_resistencia)