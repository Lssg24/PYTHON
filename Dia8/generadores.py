'''def mi_funcion():
    return 4

def mi_generador():
    yield 4'''


'''def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))'''


'''def mi_migenerador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_migenerador()

print(next(g))
print(next(g))
print(next(g))
'''

#ejercicios practicos generadores
'''def generador():
    generador = 0
    while generador >=0:
        generador += 1
        yield generador

generador=generador()
print(next(generador))
print(next(generador))
print(next(generador))
'''


'''def generador():
    generado = 0
    while generado >= 0:
        generado+=7
        yield generado


generador=generador()
print(next(generador))
print(next(generador))'''


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()

