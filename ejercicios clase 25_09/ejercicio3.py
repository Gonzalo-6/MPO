nombreCompleto = input("introduce tu nombre y apellidos: ")
nombre = nombreCompleto.split()
inicales = "" .join(nombre[0].upper() for nombre in nombre)

print(f"La iniciales de tu nombre son: {inicales} ")