class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

mi_pajaro = Pajaro('Negro', 'Tucan' )

print(mi_pajaro.color)
print(f'Mi pajaro es de color {mi_pajaro.color} y es un {mi_pajaro.especie}')
print(mi_pajaro.alas)

#ejercicio
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', '4')

print(f'casa {casa_blanca.color}, pisos {casa_blanca.cantidad_pisos}')