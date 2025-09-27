# Ejercicio 10 Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número. 
# El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. 
# El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto

import random

ramdon_num = random.randint(1, 100)
user_num = int(input("Introduce un número del 1 al 100: "))
while user_num != ramdon_num:
    if user_num > ramdon_num:
        print("El número es demasido grande.")
    else:
        print("El número es pequeño.")
    user_num = int(input("Introduce otro número: "))
print("¡Has acertado!👍")


