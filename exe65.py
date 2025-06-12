c = int(0)
sp = int(0)
si = int(0)
while c != 5:
    num1 = int(input(" Digite um numero ? "))

    if(num1 % 2 == 0):
        print(" É par ")
        sp = sp + num1

    if(num1 %2 == 1):
       print(" É impar ")
       si = si + num1
    c = c + 1 

print(" A soma dos pares é " + str(sp))
print(" A soma dos impares é " + str(si))