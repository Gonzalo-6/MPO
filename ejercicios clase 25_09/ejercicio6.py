texto = input("Introduce un texto: ")

palabras_censuradas = ["malo", "feo", "tonto"]

for palabra in palabras_censuradas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(f"Este es tu texto censurado: {texto}")
