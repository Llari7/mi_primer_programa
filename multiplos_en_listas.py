lista_numeros = [1, 2, 3, 45, 83, 95, 24, 642, 567, 24]
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

print("Lista inicial: {}".format(lista_numeros))

for numero in lista_numeros:
    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos_cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print("Múltiplos de 2: {}".format(multiplos_dos))
print("Múltiplos de 3: {}".format(multiplos_tres))
print("Múltiplos de 5: {}".format(multiplos_cinco))
print("Múltiplos de 7: {}".format(multiplos_siete))