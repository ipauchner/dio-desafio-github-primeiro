def n_primos (x):
    fator = 2
    if x == 2:
        return True
    
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


n = int(input("digite um numero inteiro: "))

while n > 0:
    if n_primos(n):
        print(n,"é primo")
    else:
        print(n,"não é primo")
    n = int(input("digite um numero inteiro: "))
    
