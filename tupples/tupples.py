#Son igual que las listas, pero no se pueden modificar. 
from re import T


mi_tuple = (1,2,3,4)
print(mi_tuple)

#Se pueden indexar
print(mi_tuple[0])

#Se pueden tener tuples de diferentes tipos de datos
mi_tuple = (1,2,(10,5),4)
print(mi_tuple)

#Se puede cambiar el tipo de dato
mi_tuple = list(mi_tuple)
print(type(tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

#Se pueden asignar valores desde un tuple a una variable cuando se tiene el mismo número de variables
t = (1,2,3)
x,y,z = t 
print(x,y,z)

