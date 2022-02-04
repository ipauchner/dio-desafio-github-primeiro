n = int(input("Digite uma lista de valores maiores que 0 "))
valores = list()

while n != 0:
    x = int(input("Digite o próximo número "))
    valores.append(x)

valores.sort(reverse=True)
print(valores)
