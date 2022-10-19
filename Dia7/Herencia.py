'''class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super.__init__(edad,color)
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f' el Pajaro vuela {metros}')

piolin=Pajaro(3,'Amarillo')

piolin.volar(100)
print(Pajaro.__bases__)#pajaro es una clase que hereda de la clase animal

print(Animal.__subclasses__())#Animal trasmite su herencia a pajaro solamente. Actualmente'''

class Padre:
    def hablar(self):
        print('Hola')
class Madre:
    def reir(self):
        print('Jaja')
    def hablar(self):
        print('Que tal')

class Hijo(Padre, Madre):
        pass

class Nieto(Hijo):
        pass

mi_nieto = Nieto()
mi_nieto.hablar()#Segun orden del los metodos es el atributo que da la herencia
mi_nieto.reir()
print(Nieto.mro())


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Ave,):
    pass
julio=Ornitorrinco()
