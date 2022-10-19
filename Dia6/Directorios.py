import os


ruta = os.getcwd() #ruta actual de el projecto

#ruta = os.makedirs('C:\\Users\\luxitomario\\Desktop\\alternativo\\otra') #crear un directorio
ruta = os.rmdir('C:\\Users\\luxitomario\\Desktop\\alternativo\\otra')#eliminan carpeta
ruta = os.chdir('C:\\Users\\luxitomario\\Desktop\\alternativo') #acceder a carpetas en directorios



archivo = open('Otro_archivo.txt')
print(archivo.read())

