numero_ganador = 5

numero_usuario = int(input("Adivine el numero(1-10): "))
if numero_usuario == numero_ganador: print("¡Has ganado!")
else: print("Has perdido, el número ganador era {} y has escogido el número {}".format(numero_ganador, numero_usuario))