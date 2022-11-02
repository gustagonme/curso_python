#Permite obtener los indices de una lista de una forma mas dinámica
lista = ["a", "b", "c"]

for indice, item in enumerate(lista):
    print(indice, item)
    
#Se pueden hacer conversiones de lista de tuples

mis_tuples = list(enumerate(lista))
print(mis_tuples)