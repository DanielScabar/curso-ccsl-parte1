n = int(input("Digite um número inteiro:"))

possuiNumerosAdjacentes = False

while n != 0 and not possuiNumerosAdjacentes:
    digitoDireita = n % 10
    n = n // 10
    digitoEsquerda = n % 10
    if digitoDireita == digitoEsquerda:
        possuiNumerosAdjacentes = True

if possuiNumerosAdjacentes:
    print("sim")
else:
    print("não")
