import random


def jugar():
    numero_secreto = random.randint(1, 100)
    
    c_intentos = 0
    adivinado = False

    print("🎉¡Bienvenido al juego del número secreto!🎉")
    print("Adivina el número del 1 al 100 😜")
    print("Tienes 10 intentos 🫥")

   

    while not adivinado:
        c_intentos = c_intentos + 1
        intento = int(input("Ingresa un número👌: "))
        if c_intentos > 10: 
         print("juego terminado")
        
        if intento == numero_secreto:
            print(" ¡Felicidades!🎉 Adivinaste el número😍")
            print("intentos: ", c_intentos, " ✌️")
            adivinado = True
        elif intento < numero_secreto:
            print(" El número secreto es mayor👆")
            print("ya usaste: ", c_intentos,"intentos 😬" 
            "")
        else:

            print(" El número es secreto menor👇")
            print("ya usaste: ", c_intentos,"intentos 😬"
            "")
            

if __name__ == "__main__":
        jugar()