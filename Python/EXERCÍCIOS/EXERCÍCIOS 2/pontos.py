x1 = float(input("Digite o valor de x "))
y1 = float(input("Digite o valor de y "))
x2 = float(input("Digite o valor de x "))
y2 = float(input("Digite o valor de y "))

import math

temp = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if temp >= 10:
    print("longe")
else:
    print("perto")