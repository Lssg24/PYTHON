monedas = 10
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -=1
else:
    print('No tengo mas monedas')

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres seguir (s/n): ')
else:
    print('Gracias')

#pass

'''respuesta = 's'
while respuesta == 's':
    pass
print("Hola")'''

#break con for
nombre = input('Tu nombre: ')
for letra in nombre:
    if letra =='r':
# break se detiene en la letra indicada
        continue # se salta la letra indicada
    print(letra)
print('\n')
#practica loop while 2
numero = 50
while numero >= 0:
    if numero%5==0:
        print(numero)
    else:
        numero-=1
    numero-=1

print('\n')
numero=0
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)
