numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 1235, 736, 45, 67]

for indice in range(len(numeros)):
    if (numeros[indice] % 3 == 0) and (numeros[indice] % 5 == 0):
        numeros[indice] = "FizzBuzz"
    elif numeros[indice] % 3 == 0:
        numeros[indice] = "Fizz"
    elif numeros[indice] % 5 == 0:
        numeros[indice] = "Buzz"

print(numeros)