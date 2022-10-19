nombre=input('Ingresa tu nombre: ')
ventas=input('Ingresa el valor total de ventas realizadas: ')
ganancia=float(ventas)*13/100
final=round(ganancia,2)
print(f'{nombre}, la ganancia del 13% es :${final}')