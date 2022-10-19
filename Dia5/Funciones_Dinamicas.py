from random import *
def chequear_3_cifras(lista):
    #return numero in range(100,1000):
    listacifras=[]

    for n in lista:
        if n in range(100,1000):
            listacifras.append(n)
        else:
            pass
    return listacifras


resultado=chequear_3_cifras([555,99,600])
#print(resultado)

#practicos dia 5
def todos_positivos(numeros):
    negativos=[]
    positivos=[]
    lista_numeros=[]
    for n in numeros:
        if n < 0:
            negativos.append(n)
            lista_numeros.append(n)

        else:
            positivos.append(n)
            lista_numeros.append(n)

    if len(negativos) < 1 and len(positivos) > 0:
        return True
    else:
        return False

lista_numeros=[1,2,3,-8]
lista_numeros=todos_positivos(lista_numeros)
print(lista_numeros)


def suma_menores(lista_numeros):
    total=0
    for n in lista_numeros:
        if n in range(0,1000):
            suma=n+total
            total=suma

    return total

lista_numeros=[1,2,3,5,2000]
resultado= suma_menores(lista_numeros)
print(resultado)

def cantidad_pares(lista_numeros):

    pares=[]
    for n in lista_numeros:

        if not n%2:
            print(n)
            pares.append(n)
        else:
            pass
    return len(pares)

lista_numeros = [2,4,5,6]
resul=cantidad_pares(lista_numeros)
