lista = ["Hola", "Mundo", "Nuevo ejercicio", "del curso de Nate Gentile de Python"]

lista_longitudes = []
contador = 0

for str in lista:
    for i in str:
        contador += 1
    lista_longitudes.append(contador)
    contador = 0

print("Lista longitudes SIN LEN: {}".format(lista_longitudes))