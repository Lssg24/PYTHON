dic = {'clave':100,'clave2':500}

a = dic.popitem()
print(a)
print(dic)

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
texto2=texto.lstrip(',:_#%')
print(texto2)


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'Naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados=marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)