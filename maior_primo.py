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

def maior_primo(n):
    if n > 1:        
        while True:
            if(primalidade(n)):
                return n
            n = n - 1

    
