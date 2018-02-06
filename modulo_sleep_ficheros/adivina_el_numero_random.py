from random import randint
from time import sleep

winner_number = randint(1, 10)

user_number = int(input("¿Cúal es el número ganador? (1-10) "))
sleep(3)
if user_number == winner_number:
    print("¡Felicidades, has ganado!")
else:
    print("Incorrecto, el número ganador era {}".format(winner_number))