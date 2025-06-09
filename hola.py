print("hello world")

import tkinter as tk
from tkinter import messagebox


print("""
****************************************************
****************************************************
  ____  _                           _     _        
 |  _ \(_)                         (_)   | |       
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___   
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \  
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | 
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/  
  / ____|    (_)   | |            | |              
 | |     _ __ _ ___| |_ ___  _ __ | |__   ___ _ __ 
 | |    | '__| / __| __/ _ \| '_ \| '_ \ / _ \ '__|
 | |____| |  | \__ \ || (_) | |_) | | | |  __/ |   
  \_____|_|  |_|___/\__\___/| .__/|_| |_|\___|_|   
++++++++++++++++++++++++++++| |+++++++++++++++++++++++                    
++++++++++++++++++++++++++++|_|+++++++++++++++++++++++
      


      """)







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