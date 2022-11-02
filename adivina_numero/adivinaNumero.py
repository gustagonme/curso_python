
#Construir un programa que permita al usuario adivinar un número al azar, teniendo 8 intentos para adivinar. 
#El programa debe solicitar un número cada que el usuario no acierte.  
#Pedir nombre
#Pedir un número del 1 al 100
#El programa debe validar si el número está dentro del 1 y el 100, si el número es menor al número secreto
#si el número es mayor al número secreto y si el usuario adivina el número secreto. 

from random import randint


nombre = input("Como te llamas? ")
numero = int(input(f"Hola {nombre}, por favor digita un número entre 1 y 100 "))

numeroSecreto = randint(1,101);
intentos = 8

while intentos > 0:
    if numero > 0 and numero < 101:
        if numeroSecreto < numero:
            print("El número secreto es menor al número proporcionado")
            numero = int(input(f"{nombre}, por favor digita otro número entre 1 y 100 "))
            intentos -=1
        elif numeroSecreto > numero:
            print("El número secreto es mayor al número proporcionado")
            numero = int(input(f"{nombre}, por favor digita otro número entre 1 y 100 "))
            intentos -=1
        elif numero == numeroSecreto :
            print(f"Lo lograste! has adivinado el número secreto, el cual era {numeroSecreto}")
            break
    else:
        print("El número está fuera del rango entre 1 y 100")
        numero = int(input(f"{nombre}, por favor digita otro número entre 1 y 100 "))
        intentos -=1

if intentos == 0:
    print("Has acabado con todos tus intentos :(")
    print(f"El número secreto era: {numeroSecreto}")

