lista = ["Sigue", 1, "el", 2, 3, "orden", "de", "la", 4, "lista"]
lista_ints = []
lista_strings = []

for i in lista:
    if type(i) == type(0):
        lista_ints.append(i)
    elif type(i) == type(""):
        lista_strings.append(i)
    else:
        print("El tipo de este elemento no es un string ni un integer.")

print("Lista original: {}".format(lista))
print("Lista de strings: {}".format(lista_strings))
print("Lista de integers: {}".format(lista_ints))