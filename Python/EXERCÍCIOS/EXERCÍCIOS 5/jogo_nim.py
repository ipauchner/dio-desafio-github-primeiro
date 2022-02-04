def jogo ():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    tipo_jogo = int(input())

    if tipo_jogo == 2:
        print("Você escolheu um campeonato!")
    else:
        print("Você escolheu uma partida isolada")

def regras():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if m >= n:
        print("Dados inválidos, favor digitar novamente")
        regras()

    if n % (m+1) == 0:
        print("Você começa!")
    else:
        print("O computador começa!")

jogo()
regras()

    