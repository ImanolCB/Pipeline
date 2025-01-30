import tkinter as tk
import csv
from datetime import datetime

now = datetime.now()

def guardar_datos():
    # Obtener los datos de los campos de texto
    nombre = entry_nombre.get()
    apellido1 = entry_apellido1.get()
    apellido2 = entry_apellido2.get()
    alias = entry_alias.get()
    edad = entry_edad.get()
    email = entry_email.get()
    genero = genero_var.get()  # Obtener el género seleccionado
    oficio = oficio_var.get()  # Obtener el oficio seleccionado
    

    # Guardar los datos en un archivo CSV
    with open(f'data/datos_formulario_{now.strftime('%S%M%H_%d%m%Y')}.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
            # Escribir la cabecera
        writer.writerow(["nombre", "apellido1", "apellido2", "alias", "edad", "email", "genero", "oficio"])
        writer.writerow([nombre, apellido1, apellido2, alias, edad, email, genero, oficio, now])

    # Limpiar campos después de guardar
    entry_nombre.delete(0, tk.END)
    entry_apellido1.delete(0, tk.END)
    entry_apellido2.delete(0, tk.END)
    entry_alias.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Crear ventana de la aplicación
root = tk.Tk()
root.title("Formulario")
root.geometry("400x450")  # Establecer tamaño de la ventana inicial

# Personalización de estilo
root.configure(bg="#f0f0f0")  # Color de fondo de la ventana

# Crear los campos de entrada con estilos
label_nombre = tk.Label(root, text="Nombre:", bg="#f0f0f0", font=("Arial", 12))
label_nombre.grid(row=0, column=0, pady=10, sticky="w", padx=10)
entry_nombre = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_nombre.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

label_apellido1 = tk.Label(root, text="Apellido1:", bg="#f0f0f0", font=("Arial", 12))
label_apellido1.grid(row=1, column=0, pady=10, sticky="w", padx=10)
entry_apellido1 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_apellido1.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

label_apellido2 = tk.Label(root, text="Apellido2:", bg="#f0f0f0", font=("Arial", 12))
label_apellido2.grid(row=2, column=0, pady=10, sticky="w", padx=10)
entry_apellido2 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_apellido2.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

label_alias = tk.Label(root, text="Alias:", bg="#f0f0f0", font=("Arial", 12))
label_alias.grid(row=3, column=0, pady=10, sticky="w", padx=10)
entry_alias = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_alias.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

label_edad = tk.Label(root, text="Edad:", bg="#f0f0f0", font=("Arial", 12))
label_edad.grid(row=4, column=0, pady=10, sticky="w", padx=10)
entry_edad = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_edad.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

label_email = tk.Label(root, text="Email:", bg="#f0f0f0", font=("Arial", 12))
label_email.grid(row=5, column=0, pady=10, sticky="w", padx=10)
entry_email = tk.Entry(root, font=("Arial", 12), bg="#ffffff", bd=1)
entry_email.grid(row=5, column=1, pady=10, padx=10, sticky="ew")

# Crear un select de género
label_genero = tk.Label(root, text="Género:", bg="#f0f0f0", font=("Arial", 12))
label_genero.grid(row=6, column=0, pady=10, sticky="w", padx=10)

# Variable para almacenar la selección del género
genero_var = tk.StringVar()
genero_var.set("Selecciona un género")  # Valor por defecto
opciones_genero = ["Masculino", "Femenino", "No binario", "Prefiero no decirlo"]

# Crear el menú desplegable
genero_select = tk.OptionMenu(root, genero_var, *opciones_genero)
genero_select.config(font=("Arial", 12), bg="#ffffff", bd=1)
genero_select.grid(row=6, column=1, pady=10, padx=10, sticky="ew")

# Crear un select de género
label_genero = tk.Label(root, text="Oficio:", bg="#f0f0f0", font=("Arial", 12))
label_genero.grid(row=7, column=0, pady=10, sticky="w", padx=10)

# Variable para almacenar la selección del oficio
oficio_var = tk.StringVar()
oficio_var.set("Selecciona un oficio")  # Valor por defecto
opciones_oficio = ["Electricista", "Informatico", "Medico", "Profesor", "Estudiante", "Camarero"]

# Crear el menú desplegable
oficio_select = tk.OptionMenu(root, oficio_var, *opciones_oficio)
oficio_select.config(font=("Arial", 12), bg="#ffffff", bd=1)
oficio_select.grid(row=7, column=1, pady=10, padx=10, sticky="ew")

# Configuración de la columna para que se estire
root.grid_columnconfigure(1, weight=1)  # Hacer que la columna 1 (donde están los campos de texto) sea flexible

# Botón con estilo
boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", bd=2)
boton_guardar.grid(row=8, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

# Ejecutar la interfaz gráfica
root.mainloop()
