from pathlib import Path


def abrir_leer(open):

    read = open.read_text()
    return read


open = abrir_leer(Path('prueba.txt'))
print(open)
