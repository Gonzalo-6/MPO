texto = str(input("Introduce un texto: "))

letras = len(texto)
palabras = len(texto.split())
mas_larga = max(texto.split(), key=len)

print(f"El texto contiene {letras} letras y {palabras} palabras.")
print(f"La palabras mas laraga es: {mas_larga} y contienen {len(mas_larga)} letras.")