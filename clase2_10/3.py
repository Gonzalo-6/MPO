def guardar_nombres_en_archivo(lista_nombres,nombre_archivo):



   with open(nombre_archivo, "w") as archivo:
       for nombre in lista_nombres:
        archivo.write(nombre + "\n")
   print(f"Los nombres se han guardado en el archivo '{nombre_archivo}. ")

nombres = []

while True:
    nombre = input("Introduce un nombre (o escribe 'salir' para terminar): ")

    if nombre.lower() == 'salir':
        break
    nombres.append(nombre)

archivo = "lista_nombres.txt"
guardar_nombres_en_archivo(nombres, archivo)



