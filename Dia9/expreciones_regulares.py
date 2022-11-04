import re

texto = 'si necesitas ayuda llama al (685)-598-9977 las 24 horas al servicio de ayuda online'

palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda.span())

busqueda2 = re.findall(patron, texto)
print(busqueda2)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

# ----------------------------------------------------------------------------------

texto2 = 'llama al telefono 555-654-5896 ya mismo'

patron2 = r'\d\d\d-\d\d\d-\d{4}'

resultado = re.search(patron2, texto2)
print(resultado.group())

texto2 = 'llama al telefono 555-654-5896 ya mismo'

patron2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d{4})')  # imprimir por grupos separados compilar

resultado = re.search(patron2, texto2)
print(resultado.group(2))  # imprimir por grupos separados

# ------------------------------------------

'''clave = input('clave: ')
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear)'''

# ------------------------------------------------------
'''texto = 'no atendemos los dias lunes por la tarde'
buscar = re.search(r'demos', texto)
buscar = re.search(r'^\D',
                   texto)  # ^\D no comienza con un digito \D$ no hay un digito al final [^\s] excluir rspacios vacios, [^\s]+ busca los espacios y construye palabras
print(buscar.group())'''


def verificar_email(email):
    patron = r'(^[\w]+)@([\w]+)' + '.com'
    resultado = re.search(patron, email)

    if resultado:
        print('OK')
    else:
        print("NO")


verificar_email('usuario@host.com')
