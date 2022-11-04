# import send2trash
# import shutil
import os

'''print(os.getcwd())
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())'''
# shutil.move('curso.txt', 'c:\\Users\\luxitomario\\Desktop')  # mover archivos
# send2trash.send2trash('c:\\Users\\luxitomario\\Desktop\\curso.txt')  # envia a la papelera

ruta = 'E:\\juegos'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: {subcarpeta}')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')
