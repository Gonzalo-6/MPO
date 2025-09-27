precio = input("introduce el precio del producto: ")
descuento = input("introduce el descuento en %: ")

precioFinal = float(precio) - (float(precio) * float(descuento) /100)

print(f"El producto marca {precio} con un descuento de {descuento}% se queda en {precioFinal:.2f}euros.")