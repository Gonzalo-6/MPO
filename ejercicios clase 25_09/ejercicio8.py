import random
from collections import Counter

# Generar 10 tiradas de un dado de 1 a 6
tiradas = [random.randint(1, 6) for _ in range(10)]

# Contar cuántas veces aparece cada número
contador = Counter(tiradas)

# Obtener el número más repetido (moda)
moda, repeticiones = contador.most_common(1)[0]

# Mostrar resultados
print(f"Las tiradas han sido: {tiradas}")
print(f"El número más repetido es: {moda} ({repeticiones} veces)")
