import numeros2

def preguntar():
    print('Bienvenido a Farmacia python')

    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] -  Cosmetica')
        try:
            mi_area = input('Elija la area: ').upper()
            ['P','F','C'].index(mi_area)
        except ValueError:
            print('Esa no es una alternativa valida')
        else:
            break
    numeros2.decorador(mi_area)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Quieres sacar otro turno S/N').upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita a la farmacia python')
                break

inicio()