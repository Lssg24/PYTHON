#ejercicio 1

def devolver_distintos(*args):
    if sum(args) > 15:
        numero=max(args)
    elif sum(args) < 10:
        numero=min(args)
    elif sum(args) >= 10 & sum(args) <= 15:
        for val in args:
            if val != max(args) and val != min(args):
                numero=val
            else:
                numero = val
    return numero

print(devolver_distintos(3,6,6))

#ejercicio 2

def palabra(palabra):
    separa=[]
    for letra in palabra:
        separa.append(letra)
    separa=sorted(list(set(separa)))
    return separa
print(palabra('entretenido'))

#3j3rcicio 3

def ceros(*args):
    numero=args.index(0)
    siguente=(args.index(0))+1
    if args[numero] == args[siguente]:
        ceros=True
    else:
        ceros=False
    return ceros

print(ceros(1,2,0,6,5,8,0,7,9))


#ejercicio4





def contar_primos(num):

    num = num + 1
    primo = True
    cont = 0
    for x in range(2,num):
        for i in range(2,x):
            if x%i == 0 and x!=i:
                primo = False
                break
            else:
                primo = True
        if primo:
            print(f"{x} es primo")
            cont = cont + 1
        else:
            print(f"{x} no es primo")
    print(f"Total de numeros primos: {cont}")


contar_primos(10)

#primos
def otra(num):
    primos = [2]
    iteracion = 3
    if num <2 :
        return 0
    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion+=2
                break
        else:
            primos.append(iteracion)
            iteracion+=2
    print(primos)
    return len(primos)

otra(100)


palabra='hola'
print(palabra[1])