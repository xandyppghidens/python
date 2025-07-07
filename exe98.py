vet = [0,0,0,0]
c = int(0)
c9 = int(0)

for c in range(4):
    vet[c] = int(input("Digite um numero ? "))

    if(vet[c] == 9 ):
        c9 = c9 + 1


print(f"Os numeros digitados {vet[c]}")
print(f"A quantidade de vezes que o 9 apareceu é {c9}")