a = int(input("Digite o valor de a " ))
b = int(input("Digite o valor de b " ))
c = int(input("Digite o valor de c " ))
import math
delta = (int(b**2 - 4*a*c))

if delta > 0:
    x1 = ((-b + math.sqrt(delta)) / (2 * a))
    x2 = ((-b - math.sqrt(delta)) / (2 * a))
    if x1 < x2:
        print("as raízes da equação são",x1, "e",x2)
    else:
        print("as raízes da equação são",x2, "e",x1)

if delta == 0:
    x1 = -b / (2*a)
    x2 = x1
    print("a raiz desta equação é ",x1)
if delta < 0:
    print("esta equação não possui raízes reais")
