#Ejercicio 1: Operaciones numericas complejas
#define cinco variables numéricas distintas



#num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j
#resultado = (f"Potencia: {num1 ** num2}, Division entera: {num1//num2}, "
             #f"Modulo: {num1%num2}, Multiplicacion: {num3*num4}, Complejo: {num5}")
#print(resultado)
#oracion = (f"Hola mundo: {num3*num1}, Suma: "
           #f"{num3+num5}")

#print(oracion)

#Ejercicio 2

#num_int, num_float= 8, 3.5
#cadena1, cadena2, cadena3 = "Resultado: ", "la suma es", "y la división es"
#resultado = (cadena1 + "" + cadena2 + "" + str(num_int/num_float) + cadena3 + str(num_int/num_float))
#print(resultado)


#Ejercicio 3

#cadena = " Esto es una cadena para manipular "
#nueva_cadena = cadena.strip().upper().split()
#print(nueva_cadena)

#Ejercicio 4

#cadena_extensa = "Python es un super lenguaje que me re encanta"
#subcadena = cadena_extensa[0:6] + "" + cadena_extensa [11:20]
#resultado = subcadena[::-1]
#print(resultado)

#Ejercicio 5

#entero, flotante, complejo = 12, 345.23976, 5+3j
#formato = f"Entero: {entero}, Flotante: {flotante: .2f}, Notacion CIentifica: {flotante:.2e}"
#print(formato)

# Ejercicio 6

#num_a, num_b = 15, 4
#cad_a, cad_b = "La multiplicación da: " , "y el resto es: "
#resultado = f"{cad_a}{num_a*num_b}, {cad_b}{num_a%num_b}"
#print(resultado)


# Ejercicio 7

#largo, ancho, radio, altura = 10, 5, 3, 4
#area_rectangulo = largo*ancho
#perimetro_rectangulo = 2*(largo+ancho)
#area_circulo = 3.14 * radio ** 2
#perimetro_circulo = 2*3.14*radio
#area_triangulo = (largo*altura)/2
#resultado = (f"Area de un rectangulo: {area_rectangulo}, "
#f"perimetro del rectangulo {perimetro_rectangulo}, "
             #f"\nCirculo: Area:{area_circulo} y perimetro: {perimetro_circulo}, "

#print(resultado)

#Ejercicio 8.

parrafo = "Soy un ejemplo de parrafo largo de narices para ocupar todo el espacio posible"
caracteres = len(parrafo)
palabroides = len(parrafo.split())
mayusculas = parrafo.upper()
resultado = (f"Total de caracteres: {caracteres}, total de palabras: {palabroides}, Texto en mayusculas: {mayusculas}, ")
print(resultado)

# Ejercicio 9
a, b, c = 1, -3, 2
discriminante = (b ** 2-4*a*c)**0.5
raiz1 = (-b + discriminante)/(2*a)
raiz2 = (-b-discriminante)/(2*a)
resultado= f"Coeficientes: a={a}, b={b}, c={c}. Raíces: {raiz1}, {raiz2}"
print(resultado)

#Ejercicio 10
nombre, edad, peso, altura= "Gonzalo", 41, 74, 175
imc= peso / altura **2
resultado = f"Nombre: {nombre}, Edad: {edad}, Peso: {peso} kg, Altura: {altura} cm, IMC: {imc:2f}"
print(resultado)