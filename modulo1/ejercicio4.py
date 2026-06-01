# Ejercicio 4 - Uso de booleanos y operadores relacionales

# Pedir la edad al usuario
edad = int(input("Introduce tu edad: "))

# Condiciones lógicas
es_mayor_de_edad = edad >= 18
tiene_18 = edad == 18
entre_18_y_30 = edad >= 18 and edad <= 30

# Mostrar resultados
print("\nResultados booleanos:")
print("¿Es mayor de edad?:", es_mayor_de_edad)
print("¿Tiene exactamente 18 años?:", tiene_18)
print("¿Está entre 18 y 30 años?:", entre_18_y_30)