import math
import os
import re
import time

inicio = time.time()

ruta = 'C:\\Users\\luxitomario\\OneDrive\\Documentos\\PROGRAMANDO\\Python\\Dia9\\proyectoDia9\\extraccionproyecto9\\Mi_Gran_Directorio'
patron = r'([N]\D{3}-\d{5})'


def busca_archivo():
    contador = 0
    print('Archivo\t\t\t\tNRO.Serie')
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            txt = carpeta + '\\' + arch
            lee = open(txt)
            lectura = lee.read()
            resultado = re.search(patron, lectura)
            if resultado:
                result = (arch + '\t\t' + resultado.group())
                print(result)
                contador += 1
            lee.close()
    return contador


contador = busca_archivo()
print(f'\nNúmeros encontrados: {contador}')
fin = time.time()
duracion = fin - inicio
print(f'Duracíon de la busqueda: {math.ceil(duracion)} segundo')
