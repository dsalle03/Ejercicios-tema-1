# Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
# Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Finalmente muestra el valor final del numero_magico por pantalla


while True:
    try:
        numero_magico = 12345679
        numero_usuario = int(input(print("Dime un número del 1 al 9: ")))
        numero_usuario_2 = numero_usuario*9
        numero_magico_2 = numero_magico*numero_usuario_2
    finally:
        print(numero_magico_2)
        break
