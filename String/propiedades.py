#Los string son inmutables, es decir que no se pueden cambiar. Esto devuelve un error
# nombre = "Gustabo"
# nombre[5] = "v"
# print(nombre)

#Concatenar y multiplicar
n1 = "Gus"
n2 = "tavo"
resultado = n1+n2
print(resultado)
resultado = resultado * 5
print(resultado)

#Salto de linea sin necesidad de una función.
texto = """Este es un texto
Este es otro en otra linea
y aqui un tercero en una linea más
"""
print(texto)

#Saber si existe una palabra en un string.
texto = """Este es un texto
Este es otro en otra linea
y aqui un tercero en una linea más
"""
print("aqui" in texto)

#Contar el tamaño de un string
text = "Hola"
print(len(text))