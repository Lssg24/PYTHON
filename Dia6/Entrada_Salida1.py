mi_archivo=open('prueba.txt')
#print(mi_archivo.read())
print(mi_archivo.readline())
mi_archivo.close()#simpre al leer un archivo cerrar para liberar memoria

archivo = open('mi_archivo.txt','w')
archivo.write('Nuevo Textoffff')
archivo.close()
archivo = open('mi_archivo.txt')
print(archivo.read())
archivo.close()


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
registro = '\t'.join(registro_ultima_sesion)
archivo.writelines(registro)
archivo.close()
archivo = open('registro.txt', 'r')
print(archivo.read())

