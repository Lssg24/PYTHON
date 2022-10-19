lista = ['a','b','c']
indice=0

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

#tgransformar en taple
mi_tuples=list(enumerate(lista))
print(mi_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


lista_indice='Python'
for indice,letra in enumerate(lista_indice):
    print(indice,letra)

mi_tuples=list(enumerate(lista_indice))
print(mi_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for item,nombre in enumerate(lista_nombres):
    if nombre.find('M') == 0:
        print(item)







