#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la

import math

lista=[2,3,7,12,2]
print(lista)
lista2 = [item * 2 for item in lista]
print(lista2)