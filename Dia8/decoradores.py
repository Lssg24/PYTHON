'''def cambiar_letras(tipo):

    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas


operacion = cambiar_letras('may')
operacion('palabra')'''

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


mayusculas_decoradas = decorar_saludo(mayusculas)

mayusculas_decoradas('luxo')

#decoradores complementar conocimiento
