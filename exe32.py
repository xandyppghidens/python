num1 = int(input(" Digite um numero ? "))
num2 = int(input(" Digite um numero ? "))
num3 = int(input(" Digite um numero ? "))

sp = int(0)
si = int(0)


if(num1 %2 == 0):
     sp = sp + num1

if(num1 %2 == 1):
     si = si + num1

if(num2 %2 == 0):
     sp = sp + num2

if(num2 %2 == 1):
     si = si + num2

if(num3 %2 == 0):
     sp = sp + num3

if(num3 %2 == 1):
     si = si + num3

print(" A soma dos pares é " + str(sp))
print(" A soma dos impares é " + str(si))



