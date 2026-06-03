# Importamos NumPy y Matplotlib
import numpy as np
import matplotlib.pyplot as plt


# Tal vez tengas que instalar la libreria matplotlib si no la tienes.
# Usa el siguiente comando:  python3.exe -m pip install matplotlib
# Esta se usa para ver los graficos.


# Definimos las constantes del problema
h0 = 100      # altura inicial (m)
g = 9.81      # gravedad (m/s²)

# Generamos valores de tiempo entre 0 y 5 segundos
t = np.linspace(0, 5, 100)

# Aplicamos la ecuación de caída libre
h = h0 - 0.5 * g * t**2

# Creamos el gráfico
plt.plot(t, h, color="blue")

# Añadimos título y etiquetas
plt.title("Caída libre de un objeto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")

# Mostramos cuadrícula
plt.grid(True)

# Mostramos el gráfico
plt.show()