def multiples_of_two(list):
    pair_list = []
    for num in list:
        if num % 2 == 0:
            pair_list.append(num)
    return pair_list

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("La lista de números inicial es: {}".format(numeros))
print("Los múltiplos de 2 de dicha lista son: {}".format(multiples_of_two(numeros)))