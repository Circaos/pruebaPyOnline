print("hello world")

import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Saludo", f"Hola, {entrada.get()}!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi primera GUI")

# Añadir widgets
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Ejecutar el bucle principal
ventana.mainloop()