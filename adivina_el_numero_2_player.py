numero_ganador = int(input("Número a adivinar (1-10): "))
numero_aspirante = 0

while numero_aspirante != numero_ganador:
    numero_aspirante = int(input("Adivina el número: "))
print("¡Enhorabuena, has adivinado el número ganador!")
