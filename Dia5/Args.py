def suma (*args):
    '''total=0
    for arg in args:
        total += arg
    return total'''
    return sum(args)

print(suma(5,6,9))

print('\n')

def suma_cuadrados(*args):
    result = []
    for arg in args:
       result.append(arg**2)
    return sum(result)
print(suma_cuadrados(1,2,3))



import operator
def suma_absolutos(*args):
    numeros=[]
    for n in args:
        n=abs(n)
        numeros.append(n)
    return sum(numeros)
print(suma_absolutos(2,2,-2))


'''def numeros_persona(*args):
    numeros=[]
    nombre=''
    for p in args:
        if type(p) is str:
            nombre=p
        elif type(p) is int:
            numeros.append(p)
    return nombre,sum(numeros)
nombre,b=numeros_persona("Federico", 75, 20, 65)
print(f'{nombre}, la suma de tus números es {b}')'''

def numeros_persona(nombre,*args):
    suma_numeros=sum(args)
    mensaje = (f'{nombre}, la suma de tus números es {suma_numeros}')
    return mensaje
mensaje=numeros_persona("Federico", 75, 20, 65)
print(mensaje)





