#Son secuencias ordenadas de objetos, pueden estar compuestas por objetos de diferente tipo de datos.
#También se puede tener listas de listas
#No son inmutables
#Vemos el tipo de dato
lista = ["a", "b", "c"]
print(type(lista))

# Ver el tamaño de la lista
print(len(lista))

# Podemos indexar, asi como los strings, pueden manejar rangos. 
print(lista[0])

#concatenar listas
lista_2 = ["d", "e", "f"]
print(lista + lista_2)

#Alterar elementos de una lista
lista[0] = "alfa"
print(lista)

#Agregar elementos
lista.append("g")
print(lista)

#Remover elementos, se puede especificar el indice del elemento que quieres eliminar. Si no se especifica se elimina por defecto el último.
lista.pop()
print(lista)

#Se puede reservar el elemento eliminado en una variable
eliminado = lista.pop(0)
print(eliminado)

#Ordenar elementos de una lista, solo se puede ordenar la lista seleccionada, no se puede almacenar como resultado en otra variable
lista = ["m", "a", "z", "r", "p", "s"]
lista.sort()
print(lista)

#Inversion del orden de la lista
lista = ["m", "a", "z", "r", "p", "s"]
lista.sort()
lista.reverse()
print(lista)