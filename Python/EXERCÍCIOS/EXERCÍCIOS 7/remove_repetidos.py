def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

numeros = (input("Digite uma lista com números inteiros: "))
lista = []
lista = numeros

lista = remove_repetidos(lista)
print (lista)