
pikachu_vida = 100
pikachu_chispazo = 10
pikachu_voltio = 12

enemigo_vida = 0
enemigo_ataque = 0

pokemon_elegido = input("Contra que pokemon quieres luchar (Charmander / Squirtle / Bulbasaur): ")
if pokemon_elegido == "Charmander":
    enemigo_vida = 80
    enemigo_ataque = 7

if pokemon_elegido == "Squirtle":
    enemigo_vida = 90
    enemigo_ataque = 8

if pokemon_elegido == "Bulbasaur":
    enemigo_vida = 100
    enemigo_ataque = 10

if pokemon_elegido != "Charmander" and pokemon_elegido != "Squirtle" and pokemon_elegido != "Bulbasaur":
    print("No se ha escogido ninguna de la opciones posibles, el combate se ha anulado.")
else:
    while pikachu_vida > 0 and enemigo_vida > 0:
        print("Pikachu - Vida = {}".format(pikachu_vida))
        if pokemon_elegido == "Charmander":
            print("Charmander - Vida = {}".format(enemigo_vida))
            print("Charmander ha usado ascuas.")
        if pokemon_elegido == "Squirtle":
            print("Squirtle - Vida = {}".format(enemigo_vida))
            print("Squirtle ha usado pistola agua.")
        if pokemon_elegido == "Bulbasaur":
            print("Bulbasaur - Vida = {}".format(enemigo_vida))
            print("Bulbasaur ha usado hoja afilada.")
        pikachu_vida -= enemigo_ataque
        if pikachu_vida > 0:
            pikachu_ataque = input("Que ataque desea realizar (Chispazo / Bola Voltio): ")
            if pikachu_ataque == "Chispazo":
                print("Pikachu ha usado Chispazo")
                enemigo_vida -= pikachu_chispazo
            if pikachu_ataque == "Bola Voltio":
                print("Pikachu ha usado Bola Voltio")
                enemigo_vida -= pikachu_voltio
            if pikachu_ataque != "Chispazo" and pikachu_ataque != "Bola Voltio":
                print("No ha escogido un ataque válido, ha perdido el turno")

    if pikachu_vida > enemigo_vida:
        print("¡Has ganado el combate pokemon!")
    else:
        print("Has perdido el combate pokemon.")
