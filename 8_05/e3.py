
#Ejerciccio 11
# Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. 
#Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. 
#El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1.
#Al final, imprime la media.
''''
Introduce el número de evaluaciones: 3
Notas de la evaluación 1: 6 8 4 3.5 9 -1
Notas de la evaluación 2: 7 5 8.5 -1
Notas de la evaluación 3: 9 10 8.5 -1
La media de la evaluación 1 es: 6.5
La media de la evaluación 2 es: 7.5
La media de la evaluación 3 es: 9.
'''''

evaluaciones = int(input("Introduce el número de evaluaciones: "))
for i in range(evaluaciones):
    nota = float(input("Introduce la siguiente nota: "))
    num_notas = 0
    suma_notas = 0
    while nota != -1:
        num_notas += 1
        suma_notas += nota
        nota = float(input("Introduce la siguiente nota: "))
    print(f"Nota media evaluación {i+1} : {suma_notas/num_notas}")