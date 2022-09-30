lista_descompuesta = []
while True:
    try:
        numero_descomponer = input(print("Dime un número de 4 cifras: "))
        a = 1
        for i in range(0, len(numero_descomponer), a):
            lista_descompuesta.append(int(numero_descomponer[i : i + a]))
        lista_descompuesta = str(lista_descompuesta)
        print("000" + lista_descompuesta[10])
        print("00" + lista_descompuesta[7] + "0")
        print("0" + lista_descompuesta[4] + "00")
        print(lista_descompuesta[1] + "000")
        print("El número del usuario es: " + lista_descompuesta[1] + lista_descompuesta[4] + lista_descompuesta[7] + lista_descompuesta[10])
        break
    except ValueError:
        print("Solo se aceptan números enteros")
    

    