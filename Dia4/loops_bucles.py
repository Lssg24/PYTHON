letras = ['a','b','c','d'] #lista
for letra in letras:
    numero_letra=letras.index(letra)+1
    print(f'Letra: {letra} y su indice es {numero_letra}')

lista_nombres = ['pablo','Luis','Antonella','Carolina','Fernanda','Laura']
for nombre in lista_nombres:
    if nombre.startswith('L'):#imprime solos con la condicion que se cumple
        print(nombre)
    else:
        print(f'Nombre que no comienza con L {nombre}')


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor)

palabra='python'
for letra in palabra:
    print(letra)


for a,b in [[1,2],[3,4],[5,6]]:#imprime ambos objecos que se encuentran en la lista de la lista
    print(a)
    print(b)

dic= {'clave1': 'a', 'clave2': 'b','clave3':'c'}
for item in dic.items():#o metodo value para ver solo el valor
    print(item)

#practicos

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print (f'"Hola" {nombre}')

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros =0
for numero  in lista_numeros:
    suma_numeros=suma_numeros+numero
print(suma_numeros)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares =0
suma_impares =0
for numero in lista_numeros:
    if numero%2==0:
        suma_pares=numero+suma_pares
    else:
        suma_impares=numero+suma_impares
print(suma_pares)
print(suma_impares)




