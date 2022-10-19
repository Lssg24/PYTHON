mi_tuple = (1,2,3,4) #con o sin parentesis sirve\ estos son inmutables
mi_tuple1 = (1,2,(5,67,100),4,3.5,'hola')
print(mi_tuple1[2][1])

print(type(mi_tuple))

print(mi_tuple)

print(mi_tuple1)

mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t=(1,2,3)
x,y,z=t
print(x,y,z)