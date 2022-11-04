from collections import Counter
from collections import defaultdict

numeros = [8, 9, 5, 4, 8, 7, 5, 8, 9, 8, 9, 5, 8, 7, 4, 8, 5, 8, 5, 8, 5, 9, 8, 5]
palabra = 'missisipi'
frase = 'el pan se lo come el huaso'
print(Counter(numeros))
print(Counter(palabra))
print(Counter(frase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])
print(serie.most_common())  # ordena de el que tiene mas

mi_dic = defaultdict(lambda: 'nada')
# mi_dic =  {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.50, 60)
print(ariel.altura)
print(ariel[2])

from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)
