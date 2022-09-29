def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
            pares.sort()
        else:
            impares.append(i)
            impares.sort()
    return pares, impares


lista = [6,5,2,1,7]
separado = separar(lista)
print(separado)





