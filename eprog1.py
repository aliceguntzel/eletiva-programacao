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

print("bem-vindo à calculadora da eletiva de programação!")

calculadora = True
while calculadora:
    op = input("""escolha a operação matemática. escreva 'a' para adição, 's' para subtração, 
    'm' para multiplicação, 'd' para divisão e 'e' para exponenciação: """)
    n1 = int(input("insira o primeiro número: "))
    n2 = int(input("insira o segundo número: "))
    if op.lower() == "a":
        ad(n1, n2)
    elif op.lower() == "m":
        mt(n1, n2)
    elif op.lower() == "s":
        sb(n1, n2)
    elif op.lower() == "d":
        dv(n1, n2)
    elif op.lower() == "e":
        ep(n1, n2)
    again = input("quer usar a calculadora novamente? responda 's' para sim e 'n' para não: ")
    if again.lower() == "n":
        print("obrigada por ter usado a calculadora!")
        calculadora = False