while True:
    try:
        numero_magico = 12345679
        numero_usuario = int(input(print("Dime un número del 1 al 9: ")))
        numero_usuario_2 = numero_usuario*9
        numero_magico_2 = numero_magico*numero_usuario_2
        print(numero_magico_2)
        break
    except ValueError:
        print("Solo se aceptan números")