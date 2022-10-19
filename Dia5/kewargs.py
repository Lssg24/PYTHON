def suma(**kwargs):
    total=0

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3, y=5, z=2))

def lista_atributos(**kwargs):
    valores=list(kwargs.values())
    return valores
print(lista_atributos(x=3, y=5, z=2))

def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}:')
    for nombre_argumento,valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')

print(describir_persona('Carolina',color_pelo='negro',color_ojos='Cafes'))