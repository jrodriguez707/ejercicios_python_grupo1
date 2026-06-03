# Importamos SymPy
import sympy as sp

# Tal vez tengas que instalar la libreria sympy si no la tienes.
# Usa el siguiente comando:  python3.exe -m pip install sympy
# Esta se usa para ver definir funciones.


# Definimos la variable simbólica
x = sp.Symbol('x')

# Definimos la función
f = x**3 + 2*x**2 - x

# Calculamos la derivada
derivada = sp.diff(f, x)

# Evaluamos en x=2
valor = derivada.subs(x, 2)

# Mostramos resultados
print("Función:", f)
print("Derivada:", derivada)
print("Derivada evaluada en x=2:", valor)