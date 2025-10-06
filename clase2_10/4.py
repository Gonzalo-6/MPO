def copiar_archivo(origen, destino):

    try:
        with open(origen,"r") as archivo_origen:
            contenido =archivo_origen.read()

        with open(destino, "w") as archivo_destino:
            archivo_destino.write(contenido)

        print(f"El contido '{origen}' se ha copiado correctamente en '{destino}'. ")
    except FileNotFoundError:
        print(f"Error: el archivo '{origen}' no existe. ")
    except Exception as e:
        print(f"Ocurrio un error: {e}")


archivo_origen = input("Introduce el nombre del archivo de origen: ")
archivo_destino = input("Introduce el nombre del archico de destino: ")

copiar_archivo(archivo_origen,archivo_destino)