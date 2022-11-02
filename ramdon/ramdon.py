#Permite obtener valores aleatorios
from random import *

aleatorio = randint(1,50);
print(aleatorio)

aleatorio = uniform(1,5)
print(round(aleatorio, 2))

aleatorio = random()
print(aleatorio)

colores = ["Rojo", "Azul", "verde", "Amarillo"]
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)