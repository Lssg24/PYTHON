from random import * #randint

aleatorio = randint(1,50)#numero entero aleatorio
print(aleatorio)

aleatorio = round(uniform(1,5),1)#valor decimal aleatorio
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))#numeros random dentro de un rango dado, no se puede integrar string

shuffle(numeros)

print(numeros)

palabra='olitas'
palabra=list(palabra)
letra='a'
print(palabra.index(letra))

