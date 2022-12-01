from tkinter import *

operador = ''


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# iniciar tkinter
aplicacion = Tk()
# tamaño de la ventana
aplicacion.geometry('1150x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturación')

# color de  fonde de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
# etiqueta
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4', font=("aAtomicMd", 50),
                        bg='burlywood', width=27, )
etiqueta_titulo.grid(row=0, column=0)

# panel izquerdo
panel_izquerdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquerdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquerdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquerdo, text='Comida', font=("aAtomicMd", 20, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_comidas.pack(side=LEFT)

# panel Bebidas
panel_bebidas = LabelFrame(panel_izquerdo, text='Bebidas', font=("aAtomicMd", 20, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel Postres
panel_postres = LabelFrame(panel_izquerdo, text='Postres', font=("aAtomicMd", 20, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista comidas
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'pizza1', 'pizza2', 'pizza3', 'jsjsjsj']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino', 'vino2', 'cerverza1', 'cerveza2']
lista_postre = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comidas
variables_comida = []
# CUADRO COMIDA
cuadros_comidas = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    # crear check buttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('aAtomicMd', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de las entradas
    cuadros_comidas.append('')
    texto_comida.append('')
    cuadros_comidas[contador] = Entry(panel_comidas, font=('aAtomicMd', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                      textvariable=texto_comida[contador])

    cuadros_comidas[contador].grid(row=contador, column=1)

    contador += 1

# generar items bebidas
variables_bebida = []
cuadros_bebidas = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('aAtomicMd', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    cuadros_bebidas.append('')
    texto_bebida.append('')
    cuadros_bebidas[contador] = Entry(panel_bebidas, font=('aAtomicMd', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                      textvariable=texto_bebida[contador])

    cuadros_bebidas[contador].grid(row=contador, column=1)

    contador += 1

# generar items postres
variables_postre = []
cuadros_postres = []
texto_postre = []
contador = 0

for postre in lista_postre:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('aAtomicMd', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)

    cuadros_postres.append('')
    texto_postre.append('')
    cuadros_postres[contador] = Entry(panel_postres, font=('aAtomicMd', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                      textvariable=texto_postre[contador])

    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

    # falta contedo en esta parte

    # botones
    botones = []

    # calculadora
    visor_calculadora = Entry(panel_calculadora, font=('aAtomicMd', 16, 'bold'), width=32)
    visor_calculadora.grid(row=0, column=0, columnspan=4)

    botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']

    botones_guardados = []

    fila = 1
    columna = 0
    for boton in botones_calculadora:
        boton = Button(panel_calculadora, text=boton.title(), font=('aAtomicMd', 16, 'bold'), fg='white', bg='azure4',
                       bd=1, width=8)

        botones_guardados.append(boton)

        boton.grid(row=fila, column=columna)

        if columna == 3:
            fila += 1

        columna += 1

        if columna == 4:
            columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))

# evitr que la pantalla se cierre
aplicacion.mainloop()
