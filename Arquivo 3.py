#Objetivo: Criar um programa que organize uma lista de nomes em ordem alfabetica
#Bonus: Organizar por ordem alfabetica da ultima letra do nome

lista=["Alexandre","Alice","André","Arthur","Arthur","Artur","Augusto","Bernardo","Bernardo","Bruno","Davi","Diego",
"Eduardo","Fabrício","Felipe","Fernando","Francisco","Francisco","Gabriel","Gabriel","Giovanna","Giovanni","Guilherme",
"Guilherme","Hector","Henrique","Inácio","João","João","Joaquim","Júlia","Lauren","Leonardo","Leonardo","Lucas","Marina","Matheus",
"Matheus","Paula","Pedro","Pedro","Pedro","Pedro","Rafael","Regis","Sofia","Stella","Thiago","Valentina","Vicente","Lucas"]
ordemlista = sorted(lista)
print(ordemlista)
ordemlista2 = sorted(lista, key=lambda x: x[::-1])
print(ordemlista2)