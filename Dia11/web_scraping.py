import bs4
import requests

resultado = requests.get('https://escueladirecta.com/')
# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
buscando_clase = sopa.select('.content-body label')

print(sopa.select('title')[0].getText())
print(buscando_clase)

for l in buscando_clase:
    print(l.getText())

# capturar imagenes

imagenes = sopa.select('.course-box-image')[0]['src']

print(imagenes)

imagen_curso1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso1.content)
f.close()
