# = signo de asignación
# == signo de igualdad 
# < menor que
# > mayor que
# != diferente de
# and conjunción
# or disyunción
# not negación

comparar = 5 == 10
print(comparar)

#Evaluar valores con operadores lógicos
comparar = 4 < 5 and 5<6
print(comparar)

comparar = 4 < 5 and 5>6
print(comparar)

comparar = 4 < 5 or 5<6
print(comparar)

text = "Este es un texto breve"
comparar = ("texto" in text) and ("breve" in text)
print(comparar)