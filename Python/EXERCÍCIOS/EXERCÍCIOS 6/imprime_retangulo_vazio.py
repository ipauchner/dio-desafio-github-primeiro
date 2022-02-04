largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 1
coluna = 1

while linha <= altura:
    while coluna <= largura:
        if coluna == 1 or coluna == largura or linha == 1 or linha == altura:
            print("#", end ="")
        else:
            print(" ", end ="")
        coluna += 1
    print()
    linha += 1
    coluna = 1


