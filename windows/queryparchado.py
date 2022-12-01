import tkinter
from tkinter import ttk, END

import wmi

ventana = tkinter.Tk()


def consulta():
    tabla.delete(*tabla.get_children())
    c = wmi.WMI(computer=maquina.get())
    for os in c.Win32_QuickFixEngineering():
        tabla.insert('', END, text=os.CSName, values=(os.HotFixID, os.InstalledOn))


ventana.title('Revisión de parchado')
ventana.geometry('380x300')
lbl_maquina = tkinter.Label(ventana, text='Ingresar Nombre de máquina: ')
lbl_maquina.grid(row=0, column=0)
maquina = tkinter.Entry(ventana)
maquina.grid(row=0, column=1)
maquina.focus()
tkinter.Button(ventana, text='Consultar', command=consulta).grid(row=0, column=3, columnspan=1)

tabla = ttk.Treeview(ventana, columns=('col1', 'col2'), selectmode='extended')
tabla.column('#0', width=100)
tabla.column('col1', width=100)
tabla.column('col2', width=100)
tabla.heading('#0', text='Nombre')
tabla.heading('col1', text='KB')
tabla.heading('col2', text='Fecha Inst')
tabla.grid(row=1, columnspan=7, rowspan=7)

ventana.mainloop()
