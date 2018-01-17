lista_numeros = []

for i in range(10):
    numero_usuario = int(input("Elija un número: "))
    lista_numeros.append(numero_usuario)
print("El mayor número de la lista es: {}".format(max(lista_numeros)))