#metodos de instancia, pueden acceder y modificar atributos de los objetos

class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')

piolin=Pajaro('amarillo', 'Canario')

piolin.piar()
piolin.volar(50)


