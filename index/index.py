#·l método index me permite conocer los valores o las posiciones de los caracteres en un String
text = "Esta es una prueba"
resultado = text[0] #enviamos el indice 0 para saber el valor que representa.
print(resultado)

resultado = text.index("E") #asi sabremos en que posición está
print(resultado)
# Tener en cuenta que el string es sensible a mayusculas y debe existir en la cedena buscada. 
# El método index buscará de izquierda a derecha hasta encontrar el primer caracter que coincida
resultado = text.index("a") #asi sabremos en que posición está
print(resultado)
#Index también puede recibir como parámetro un número donde quieres que inicie tu busqueda
resultado = text.index("a",5) #asi sabremos en que posición está
print(resultado)
#El método rindex hace lo mismo pero de derecha a izquierda
resultado = text.rindex("a",5) #asi sabremos en que posición está
print(resultado)