from random import *

'''#Lista inicial
palitos = ['-','--','---','----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

#Comprobar intento
def chek_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'te ha tocado {lista[intento-1]}')

patitos_mezclados= mezclar(palitos)
seleccion = probar_suerte()
chek_intento(patitos_mezclados,seleccion)'''

#practico dados


'''def lanzar_dados():
    dado1=randint(1,6)
    dado2=randint(1,6)
    return dado1,dado2

def evaluar_jugada(d1,d2):
    suma_dados=d1+d2
    if suma_dados <= 6:
        texto = print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        texto = print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    else:
        texto = print(f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')
    return texto
d1,d2=lanzar_dados()
evaluar_jugada(d1,d2)'''


def reducir_lista(lista):
    numero_mayor = max(lista)
    lista.remove(numero_mayor)
    lista = list(set(lista))
    return lista

def promedio(lista1):
    prom=sum(lista1)/len(lista1)
    return prom
lista_numeros = [1,2,15,7,2]
lista=reducir_lista(lista_numeros)
resultado=promedio(lista)
print(lista)
print(resultado)

#pratico dia 5
def lanzar_moneda():
    moneda=['Cara','Cruz']
    moneda=choice(moneda)
    return moneda

def probar_suerte(moneda,lista_numeros):
    if moneda == 'Cara' :
        print('La lista de autodestruirá')
        lista_numeros.clear()

    else:
        print('La lista fue salvada')

    return lista_numeros

lista_numeros=[1,2,3,4,5]
moneda=lanzar_moneda()
probar_suerte(moneda,lista_numeros)
print(lista_numeros)

