nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades=['Lima','Peru','Mexico']
# si se agregar valores adicionales a las listas,
# se limitara a que calzen las listas o tuplas y se limita al mas corto
combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} y vive en {ciudad}')

marcas = ['Adidas', 'Nike', 'Vans']
productos = ['Chaqueta', 'Zapatillas', 'Pantalones']
mi_zip = list(zip(marcas, productos))
print(mi_zip)

#practuco zip
numeros = []

español = ['uno','dos','tres','cuatro','cinco']
portuges = ['um','dois','três','quatro','cinco']
ingles= ['one','two','three','four','five']

numeros = list(zip(español,portuges,ingles))

print(numeros)


