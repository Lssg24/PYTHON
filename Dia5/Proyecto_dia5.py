from random import *
nombre=input('Bienvenido al juego del ahorcado, porfavor ingresa tu nombre: ')
final=[]

def elejir_palabra():
    palabras=['murcielago','amarillo','camion','guanaco','auto','refrigerador']
    plabra=choice(palabras)
    return plabra

def elegir_letra(palabra):
    guion=[]
    count_letras=int(len(palabra))
    l=0
    while l < count_letras:
        guion.append('_')
        l+=1
    return guion

def comprobar(palabra, guion):
    palabra=(list(palabra))
    encuentra=[]
    vidas = 7
    incorrectas=[]
    while guion.count('_') > 0 and vidas > 0:
        encuentra.clear()
        print(f'Letras incorrectar {set(incorrectas)}')
        letra=input(f'{nombre}, te quedan {vidas} Ingresa la letra que crees que se encuentre en la palabra: ')
        if letra in palabra:
            count=palabra.index(letra)
            while count < len(palabra):
                if letra == palabra[count]:
                    encuentra.append(count)
                    count += 1
                    for l in encuentra:
                        guion[l] = letra
                    print(guion)
                else:
                    count += 1
        else:
            incorrectas.append(letra)
            vidas -= 1
    else:
        if vidas == 0:
            print('Te quedaste sin vida, has perdido')
        else:
            print('Victoria')

palabra=elejir_palabra()
guion=elegir_letra(palabra)
final=comprobar(palabra,guion)
