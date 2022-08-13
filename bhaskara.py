import math

def delta(a, b, c):
    return b**2 - 4*a*c

def main():
    a = float(input("Digite o valor de a:"))
    b = float(input("Digite o valor de b:"))
    c = float(input("Digite o valor de c:"))
    bhaskara(a, b, c)
    
def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        if x1 > 0:
            print("as raízes da equação são", x2,"e", x1)
        else:
            print("as raízes da equação são", x1,"e", x2)   
    else:
        if d == 0:
            x = (-b) / (2*a)
            print("a raiz desta equação é", x)
        else:
            print("esta equação não possui raízes reais")



