lista_numeros = [1,2, 3, 4, 5, 6, 7, 8, 9]
numero_usuario = int(input("Introduzca un número: "))

print("Tabla de multiplicar del número {}:".format(numero_usuario))
for m in lista_numeros:
    resultado = numero_usuario * m
    print("{} x {} = {}".format(numero_usuario, m, resultado))


