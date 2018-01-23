def max_three_num(first, second, third):
    if first >= second and first >= third:
        max_num = first
    elif second >= first and second >= third:
        max_num = second
    elif third >= first and third >= second:
        max_num = third
    return max_num

print("Ha continuacion se le pedirán 3 números para hallar el máximo de ellos.")
primero = int(input("Introduzca el primer número: "))
segundo = int(input("Introduzca el segundo número: "))
tercero = int(input("Introduzca el tercer número: "))


print("EL mayor de {}, {} y {} es: {}".format(primero, segundo, tercero, max_three_num(primero, segundo, tercero)))
