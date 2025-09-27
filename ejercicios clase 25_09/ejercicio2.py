edad = int(input("escribe tu edad: "))

if edad < 0:
    print("No has nacido todavía.")
elif edad (0 <= edad <=  12):
    print(f"Con {edad} años eres un niño.")
elif edad <=17:
    print(f"Con {edad} años eres un adolescente.")
elif edad <=64:
    print(f"Con {edad} años eres un adulto.")
else:
    print(f"Con {edad} años eres un senior.")
