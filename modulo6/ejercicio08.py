# Importamos Matplotlib
import matplotlib.pyplot as mplt


# Tal vez tengas que instalar la libreria matplotlib si no la tienes.
# Usa el siguiente comando:  python3.exe -m pip install matplotlib
# Esta se usa para ver los graficos.


# Datos experimentales
temperatura = [20, 22, 25, 27, 30]
presion = [1.01, 1.03, 1.05, 1.08, 1.10]

# Creamos el gráfico de dispersión
mplt.scatter(temperatura, presion, color="red")

# Añadimos título y etiquetas
mplt.title("Relación entre temperatura y presión")
mplt.xlabel("Temperatura (°C)")
mplt.ylabel("Presión (atm)")

# Mostramos cuadrícula
mplt.grid(True)

# Mostramos el gráfico
mplt.show()