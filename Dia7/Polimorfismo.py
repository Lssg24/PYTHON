class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muuu")

class Oveja():
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + "dice beee")

vaca1=Vaca('Aurora')
oveja1=Oveja('Ñau')

def animal_habla(animal):
    animal.hablar()


animal_habla(oveja1)


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


uno=Mago()
dos=Arquero()
tres=Samurai()
personajes=[uno,dos,tres]
for pj in personajes:
    pj.atacar()