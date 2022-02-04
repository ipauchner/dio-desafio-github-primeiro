def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

coef_bin = (factorial(n) / (factorial(k) * factorial(n - k)))

print(coef_bin)