frase = input("Introduzca la frase que quiera cambiar: ")
vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

print("La frase inicial es: {}".format(frase))
for letra in frase:
    if letra in vocales:
        frase = frase.replace(letra, "i")

print("La frase camiada es: {}".format(frase))