# Importamos NumPy y Matplotlib
import numpy as np
import matplotlib.pyplot as mplt


# Tal vez tengas que instalar la libreria matplotlib si no la tienes.
# Usa el siguiente comando:  python3.exe -m pip install matplotlib
# Esta se usa para ver los graficos.


# Generamos 100 valores de tiempo entre 0 y 10 segundos
t = np.linspace(0, 10, 100)

# Calculamos la posición usando x = t²
x = t ** 2

# Creamos el gráfico
mplt.plot(t, x)

# Añadimos título y etiquetas
mplt.title("Posición en función del tiempo")
mplt.xlabel("Tiempo (s)")
mplt.ylabel("Posición (m)")

# Mostramos una cuadrícula
mplt.grid(True)

# Mostramos el gráfico
mplt.show()