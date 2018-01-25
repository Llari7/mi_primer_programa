colores = {"rojo": "red",
           "azul": "blue",
           "amarillo": "yellow",
           "verde": "green",
           "naranja": "orange",
           "morado": "purple",
           "rosa": "pink",
           "negro": "black",
           "blanco": "white",
           "gris": "grey"}

color = input("¿Qué color desea traducir? ").lower()
if color in colores:
    print("El color {} en inglés es: {}".format(color, colores[color]))
else:
    print("El color escogido no esta en nuestra base de datos, lo sentimos.")