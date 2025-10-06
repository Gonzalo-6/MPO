from os.path import split
"""
log = open("errores.txt", "r")

log_data = log.readlines()

linea = len(log_data)
texto_completo = "".join(log_data)

palabra = texto_completo.split()

num_palabras = len(palabra)

print(f"El texto tiene {linea} líneas y {num_palabras} palabras")
"""
def contar_lineas_y_palabras(nombre_archivo):

    try:
        with open("errores.txt", "r") as archivo:
            lineas = archivo.readlines()
            num_lineas = len(lineas)
            texto = "".join(lineas)
            num_palabras = len(texto.split())
            return num_lineas, num_palabras
    except FileNotFoundError:
        print("Error: el archivo no existe.")
        return 0, 0



nombre = "errores.txt"
lineas, palabras = contar_lineas_y_palabras(nombre)
print(f"El archivo {nombre} tiene {lineas} líneas y {palabras} palabras.")