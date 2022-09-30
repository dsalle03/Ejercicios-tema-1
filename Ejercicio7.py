def agregar_una_vez(lista):
    elemento = (input(print("Dime un elemento: ")))
    lista.append(elemento)
    lista.append(10)
    lista.append(-2)
    lista.append("Hola")
    return lista

lista = [input(print("Dame una lista: "))]
lista_1 = agregar_una_vez(lista)
print(lista_1)