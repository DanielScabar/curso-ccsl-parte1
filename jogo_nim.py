def computador_escolhe_jogada(n, m):
    i = m
    while i > 0:
        if (n - i) % (m + 1) == 0:
            return i
        i = i - 1
    return m
        
def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= m and jogada > 0:
            return jogada
        print()
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    i = n

    while i > 0:
        print()
        if i == n:
            if n % (m + 1) == 0:
                print("Você começa!")
                vez = True
                print()
            else:
                print("Computador começa!")
                vez = False
                print()
        if vez:
            jogada = usuario_escolhe_jogada(n, m)
            i = i - jogada
            vez = False
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", jogada, "peças.")

        else:
            jogada = computador_escolhe_jogada(i, m)
            i = i - jogada
            vez = True
            if jogada == 1:
                print("Computador tirou uma peça.")
            else:
                print("Computador tirou", jogada, "peças.")
        if i == 1:
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            if i != 0:
                print("Agora resta apenas", i, "peças no tabuleiro.")
            else:
                print("Fim do jogo! O computador ganhou!")

def campeonato():
    j = 1
    while j <= 3:
        print()
        print("**** Rodada", j, "****")
        print()
        partida()
        j = j + 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")

print()
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))

if escolha == 1:
    partida()
if escolha == 2:
    print()
    print("Voce escolheu um campeonato!")
    print()
    campeonato()

