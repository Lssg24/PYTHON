mi_set=set({1, 2, 3, 4, 5})
print(type(mi_set))
print(mi_set)

'''otro_set={1,2,3}
print(type(otro_set))
print(otro_set)'''

#no soportan asignacion de items, solo admite tuples, los valores duplicados los elimina

mi_set=set({1, 2, 3,(1,2,3), 4, 5})
print(type(mi_set))
print(mi_set)
print(len(mi_set))
print(2 in mi_set)

#Union de set

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

s1={1,2,3}
s1.add('damian')
print(s1)
s1.remove(1)
print(s1)
s1.discard(5)
print(s1)
s1.clear()#vacia el set
print(s1)
