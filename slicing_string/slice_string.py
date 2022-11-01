#Usando los corchetes se puede tomar un rango de valores, especificando el desde y el hasta separados con dos puntos
from traceback import print_tb


text = "Esto es una prueba"
resultado = text[2:5]
print(resultado)
#Si no se especifica nada en el hasta, se determina que se toman todos desde el valor inicial
text = "Esto es una prueba"
resultado = text[2:]
print(resultado)
#De esta manera se puede invertir una cadena
text = "Esto es una prueba"
resultado = text[:: -1]
print(resultado)
