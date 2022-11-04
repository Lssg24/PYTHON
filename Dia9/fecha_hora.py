# import datetime


'''mi_hora = datetime.time(17, 35)
print(mi_hora.minute)'''  # puedes adicionar mas datos

'''mi_dia = datetime.date(2022, 10, 17)
print(mi_dia.year)  # puedes adicionar otros datos
mi_dia = mi_dia.today()
print(mi_dia)'''

from datetime import datetime, date

mi_fecha = datetime(2024, 5, 15, 22, 10, 15, 2500)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

nacimiemto = date(1995, 3, 5)
defunfion = date(2095, 6, 19)

vida = defunfion - nacimiemto

print(vida.days)
# -----------------------------------

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia.seconds)

mi_fecha = date(1999, 2, 3)
print(mi_fecha)

hoy = datetime.today().minute
print(hoy)
