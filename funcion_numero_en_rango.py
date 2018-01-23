def number_in_range(number, min, max):
    if number > min and number < max:
        return True
    else:
        return False

confirmacion = False

while not confirmacion:
    print("Ha continuación se le pedirán 1 número y un rango (número mínimo y número máximo) respectivamente para concretar si dicho número está en el rango contemplado.")
    numero = int(input("Introduzca el número a comprobar: "))
    minimo = int(input("Introduzca el límite inferior del rango (mínimo valor): "))
    maximo = int(input("Introduzca el límite superior del rango (máximo valor): "))
    if minimo < maximo:
        confirmacion = True
    else:
        print("El rango introducido es incorrecto (límite inferior es mayor que el límite superior) se procederá a repetir el proceso.\n")

if number_in_range(numero, minimo, maximo):
    print("El número {} está en el rango ({},{})".format(numero, minimo, maximo))
else:
    print("Lo sentimos, pero el número {} NO está en el rango ({},{})".format(numero, minimo, maximo))
