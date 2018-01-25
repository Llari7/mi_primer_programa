contador = dict()
palabra = ""

frase = input("Escriba la frase que quiera contabilizar: ")
frase += " "
for letra in frase:
    if not letra.isspace():
        palabra += letra
    else:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
        palabra = ""

for palabra_contada in contador:
    print("{}: {} veces.".format(palabra_contada, contador[palabra_contada]))