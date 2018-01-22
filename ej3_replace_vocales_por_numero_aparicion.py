frase = "aurora boreal"
vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
numero_de_aparicion = 1

print("La frase inicial es: {}".format(frase))
for letra in frase:
    if letra in vocales:
        frase = frase.replace(letra, str(numero_de_aparicion), 1)
        numero_de_aparicion += 1

print("La frase cambiada es: {}".format(frase))

