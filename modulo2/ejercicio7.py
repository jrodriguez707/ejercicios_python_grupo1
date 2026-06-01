# Generamos temperaturas desde 0 hasta 100
for celsius in range(0, 101, 10):

    # Aplicamos la fórmula de conversión
    fahrenheit = (9/5) * celsius + 32

    print(f"{celsius} °C = {fahrenheit:.1f} °F")