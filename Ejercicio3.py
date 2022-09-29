lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = lista_1+lista_2
lista_repetidos = []

for i in lista_3:
    if i not in lista_repetidos:
        lista_repetidos.append(i)

print(lista_repetidos)
