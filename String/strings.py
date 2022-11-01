print("Hola", "mundo")

# Se puede concatenar con + o con coma.
# el caracter \ sirve para tomar los caracteres especiales dentro de una cadena como funciones, ej: \t, \n, \"
# A esto se le llama barra de escape.
nombre = "Gus"
apellido = "Gonzo"
print("tu nombre es {} y tu apellido es {}".format(nombre, apellido))
print(f"tu nombre es {nombre} y tu apellido es {apellido}")

#Métodos de String
#Cambiar a minúsculas
texto = "Este texto es una prueba"
resultado = texto.lower()
print(resultado)

#Cambiar a mayúsculas
texto = "Este texto es una prueba"
resultado = texto.upper()
print(resultado)

#Cambiar a mayúsculas o minusculas un solo caracter o rango
texto = "Este texto es una prueba"
resultado = texto[2].upper()
print(resultado)

#Separar elementos en una lista
texto = "Este texto es una prueba"
resultado = texto.split()
print(resultado)

#Separar elementos en una lista a partir de un elemento
texto = "Este texto es una prueba"
resultado = texto.split("e")
print(resultado)

#Unir elementos en una lista a partir de un elemento
a = "Este"
b = "texto"
c = "es"
d = "una"
e = "prueba"
espacios = " "
resultado = espacios.join([a,b,c,d,e])
print(resultado)

#Reemplazar texto de un string
texto = "Este texto es una prueba"
resultado = texto.replace("prueba", "pruebita")
print(resultado)