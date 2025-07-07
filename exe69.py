c = int(0)
soma = int(0)
media = int(0)
while c != 3000:
    num1 = int(input(" Digite um numero ? "))

    p = str(input(" Voce quer parar ? "))

    soma = soma + num1
    media = soma / num1

    if(p == "s"):
        break
    if(p == "n"):
         True
    c = c + 1
print(f"A soma é {soma}")
print(f"A media é {media}")





















