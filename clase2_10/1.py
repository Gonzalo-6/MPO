
log = open("errores.txt", "r")

log_data = log.readlines()

num_lineas = len(log_data)

print(f"Este archico tiene: {len(log_data)} líneas")

"""
def contar_lineas(nombre_archivo):
    
    Abre un archivo de texto y cuenta el número de líneas que contiene.
    
    try:
        with open(nombre_archivo, "r") as archivo:
            contador = sum(1 for _ in archivo)
        return contador
    except FileNotFoundError:
        print("❌ Error: el archivo no existe.")
        return 0

# Programa principal
nombre = "info.txt"
num_lineas = contar_lineas(nombre)
print(f"El archivo '{nombre}' tiene {num_lineas} líneas.")"""