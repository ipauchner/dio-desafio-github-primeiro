l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

l1 = 0
a1 = 0

while a1 < a:
    while l1 < l:
        print("#", end = "")
        l1 = l1 + 1
    a1 = a1 + 1
    print()
    l1 = 0

