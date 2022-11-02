#Forma dinámica para crear una lista

#Forma tradicional
palabra = "python"
lista = []

for letra in palabra:
    lista.append(letra)  
print(lista)

#Forma dinámica
lista = [ letra for letra in palabra]
print(lista)

lista = [ numero for numero in range(0,21,2)]
print(lista)

lista = [ numero for numero in range(0,21,2) if numero*2 >10]
print(lista)

pies = [10,20,30,40]
metros = [p* 3.281 for p in pies]

print(metros)