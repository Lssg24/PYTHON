from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/luxitomario/OneDrive/Documentos/PROGRAMANDO/Python/Dia6/prueba.txt')

rita=carpeta.parents[3]
print(rita)

rutawindows = PureWindowsPath(carpeta)


if carpeta.exists():

    print('El archivo existe')
else:
    print('El archivo no existe')


print(carpeta.read_text())#no es necesario abrir ni cerrar el documento
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

print(rutawindows)