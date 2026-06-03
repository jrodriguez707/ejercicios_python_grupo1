# Importamos Tkinter
import tkinter as tk

# Función que realiza el cálculo
def calcular_esfuerzo():

    fuerza = float(entry_fuerza.get())
    area = float(entry_area.get())

    esfuerzo = fuerza / area

    resultado.config(
        text=f"Esfuerzo = {esfuerzo:.2f} Pa"
    )

# Creamos la ventana principal
ventana = tk.Tk()

ventana.title("Calculadora de esfuerzo")

# Ancho x Alto
ventana.geometry("300x200")

# Etiquetas
tk.Label(ventana, text="Fuerza (N)").pack()

# Caja de texto para fuerza
entry_fuerza = tk.Entry(ventana)
entry_fuerza.pack()

# Etiqueta área
tk.Label(ventana, text="Área (m²)").pack()

# Caja de texto para área
entry_area = tk.Entry(ventana)
entry_area.pack()

# Botón para calcular
tk.Button(
    ventana,
    text="Calcular",
    command=calcular_esfuerzo
).pack()

# Etiqueta donde se mostrará el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciamos la aplicación
ventana.mainloop()