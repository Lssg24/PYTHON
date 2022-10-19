class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')


    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        #no permite aceder a atributos de instanacia pero si los de clase
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod # no permite acceder ni modificar atributos de instancia ni de clase
    def mirar():
        print('El pajaro Mira')


Pajaro.poner_huevos(7)
Pajaro.mirar()
