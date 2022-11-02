#Combina dos o mas listas, entrelazando sus elementos como tuples
nombres = ["Gus", "Cami", "Clau"]
edades = [31,27,50]
ciudades = ["Cali", "Manizales", "Atlanta"]

#Para poder visualizarlos lo recomendable es castearlo como lista
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")