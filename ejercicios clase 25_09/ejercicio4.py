texto = input("Introduce un texto: ")

mayusculas = 0
minusculas= 0

for caracter in texto:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1

print(f" el texto contiene {mayusculas} mayúsculas y {minusculas} minúsculas.)")