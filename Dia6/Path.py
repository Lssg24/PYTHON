from pathlib import Path

base=Path.home()#ruta absoluta al usuario actual
guia =  Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)

