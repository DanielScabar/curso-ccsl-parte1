def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

def binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

def teste_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if fatorial(3) == 6:
        print("Funciona para 3")
    else:
        print("Não funciona para 3")

    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
