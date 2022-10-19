#lista = [1,2,3,4]

for numero in range(1,7,2):#desde hasta y con saltos
    print(numero)

print('\n')

lista = list(range(1,30))#crear una lista a partir de rangos
print(lista)

suma_cuadrados = 0
numeros = list(range(1,16))
cuadrado=[]
for numero in numeros:
    cuadrado.append(numero**2)
    suma_cuadrados+=numero**2
print(suma_cuadrados)

