# Contraseña correcta
password_correcta = "python123"

# Contador de intentos
intentos = 0

# Máximo 3 intentos
while intentos < 3:
    password = input("Introduce la contraseña: ")

    # Si coincide, se concede acceso
    if password == password_correcta:
        print("Acceso concedido")
        break

    intentos += 1
    print("Contraseña incorrecta")

# Si llega a 3 intentos sin acertar
if intentos == 3:
    print("Acceso bloqueado")