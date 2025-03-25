#creame un diccionario
persona = {
    "nombre" : "Gonzalo",
    "edad" : 41,
    "registrado" : True

}
print(persona)
#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir una nueva clave-valor








#Eliminar una clave
#del persona["registrado"]
#print(persona)


#comprobar si una clave ya existe
existe_nombrecito = "nombre" in persona
existe_gonzalo = "Gonzalo" in persona["nombre"]
print(existe_nombrecito)
print(existe_gonzalo)

#comparar dos volres booleanos
es_menor_y_registrado = (persona["edad"]>18 and persona["registrado"])
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#creame un conjunto a partir de una lis con duplicados
numeritos =[7,8,4,7,1,2,3,4,5,7,2,6,8,4]

#convierto a conjunto
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos unicos
coleccion_a = set([1,2,2,3])
coleccion_b = set([3,2,1])

mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)
