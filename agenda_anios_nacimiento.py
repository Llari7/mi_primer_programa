agenda = dict()
confirmacion = False

while True:
    accion = input("Que desea hacer? (Añadir[A] / Consultar[C] / Salir[S]) ")
    if accion.upper() == "A":
        print("Se añadirá un año de nacimiento al sistema.")
        print("+++++++++++++++++++++++++++++++++++++++++++\n")
        nombre = input("Nombre: ")
        anio = input("Año de nacimiento: ")
        agenda[nombre] = anio
        print("El año de nacimiento de {} se ha añadido correctamente.".format(nombre))
    elif accion.upper() == "C":
        if len(agenda) != 0:
            print("Se consultará un año de nacimiento de los almacenados en el sistema.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            nombre_consulta = input("¿De quién quiere consultar el año de nacimiento? ")
            if nombre_consulta in agenda:
                print("El año de nacimiento de {} es {}.".format(nombre_consulta, agenda[nombre_consulta]))
            else:
                print("La persona que ha seleccionado no está en el sistema.")
        else:
            print("No se puede consultar ningún año de nacimiento, la agenda está vacía.")
    elif accion.upper() == "S":
        print("Ha salido del programa, hasta la próxima.")
        exit()