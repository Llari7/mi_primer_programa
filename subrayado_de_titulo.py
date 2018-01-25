def mostrar_titulo_subrayado(titulo):
    titulo_subrayado = {titulo: ""}
    for i in range(len(titulo)):
        titulo_subrayado[titulo] += "-"
    print("{}".format(titulo))
    print("{}".format(titulo_subrayado[titulo]))

titulo_usuario = input("Introduzca el título que desee subrayar: ")
mostrar_titulo_subrayado(titulo_usuario)