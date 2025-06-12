v1 = int(input(" Digite um valor ? "))
v2 = int(input(" Digite um valor ? "))
v3 = int(input(" Digite um valor ? "))

ci = int (0)
cp = int (0)

if(v1 % 2 == 0):
    print(" É par")
    cp = cp + 1

if(v2 %2 == 0):
     print(" É par")
     cp = cp + 1

if(v3 %2 == 0):
     print("É par")
     cp = cp + 1


if(v1 % 2 == 1):
    print(" É impar")
    ci = ci + 1

if(v2 %2 == 1):
     print(" É impar")
     ci = ci + 1

if(v3 %2 == 1):
     print("É impar")
     ci = ci + 1

print(" Foram encontrados pares " + str(cp)) 
print("foram encontrados impares " + str(ci))









