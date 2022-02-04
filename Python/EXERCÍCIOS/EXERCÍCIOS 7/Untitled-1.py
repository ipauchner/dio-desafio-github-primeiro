lista_numeros = []

a = 1

while a != 0:
    x1 = int(input("Digite um número maior que 0 "))
    lista_numeros.append(x1)

    if x1 == 0:
        a = 0
        lista_numeros.pop(-1)
        lista_numeros.sort(reverse=True)
        print(lista_numeros)
