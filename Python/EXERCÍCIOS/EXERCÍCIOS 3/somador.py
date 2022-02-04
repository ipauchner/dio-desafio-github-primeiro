x = int(input("digite o valor de n: "))
soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print(soma)