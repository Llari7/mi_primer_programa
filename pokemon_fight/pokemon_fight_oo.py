from time import sleep


class Pokemon:
    name = "Pokemon"
    max_health = 0
    attack = 0

    def __init__(self):
        self.health = self.max_health

    def print_health(self):
        print("{} tiene {} de vida.".format(self.name, self.health))

    def attacking(self, enemy):
        print("{} ha atacado a {}, le ha quitado {} de vida.".format(self.name, enemy.name, self.attack))
        enemy.health -= self.attack


class Pikachu(Pokemon):
    name = "Pikachu"
    max_health = 90
    attack = 12


class Charmander(Pokemon):
    name = "Charmander"
    max_health = 100
    attack = 10


class Squirtle(Pokemon):
    name = "Squirtle"
    max_health = 110
    attack = 8


class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    max_health = 120
    attack = 6


def main():
    enemy_pokemon = None

    your_pokemon = Pikachu()
    print("El pokemon con el que empiezas es {}".format(your_pokemon.name))
    sleep(2)
    choosed_pokemon = input("Contra que pokemon quieres luchar (Charmander / Squirtle / Bulbasaur): ")
    if choosed_pokemon == "Charmander":
        enemy_pokemon = Charmander()

    elif choosed_pokemon == "Squirtle":
        enemy_pokemon = Squirtle()

    elif choosed_pokemon == "Bulbasaur":
        enemy_pokemon = Bulbasaur()

    else:
        print("No se ha escogido ninguna de la opciones posibles, el combate se ha anulado.")
        sleep(2)
        exit()

    while your_pokemon.health > 0 and enemy_pokemon.health > 0:
        your_pokemon.print_health()
        sleep(1)
        enemy_pokemon.print_health()
        sleep(1)
        your_pokemon.attacking(enemy_pokemon)
        sleep(1)
        enemy_pokemon.attacking(your_pokemon)
        sleep(1)

    if your_pokemon.health > enemy_pokemon.health:
        print("¡Has ganado el combate pokemon!")
    else:
        print("Has perdido el combate pokemon.")


if __name__ == '__main__':
    main()
