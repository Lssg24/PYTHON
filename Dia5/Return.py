def multiplicar(num1, num2):
    total = num1 * num2
    return total
    #return num1 * num2

resultado  =multiplicar(5,6)
print(resultado)


def usd_a_eur(valor):
    result=valor*0.90
    return result
result=usd_a_eur(8)
print(result)

palabra='Python'
def invertir_palabra(palabra):
    palabra=palabra.upper()
    invertida=palabra[::-1]
    return invertida
invertir_palabra(palabra)