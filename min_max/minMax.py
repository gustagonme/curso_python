#Permite determinar valores minimos o maximos en una lista

menor = min(58,96,36,72,64,35)
mayor = max(58,96,36,72,64,35)

print("El mayor es", mayor)
print("El menor es", menor)

#Desde una lista se puede determinar asi

lista = [58,96,36,72,64,35]

print(f"El mayor es {max(lista)} y el menor es {min(lista)}")

#Los strings tambien se pueden ordenar alfabeticamente
#Tener en cuenta las mayusculas y minusculas, dado que siempre tendrá como valor minimo la mayuscula. Usar lower()
nombres = ["Gus", "Cami", "Clau"]
print(min(nombres))

#Usos en diccionarios
dic = {"c1": 45, "c2": 47}
print(min(dic))
print(min(dic.values()))