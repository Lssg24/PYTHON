# crear base de datos
import datetime
import os

import cv2
import face_recognition as fr
import numpy

ruta = 'empleados'
mis_imagenes = []

nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombres in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\{nombres}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombres)[0])

print(nombres_empleados)


# codificar imagenees

def codificar(imagenes):
    lista_codificada = []

    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)
    # devolver lista codificada

    return lista_codificada


# registrar los ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r')
    lista_datos = f.readline()
    nombres_registros = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registros.append(ingreso[0])
    if persona not in nombres_registros:
        ahora = datetime.datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona},{string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)

# toma una captura de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer la imagen capturada

exito, imagen = captura.read()

if not exito:
    print('No se logra reconocer rostro')
else:
    # reconocer el rostro
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencia
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con ninguno de los empleados')

        else:
            print('Bienvenido al trabajo')
            # buscar el nombre del empleado encontrado
            nombre = lista_empleados[indice_coincidencia]
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 - 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registrar_ingresos(nombre)

            # mostrar la imagen
            cv2.imshow('Imagen web', imagen)

            # mantener ventana abierta
            cv2.waitKeyEx(0)
