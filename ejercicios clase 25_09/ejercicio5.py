lista= input("Introduce una lista de frutas separas por comas: ")

frutas = [fruta.strip() for fruta in lista.split(",")]

ordenadas = sorted(set(frutas))

print(f"Tu lista de frutas ordenadas por orden alfabetico y sin repeticiones es: {ordenadas}")
