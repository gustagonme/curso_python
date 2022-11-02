#El ciclo for es un bucle que permite iterar valores.
nombres= ["Gus", "Cami", "Clau", "Rosa", "Abby"]

for nombre in nombres:
    print("Hola", nombre)
    
#Se puede obtener el índice del elemento con el método index
for nombre in nombres:
    i = nombres.index(nombre)
    print(f"Nombre {i}: {nombre}")
    
#Se pueden anidar otras operaciones como condicionales
for nombre in nombres:
    if nombre.startswith("C"):
        print(nombre)
#Iterar dentro de una lista
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    
#Iterar un diccionario
dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
for item in dic.items():
    print(item)
    
for a,b in dic.items():
    print(a,b)
    
for item in dic:
    print(item)
    
for item in dic.values():
    print(item)
