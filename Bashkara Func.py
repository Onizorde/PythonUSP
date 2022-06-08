import math
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

def Bas():
    d = (b**2)-(4*a*c)
    if d >= 0:
        x = ((-b + math.sqrt(d)) / (2*a))
        y = ((-b - math.sqrt(d)) / (2*a))
        if x == y:
            print("A raiz desta equação é ", x)
        else:
            print( "As raízes da equação são", x ,"e", y)
    else:
        print("Esta equação não possui raízes reais")

Bas()
