num1 = int(input(" Digitye um numero ? "))
num2 = int(input(" Digitye um numero ? "))
num3 = int(input(" Digitye um numero ? "))
num4 = int(input(" Digitye um numero ? "))

sp = int(0)
mp = int(0)

if(num1 %2 == 0):
    sp = sp + num1
    mp = num1

if(num2 %2 == 0):
    sp = sp + num2
    mp = num2

if(num3 %2 == 0):
    sp = sp + num3
    mp = num3

if(num4 %2 == 0):
    sp = sp + num4
    mp = num4

print(" A soma dos pares é " + str(sp))
print(" O maior par é " + str(mp))