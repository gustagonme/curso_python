#El ciclo while como su nombre lo dice, se ejecuta mientras una condición se cumpla en la ejecución del programa.
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:
    print("No tengo mas dinero")
    
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir? s/n: ")
else:
    print("Gracias")
    
#Break y continue
nombre = input("Ingresa tu nombre ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)
    
for letra in nombre:
    if letra == "r":
        continue
    print(letra)
    
