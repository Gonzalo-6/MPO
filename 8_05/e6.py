'''Ejercicio 15 - Banca online¶
Escribe un programa que simule una cuenta bancaria. El programa debe permitir al usuario realizar las siguientes operaciones:

Ingresar dinero
Retirar dinero
Consultar saldo
Salir
Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.'''

saldo = 0
opcion = -1

while opcion != 4:
    print("Escoge una opción:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo") 
    print("4. Salir")

    opcion = int(input())

    if opcion == 1:
        saldo += int(input("¿Cuánto dinero quieres ingresar? "))