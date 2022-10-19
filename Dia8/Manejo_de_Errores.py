'''def suma():
    n1= int(input('Ingresa número 1: '))
    n2= int(input('Ingresa numero 2:'))
    print(n1 + n2)

try:
    suma()
except TypeError:
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    print('Ingresaste valores que no corresponden no es un nmero')
else:
    print('Hiciste todo bien')
finally:
    print('Eso fue todo')'''

def pedir_numero():
    while True:
        try:
            numero = int(input('ingresar un número: '))
        except:
            print('ese no es un número')
        else:
            break

    print('Gracias')
pedir_numero()
