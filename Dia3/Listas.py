mi_lista=['z','b','c','a','n']
'''otra_lista=['hola',55,6.1]'''

resultado = len(mi_lista)
'''resultado = mi_lista[0]'''
'''resultado = mi_lista[0:]'''
'''Se pueden concatenar listas con el operador +'''
print(resultado)
print(type(mi_lista))

'''agregar elementos a la lista'''
mi_lista.append('h')
print(mi_lista)
'''eliminar elemento desde la lista'''
mi_lista.pop(0)
print(mi_lista)
'''ordenar listas alfabeticamente'''
mi_lista.sort()
mi_lista.reverse()
print(mi_lista)
'''trabajo practico'''
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado=frutas[2]
frutas.pop(2)
print(eliminado)
print(frutas)