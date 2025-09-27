#While
#Ejercicio 9 Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números. 
# El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

print("Introduce números para sumarlos y para acabar introduce 0.")
numero = int(input())
resultado = 0

while numero != 0:
    resultado += numero
    numero = int(input())
print(f"La suma es: {resultado}")
   
   



