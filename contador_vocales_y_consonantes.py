frase = input("Introduzca una frase: ")
lista_vocales = ["a", "e", "i", "o", "u"]
vocal = 0
consonante = 0

for letra in frase:
    if letra.lower() in lista_vocales:
        vocal += 1
    elif not letra.isspace() and letra.isalpha():
        consonante += 1

print("{!r} contiene {} vocales y {} consonantes".format(frase, vocal, consonante))