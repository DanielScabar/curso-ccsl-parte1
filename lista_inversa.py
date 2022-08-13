n = 1
listaNumeros = []
listaInversa = []
while n != 0:
    n = int(input("Digite um número: "))
    listaNumeros.append(n)

tam = len(listaNumeros) - 1
while tam >= 0:
    listaInversa.append(listaNumeros[tam])
    tam = tam - 1

print(listaInversa)
