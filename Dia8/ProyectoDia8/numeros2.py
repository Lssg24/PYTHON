def numero_perfumeria():
    for n in range(1, 10000):
        yield f'P - {n}'


def numero_farmacia():
    for n in range(1, 10000):
        yield f'F - {n}'


def numero_cosmetica():
    for n in range(1, 10000):
        yield f'C - {n}'


p = numero_perfumeria()
f = numero_farmacia()
c = numero_cosmetica()


def decorador(area):
    print('\n' + '*' * 23)
    print('su numero es:')
    if area == 'P':
        print(next(p))
    elif area == 'F':
        print(next(f))
    else:
        print(next(c))
    print('Espere su turno')
    print('*' * 23 + '\n')

