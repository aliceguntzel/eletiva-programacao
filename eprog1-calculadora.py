import math
def ad (n1, n2):
    print("o resultado é", n1+n2)
def sb(n1, n2):
    print("o resultado é", n1-n2)
def mt(n1, n2):
    print("o resultado é", n1*n2)
def dv(n1, n2):
    print("o resultado é", n1/n2)
def ep(n1, n2):
    print("o resultado é", n1**n2)
def rq(n1):
    print("o resultado é", math.sqrt(n1))
def inv(n1):
    print("o resultado é", 1/n1)

print("bem-vindo à calculadora da eletiva de programação!")

calculadora = True
while calculadora:
    n1 = int(input("insira o primeiro número: "))
    op = input("""escolha a operação matemática. escreva 'a' para adição, 's' para subtração, 
    'm' para multiplicação, 'd' para divisão,'e' para exponenciação, 'r' para raiz quadrada e 'i' para o inverso do número: """)
    if op.lower() == "r":
        rq(n1)
    if op.lower() == "i":
        inv(n1)
    if op.lower() == "a":
        n2 = int(input("insira o segundo número: "))
        ad(n1, n2)
    elif op.lower() == "m":
        n2 = int(input("insira o segundo número: "))
        mt(n1, n2)
    elif op.lower() == "s":
        n2 = int(input("insira o segundo número: "))
        sb(n1, n2)
    elif op.lower() == "d":
        n2 = int(input("insira o segundo número: "))
        dv(n1, n2)
    elif op.lower() == "e":
        n2 = int(input("insira o segundo número: "))
        ep(n1, n2)
    again = input("quer usar a calculadora novamente? responda 's' para sim e 'n' para não: ")
    if again.lower() == "n":
        print("obrigada por ter usado a calculadora!")
        calculadora = False
