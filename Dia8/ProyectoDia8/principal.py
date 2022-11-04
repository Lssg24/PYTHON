from numeros import numero

areas={1:'Farmacia',2:'Cosmetica',3:'Perfumeria'}

opcion = True

while opcion == True:
    def main():
        while True:
            try:
                print('Bienvenido a mi Farmacia: \n ¿En que area deseas tomar número?')
                print('\n1 - Farmacia\n2 - Cosmetica\n3 - Perfumería\n4 - Salir4')
                area = int(input('\nIngresa el número: '))
            except:
                print('Ingresa solo números')
            else:
                break

        if area <=0 or area > 4:
            print('La opcion ingresada no exite')
            main()
        elif area == 4:
            exit()
        else:
            return area

    def decorar(area,turno):
        print(f'Area de {area}')
        print(f'Su turno es {next(turno)}')
        print('Favor espera tu turno')
        opcion=input('Deseas tomar otro número: (s/n) ')
        if opcion == 'S' or opcion == 's':
            return True
        else:
            return False

    area=main()
    turno=numero(area)
    opcion=decorar(areas[area],turno)

else:
    exit()