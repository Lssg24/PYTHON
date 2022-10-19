mi_variable = 'Hola Mundo'
mi_bool=10==25

mi_bool='blanco'!='blanco'
print(mi_bool)

#practicos
num1=64*3
num2=24*8
mi_bool= num1!=num2

mi_bool=(4 < 5) and (5 < 6)
mi_bool=(4 < 5) and ('perro' == 'perro')
mi_bool=(10 < 5) or ('perro' == 'gato')

texo='Esta frase es breve'
mi_bool=('frase' in texo) and ('hola' in texo)
mi_bool= not ('a'=='a')#esta comparacion no es falsa lo contrario
print(mi_bool)

#practico 2
num1=36
num2=72/2
num3=48
mi_bool=(num1>num2) or (num1<num3)
frase="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1='éxito'
palabra2='tecnología'
mi_bool= not (palabra1 in frase) and not (palabra2 in frase)
print(mi_bool)