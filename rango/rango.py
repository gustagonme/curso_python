#Range permite crear un rango de números sin necesidad de declarar una lista o una variable
#puedes especificar en los argumentos del método range, el rango de números que quieres obtener, 
#si solo se pone un número, este tomará como valor inicial 0 y valor final el número menos 1.

for numero in range(5):
    print(numero)
    
for numero in range(1,5):
    print(numero)
    
#Si se especifica un tercer parametro, este dictará los saltos que dará entre cada posición
for numero in range(20,30, 2):
    print(numero)
