def éPrimo(n):
    i = 1
    divisivel = 0
    while i <= n:
        if n % i == 0:
            divisivel = divisivel + 1
        i = i + 1
    if divisivel == 2:
        return True
    else:
        return False

n = int(input("Digite um número inteiro: "))

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo :-(")
    n = int(input("Digite um número inteiro: "))

