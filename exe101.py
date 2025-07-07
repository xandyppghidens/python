vet = [0,0,0,0,0,0,0,0,0,0]
c = int(0)
sp = int(0)
si = int(0)
c2 = int(0)

for c in range(10):
    vet[c] = int(input("Digite um numero ? "))

    if(vet[c] %2 == 0):
        print(" É par ")
        sp = sp + vet[c]

    if(vet[c] %2 == 1):
        print(" É impar ")
        si = si + vet[c]

for c2 in range(10):    
   if(vet[c2]%2 == 0):
        print(f"vetores pares repetidos no vetor({vet[c2]})")
   else: False   
print(f" A soma dos pares é soma({sp}) ")
print(f" A soma dos impares é soma({si}) ")