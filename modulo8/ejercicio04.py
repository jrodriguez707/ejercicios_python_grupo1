# Importamos fsolve
from scipy.optimize import fsolve

# Definimos la función
def ecuacion(x):
    return x**3 - x - 2

# Estimación inicial
x0 = 1

# Calculamos la raíz
raiz = fsolve(ecuacion, x0)

# Mostramos el resultado
print("Raíz aproximada:", raiz[0])