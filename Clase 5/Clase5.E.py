# 1. Evaluación de expresiones booleanas
# definimos expresiones matemáticas y evaluamos su valor booleano
exp1 = 10 > 5   # True
exp2 = 7 + 3 == 10  # True
exp3 = 20 < 15  # False
exp4 = 4 * 2 == 9  # False
# mostramos los resultados
print(exp1, exp2, exp3, exp4)

# 2. Operaciones matemáticas con booleanos

print(True + True)
print(False + True)
print(True * 10)
print(False * 50)

# 3. Conversión entre tipos básicos
# convierto un número en cadena
numero = 123
cadena = str(numero)
print(cadena)

# convierto una cadena numérica en entero

cadena_numerica = "456"
numero_convertido = int(cadena_numerica)
print(numero_convertido)

# convierto un booleano en número

print(int(True))
print(int(False))

# 4. Propiedades de las cadenas

# creo una cadena con un nombre
nombre = "Gonzalo"

print(nombre[0])
print(nombre[-1])

# muestro la longitud de la cadena
print(len(nombre))

# convierto la cadena a mayúsculas y minúsculas

print(nombre.upper())
print(nombre.lower())

# 5. Operaciones con cadenas y números

edad = 41
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)
# repetir una cadena varias veces
repetido = "Guapo " * 3
print(repetido)

# 6. Operaciones con caracteres y códigos ASCII
# obtengo el código ASCII de una letra
codigo = ord('A')
print(codigo)

# convierto un número en un carácter
letra = chr(66)
print(letra)



# 1. Comparación de números y booleanos
# creo tres variables con diferentes valores
a = 6
b = 10
c = 8

# comparo los valores y almaceno los resultados en variables booleanas
mayor = a > b
menor = c < b
igual = a == c
diferente = b != c

# muestro los resultados de las comparaciones
print(mayor, menor, igual, diferente)

# 2. Propiedades y manipulación de cadenas

# defino una cadena con una frase corta
frase = ("La Elipa me flipa")

# muestro la cantidad de caracteres en la cadena
print(len(frase))

# convierto la cadena a mayúsculas y la muestro
print(frase.upper())

# convierto la cadena a minúsculas y la muestro
print(frase.lower())

# cuento cuántas veces aparece la letra "o"
print(frase.count("a"))


# 3. Operaciones matemáticas con números y booleanos

# defino variables booleanas
hola = True
adios = False

# realizo operaciones matemáticas con booleanos
suma = hola + adios
resta = hola - adios
multiplicacion = hola * 5
multiplicacion_falsa = adios * 10

# muestro los resultados de las operaciones
print(suma, resta, multiplicacion, multiplicacion_falsa)


# 4. Extracción de caracteres en una cadena

# defino una cadena con una palabra
palabra = "Educacion"

# extraigo los tres primeros caracteres
print(palabra[:3])

# extraigo los tres últimos caracteres
print(palabra[-3:])

# extraigo los caracteres en posiciones impares
print(palabra[::2])


# 5. Conversión de tipos y evaluación booleana

# convierto un número en una cadena y muestro su tipo
num = 500
num_cadena = str(num)
print(num_cadena, type(num_cadena))

# convierto una cadena numérica en entero y muestro su tipo
cadena_num = "75"
num_convertido = int(cadena_num)
print(num_convertido, type(num_convertido))

# convierto varios valores a booleanos y muestro los resultados
print(bool(""))
print(bool("Texto"))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(None))


