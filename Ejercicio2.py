numero_magico = 12345679
numero_usuario = int(input(print("Dime un número del 1 al 9: ")))
if numero_usuario in range (10):
    numero_usuario_2 = numero_usuario**9
    print(numero_magico*numero_usuario_2)
else:
    print("El número tiene que ser del 1 al 9")

