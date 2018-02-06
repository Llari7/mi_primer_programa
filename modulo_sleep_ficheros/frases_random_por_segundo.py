from time import sleep
import random
import datetime

happy_phrases = ["Hoy es un buen día", "De todo lo malo se aprende", "Siempre hay algo por lo que sonreir", "La vida es maravillosa"]
furniture_names = ["Silla", "Sofá", "Mesa", "Cama"]
drinks_names = ["Zumo", "Agua", "Vino", "Whisky"]
hate_phrases = ["Te vas a pasar la vida solo", "Te mereces la muerte", "Eres un ser deleznable", "Ojalá te mueras"]
food_names = ["Arroz con Bogavante", "Pizza", "Cocido", "Entrecot a la plancha"]
absurd_phrases = ["Te perro a veces", "Mesa cuando móvil vence", "Invierno debe segundo almohada", "Biblioteca Alonso donde luz"]
animal_names = ["Perro", "Tigre", "Elefante", "Tiburón"]
motivational_phrases = ["Puedes conseguir lo que te propongas", "Lucha por tus sueños", "No hay nada imposible", "Un día más es un día menos"]
animal_sounds = ["Guau", "Miau", "Kikiriki", "Gri Gri"]
sad_phrases = ["La vida es una mierda", "Solo ocurren desgracias", "El mundo se acaba", "Todos moriremos"]

phrases = [happy_phrases, furniture_names, drinks_names, hate_phrases, food_names, absurd_phrases, animal_names, motivational_phrases, animal_sounds, sad_phrases]



while True:
    sleep(1)
    actual_time = datetime.datetime.now()
    actual_seconds = str(actual_time.second)
    second_index = int(actual_seconds[len(actual_seconds)-1])
    random_index = random.randint(0, len(phrases[second_index])-1)
    print(phrases[second_index][random_index])
