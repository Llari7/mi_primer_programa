import random
from time import sleep

text_list = ["Hola Mundo", "Es hora de ir a comer", "Ponte a estudiar", "Adios Mundo"]

while True:
    random_index = random.randint(0, len(text_list) - 1)
    print(text_list[random_index])
    sleep(3)