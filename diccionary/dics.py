#Es una colección de pares, indexado por llave - valor
#El orden no importa, ya que no se pueden llamar por su indice, sino por su llave. 
#Las llaves deben ser únicas.
diccionario = {
    "nombre": "Gus",
    "apellido" : "Gonzalez"
}
print(diccionario)

#Llamar el contenido de una llave
print(diccionario["nombre"])

#Diccionario con multiples tipos de datos
diccionario = {
    "nombre": "Gus",
    "apellido" : "Gonzalez",
    "cositas" : [10,20,30],
    "diccionario" : {"clave1": "Valor1", "clave2": "valor2"}
}
print(diccionario["cositas"])
print(diccionario["cositas"][1])
print(diccionario["diccionario"]["clave1"])

dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())

#Agregar elementos a un diccionario
diccionario = {
    "nombre": "Gus",
    "apellido" : "Gonzalez",
    "cositas" : [10,20,30],
    "diccionario" : {"clave1": "Valor1", "clave2": "valor2"}
}
diccionario["mas_cositas"] = "Estas cositas"
print(diccionario)

#Sobreescribir una clave
diccionario["nombre"] = "Tavo"
print(diccionario)

#Conocer elementos del diccionario
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
print(len(diccionario))