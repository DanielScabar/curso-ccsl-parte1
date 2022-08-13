def primalidade(n):
    i = 1
    divisibilidade = 0
    while i <= n:
        if n % i == 0:
            divisibilidade = divisibilidade + 1
        i = i + 1
    if divisibilidade == 2:
        return True
    else:
        return False

def n_primos(n):
    if n >= 2:
        contador = 0
        i = 2
        while i <= n:
            if primalidade(i):
                contador = contador + 1
            i = i + 1

        return contador
        
    
