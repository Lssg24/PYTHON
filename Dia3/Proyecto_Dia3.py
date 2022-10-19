texto=input('Ingresa u8n texto, como un poema, frasescelebres o una historia que desees: ')
letras= []
letras.append(input('Ingresa primera letra a elección: ').lower())
letras.append(input('Ingresa segunda letra a elección: ').lower())
letras.append(input('Ingresa tercera letra a elección: ').lower())

result_l1=texto.count(letras[0])
result_l2=texto.count(letras[1])
result_l3=texto.count(letras[2])

print(f'La letra {letras[0]}, aparece {result_l1} veces\n'
      f'La letra {letras[1]}, aparece {result_l2} veces\n'
      f'La letra {letras[2]}, aparece {result_l3} veces')

palabras_texto=texto.split()
print(f'Existen {len(palabras_texto)} palabras en el texto')

print(f'La primera letra del texto es {texto[0]}')
print(f'La ultima letra del texto es {texto[-1]}')

palabras_texto.reverse()
texto_invertido=' '.join(palabras_texto)
print(texto_invertido)

res1=texto.find('python')
res2=texto.find('PYTHON')
res3=texto.find('Python')

if res1>=1 or res2>=1 or res3>=1  :{
    print('Si exite la palabra Python')
}

else: {
    print('No exite la palabra Python')
}




