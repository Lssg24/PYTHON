# import zipfile

'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('mio.txt')
mi_zip.write('mio2.txt')
mi_zip.close()'''

'''zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()'''
import shutil

'''ruta_origen = "C:\\Users\\luxitomario\\Desktop\\UTILIDADES"
archivo_destino = 'todo comprimido'
shutil.make_archive(archivo_destino, 'zip', ruta_origen)'''
shutil.unpack_archive('todo comprimido.zip', 'extraccionshutil', 'zip')
