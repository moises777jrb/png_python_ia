from Calculadora import *
from Lambda import *

class Main:
    x=int(input("Escolha a sua operação:\n1 - adiçãon\n2 - subtração\n3 - multiplicação\n4 - divisão"))
    if(x==1):
        a=int(input("Digite o n1: "))
        b=int(input("Digite o n2: "))
        print(Lambda.adi(a,b))
    if(x==2):
        a=int(input("Digite o n1: "))
        b=int(input("Digite o n2: "))
        print(Lambda.sub(a,b))
    if(x==3):
        a=int(input("Digite o n1: "))
        b=int(input("Digite o n2: "))
        print(Lambda.mul(a,b))
    if(x==4):
        a=int(input("Digite o n1: "))
        b=int(input("Digite o n2: "))
        print(Lambda.div(a,b))