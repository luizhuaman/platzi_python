import random

def run():
    numero_random = random.randint(1, 100)
    numero_elegido = int(input("Introduce un numero del 1 al 100: "))
    vidas = 5
    while numero_random != numero_elegido :
        vidas -= 1
        if numero_random < numero_elegido and vidas > 0:
            print("Elige un numero mas pequeño.")
        elif numero_random > numero_elegido and vidas > 0:
            print("Elige un numero mas grande.")
            
        if vidas == 0 :
            print("GAME OVER")
            break

        print("Tienes", vidas, "vidas")
        numero_elegido = int(input("Introduce numero: "))

    if numero_random == numero_elegido : 
        print("Felicidades Ganaste")


if __name__ == "__main__" :
    run()