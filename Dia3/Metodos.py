texto = 'Este es el texto de Luis'
'''Mayusculas'''
resultado = texto.upper()
'''Minusculas'''
resultado = texto.lower()
'''Separador quita el identificado'''
resultado = texto.split('t')
print(resultado)
'''Unir'''
a='Aprender'
b='Python'
c='es'
d='genial'
e=' '.join([a,b,c,d])
print(e)
resultado= texto.find('j')
'''Si n o lo encuentra entrega -1'''

resultado=texto.replace('e','x')
print(resultado)


