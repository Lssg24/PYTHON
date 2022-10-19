archivo = open('prueba1.txt','w') #w reemplazatodo con en nuevo texto, si el archivo no existe lo crea
#escribe sin salto de lineas
#archivo.write('Soy el nuevo texto')
#archivo.writelines(['hola','mundo','aqui','estoy'])
#abrir el archivo con 'a' se posiciona en al final de lo ya creado
archivo.write('\n')
archivo.write('Soy el otro nuevo texto')
archivo.close()