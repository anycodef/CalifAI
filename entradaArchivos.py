from tkinter import filedialog


def folderSelection() -> str:
    pathFolder = filedialog.askdirectory(initialdir="/", title="Selecciona la carpeta donde están los trabajos")
    #pathFolder = filedialog.askopenfilename(initialdir="/", title="Seleccione un trabajo")
    return pathFolder


if __name__ == '__main__':
    print(folderSelection())
