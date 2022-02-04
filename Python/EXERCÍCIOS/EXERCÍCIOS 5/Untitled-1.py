print("Bem vindo ao jogo do NIM! Escolha: ")

print("1 -  para uma partida isolada: ")

print("2 -  para um campeonato: ")

escolha = int(input("Escolha: "))

def computador_escolhe_jogada(n, m):

    while n!=0:

        m = 1

        n = n - m
        
        return(print("Restam", n," peças", ))

def usuário_escolhe_jogada(n, m):

    while n!=0:

        m = int(input("Escolha o valor de m : "))

        n= n-m

        return (print("Restam", n, "peças"))

def partida():

    n = int(input("Valor máximo de peças"))

    m= print("Pode retirar no máximo", n-1, "peças")

    while n!=0:

        if escolha == 1:

            return(usuário_escolhe_jogada(n, m), computador_escolhe_jogada(n, m))

def campeonato():

    return partida()

    return partida()

    return partida()

if escolha == 1:

    partida()

else:

    campeonato()