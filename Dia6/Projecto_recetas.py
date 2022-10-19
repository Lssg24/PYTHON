import os
from pathlib import Path

nombre = input('Ingresar Nombre: ')
ruta = Path.home()

def ubicacion_recetas():
    categorias = ['carnes', 'ensaladas', 'pastas', 'postres']
    if Path(ruta,'recetas').exists():
        return Path(ruta,'recetas')
    else:
        creapath=Path(ruta,'recetas')
        creapath.mkdir(parents=True)
        for categoria in categorias:
            creacategorias=Path(creapath,categoria)
            creacategorias.mkdir(parents=True)
    return creapath


def catidad_de_recetas():
    ubicacion=Path(ruta,'recetas')
    cat= []
    cantidad_recetas = os.listdir(ubicacion)
    for cantidad_receta in cantidad_recetas:
        cant = len(os.listdir(Path(ubicacion, cantidad_receta)))
        cat.append(cantidad_receta)
        cat.append(cant)
    return cat


def selecciona_categoria():
    ubicacion=Path(ruta,'recetas')
    categorias=[]
    cantidad_recetas = os.listdir(ubicacion)
    for cate in cantidad_recetas:
        categorias.append(cate)
    return categorias

def menu(ubicacion):
    os.system('cls')
    print(f'Bienvenido a "Tu Recetario", {nombre} aqui encontrarás las recetas más ricas')
    print(f'La ruta de nuestras recetas se encuntran en: {ubicacion}')
    print('Cantidades de recetas: ')
    print(catidad_de_recetas())
    list_opciones = ['Leer recetas','Crear Receta', 'Crear Categoria','Eliminar receta','Eliminar categoria','Cerrar App']
    seleccion = 10
    while seleccion > 5 :
        print(f'{nombre} Estas son las opciones disponibles: ')
        for opc in list_opciones:
            opcion = list_opciones.index(opc)
            print(f'{opcion} - {opc}')
        seleccion=int(input('Ingresa la opción que desear realizar: '))
        os.system('cls')
    return seleccion

def app(seleccion):
    if seleccion == 0:
        leer_receta()
    if seleccion == 1:
        crear_receta()
    if seleccion == 2:
        crear_categoria()
    if seleccion == 3:
        eliminar_receta()
    if seleccion == 4:
        eliminar_categoria()
    if seleccion == 5:
        cerrar_app()


def leer_receta():
    lst_receta=[]
    select_categoria=selecciona_categoria()
    for cate in select_categoria:
        print(select_categoria.index(cate),cate)
    seleccionade=int(input('Ingresa la categoria que desees: '))
    categoria_seleccionada=select_categoria[seleccionade]
    os.system('cls')
    print(f' Seleccionaste la categoria de {categoria_seleccionada}:')
    lista_recetas = Path(ruta, 'recetas',categoria_seleccionada)
    for txt in lista_recetas.glob("*.txt"):
        lst_receta.append(txt)
    for lst in lst_receta:
        print(lst_receta.index(lst),lst)
    abrir_receta=int(input('Que receta deseas leer: '))
    print(lst_receta[abrir_receta].read_text())
    tecla=input('Presiona "M", para ir al menu o "V", para volver a las categorias')
    if tecla == "M" or tecla == "m":
        os.system('cls')
        menu(ubicacion)
    else:
        os.system('cls')
        leer_receta()

def crear_receta():
    select_categoria = selecciona_categoria()
    for cate in select_categoria:
        print(select_categoria.index(cate), cate)
    seleccionade = int(input('Ingresa la categoria que desees: '))
    categoria_seleccionada = select_categoria[seleccionade]
    os.system('cls')
    print(f' Seleccionaste la categoria de {categoria_seleccionada}:')
    nombre_receta=input('Ingresa el nombre de la receta: ')
    lista_recetas = Path(ruta, 'recetas', categoria_seleccionada, nombre_receta+'.txt')
    receta=input('Escribe la receta: ')
    print(lista_recetas)
    archivo=open(lista_recetas, 'w')
    archivo.write(receta)
    archivo.close()
    print(f'Receta {nombre_receta} creada en categoria {categoria_seleccionada}')

def crear_categoria():
    os.system('cls')
    print('Estas son las categorias actuales: ')
    select_categoria = selecciona_categoria()
    for cate in select_categoria:
        print(select_categoria.index(cate), cate)
    opcion=input('Deseas crear una categoria "S", para crear o presiona cualquier tecla para volver al menu: ')
    if opcion == "S" or opcion == "s":
        os.system('cls')
        nuevacategoria=input('Ingresa el nombre de la nueva categoria: ')
        nueva_cat = Path(ruta, 'recetas',nuevacategoria)
        os.mkdir(nueva_cat)
        crear_categoria()
    else:
        os.system('cls')
        menu(ubicacion)

def eliminar_receta():
    lst_receta=[]
    select_categoria=selecciona_categoria()
    for cate in select_categoria:
        print(select_categoria.index(cate),cate)
    seleccionade=int(input('Ingresa la categoria que desees: '))
    categoria_seleccionada=select_categoria[seleccionade]
    os.system('cls')
    print(f' Seleccionaste la categoria de {categoria_seleccionada}:')
    lista_recetas = Path(ruta, 'recetas',categoria_seleccionada)
    for txt in lista_recetas.glob("*.txt"):
        lst_receta.append(txt)
    for lst in lst_receta:
        print(lst_receta.index(lst),lst)
    elimina_receta=int(input('Que receta deseas eliminar: '))
    os.remove(lst_receta[elimina_receta])


def eliminar_categoria():
    os.system('cls')
    print('Estas son las categorias actuales: ')
    select_categoria = selecciona_categoria()
    for cate in select_categoria:
        print(select_categoria.index(cate), cate)
    opcion = int(input('ingresa la categoria a eliminar'))
    elimina_cat = Path(ruta, 'recetas', select_categoria[opcion])
    print(elimina_cat)
    os.rmdir(elimina_cat)


def cerrar_app():
    exit()


ubicacion=ubicacion_recetas()
catidad_de_recetas()
seleccion=menu(ubicacion)
app(seleccion)


