import os

'''
1- Comprobar que existe el archico
2-Comprobar que sea un archivo
3- Comprobar que exista ña nueva ruta
4- Comprobar que la nueva ruta es un directorio
5- Comprovamos que path y new_path no son iguales
6- Mover el archivo a new_path
'''

def move_file(path, new_path):
    if not os.path.isfile(path):
        raise FileNotFoundError("No existe el archivo")
    if not os.path.isdir(new_path):


    if path == new_path:
    pass

path = input("Introduce un archivo que quieras mover\n")
new_path = input("Introduce la ruta done queres moverloªn")

try:
    print(move_file(path, new_path))
except Exception
