c = int(0)
mult3 = int(0)
mult5 = int(0)
while c != 7:
    num1 = int(input(" Digite um numero ? "))

    if(num1 %3 == 0):
        mult3 = num1

    if(num1 %5 == 0):
        mult5 = num1

    c = c + 1 


print(f" Foram encontrados multiplos de três {mult3}")
print(f" Foram encontrados multiplos de cinco {mult5}")








