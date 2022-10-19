diccionario={'c1':'valor1','c2':'valor2'}
'''Las claves no se pueden repetir, sus valores si'''
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuente','peso':88,'talla':1.76,}
consulta = cliente['peso']
print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2={'c1':['a','b','c'],'c2':['d','e','f']}
print(str((dic2['c1'])+(dic2['c2'])).upper())

dic = {1:'a',2:'b'}
print(dic)
dic[3]='c'
print(dic)
dic[2]='B'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
dic['país'] = 'Colombia'
print(dic)