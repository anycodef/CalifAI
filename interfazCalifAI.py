import tkinter as tk
from tkinter import filedialog


def file_selection():
    file = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    # Hacer algo con el archivo seleccionado, por ejemplo imprimir la ruta
    print("Archivo seleccionado:", file)


def folder_selection():
    carpeta = filedialog.askdirectory(initialdir="/", title="Seleccionar carpeta")
    # Hacer algo con la carpeta seleccionada, por ejemplo imprimir la ruta
    print("Carpeta seleccionada:", carpeta)


def rubric_load():
    # Aquí puedes agregar la lógica para cargar la rúbrica desde un archivo o base de datos
    print("Rúbrica cargada")


def compute():
    # Aquí puedes agregar la lógica para la evaluación
    print("Evaluando...")


def send_result():
    # Aquí puedes agregar la lógica para enviar los resultados
    print("Resultados enviados")


# Crear una instancia de Tkinter
root = tk.Tk()
root.title("Interfaz de Evaluación")

# Botones para las acciones
btn_seleccionar_archivo = tk.Button(root, text="Seleccionar Archivo", command=file_selection)
btn_seleccionar_archivo.pack(pady=5)

btn_seleccionar_carpeta = tk.Button(root, text="Seleccionar Carpeta", command=folder_selection)
btn_seleccionar_carpeta.pack(pady=5)

btn_cargar_rubrica = tk.Button(root, text="Cargar Rúbrica", command=rubric_load)
btn_cargar_rubrica.pack(pady=5)

btn_evaluar = tk.Button(root, text="Evaluar", command=compute)
btn_evaluar.pack(pady=5)

btn_enviar_resultados = tk.Button(root, text="Enviar Resultados", command=send_result)
btn_enviar_resultados.pack(pady=5)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
