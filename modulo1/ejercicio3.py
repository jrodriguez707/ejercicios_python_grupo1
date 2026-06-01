# Ejercicio 3 - Manipulación de cadenas

# Pedir al usuario su nombre completo
nombre = input("Introduce tu nombre completo: ")

# Convertir a mayúsculas
mayusculas = nombre.upper()

# Convertir a minúsculas
minusculas = nombre.lower()

# Contar caracteres sin espacios
sin_espacios = nombre.replace(" ", "")
longitud_sin_espacios = len(sin_espacios)

# Primeros 4 caracteres
primeros_4 = nombre[:4]

# Mostrar resultados
print("\nResultados:")
print("Nombre en mayúsculas:", mayusculas)
print("Nombre en minúsculas:", minusculas)
print("Número de caracteres (sin espacios):", longitud_sin_espacios)
print("Primeros 4 caracteres:", primeros_4)