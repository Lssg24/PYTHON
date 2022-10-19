palabra = 'python'
lista = [letra for letra in palabra]
'''for letra in palabra:
    lista.append(letra)
    print(letra)'''
print(lista)

lista = [n /2 for n in range(0,21,2) if n + 2 > 10]
print(lista)

lista = [n if n *2 > 10 else 'no' for n in range(0,21,2)]
print(lista)


pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)
#lo mismo pero con for normal
for pie in pies:
    resul=pie * 3.281
    print(resul)
print('\n')
#practicos
'''valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado= [valor**2 for valor in valores]
print(valores_cuadrado)'''

'''valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[]
valores_pares=[valor if valor%2==0 else '' for valor in valores]
print(valores_pares)'''

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[]
for valor in valores:
    if valor%2==0:
        valores_pares.append(valor)
    else:
        pass

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[]
for temp in temperatura_fahrenheit:

    grados_celsius.append((temp-32)*(5/9))


print(grados_celsius)
