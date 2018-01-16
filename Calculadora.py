
operacion = input("¿Qué operación deseas realizar? (suma / resta / multiplicación / división): ")
primer_numero = int(input("Primer número: "))
segundo_numero = int(input("Segundo número: "))

if operacion == "suma":
    print("Resultado: {}".format(primer_numero + segundo_numero))
elif operacion == "resta":
    print("Resultado: {}".format(primer_numero - segundo_numero))
elif operacion == "multiplicación":
    print("Resultado: {}".format(primer_numero * segundo_numero))
elif operacion == "división":
    print("Resultado: {}".format(primer_numero / segundo_numero))
