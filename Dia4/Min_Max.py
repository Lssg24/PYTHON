menor= min(58,96,72,64,35)
print(menor)
mayor= max(58,96,72,64,35)
print(mayor)
print(f'El número mayor es "{mayor}" y el menor es "{menor}"')

mombres = ['juan','pablo','alicia','carlos']
print(min(mombres))

mombre = 'juan'
print(min(mombre.lower()))

print('\n')

dic = {'c1':45,'c2':11}
print(min(dic))#ordena alfabeticamente
print(min(dic.values()))#ordena por el lvalor del dicionario

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango=(max(lista_numeros)-min(lista_numeros))

print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre=min(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)


