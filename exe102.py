import random

vet = [0,0,0,0]
c = int(0)
soma = int(0)
pro = int(0)
for c in range(4):
    vet[c] = int(input("Digite um numero ? "))
    s = random.randint(0,50)
    if(vet[c] == s):
        soma = vet[c] + s
        print("Ganhou")
        print(f"A soma dos ganhos sortiados é {soma}")
        break
    else:print(f"Perdeu !! O valor sorteado foi ({s})")    

    if(vet[c] == 3 or vet[c] == 8 or vet[c] == 11 or vet[c] == 14):
        pro = vet[c] + vet[c]
        print(f"A soma da escolha é {pro}")

