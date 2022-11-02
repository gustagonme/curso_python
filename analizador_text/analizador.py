#Pedirle al usuario un texto
#Pedirle al usuario 3 letras y averiguar cuantas veces aparecen estas letras en el texto.
#Contar el número de palabras que hay en total
#Obtener la primera y última letra.
#Invertir el orden de las palabras

texto = input("Ingresa un texto por favor: ")
letra1 = input("Ingresa una letra al azar: ").lower()
letra2 = input("Ingresa una segunda letra al azar: ").lower()
letra3 = input("Ingresa una tercera letra al azar: ").lower()

cantidadLetra1 = texto.lower().count(letra1)
cantidadLetra2 = texto.lower().count(letra2)
cantidadLetra3 = texto.lower().count(letra3)

print(f"La cantidad de veces que se repite la primera letra es: {cantidadLetra1}, la segunda {cantidadLetra2} y la tercera {cantidadLetra3}")


textoComoLista = texto.lower().split()
print("El número de palabras totales que tiene el texto es: ", len(textoComoLista))

primeraLetra = texto[0];
ultimaLetra = texto[len(texto)-1]

print(f"La primera letra del texto es: {primeraLetra} y la ultima letra es {ultimaLetra}")

invertirTexto = texto[:: -1]
print("Texto invertido: ", invertirTexto)

buscarPython = "python" in texto

dic = {True:"Si",False:"No" }
print(f"La palabra 'Python' existe? {dic[buscarPython]}")