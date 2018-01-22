frase = input("Introduzca la frase que quiera cambiar: ")
letra_a_cambiar = ["A", "a"]

print("La frase inicial es: {}".format(frase))
for letra in frase:
    if letra in letra_a_cambiar:
        frase = frase.replace(letra, "VACA")

print("La frase con el replace es: {}".format(frase))
