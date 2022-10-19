from random import randint
intento=8
numero=randint(1,100)
mi_numero = 0
nombre = (input("Ingresa tu nombre: "))
print(f'Bienvenido {nombre}, a Adivina el número correcto, te invito a jugar')
print('Tienes 8 intentos para adivinar un nuero entre 1 y 100')

while intento > 0 :
    mi_numero = (input (f"ingresa el numero que crees que sea tienes {intento} intentos:"))
    valida = str.isdigit(mi_numero)
    if  valida is True:
        if int(mi_numero) == numero:
            print(f'Felicidade {nombre}, acertaste con el número {numero} en el intento {9-intento}')
            break
        else:
            if int(mi_numero) < 0 or int(mi_numero) > 100:
                print('El número es menor 0 o mayor a 100')
            elif int(mi_numero) < numero:
                print('El número es menor al secreto')
            elif int(mi_numero) > numero:
                print('El número es mayor al secreto')
            intento -= 1
    else:
        print(f'{nombre} solo ingresa numeros!')
if int(mi_numero) != numero:
    print('Lo siento acabaron tus intentos')