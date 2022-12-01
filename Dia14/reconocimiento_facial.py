import cv2
import face_recognition as fr

# cargar imagen
foto_control = fr.load_image_file('mardo11.png')
foto_prueba = fr.load_image_file('mardo12.png')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar control de caras A y B
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_cofificada_A = fr.face_encodings(foto_control)[0]

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_cofificada_B = fr.face_encodings(foto_prueba)[0]

# mostrar_rectangulo de caras A y B
cv2.rectangle(foto_control, (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]), (0, 255, 0), 2)

cv2.rectangle(foto_prueba, (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]), (0, 255, 0), 2)

# comparar las caras
# resultado = fr.compare_faces([cara_cofificada_A], cara_cofificada_B, 0.9)#se puede modificar el limite de tolerancia
resultado = fr.compare_faces([cara_cofificada_A], cara_cofificada_B)
# print(resultado)


# medida de la distancia
distancia = fr.face_distance([cara_cofificada_A], cara_cofificada_B)
# print(distancia)

# mostrar resultado
cv2.putText(foto_prueba, f'{resultado} {distancia.round(2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

# mostrar las imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# mantener programa abierto
cv2.waitKey(0)
